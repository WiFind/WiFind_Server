#WiFind_Server
##Receive parket format
Version(1 byte) + Size(? bytes, In string end up with '\0', the size of the following packet, not the whole packet)
FingerPrint(size bytes)
Version: 1 stand for emergency, 2 stand for periodic message.
