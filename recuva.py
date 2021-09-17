import os
import subprocess

disk_name = input("login disk type(E,F,G etc..):")
print("""
All Right Reversed © 2021  by Taha Yagma
----------------------------------------

  --> Özel dosya uzantisi aramak için 1'e bas

  --> Özel belge adı ile aramak yapmak icin 2'e bas
  
  --> Tüm Dosyalari aramak için 3'e bas
  
-----------------------------------------
""")
while True:
    chose = int(input("lütfen bir islem secin:"))
    if chose != 1 and chose != 2:
        print("Lütfen gecerli bir islem girin")
        continue
    else:
        if chose == 1:
            file_type = input("Lütfen dosya uzantısı gir(.docx .pdf .png  ...):")
            for r, d, f in os.walk(f"{disk_name}:\\"):
                for file in f:
                    filepath = os.path.join(r, file)    
                    if f"{file_type}" in file:
                        print(os.path.join(r, file))
        elif chose == 2:
            file_name = input("Lütfen belge adını gir gir:")
            for r, d, f in os.walk(f"{disk_name}:\\"):
                for file in f:
                    filepath = os.path.join(r, file)
                    if f"{file_name}" in file:
                        print(os.path.join(r, file))
        else:
            for r, d, f in os.walk(f"{disk_name}:\\"):
                for file in f:
                    filepath = os.path.join(r, file)
                    if "." in file:
                        print(os.path.join(r, file))
                
            #Popen(r"copy {} {}\system".format(os.path.join(r, file),os.getcwd()), shell=True, stderr=PIPE, stdout=PIPE)
            #elif ".jpg" in file:
                #Popen(r"copy {} {}\system".format(os.path.join(r, file), os.getcwd()), shell=True, stderr=PIPE, stdout=PIPE)
