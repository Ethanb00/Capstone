import json as simplejson
import urllib
import webbrowser


ELEVATION_BASE_URL = 'http://maps.googleapis.com/maps/api/elevation/json'
CHART_BASE_URL = 'http://chart.apis.google.com/chart'

def getChart(chartData, chartDataScaling="-50,1000", chartType="lc",chartLabel="Elevation in Meters",chartSize="1000x300",chartColor="orange", **chart_args):
    chart_args.update({
      'cht': chartType,
      'chs': chartSize,
      'chl': chartLabel,
      'chco': chartColor,
      'chds': chartDataScaling,
      'chxt': 'x,y',
      'chxr': '1,-50,1000'
    })

    dataString = 't:' + ','.join(str(x) for x in chartData)
    chart_args['chd'] = dataString.strip(',')

    chartUrl = CHART_BASE_URL + '?' + urllib.urlencode(chart_args)

    print chartUrl

def getElevation(path="49.310255, -0.706981|49.371351, -0.709436",samples="100",sensor="false", **elvtn_args):
      elvtn_args.update({
        'path': path,
        'samples': samples,
        'sensor': sensor
      })

      url = ELEVATION_BASE_URL + '?' + urllib.urlencode(elvtn_args)
      response = simplejson.load(urllib.urlopen(url))
	
      # Create a dictionary for each results[] object
      elevationArray = []

      for resultset in response['results']:
        elevationArray.append(resultset['elevation'])

      # Create the chart passing the array of elevation data
      getChart(chartData=elevationArray)
      webbrowser.open(url)

if __name__ == '__main__':
    # Vaux-sur-Aure, inside France, near Normandy
    startStr = "49.343622, -0.716989"
    # English Channel
    endStr = "49.371351, -0.709436"

    pathStr = startStr + "|" + endStr

    getElevation(pathStr)
	
