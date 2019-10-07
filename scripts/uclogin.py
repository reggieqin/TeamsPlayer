import requests
import sys
import json

def execute(host, params):
    try:
        # Login with test account
        ucaccount = json.loads(params)

        url = 'http://{}:8000/uclogin'.format(host)
        response = requests.post(url, json=ucaccount)
        if response.status_code != 202:
            print "Failed to uclogin"
            return False

        return True
    except Exception as e:
        print e
        return False

if __name__ == '__main__':
    execute('127.0.0.1', '{"username":"cmbucitest1", "password":"Happy123!@#", "ucdomain":"hz.jabberqa.cisco.com"}')