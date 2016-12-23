#!/usr/bin/env python
# -- coding: utf-8 --

from __future__ import (absolute_import, division,
                        print_function, unicode_literals)

try:
        from PyDect200 import PyDect200
except:
        print(u'PyDect200 is not installed!')
        print(u'run: pip install PyDect200')
        exit()
import getpass

try:
    PyDect200.__version__
except:
    PyDect200 = PyDect200.PyDect200

fritzbox_user = getpass.getpass(prompt='Please insert your fritzbox-username: ', stream=None)
fritzbox_pw = getpass.getpass(prompt='Please insert your fritzbox-password: ', stream=None)

print(u"Welcome to PyDect200 v%s, the Python AVM-DECT200 API" % PyDect200.__version__)

# you can also use the .crt exported from your Browser llike FireFox
# Firfox: -> go to login site of your FritBox
# Right Click->Siteinfromation->Security->Show Certificate->Export
# Save it
f = PyDect200.PyDect200(fritzbox_pw, fritzbox_user, "/home/fritz.pem","https://fritz.box")
f.get_sid() # SID will be timedout after 1h you have to fetch an new one after timeout
try:
        info = f.get_info()
        power = f.get_power_all()
        names = f.get_device_names()
except Exception:
    print(u'HTTP-Error, wrong password?')
    exit()

print(u'')
for dev_id in info.keys():
        print(u"Device ID:           %s" % dev_id)
        dev_name = names.get(dev_id)
        try:
            print(u"Device Name:         %s" % dev_name)
        except:
            print(u"Device Name:         %s" % dev_name.encode('utf-8').decode('utf-8', 'ignore'))

        print(u"Device State:        %s" % ('ON' if info.get(dev_id) == '1' else 'OFF'))
        dev_power = power.get(dev_id)
        if dev_power.isdigit():
            dev_power = float(dev_power) / 1000
        print(u"Device Power:        %sW" % dev_power)
        print(u"Device Energy:       %sWh" % f.get_energy_single(dev_id))
        print(u"Device Temperature:  %s degree Celsius  " % (f.get_temperature_single(dev_id)))
        
f.logout()
