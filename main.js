var SQUARE_SIZE = 300;

$(function() {
  var div = $('#text');

  div.html(div.text().replace(' ', '&nbsp;'));

	var size = 30;
  while(div[0].scrollHeight <= SQUARE_SIZE) {
		div.css('font-size', size + 'px');
		size += 0.1;
  }
  div.css('font-size', (size - 0.2) + 'px');

  var lh = 65;
  while(div[0].scrollHeight <= SQUARE_SIZE) {
		div.css('line-height', lh + 'px');
		lh += 0.1;
  }
  div.css('line-height', (lh - 0.1) + 'px');
});
