# Echo server programn the Ethernet frame. The MAC address of the destination endpoint does not go in the Ethn the Etn the Ethernet frame. The MAC address of the destination endpoint does not go in the Ethhernet frame. The MAC address of the destination endpoint does not go in the Eth
import socket
import threading
import json

# This is needed to access the database

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

os.environ['DJANGO_SETTINGS_MODULE'] = 'WiFind.local_settings'
import django
django.setup()

from nursecall.models import Device, Patient

HOST = ''					# Symbolic name meaning all available interfaces
PORT = 8000					# Arbitrary non-privileged port

REDPIN_HOST = 'localhost'	# host for RedPin server
REDPIN_PORT = 50007				# port for RedPin

WEB_SERVER_HOST = ''
WB_SERVER_PORT = 123

threads = []

LOCATION_INFO = [
        ('R2336', 1000, 1109),
        ('R2301', 2058, 1186),
        ('R2211', 1796, 1641),
    ]

LOCATION_COUNTER = 0

def main():
    # Example query of WiFind devices, and prints mac addresses
    for entry in Device.objects.all():
        print entry.mac_addr

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((HOST, PORT))
    s.listen(1)
    while LOCATION_COUNTER < len(LOCATION_INFO):
        conn, addr = s.accept()
        print 'Connected by', addr
        handle_message(conn, addr)
        # t1 = threading.Thread(handle_message(conn, addr))


def handle_message(conn, address):
    # format of receive header:
    # "*HELLO*<MACADDR> 1 <wifi scan length>\n" 1 is HELP
    # "*HELLO*<MACADDR> 2 <wifi scan length>\n" 2 is check in
    conn.recv(7)
    mac_addr = conn.recv(17)
    dev, created = Device.objects.get_or_create(mac_addr=mac_addr)
    print "%s" % str(dev.mac_addr)
    # Recieve space
    conn.recv(1)
    
    if dev.notify:
        # format request
        conn.sendall('1')
    else:
        conn.sendall('0')

    dev.notify = False
        
    message_type = int(conn.recv(1))
    # Recieve space
    conn.recv(1)

    scan_length = ""
    # TODO recieve MAC address in header
    while '\n' not in scan_length:
        scan_length += conn.recv(1)
    # cut off the newline character, and store the integer scan length
    scan_length = int(scan_length[:-1])
    scan = ""
    while "END:" not in scan:
        local_data = conn.recv(1)
        if not local_data:
            raise RuntimeError("Socket closed unexpectedly")

        #data_to_scan -= len(local_data)
        scan += local_data

    # at this point, scan contains the incoming scan data. Now to parse it.
    # TODO parse scan
    if message_type == 1:
        dev.help_req = True
        # Ask for help and clear any pending requests
        print 'help!'
    formatedData = dataParse(scan)

    # Check if a request exists, if it does, alert the user
        

    # TODO senn requestme. The MAC address of the destination endpoint does not go in the Eth to RedPin to get location
    RedPin = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    RedPin.connect((REDPIN_HOST, REDPIN_PORT))
    print 'connect to the RedPin server'
    RedPin.sendall(formatedData)
    location = ''
    while '\n' not in location:
        location += RedPin.recv(1)
    RedPin.close();
    print 'close'
    print location
    
    # TODO add no location exception here
    parsed = json.loads(location)
    if parsed['status'] != 'ok':
        print "not fingerprinting matches"
        conn.close()
        return 
    parsed_map = parsed['data']['map']
    print repr(parsed)
    dev.map_url = parsed_map['mapURL']
    dev.x_loc = parsed['data']['mapXcord']
    dev.y_loc = parsed['data']['mapYcord']
    dev.save()


    # TODO print out any messages we need to
    print location
    # TODO send messsage back to WiFind device if necessary

    conn.close()

def dataParse(data):
        # TODO 
        num = data[14:15]
        sData = data.splitlines()
        formatedData = '{"action":"setFingerprint","data":{"location":{"symbolicID":"%s","mapXcord":%d,"mapYcord":%d,"map":{"id":3,"mapName":"EECS Floor 2","mapURL":"http://wifind.jonesnl.com/static/eecsmaps/floor2.png"}},"measurement":{"wifiReadings":['
        formatedData = formatedData % LOCATION_INFO[LOCATION_COUNTER]
        for line in sData[2:-1]:
            elt = line.split(',')
            capabilities = elt[4]
            privacy = capabilities[0]
            if privacy == '1' or privacy == '3':
                wepEnable = 'true'
            else:
                wepEnable = 'false'
            infrastructure = capabilities[1]
            if infrastructure == '1':
                Infra = 'false'
            else:
                Infra = 'true'
	    formatedDataLine = '{"ssid":"%s","bssid":"%s","wepEnabled":%s,"rssi":%s,"isInfrastructure":%s},' % (elt[8], elt[7], wepEnable,elt[2], Infra)
	    formatedData += formatedDataLine
	formatedData = formatedData[:-1]
	formatedData += "]}}}\r\n"

	# format into <ssid> <bssid> <wepEnable> <rssi> <infrastructure>
	return formatedData

# If we call this file like "python server.py", call the main() function
if __name__ == "__main__":
    main()
