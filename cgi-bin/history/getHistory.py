import urllib
from datetime import timedelta, datetime
import re
import urllib2
import json
import pickle

params = {}

params['instrument'] = 'EUR_USD'
params['count'] = '5000'
params['start'] = '2013-04-03T18%3A30%3A30Z'
#params['side'] = 'buy'
#params['type'] = 'marketIfTouched'
#params['price'] = 1.2
#params['expiry'] = (datetime.now()+timedelta(hours=10)).strftime('%Y-%m-%dT%H:%M:%SZ')
#params['units'] = 2
#params = urllib.urlencode(params)
data = []
response = urllib2.urlopen("http://api-sandbox.oanda.com/v1/history?instrument="+params['instrument']+"&start="+params['start']+"&count="+params['count']+"&granularity=M1")
data = json.load(response)['candles']
date = datetime.strptime(data[-1:][0]['time'], '%Y-%m-%dT%H:%M:%SZ') 
outfile = open(params['instrument']+'.json', 'w')
while(date < (datetime.now()-timedelta(days=20))):
	date = datetime.strptime(data[-1:][0]['time'], '%Y-%m-%dT%H:%M:%SZ') + timedelta(minutes=1)
	params['start'] = str(date.isoformat('T')+'Z').replace(':','%3A') 
	response = urllib2.urlopen("http://api-sandbox.oanda.com/v1/history?instrument="+params['instrument']+"&start="+params['start']+"&count="+params['count']+"&granularity=M1")
	data.extend(json.load(response)['candles'])

json.dump(data, outfile)
#print data
	#print data
	
#print data
#	if data[0]['time'] > '2013-12-01T18%3A30%3A30Z':
#		exit()
#	else: 
		#json.dump(data,f1)
		
		
#print data