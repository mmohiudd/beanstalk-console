#!/usr/bin/python
'''
this script prodices the task
'''

import sys
import getopt
import os
import beanstalkc
import random
import json
import time

def perform(*args, **kwargs):
    retvalue = os.system
    #call(["stressapptest", "-M 100 -s 2 -m 3"])
    M = kwargs.get("M", 100)
    s = kwargs.get("s", 30)
    m = kwargs.get("m", 1)

    command = "stressapptest -M %s -s %s -m %s" % (M, s, m)

    retvalue = os.system(command)

    print retvalue


def main(argv):
    tube = None
    host = None
    port = 11300
    sleep = 5

    try:
        opts, args = getopt.getopt(argv, "t:h:p:s:", ["tube=", "host=", "port="])
    except getopt.GetoptError as err:
        print str(err)
        sys.exit(2)

    #print opts

    for o, a in opts:
        #print o
        if o == "-t":
            tube = a
        if o == "-h":
            host = a
        if o == "-p":
            port = a
        if o == "-s":
            sleep = float(a)

    if tube is None:
        print "please provide a tube name"
        sys.exit(2)

    if host is None:
        print "please provide a host"
        sys.exit(2)

    try:
        beanstalk = beanstalkc.Connection(host=host, port=port)  # connect to beanstalk here
    except:
        print "could not connect to %s:%s for %s " % (host, port, tube)
        sys.exit(2)

    while True:
        try:  # run till we are interrupted via keyboard
            job_data = {
                "M": random.randint(10, 100),
                "s": random.randint(10, 120),
                "m": random.randint(1, 2)
            }

            # start putting jobs here
            beanstalk.use(tube)
            beanstalk.put(json.dumps(job_data))
            print "submitted job to %s with M:%s s:%s m:%s - sleeping for %s second(s)  \n" % (tube, job_data['M'], job_data['s'], job_data['m'], sleep)
            time.sleep(sleep)
        except KeyboardInterrupt:
            break


if __name__ == "__main__":
    main(sys.argv[1:])
