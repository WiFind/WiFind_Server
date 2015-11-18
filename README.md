
#WiFind_Server
##Receive parket format from WiFind band
```text
<MAC_ADDR>1<Wifi scan length>\0\r\n
```

##Request to Wifind band
```text
<1/0>
1: there is a request
0: no request
```

##Fingerprint to Redpin Server
```json
{"action":"getLocation","data":
	{
		"wifiReadings":
		[
			{"ssid":"eth","bssid":"0:3:52:1c:32:e0",
				"wepEnabled":false,
				"rssi":-83,"isInfrastructure":true
			},
			{"ssid":"public",
				"bssid":"0:3:52:4d:bd:c1",
				"wepEnabled":false,
				"rssi":-89,"isInfrastructure":true
			},
			...
			{"ssid":"MOBILE-EAPSIM",
				"bssid":"0:3:52:1c:13:62",
				"wepEnabled":false,
				"rssi":-83,"isInfrastructure":true
			}
		]
	}
}
```

##Location from Redpin Server
```json
{"status":"ok",
	"data":
	{
		"id":1,"symbolicID":"44",
		"map":
		{
			"id":1,"mapName":"IFW A",
			"mapURL":"http://www.rauminfo.ethz.ch/..."
		},
		"mapXcord":446,"mapYcord":340,"accuracy":7
	}
}
```
##Database between Django server and our server


