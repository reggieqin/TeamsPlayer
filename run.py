import sys
import argparse
import time
import os
from datetime import datetime, timedelta
import xml.etree.ElementTree as ET

ap = argparse.ArgumentParser()
ap.add_argument("-f", "--file", help="path of case")
sys.path.append(os.path.join(os.getcwd(), "scripts"))

def parse_xml(root, func):       
    name = root.get('name')
    host = root.get('host') or "127.0.0.1"
    params = root.get('params')
    repeat = root.get('repeat') or 1
    timeout = root.get('timeout') or 1

    if name is None:
        print ('Script name can not be empty')
        return False

    for x in range(int(repeat)):        
        print('Executing [{0}] host: {1} params: {2} for {3} times. Timeout {4} seconds'.format(name, host, params, x + 1, timeout))
        ret = False
        t_timeout = datetime.now() + timedelta(seconds=int(timeout))
        while datetime.now() <= t_timeout:
            ret = func(name, host, params)
            if ret:
                print ("Succeed to execute [{}]".format(name))
                break
            else:
                time.sleep(1)

        if ret:
            for child in root:
                parse_xml(child, func)
        else:
            print ("Timeout to execute [{}] for {} times".format(name, x + 1))

def execute(*argv):
    name = argv[0]
    host = argv[1] 
    params = argv[2] 

    module = __import__(name)
    
    return module.execute(host, params)

if __name__ == '__main__':
    args = vars(ap.parse_args())
    if args["file"]:
        inputfile = args["file"]

    tree = ET.parse(inputfile)

    for scripts in tree.getroot():
        parse_xml(scripts, execute)

