import requests
import sys
import json

def execute(host, params):
    try:
        destination = json.loads(params)

        url = 'http://{}:8000/makecall'.format(host)
        response = requests.post(url, json=destination)
        if response.status_code != 202:
            print "Failed to makecall"
            return False

        return True
    except Exception as e:
        print e
        return False

if __name__ == '__main__':
    if execute('127.0.0.1', '{"uri":"regqin@cisco.com"}'):
        print "Succeed"
    else:
        print "Failed"