#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import commands


# firmware_state = ["Failed",
#                   "Online, Spun Up",
#                   "Online, Spun Down",
#                   "Unconfigured(bad)",
#                   "Unconfigured(good), Spun down",
#                   "Hotspare, Spun down",
#                   "Hotspare, Spun up",
#                   "not Online",
#                   "JBOD"]


(_, result) = commands.getstatusoutput("/opt/MegaRAID/MegaCli/MegaCli64 -PDList -aALL | grep 'Firmware state' | awk -F ':' '{print $2}' | sed 's/^[ \t]*//g'")

if result == '':
    sys.exit(1)

result = result.split('\n')
result = list(set(result))

if ("Failed" in result) or ("Online, Spun Down" in result) or ("Unconfigured(bad)" in result) or ("Unconfigured(good), Spun down" in result) or ("Hotspare, Spun down" in result) or ("not Online" in result):
    print 100
else:
    print 200

