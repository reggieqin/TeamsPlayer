import requests
import sys

def execute(host, params = None):
    try:
        url = 'http://{}:8000/isUCloggedin'.format(host)
        response = requests.get(url)
        return response.status_code == 200
    except Exception as e:
        print e
        return False

if __name__ == '__main__':
    if execute('127.0.0.1'):
        print "Succeed"
    else:
        print "Failed"