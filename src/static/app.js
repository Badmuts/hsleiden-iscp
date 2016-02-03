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

	var data = {
	    labels: ["Positive", "Negative", "Neutral"],
	    datasets: [
	        {
	            label: "Tweet sentiment",
	            fillColor: "rgba(0, 161, 245,0.2)",
	            strokeColor: "rgba(0, 161, 245,1)",
	            pointColor: "rgba(0, 161, 245,1)",
	            pointStrokeColor: "rgb(255, 255, 255)",
	            pointHighlightFill: "#fff",
	            pointHighlightStroke: "rgba(220,220,220,1)",
	            data: [0, 0, 0]
	        }
	    ]
	};

	var options = {
		angleLineColor: "#445664",
		scaleLineColor: "#243241",
		scaleFontColor: "#ffffff"
	};

	var radarCtx = document.getElementById("radar-chart").getContext("2d");
	var myRadarChart = new Chart(radarCtx).Radar(data, options);

	btn.addEventListener('click', function (event) {
		if (isAnalyzing) {
			return;
		}
		showLoader();

		// if (parseInt(analyzed.textContent) > 0) {
		// 	analyzed.textContent = 0;
		// }

		var xhrStartStream = new XMLHttpRequest();
		var keyword = encodeURIComponent(keywordInput.textContent)
		xhrStartStream.addEventListener('load', function() {
			isAnalyzing = true;
		});
		xhrStartStream.open('GET', '/start_stream?keyword=' + keyword)
		xhrStartStream.send();

		interval = setInterval(function() {
			var xhrStatus = new XMLHttpRequest();
			xhrStatus.addEventListener('load', updateView)
			xhrStatus.open('GET', '/status')
			xhrStatus.send();
		}, 300);
	});

	function updateView() {
		var resp = JSON.parse(this.responseText);
		updateChart(resp);
		analyzed.textContent = resp[2];
		mood.textContent = resp[3].toUpperCase()
		if (resp[3] === 'pos') {
			mood.className = 'pos';
		} else if (resp[3] === 'neu') {
			mood.className = 'neu';
		} else {
			mood.className = 'neg';
		}

		if (resp[2] >= getLimit()) {
			clearInterval(interval);
			isAnalyzing = false;
			hideLoader();
			stopStream();
		} else if (resp[1] === "inactive") {
			clearInterval(interval);
			isAnalyzing = false;
			hideLoader();
		}
	}

	function updateChart(resp) {
		myRadarChart.datasets[0].points[0].value = resp[4];
		myRadarChart.datasets[0].points[1].value = resp[5];
		myRadarChart.datasets[0].points[2].value = resp[6];
		myRadarChart.update();
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

	function stopStream() {
		var stopStream = new XMLHttpRequest();
			stopStream.open("GET", "/stop_stream");
			stopStream.send()
	}
})();