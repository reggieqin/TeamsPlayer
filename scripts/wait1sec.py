import sys
import time

def execute(host, params = None):
    time.sleep(1)
    return True

if __name__ == "__main__":
    if execute(''):
        print "Succeed"
    else:
        print "Failed"