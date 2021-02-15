import os
#os.system('python -m pip install Figlet')
#os.system('python -m pip install pyfiglet')
import webbrowser
import socket
import datetime
import sys
os.system('clear')
print("\u001b[31m###########################################################")
print("\u001b[31m##################################################\u001b[32m   \u001b[31m######")
print("\u001b[31m##############################################\u001b[32m   /~\   \u001b[31m####")
print("\u001b[31m###########################################\u001b[32m   _- `~~~', \u001b[31m###")
print("\u001b[31m#########################################\u001b[32m  _-~       )  \u001b[31m###")
print("\u001b[31m######################################\u001b[32m  _-~          |  \u001b[31m###")
print("\u001b[31m###################################\u001b[32m  _-~            ;  \u001b[31m####")
print("\u001b[31m#########################\u001b[32m  __---___-~              |   \u001b[31m####")
print("\u001b[31m######################\u001b[32m   _~   ,,                  ;  `,,  \u001b[31m#")
print("\u001b[31m####################\u001b[32m  _-~    ;'                  |  ,'  ; \u001b[31m#")
print("\u001b[31m##################\u001b[32m  _~      '                    `~'   ; \u001b[31m##")
print("\u001b[31m###########\u001b[32m   __---;                                 ,' \u001b[31m###")
print("\u001b[31m#######\u001b[32m   __~~  ___     TrapView v1.1              ,' \u001b[31m#####")
print("\u001b[31m####\u001b[32m  _-~~   -~~ _                               ,' \u001b[31m#######")
print("\u001b[31m####\u001b[32m `-_         _                              ; \u001b[31m#########")
print("\u001b[31m######\u001b[32m  ~~----~~~   ;                          ; \u001b[31m##########")
print("\u001b[31m########\u001b[32m  /          ;                        ; \u001b[31m###########")
print("\u001b[31m######\u001b[32m  /             ;                      ; \u001b[31m############")
print("\u001b[31m####\u001b[32m  /                `                    ; \u001b[31m#############")
print("\u001b[31m##\u001b[32m  /                                      ; \u001b[31m##############")
print("\u001b[31m#\u001b[32m /                                       ;\u001b[31m################")
print("\u001b[33m##################################### By @Dr_sans_fil #####\u001b[0m")
print("Outil De scan des ports via une adresse ip \n EX : xxx.xxx.xxx.xxx")
print("-------------------------------------------")
ok=0
def scan_port(ipadress,port):
	global ok
	try:
		sock = socket.socket()
		sock.settimeout(1)
		sock.connect((ipadress,port))
		print('\u001b[32m [ OK ] \u001b[0m : port ' + str(port) + ' is open')
		rapport.write('[ OK ] port ' + str(port) + ' is open\n')
		file_port.write(" "+str(port)+",")
		ok=ok+1

	except:
		print('\u001b[31m [-] \u001b[0m : port ' + str(port) + ' is closed')
		rapport.write('[-] port ' + str(port) + ' is closed\n')


ipadress=input('[+] Entrez une adresse Ip :')
try:
	socket.inet_aton(ipadress)
	print('Entrez une plage de port a Scanner ')
	debut =input('Allant de  : ')
	fin=input('a  : ')
	s =int(fin)-int(debut)

	if int(s)<3:
		print("\u001b[31m [Error] \u001b[0m : Veuillez Selectionner une plage d'aumoins 3 ports !")
	else:
		date = datetime.datetime.now()
		rapport = open("Rapport ["+ipadress+"].txt", "a")
		file_port = open("ports.txt", "a")
		rapport.write('\n['+str(date)+'] Debut du scan de ['+str(ipadress)+'] port ('+str(debut)+':'+str(fin)+')\n')
		print('__________ DEBUT DU SCAN ______________')

		for port in range(int(debut),int(fin)):
			scan_port(ipadress, port)

		print('__________ FIN DU SCAN ______________')
		rapport.write('========================= FIN ===================================\n')
		print('\u001b[0m [+] Creation du rapport du scan .... \n File: Rapport['+ipadress+'].txt')

		print('[+] Creation du rapport Terminer ')
		print("Nombre de port ouvert : " + str(ok))

		plus =input(" \u001b[33m Recuperer plus d'info ? \u001b[37m [y/n]:")

		if plus == "y":
			plus_text = os.system('whois '+ ipadress+'')
			rapport.write(str(plus_text))
		else:
			print("\u001b[32m --__--__--__-- FIN --__--__--__--__--__")


except socket.error:
	print("\u001b[31m [Fatal Error] \u001b[0m : Ip Invalide Ex :[xxx.xxx.xxx.xxx]")
rapport.close()




