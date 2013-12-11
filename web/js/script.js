function graphData() {
	$.getJSON('output.json', function (data) {
		data = data.data;
		//Format the data by turning the dateString into milliseconds
		for (var i = 0; i < data.length; ++i) {
			data[i][0] = (new Date(data[i][0])).getTime();
		}
		
		// Create the chart
		$('#container').highcharts('StockChart', {
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