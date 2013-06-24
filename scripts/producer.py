#!/usr/bin/python
'''
this script prodices the task
'''
import os
import sys
import json
import time
import random
import getopt
import beanstalkc


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
    tubes = {
        "master1.1": ["tube_a", "tube_b", "tube_c"],
        "master1.2": ["tube_d", "tube_e", "tube_f"],
        "master1.3": ["tube_g", "tube_h", "tube_i"]
    }

    port = 11300
    sleep = 5

    try:
        opts, args = getopt.getopt(argv, "s:", ["sleep="])
    except getopt.GetoptError as err:
        print str(err)
        sys.exit(2)

    #print opts

    for o, a in opts:
        if o == "-s":
            sleep = float(a)

    while True:
        try:  # run till we are interrupted via keyboard

            host = random.choice(tubes.keys())
            tube = random.choice(tubes[host])

            try:
                beanstalk = beanstalkc.Connection(host=host, port=port)  # connect to beanstalk here

                job_data = {
                    "M": random.randint(10, 100),
                    "s": random.randint(10, 30),
                    "m": random.randint(1, 2)
                }

                # start putting jobs here
                beanstalk.use(tube)
                beanstalk.put(json.dumps(job_data))
                print "submitted job to %s with M:%s s:%s m:%s - sleeping for %s second(s)  \n" % (tube, job_data['M'], job_data['s'], job_data['m'], sleep)
                time.sleep(sleep)

            except beanstalkc.SocketError:
                print "could not connect to %s:%s for %s " % (host, port, tube)

        except KeyboardInterrupt:
            break

if __name__ == "__main__":
    main(sys.argv[1:])
