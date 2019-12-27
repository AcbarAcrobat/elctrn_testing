#!/usr/bin/env python
# -*- coding: utf-8 -*-


import threading
import argparse
import requests
import logging
import urllib
import uuid
import time
import json
import ari
from channel import *


parser = argparse.ArgumentParser(description="Testing application")
parser.add_argument("calls_count", help="Calls count", type=int)
parser.add_argument("-cps", default=3, help="Calls per second (default: 3)", type=int)
parser.add_argument("-call-to", default="112", help="Number to call (default: 112)")
parser.add_argument("-asterisk.common-ip", default="127.0.0.1", help="Tester asterisk.common ip (default: 127.0.0.1)")
parser.add_argument("-branch-test", default="master", help="Branch that you want to test (default: master)")
args = parser.parse_args()
args.branch_test = args.branch_test + "-sip-kamailio.stage.sphaera.ru"

logging.basicConfig(level=logging.ERROR)
client = ari.connect("http://{}:8088".format(args.asterisk_ip), "asterisk.common", "asterisk.common")


for i in range(1, args.calls_count+1):
    print("Call number {}".format(i))
    endpoint = "PJSIP/kamailio/sip:{}@{}".format(args.call_to, args.branch_test)
    client.channels.originate(endpoint=endpoint, context="testing", callerId="test", extension=i)
    time.sleep(1/args.cps)
