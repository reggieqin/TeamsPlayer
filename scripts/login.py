import requests
import sys
import json

def execute(host, params = None):
    try:
        # Retrieve test user account
        url = 'http://{}:8000/testuser'.format(host)
        response = requests.get(url)
        if response.status_code != 200:
            print "Failed to retrieve test user account"
            return False
        r = response.json()
        name = r['username']
        pwd = r['password']
        if name == None or pwd == None:
            print "username or password is none"
            return False
        
        # Login with test account
        url = 'http://{}:8000/login'.format(host)
        response = requests.post(url, json={'username':name, 'password':pwd})
        if response.status_code != 202:
            print "Failed to login"
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