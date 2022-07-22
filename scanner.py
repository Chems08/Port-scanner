import socket as s

ip = "127.0.0.1"

port = 65535

z = []

for i in range(port):

    sock = s.socket(s.AF_INET, s.SOCK_STREAM)

    sock.settimeout(2)

    if sock.connect_ex((ip, i)):
        i = i + 1

    else:
        try:
            serviceName = s.getservbyport(i, "tcp")
            print("Port", str(i), ": Open -", serviceName)
        except OSError:
            print("Port", str(i), ": Open")

        z.append(i)

print("List of open ports : ", z)

