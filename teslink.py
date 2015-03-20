import json
import urllib2

from bottle import Bottle, run, hook, response, request
app = Bottle()

@app.hook('after_request')
def enable_cors():
	response.headers['Access-Control-Allow-Origin']='*'

@app.route('/apis/test', method='GET')
def test():
	try:
		rlink =  request.query.link
		if rlink is None or rlink == "":
			return "Link kosong"

		f = urllib2.urlopen(rlink)
		data = f.read()
		if data:
			result_json = json.loads(data, encoding='utf-8')
			print result_json
			status = result_json['collection']['entries']['entry']['entryId']
			if status:
				return "Vote Id : %s" % status
				
	except Exception as e:
		return str(e)

def main():
	run(app, host="0.0.0.0", port=2205)

if __name__ == '__main__':
	main()
