import requests
import sys

def execute(host, params = None):
    hosts = host.split(";")

    for h in hosts:
        try:
            url = 'http://{}:8000/isalive'.format(h)
            response = requests.get(url)
            if response.status_code != 200:
                print "Failed to get alive from [{}]".format(h)
                return False
        except Exception as e:
            print e
            return False
    
    return True

if __name__ == '__main__':
    if execute('127.0.0.1;127.0.0.1'):
        print "Succeed"
    else:
        print "Failed"