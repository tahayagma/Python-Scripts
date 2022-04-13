import zipfile
import os
code = input("Cihaz sifresini girin.\nAksi halde 10 saniye sonra cihaz kapanacaktir:\n")
if len(code) !=0:
    if code == "1286":
        print("misafir girisi yapilmistir")
        os.system("shutdown -a")
        zfile =  zipfile.ZipFile(r"C:\Users\akmet\Desktop\arduino-1.8.16\examples\01.Basics\AnalogReadSerial\files12.zip","w")
        zfile.setpassword(b"password")
        for r, d, f in os.walk(r"C:\Users\akmet\Desktop\arduino-1.8.16\examples\01.Basics\AnalogReadSerial"):
            for x in f:
                if ".camrec" in x:
                    filepath = os.path.join(r, x)
                    zfile.write(f"{filepath}")
                    os.system(f"del {filepath}")
                elif ".camproj" in x:
                    filepath = os.path.join(r, x)
                    zfile.write(f"{filepath}")
                    os.system(f"del {filepath}")
        zfile.close()
        os.system("attrib +h C:\Users\akmet\Desktop\arduino-1.8.16\examples\01.Basics\AnalogReadSerial\files12.zip")
    elif code == "kk":
        print("admin root girisi")
        os.system("shutdown -a")