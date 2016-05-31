import os

import flask
import soundcloud

app = flask.Flask(__name__)
client = soundcloud.Client(client_id=os.environ['SC_CLIENT_ID'],
                           client_secret=os.environ['SC_CLIENT_SECRET'],
                           redirect_uri='http://localhost:5000/callback')

@app.route('/')
def index():
  return flask.render_template(
    'index.html', access_token=flask.session['access_token'])

@app.route('/oauth/soundcloud')
def oauth_soundcloud():  
  # redirect user to authorize URL
  return flask.redirect(client.authorize_url())

@app.route('/callback')
def callback():
  # exchange authorization code for access token
  code = flask.request.args.get('code')
  flask.session['access_token'] = client.exchange_token(code=code).access_token
  return flask.redirect('/')

@app.route('/api/sc/me')
def api_sc_me():
  client.access_token = flask.session['access_token']
  me = client.get('/me/tracks?linked_partitioning=1')
  return me.raw_data


app.secret_key = '4a510a0e33da3d7a9e4cad607fcb986fe27e6eae5d3fd96d'
if __name__ == "__main__":
    app.run(debug=True)

