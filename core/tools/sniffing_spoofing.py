#!/usr/bin/env	python
# -*- coding: utf-8 -*-

import os,sys
from core.tools import load

class category_element(object):

	def set_agv(self, argv):
		self.argv = argv

	def main(self, name):
		name = name.replace('core/tools/', "")
		self.view_tools(name)
		action = False
		while action == False:
			try:
				option = raw_input(load.input(name))
			except KeyboardInterrupt:
				os.system('clear')
				break
			try:
				if option == "back":
					break
				elif option == "clear":
					os.system('clear')
				elif option == "help":
					load.help()
				elif option == "view":
					self.view_tools(name)
				elif int(option) in range(1,33):
					self.install(option)
				elif option == "99":
					self.install(option)
				else:
					load.error()
			except ValueError:
				pass
			
	def view_tools(self,name):
		os.system('clear')
		load.title(name)
		print """
	 1) Burp Suite       17) rtpmixsound 
	 2) DNSChef          18) sctpscan 
	 3) fiked            19) SIPArmyKnife 
	 4) hamster-sidejack 20) SIPp 
	 5) HexInject        21) SIPVicious 
	 6) iaxflood         22) SniffJoke 
	 7) inviteflood      23) SSLsplit 
	 8) iSMTP            24) sslstrip 
	 9) isr-evilgrade    25) THC-IPV6 
	10) mitmproxy        26) VoIPHopper 
	11) ohrwurm          27) WebScarab 
	12) protos-sip       28) Wifi Honey 
	13) rebind           29) Wireshark 
	14) responder        30) xspy 
	15) rtpbreak         31) Yersinia 
	16) rtpinsertsound   32) zaproxy\n
	99) ALL\n
%sInsert the number of the tool to install it%s""" %(load.Green,load.Reset)

	def install(self, option):
		if option == "1":
			cmd = os.system("apt install burpsuite")
		elif option == "2":
			cmd = os.system("sudo apt install dnschef")
		elif option == "3":
			cmd = os.system("sudo apt install fiked")
		elif option == "4":
			cmd = os.system("sudo apt install hamster-sidejack")
		elif option == "5":
			cmd = os.system("sudo apt install hexinject")
		elif option == "6":
			cmd = os.system("sudo apt install iaxflood")
		elif option == "7":
			cmd = os.system("sudo apt install inviteflood")
		elif option == "8":
			cmd = os.system("sudo apt install ismtp")
		elif option == "9":
			cmd = os.system("sudo apt install isr-evilgrade")
		elif option == "10":
			cmd = os.system("sudo apt install mitmproxy")
		elif option == "11":
			cmd = os.system("sudo apt install ohrwurm")
		elif option == "12":
			cmd = os.system("sudo apt install protos-sip")
		elif option == "13":
			cmd = os.system("sudo apt install rebind")
		elif option == "14":
			cmd = os.system("sudo apt install responder")
		elif option == "15":
			cmd = os.system("sudo apt install rtpbreak")
		elif option == "16":
			cmd = os.system("sudo apt install rtpinsertsound")
		elif option == "17":
			cmd = os.system("sudo apt install rtpmixsound")
		elif option == "18":
			cmd = os.system("sudo apt install sctpscan")
		elif option == "19":
			cmd = os.system("sudo apt install siparmyknife")
		elif option == "20":
			cmd = os.system("sudo apt install sipp")
		elif option == "21":
			cmd = os.system("sudo apt install sipvicious")
		elif option == "22":
			cmd = os.system("sudo apt install sniffjoke")
		elif option == "23":
			cmd = os.system("sudo apt install sslsplit")
		elif option == "24":
			cmd = os.system("sudo apt install sslstrip")
		elif option == "25":
			cmd = os.system("sudo apt install thc-ipv6")
		elif option == "26":
			cmd = os.system("sudo apt install voiphopper")
		elif option == "27":
			cmd = os.system("sudo apt install webscarab")
		elif option == "28":
			cmd = os.system("sudo apt install wifi-honey")
		elif option == "29":
			cmd = os.system("sudo apt install wireshark")
		elif option == "30":
			cmd = os.system("sudo apt install xspy")
		elif option == "31":
			cmd = os.system("sudo apt install yersinia")
		elif option == "32":
			cmd = os.system("sudo apt install zaproxy")
		elif option == "99":
			cmd = os.system("sudo apt install -y burpsuite dnschef fiked hamster-sidejack hexinject iaxflood inviteflood ismtp")
			cmd = os.system("apt install -y isr-evilgrade mitmproxy ohrwurm protos-sip rebind responder rtpbreak rtpinsertsound")
			cmd = os.system("apt install -y rtpmixsound sctpscan siparmyknife sipp sipvicious sniffjoke sslsplit sslstrip thc-ipv6")
			cmd = os.system("apt install -y voiphopper webscarab wifi-honey wireshark xspy yersinia zaproxy")
			cmd = os.system("apt -f install")