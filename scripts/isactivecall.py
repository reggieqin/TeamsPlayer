import requests
import sys

def execute(host, params = None):
    try:
        url = 'http://{}:8000/activecall'.format(host)
        response = requests.get(url)
        if response.status_code != 200:
            print "Failed to retrieve active call"
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