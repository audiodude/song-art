# song-art
Simple HTML page to generate art for songs at http://soundcloud.com/travis-briggs

Enter the song-art directory and run a simple Python HTTP server:

Python 2.7:
```
python -m SimpleHTTPServer 3000
```

Python 3.4:
```
python -m http.server 3000
```

Then visit http://localhost:3000 and screen grab the art! Edit the colors and text in the
source file. Very basic.

## Automation
PhantomJS version 2.1, as promised, provides support for WOFF fonts such as
those used in Google Web Fonts and this project. Surprisingly, the original
capture script I wrote almost 6 months ago worked 100% accurately this time
around.

### Next steps

Next steps are to automate my soundcloud feed, so that I can generate "title"
cover art for all of my 90 songs automatically.