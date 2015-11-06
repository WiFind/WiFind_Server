# Echo server program
import socket
import json

HOST = ''					# Symbolic name meaning all available interfaces
PORT = 8000					# Arbitrary non-privileged port

REDPIN_HOST = 'localhost'	# host for RedPin server
REDPIN_PORT = 50007				# port for RedPin

def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((HOST, PORT))
    s.listen(1)
    while 1:
        conn, addr = s.accept()
        print 'Connected by', addr
        handle_message(conn, addr)


def handle_message(conn, address):
    # format of receive header:
    # "1 <wifi scan length>" 1 is HELP
    # "2 <wifi scan length>" 2 is check in
    message_type = int(conn.recv(1))
    #Recieve space
    conn.recv(1)
    scan_length = ""
    while '\n' not in scan_length:
        scan_length += conn.recv(1)
    # cut off the newline character, and store the integer scan length
    scan_length = int(scan_length[:-1])
    data_to_scan = scan_length
    scan = ""
    while "END:\r\n" not in scan:
        local_data = conn.recv(data_to_scan)
        if not local_data:
            raise RuntimeError("Socket closed unexpectedly")

        data_to_scan -= len(local_data)
        scan += local_data

    # at this point, scan contains the incoming scan data. Now to parse it.
    # TODO parse scan
	if message_type == 1:
		# TODO alert 
		print 'help!'
	formatedData = dataParse(scan)
    

    # TODO send request to RedPin to get location
	RedPin = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	RedPin.connect((REDPIN_HOST, REDPIN_PORT))
	print 'connect to the RedPin server'
	RedPin.sendall(formatedData)
	location = RedPin.recv(1024)
	RedPin.close();
        print 'close'


    # TODO print out any messages we need to
	print location
    # TODO send messsage back to WiFind device if necessary

    conn.close()

def dataParse(data):
	# TODO 
	num = data[14:15]
	sData = data.splitlines()
	formatedData = '{"action":"getLocation","data":{"wifiReadings":['
	for line in sData[2:-1]:
		elt = line.split(',')
		formatedDataLine = '{"ssid":"%s","bssid":"%s","wepEnabled":false,"rssi":%s,"isInfrastructure":true},' % (elt[8], elt[7], elt[2])
		formatedData += formatedDataLine
	formatedData = formatedData[:-1]
	formatedData += "]}}\r\n"

	# format into <ssid> <bssid> <wepEnable> <rssi> <infrastructure>
	return formatedData

def wifi_scan_to_json():
    pass

# If we call this file like "python server.py", call the main() function
if __name__ == "__main__":
    main()
