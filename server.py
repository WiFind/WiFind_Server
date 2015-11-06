# Echo server program
import socket

HOST = ''                 # Symbolic name meaning all available interfaces
PORT = 8000              # Arbitrary non-privileged port

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
    s.recv(1)
    scan_length = ""
    while '\n' not in scan_length:
        scan_length += conn.recv(1)
    # cut off the newline character, and store the integer scan length
    scan_length = int(scan_length[:-1])
    data_to_scan = scan_length
    scan = ""
    while data_to_scan != 0:
        local_data = conn.recv(data_to_scan)
        if not local_data:
            raise RuntimeError("Socket closed unexpectedly")

        data_to_scan -= len(local_data)
        scan += local_data

    # at this point, scan contains the incoming scan data. Now to parse it.
    # TODO parse scan
    

    # TODO send request to RedPin to get location

    # TODO print out any messages we need to

    # TODO send messsage back to WiFind device if necessary

    conn.close()

def wifi_scan_to_json():
    pass

# If we call this file like "python server.py", call the main() function
if __name__ == "__main__":
    main()
