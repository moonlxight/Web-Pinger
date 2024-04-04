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
    print("""
 _       __     __    ____  _                      
| |     / /__  / /_  / __ \(_)___  ____ ____  _____
| | /| / / _ \/ __ \/ /_/ / / __ \/ __ `/ _ \/ ___/
| |/ |/ /  __/ /_/ / ____/ / / / / /_/ /  __/ /    
|__/|__/\___/_.___/_/   /_/_/ /_/\__, /\___/_/     
                                /____/             
""")

def main():
    print("Ping Programına Hoş Geldiniz!")
    print("-----------------------------")

    while True:
        stdout.write("Seçenekler:")
        print("1: Belirli bir URL'e sürekli ping gönderme")
        print("2: Adresleri ana bilgisayarlara çözme")
        print("3: Programı kapat")

        choice = input("Lütfen bir seçenek numarası girin: ")

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
    """
    Belirli bir URL'ye sürekli ping gönderme işlemini gerçekleştirir.
    """
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
    address = input("Lütfen çözümlemek istediğiniz URL veya IP adresini girin: ")

    try:
        # Adresi çözümleme işlemi
        resolved_addresses = socket.getaddrinfo(address, None)
        
        print(f"{address} adresinin çözümlenmiş IP adresleri:")
        for item in resolved_addresses:
            print(item[4][0])
    except Exception as e:
        print("Bir hata oluştu:", e)

if __name__ == "__main__":
    main()