(function() {
	'use strict';

	var btn = document.querySelectorAll('button')[0];
	var loader = document.querySelectorAll('.loader')[0];
	var analyzed = document.querySelectorAll('#analyzed')[0];
	var mood = document.querySelectorAll('#mood')[0];
	var keywordInput = document.querySelectorAll('div.input.hashtag')[0];
	var limitInput = document.querySelectorAll('#limit')[0];
	var interval = null;
	var isAnalyzing = false;

	btn.addEventListener('click', function (event) {
		if (isAnalyzing) {
			return;
		}
		showLoader();

		var xhrStartStream = new XMLHttpRequest();
		var keyword = encodeURIComponent('#' + keywordInput.textContent)
		xhrStartStream.addEventListener('load', function() {
			isAnalyzing = true;
		});
		xhrStartStream.open('GET', '/start_stream?keyword=' + keyword)
		xhrStartStream.send();

		interval = setInterval(function() {
			console.log('check status')
			var xhrStatus = new XMLHttpRequest();
			xhrStatus.addEventListener('load', updateView)
			xhrStatus.open('GET', '/status')
			xhrStatus.send();
		}, 300);
	});

	function updateView() {
		var resp = JSON.parse(this.responseText);
		
		analyzed.textContent = resp[2];
		mood.textContent = resp[3].toUpperCase()
		if (resp[3] === 'pos') {
			mood.className = 'pos';
		} else if (resp[3] === 'neu') {
			mood.className = 'neu';
		} else {
			console.log('neg');
			mood.className = 'neg';
		}

		console.log(getLimit(), resp[2]);

		if (resp[2] >= getLimit()) {
			console.log('clear interval')
			clearInterval(interval);
			isAnalyzing = false;
			hideLoader();
		} else if (resp[1] === "inactive") {
			clearInterval(interval);
			isAnalyzing = false;
			hideLoader();
		}
	}

	function hideLoader() {
		loader.className = 'loader hide';
	}

	function showLoader() {
		loader.className = 'loader';
	}

	function getLimit() {
		return parseInt(limitInput.textContent);
	}
})();