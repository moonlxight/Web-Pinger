import os
import sys
import subprocess
import socket
import colorama
from colorama import Fore, Style, init
from os import system, name
from sys import stdout, stderr
init()

def web_pinger_art():
    stderr.writelines(Fore.LIGHTCYAN_EX + """
                                     _       __     __    ____  _                      
                                    | |     / /__  / /_  / __ \(_)___  ____ ____  _____
                                    | | /| / / _ \/ __ \/ /_/ / / __ \/ __ `/ _ \/ ___/
                                    | |/ |/ /  __/ /_/ / ____/ / / / / /_/ /  __/ /    
                                    |__/|__/\___/_.___/_/   /_/_/ /_/\__, /\___/_/     
                                                                    /____/             
""")

def menu():
    if name == "nt":
        os.system("cls")
    else:
        os.system("clear")
    web_pinger_art()
    stdout.write(Fore.LIGHTCYAN_EX + "Seçenekler:" + "\n")
    stdout.write(Fore.LIGHTYELLOW_EX + "[1] " + Fore.LIGHTCYAN_EX + "Belirli bir URL'ye sürekli ping gönder" + "\n")
    stdout.write(Fore.LIGHTYELLOW_EX + "[2] " + Fore.LIGHTCYAN_EX + "Girilen DNS'nin ana adresini çöz" + "\n")
    stdout.write(Fore.LIGHTYELLOW_EX + "[3] " + Fore.LIGHTCYAN_EX + "Programı kapat" + "\n")
def main():
    while True:
        menu()
        choice = input("\n" + Fore.LIGHTYELLOW_EX + "Lütfen bir seçenek numarası girin: " + Fore.LIGHTCYAN_EX)

        if choice == "1":
            ping_continuous()
        elif choice == "2":
            resolve_addresses()
        elif choice == "3":
            print("Program kapatılıyor...")
            break
        else:
            print("Geçersiz seçenek! Lütfen yeniden deneyin.")

def ping_continuous():
    # Belirli bir URL'ye sürekli ping gönderme işlemini gerçekleştirir, ismi üzerinden de anlaşılacağı üzere ping_continuous; devamlı olarak pinglenmesini ifade eder.
    url = input("Lütfen ping atmak istediğiniz URL'yi girin: ")
    
    try:
        while True:
            # Ping işlemini gerçekleştirme
            process = subprocess.Popen(["ping", "-t", url], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

            try:
                # Ping sonuçlarını alarak işlemi bekletme
                for line in process.stdout:
                    print(line.strip())
            except KeyboardInterrupt:
                # Ctrl+C'ye basıldığında ping işlemini durdur
                print("\nPing gönderme işlemi durduruldu.")
                break
            finally:
                # İşlem tamamlandığında process objesini sonlandır
                process.terminate()
                process.wait()
                
    except Exception as e:
        print("Bir hata oluştu:", e)

def resolve_addresses():
    # Adresleri ana bilgisayarlara çözme işlemini gerçekleştirin

    """
    Verilen bir URL veya IP adresinin ana bilgisayarlara çözülmesini sağlar.
    """
    if name == "nt":
        os.system("cls")
    else:
        os.system("clear")
        web_pinger_art()
    address = input(Fore.LIGHTYELLOW_EX + " [>] " + Fore.LIGHTCYAN_EX + "Lütfen çözümlemek istediğiniz URL veya IP adresini girin: ")
    try:
        # Adresi çözümleme işlemi
        resolved_addresses = socket.getaddrinfo(address, None)
        
        print(Fore.LIGHTCYAN_EX + f"{address} adresinin çözümlenmiş IP adresleri:")
        for item in resolved_addresses:
            print(Fore.LIGHTMAGENTA_EX + item[4][0])
            input("\n" + Fore.LIGHTYELLOW_EX + " [?] " + "Enter'a basarak tekrar ana menüye geçiş yapın.")
    except Exception as e:
        print("Bir hata oluştu:", e)

if __name__ == "__main__":
    main()