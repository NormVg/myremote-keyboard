import requests,sys,datetime,time
from termcolor import cprint
from pyautogui import write , hotkey

base = "http://127.0.0.1:5000/"
cli = requests.Session()

def write_txt(text):
	write(text, interval=0.2)

def press_keyg(ar):
	hotkey(*ar)

try:
	cprint("<-- Trying to connect to server -->","yellow")
	e = cli.get(base).status_code
	if e == 200:
		cprint("connected to server","green")
except:
	cprint("can not find the server , connection failed","red")
	sys.exit()

cprint("you can enjoy writing now","cyan")
while True:
	time.sleep(1)
	cprint(datetime.datetime.now(),"yellow")
	try:
		res = cli.get(base+"operator")
		data = res.json()
		for i in data:
			if i[0] == 'key':
				cprint(i[1],"cyan")
				keys = i[1].split(" ")
				press_keyg(keys)
			else:
				cprint(i[1],"cyan")
				write_txt(i[1])
	except:
		cprint("error","red")
