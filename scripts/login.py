import requests
import sys
import json

def execute(host, params = None):
    hosts = host.split(";")

    for h in hosts:
        try:
            # Retrieve test user account
            url = 'http://{}:8000/testuser'.format(h)
            response = requests.get(url)
            if response.status_code != 200:
                print "Failed to retrieve test user account for [{}]".format(h)
                return False
            r = response.json()
            name = r['username']
            pwd = r['password']
            if name == None or pwd == None:
                print "username or password is none for [{}]".format(h)
                return False
            
            # Login with test account
            url = 'http://{}:8000/login'.format(host)
            response = requests.post(url, json={'username':name, 'password':pwd})
            if response.status_code != 202:
                print "Failed to login [{}]".format(h)
                return False
        except Exception as e:
            print e
            return False
    
    return True

if __name__ == '__main__':
    if execute('10.79.36.32'):
        print "Succeed"
    else:
        print "Failed"