import os

class Config(object):
  DEBUG = False
  TESTING = False
  MONGO_URI = 'mongodb://localhost:27017/song-art-development'
  REDIRECT_URI = 'http://localhost:5000/callback'
  
class ProductionConfig(Config):
  MONGO_URI = os.environ.get('MONGOLAB_URI')
  REDIRECT_URI = '?'  # TODO

class DevelopmentConfig(Config):
  DEBUG = True

class TestingConfig(Config):
  TESTING = True

if os.environ.get('SONG_ART_MODE') == 'production':
  config = ProductionConfig
elif os.environ.get('SONG_ART_MODE') != 'testing':
  config = DevelopmentConfig
else:
  config = TestingConfig
