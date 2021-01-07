import webbrowser
import pyfiglet
from pyfiglet import Figlet
import socket
import datetime
import os
import sys


os.system('pip install Figlet')

ascii_banner = pyfiglet.figlet_format("TrapView")
print(ascii_banner)
print("___________________________________________")
print("                           By @Dr_sans_fil ")
print("___________________________________________")
print("-------------------------------------------")
print("Outil De scan des ports via une adresse ip \n EX : xxx.xxx.xxx.xxx")
print("-------------------------------------------")

ipadress=input('[+] Entrez une adresse ip :')
print('Entrez une plage de port a Scanner : ')
debut=input('Allant de  : ')
fin=input('à  : ')
print('_________ VERIFICATION _____________')
print('Ip: '+ ipadress + ' Plage de port: ('+debut+':'+fin+')' )
print('_______ LANCEMENT DU SCAN ___________')
date = datetime.datetime.now()
rapport = open("Rapport ["+ipadress+"].txt", "a")
rapport.write('========================= DEBUT ===================================\n')
rapport.write('['+str(date)+'] Debut du scan de ['+str(ipadress)+'] port ('+str(debut)+':'+str(fin)+')\n')
def scan_port(ipadress,port):
	try:
		sock = socket.socket()
		sock.connect((ipadress,port))
		print('[+] port ' + str(port)+ ' is open')
		rapport.write('[+] port ' + str(port)+ ' is open\n')
	except:
		print('[-] port ' + str(port)+ ' is closed')
		rapport.write('[-] port ' + str(port)+ ' is closed\n')
for port in range(int(debut),int(fin)):
	scan_port(ipadress, port)
print('_______ FIN DU SCAN ___________')
rapport.write('========================= FIN ===================================\n')
print('[+] Creation du rapport du scan .... \n File: Rapport['+ipadress+'].txt')

rapport.close()
print('[+] Creation du rapport Terminer ')

	
