function graphData() {
	$.getJSON('output.json', function (data) {
		data = data.data;
		//Format the data by turning the dateString into milliseconds
		for (var i = 0; i < data.length; ++i) {
			data[i][0] = (new Date(data[i][0])).getTime();
		}
		
		// Create the chart
		$('#graph').highcharts('StockChart', {
			rangeSelector: {
				selected: 1
			},
			title: {
				text: 'Backtest Results'
			},
			yAxis: {
				title: {
					text: '% Gained/Lost'
				},
			},
			xAxis: {
				type: 'datetime',
				title: {
					text: 'Date'
				},
				dateTimeLabelFormats: { // don't display the dummy year
					day: '%b %e, %Y',
					month: '%b %Y',
					year: '%b %Y'
				}
			},
			series: [{
				name: 'AAPL Stock Price',
				data: data,
				marker: {
					enabled: true,
					radius: 3
				},
				shadow: true,
				tooltip: {
					valueDecimals: 2
				}
			}]
		});
	});
}

function sendUserScript() {
	var url = "whatever_they_have_in_the_backend.py";
	var params = "user-script=" + document.getElementById('user-script').value; //get the user's input script text
	var xhr = new XMLHttpRequest();
	xhr.open("POST", url, true);

	//Send the proper header information along with the request
	xhr.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
	xhr.setRequestHeader("Content-length", params.length);
	xhr.setRequestHeader("Connection", "close");

	http.onreadystatechange = function() { //Call a function when the state changes.
		if (http.readyState == 4 && http.status == 200) {
			//Once the back end script finishes, we expect output.json to exist, so call graphData()
			graphData();
		}
	};
	xhr.send(params);
}