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
No further attempts have made at automation because PhantomJS 2.0 currently doesn't support
WOFF fonts which are used in Google Web Fonts. Additionally, I had lots of problems with the
`localToRemoteUrlAccessEnabled` [setting](http://phantomjs.org/api/webpage/property/settings.html)
of PhantomJS. I think it had something to do with the fact that I was accessing localhost. But
either way, I would get the following in the console:

```
ReferenceError: Can't find variable: $
   http://localhost:3000/main.js:3 in global code
```

Which indicated that somehow jQuery had failed to load.

### No further automation

Because of this basic failure of automating the capturing of the screen shots, I didn't go through
the trouble of trying to automate anything else, like pulling song titles using the Soundcloud API
for example.

It seems like it would be interesting to do this as a web app for Soundcloud or YouTube users for
creating thumbnails for their assets. I could function as a single page web app.
