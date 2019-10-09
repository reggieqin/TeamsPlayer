import requests
import sys
import json

def makecall(host, destination):
    url = 'http://{}:8000/makecall'.format(host)
    response = requests.post(url, json=destination)
    if response.status_code != 202:
        print "Failed to makecall"
        return False

    return True

def execute(host, params):
    try:
        destination = json.loads(params)

        if 'uri' in destination:
            return makecall(host, destination)
        elif 'host' in destination:
            url = 'http://{}:8000/loggedinuser'.format(destination['host'])
            response = requests.get(url)
            if response.status_code != 200:
                print "Failed to retrieve logged in user from {}".format(destination['host'])
                return False

            r = response.json()
            if r['email'] is None:
                print "Invalid email"
                return False

            data = {}
            data['uri'] = r['email']
            return makecall(host, data)
        else:
            print "Invalid params"
            return False
    except Exception as e:
        print e
        return False

if __name__ == '__main__':
    if execute('127.0.0.1', '{"host":"127.0.0.1"}'):
        print "Succeed"
    else:
        print "Failed"