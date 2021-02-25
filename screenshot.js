var page = require('webpage').create();
page.viewportSize = {width: 1000, height: 1000};
page.onLoadFinished = function() {
  setTimeout(function() {
    page.render('title.png');
    phantom.exit();
  }, 5000);
}
page.open('http://localhost:3000', function () { });
