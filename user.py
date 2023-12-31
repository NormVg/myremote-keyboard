import requests,sys,datetime,time
from termcolor import cprint


base = "http://127.0.0.1:5000/"
cli = requests.Session()


keys_ = ['accept', 'add', 'alt', 'altleft', 'altright', 'apps', 'backspace',
'browserback', 'browserfavorites', 'browserforward', 'browserhome',
'browserrefresh', 'browsersearch', 'browserstop', 'capslock', 'clear',
'convert', 'ctrl', 'ctrlleft', 'ctrlright', 'decimal', 'del', 'delete',
'divide', 'down', 'end', 'enter', 'esc', 'escape', 'execute', 'f1', 'f10',
'f11', 'f12', 'f13', 'f14', 'f15', 'f16', 'f17', 'f18', 'f19', 'f2', 'f20',
'f21', 'f22', 'f23', 'f24', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8', 'f9',
'final', 'fn', 'hanguel', 'hangul', 'hanja', 'help', 'home', 'insert', 'junja',
'kana', 'kanji', 'launchapp1', 'launchapp2', 'launchmail',
'launchmediaselect', 'left', 'modechange', 'multiply', 'nexttrack',
'nonconvert', 'num0', 'num1', 'num2', 'num3', 'num4', 'num5', 'num6',
'num7', 'num8', 'num9', 'numlock', 'pagedown', 'pageup', 'pause', 'pgdn',
'pgup', 'playpause', 'prevtrack', 'print', 'printscreen', 'prntscrn',
'prtsc', 'prtscr', 'return', 'right', 'scrolllock', 'select', 'separator',
'shift', 'shiftleft', 'shiftright', 'sleep', 'space', 'stop', 'subtract', 'tab',
'up', 'volumedown', 'volumemute', 'volumeup', 'win', 'winleft', 'winright', 'yen',
'command', 'option', 'optionleft', 'optionright']



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
	inp = input(f"{datetime.datetime.now().strftime('%H:%M:%S')} $$ > ")

	if inp.startswith("/key-list"):
		for i in keys_:
			cprint(i,"cyan")

	if inp.startswith("/key"):
		inp = inp.replace("/key ","")
		try:
        	        res = cli.get(base+"user-key?key="+inp)
		except:
        	        cprint("error","red")
	else:
		try:
			res = cli.get(base+"user-txt?text="+inp)
		except:
			cprint("error","red")
