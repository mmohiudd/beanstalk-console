#!/usr/bin/python
'''
this script performs the task
'''
import os
import sys
import json
import getopt
import beanstalkc


def perform(*args, **kwargs):
    retvalue = os.system
    #call(["stressapptest", "-M 100 -s 2 -m 3"])
    M = kwargs.get("M", 100)
    s = kwargs.get("s", 30)
    m = kwargs.get("m", 1)

    command = "stressapptest -M %s -s %s -m %s" % (M, s, m)
    print "performing %s " % (command)
    retvalue = os.system(command)

    print retvalue


def main(argv):
    tube = None
    host = None
    port = 11300
    try:
        opts, args = getopt.getopt(argv, "t:h:p:", ["tube=", "host=", "port="])
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
        try:
            print "started %s " % (tube)
            beanstalk.watch(tube)  # start watching
            beanstalk.ignore("default")  # stop watching default
            job = beanstalk.reserve()  # reseve the job
            job_data = json.loads(job.body)
            perform(**job_data)
            job.delete()
        except KeyboardInterrupt:
            break

if __name__ == "__main__":
    main(sys.argv[1:])
