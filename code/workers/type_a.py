#!/usr/bin/python
import sys
import getopt
import os
import task
import beanstalkc




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
        beanstalk.watch(tube)  # start watching
        beanstalk.ignore("default")  # stop watching default
        job = beanstalk.reserve()  # reseve the job
        print job.body
        job.delete()

if __name__ == "__main__":
    main(sys.argv[1:])
