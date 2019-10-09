import requests
import sys
import json

def execute(host, params = None):
    hosts = host.split(";")

    for h in hosts:
        try:
            url = 'http://{}:8000/logout'.format(h)
            response = requests.post(url, json={})
            if response.status_code != 202:
                print "Failed to logout [{}]".format(h)
                return False
        except Exception as e:
            print e
            return False

    return True

if __name__ == '__main__':
    if execute('127.0.0.1'):
        print "Succeed"
    else:
        print "Failed"