// NOTE: This doesn't work, because PhantomJS doesn't support woff files.
var page = require('webpage').create();
page.viewportSize = {width: 300, height: 300};
page.onLoadFinished = function() {
  setTimeout(function() {
    page.render('title.png');
    phantom.exit();
  }, 5000);
}
page.open('http://localhost:3000', function () {});
