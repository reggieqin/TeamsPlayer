import requests
import sys
import json

def execute(host, params = None):
    try:
        url = 'http://{}:8000/logout'.format(host)
        response = requests.post(url, json={})
        if response.status_code != 202:
            print "Failed to logout"
            return False
            
        return True
    except Exception as e:
        print e
        return False

if __name__ == '__main__':
    if execute('127.0.0.1'):
        print "Succeed"
    else:
        print "Failed"