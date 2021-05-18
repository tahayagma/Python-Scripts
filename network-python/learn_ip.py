import socket # burada socket kütüphanemizi iç aktardık
print(r"""                             
                                         
  _ _ _ _ _ _ _       \ \         / /  
 |   _ _ _ _ _  \      \ \       / /   _
 |  |         \  \      \ \     / /   |_|       _      _
 |  |          |  |      \ \   / /     _       \ \    / / 
 |  | _ _ _ _ _/ /        \ \ / /     | |       \ \  / /
 |  | _ _ _ _ _ /          \   /      | |        \ \/ /
 |  |                       | |       | |         \ \/
 |  |                       | |       | |         /\ \
 |  |                       | |       | |        / /\ \
 |_ |                       |_|       |_|       /_/  \_\  ©2019


                    LEARN IP ADDRESS FOR WEB PAGE V.1
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _
""")
computer_name = socket.gethostname()
computer_ip = socket.gethostbyname(computer_name)
print("DİKKAT ! Verilen IP adresleri kesinlik belirtmemektedir.")
print("Cihaz Adınız:{} ve IP adresiniz:{}".format(computer_name,computer_ip))
print("-------------------------------------------------------------------------")
def net_protocol(hostname):
    try:#ardından basit bir fonksiyon tanımlayarak işlemi gerçekleştirdik
        addr = socket.gethostbyname(hostname) # bu kod bloğunda hostnameyi parametre olarak veridik
        print("{} web sayfasının IP adresi: {} ".format(hostname,addr))
    except:
        print("Lütfen ağ bağlantınızı kontrol edin veya {} adında web adresi bulunmamaktadır.".format(hostname))

if __name__ == '__main__':
    while True:
        web_page_name =str(input("Bir web adresi girin >>"))
        net_protocol(web_page_name) # son olarak  fonksiyonumuza bir web adresi parametre olarak gönderdik.
