from datetime import datetime

now = datetime.now()
suan= '\n'+str(now)
file = open(r"C:\Users\akmet\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\system.txt","a")
file.write(suan)
file.close()