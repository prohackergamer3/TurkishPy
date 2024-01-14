import os,time,ctypes
try:
	import colorama
except:
	pass
	
def renkliyazikutuphanesinikullan():
	import colorama
def yazdir(metin):
	print(metin)


	
def yorum(metin):
		pass
	

def sistemkutuphanesinikullan():
	import ctypes
	
def fareklavyekilitle(bol):
	ctypes.windll.user32.BlockInput(bool(bol))

	
def sistemekomutver(cmd):
		os.system(cmd)


def zamankutuphanesinikullan():
		import time
			
def bekle(sure):
	time.sleep(int(sure))		
	
	
kullaniciadi = os.getlogin()
klasor = os.getcwd()
		