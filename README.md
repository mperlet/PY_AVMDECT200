
### Example Code

```
In [1]: from PyDect200 import PyDect200
In [2]: f = PyDect200.PyDect200(fritzbox_pw, fritzbox_user, "/home/fritz.pem","https://fritz.box")
In [3]: f.get_sid() # get the sid will you get a new login
In [4]: f.get_device_names()
Out[4]: {'16': 'Beleuchtung', '17': 'Fernseher'}
In [5]: f.get_info()
Out[5]: {u'16': u'0', u'17': u'0'}
In [6]: f.switch_onoff(16,1)
Out[6]: 
		{u'DeviceID': u'16',
		 u'RequestResult': u'1',
		 u'Value': u'0',
		 u'ValueToSet': u'1'}
In [7]: f.get_power()
Out[7]: {u'16': 68.95, u'17': 0.0}
In [8]: f.logout()
```

### Tested with

* Python3.5
* Fritzbox 7390
* FRITZ!OS: 06.51
* AVM Dect200
