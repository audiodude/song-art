import os

import flask
import pymongo
import soundcloud

from . import config

app = flask.Flask(__name__)
app.config.from_object(config.config)

client = soundcloud.Client(client_id=os.environ['SC_CLIENT_ID'],
                           client_secret=os.environ['SC_CLIENT_SECRET'],
                           redirect_uri=config.config.REDIRECT_URI)

db = pymongo.MongoClient(config.config.MONGO_URI,
                         connectTimeoutMS=30000,
                         socketTimeoutMS=None,
                         socketKeepAlive=True).get_default_database()

@app.route('/')
def index():
  return flask.render_template('index.html')

@app.route('/tracks/display')
def tracks_display():
  tracks = list(db.tracks.find({'user.id': {'$eq': flask.session['user_id']}}))
  return flask.render_template('tracks.html', tracks=tracks)

@app.route('/oauth/soundcloud')
def oauth_soundcloud():  
  # redirect user to authorize URL
  return flask.redirect(client.authorize_url())

@app.route('/callback')
def callback():
  # exchange authorization code for access token
  code = flask.request.args.get('code')
  flask.session['access_token'] = client.exchange_token(code=code).access_token
  client.access_token = flask.session['access_token']
  me = client.get('/me').obj
  flask.session['user_id'] = me['id']
  return flask.redirect('/tracks/ingest')

@app.route('/tracks/ingest')
def api_sc_me():
  client.access_token = flask.session['access_token']
  tracks = client.get('/me/tracks?linked_partitioning=1').obj
  while True:
    for track in tracks['collection']:
      track['_id'] = track['id']
      db.tracks.update({'_id': track['_id']}, track, upsert=True)
    if 'next_href' in tracks:
      tracks = client.get(tracks['next_href']).obj
    else:
      break

  return flask.redirect('/tracks/display')


app.secret_key = '4a510a0e33da3d7a9e4cad607fcb986fe27e6eae5d3fd96d'
if __name__ == "__main__":
    app.run(debug=True)

