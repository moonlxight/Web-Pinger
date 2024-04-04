# >>=========================================================<<
# ||  ______         _      __            __               __||
# || /_  __/      __(_)____/ /___  __    / /__  ____ _____/ /||
# ||  / / | | /| / / / ___/ __/ / / /_  / / _ \/ __ `/ __  / ||
# || / /  | |/ |/ / (__  ) /_/ /_/ / /_/ /  __/ /_/ / /_/ /  ||
# ||/_/   |__/|__/_/____/\__/\__, /\____/\___/\__,_/\__,_/   ||
# ||                        /____/                           ||
# >>=========================================================<<
#           Tʜɪꜱ ᴘʀᴏᴊᴇᴄᴛ ᴡᴀꜱ ᴅᴇᴠᴇʟᴏᴘᴇᴅ ʙʏ TᴡɪꜱᴛʏJᴇᴀᴅ ツ
#                    ɢɪᴛʜᴜʙ.ᴄᴏᴍ/ᴍᴏᴏɴʟxɪɢʜᴛ

import os
import sys
import subprocess  # Harici işlemler çağırmak için
import socket  # Ağ işlemleri için
import colorama
from colorama import Fore, Style, init

init()
os.system("title TwistyJead's Web Pinging Tool")
def web_pinger_art():
    sys.stderr.writelines(Fore.LIGHTCYAN_EX + """
                                     _       __     __    ____  _                      
                                    | |     / /__  / /_  / __ \(_)___  ____ ____  _____
                                    | | /| / / _ \/ __ \/ /_/ / / __ \/ __ `/ _ \/ ___/
                                    | |/ |/ /  __/ /_/ / ____/ / / / / /_/ /  __/ /    
                                    |__/|__/\___/_.___/_/   /_/_/ /_/\__, /\___/_/     
                                                                    /____/             
""")
def menu():
    # Ekran temizleniyor
    if os.name == "nt":  # Windows işletim sistemini algıla
        os.system("cls") # Windows'un ekran temizleme komutu
    else:  # Diğer işletim sistemleri için (Linux/MacOS)
        os.system("clear")

    web_pinger_art()
    
    sys.stdout.write(Fore.LIGHTCYAN_EX + "Seçenekler:" + "\n")
    sys.stdout.write(Fore.LIGHTYELLOW_EX + "[1] " + Fore.LIGHTCYAN_EX + "Belirli bir URL'ye sürekli ping gönder" + "\n")
    sys.stdout.write(Fore.LIGHTYELLOW_EX + "[2] " + Fore.LIGHTCYAN_EX + "Girilen DNS'nin ana adresini çöz" + "\n")
    sys.stdout.write(Fore.LIGHTYELLOW_EX + "[3] " + Fore.LIGHTCYAN_EX + "Programı kapat" + "\n")

# Ana döngüyü başlatan fonksiyon
def main():
    while True:
        # Ana menüyü göster
        menu()
        
        # Kullanıcıdan seçim yapmasını iste
        choice = input("\n" + Fore.LIGHTYELLOW_EX + "Lütfen bir seçenek numarası girin: " + Fore.LIGHTCYAN_EX)

        # Kullanıcının seçimine göre işlem yap
        if choice == "1":
            ping_continuous()
        elif choice == "2":
            resolve_address()
        elif choice == "3":
            print("Program kapatılıyor...")
            break
        else:
            print("Geçersiz seçenek! Lütfen yeniden deneyin.")

# Belirli bir URL'ye sürekli ping gönderen fonksiyon
def ping_continuous():
    # Windows veya diğer işletim sistemleri için ekran temizleme işlemleri bölümü
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

    web_pinger_art()
    url = input("Lütfen ping atmak istediğiniz URL'yi girin: ") # Kullanıcıdan ping atılacak URL'yi al
    
    try:
        while True:
            process = subprocess.Popen(["ping", "-t", url], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True) # Ping işlemini gerçekleştirir

            try:
                for line in process.stdout:
                    print(line.strip())
            except KeyboardInterrupt: # Ctrl+C kısayolunu dinler
                print("\nPing gönderme işlemi durduruldu.") # Ctrl+C'ye basıldığında ping işlemini durdur
                break
            finally:
                # İşlem tamamlandığında "process" yani "işlem" mnanasına gelen nesneyi sonlandır
                process.terminate()
                process.wait()
                
    except Exception as e:
        print("Bir hata oluştu:", e)

def resolve_address(): # Girilen URL'nin IP adresini çözen fonksiyon
    # Windows veya diğer işletim sistemleri için ekran temizleme işlemleri bölümü
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")
    
    web_pinger_art()
    
    address = input(Fore.LIGHTYELLOW_EX + " [>] " + Fore.LIGHTCYAN_EX + "Lütfen çözümlemek istediğiniz URL'yi girin: ") # Kullanıcıdan çözümlenmek istenen URL'yi al
    
    try:
        # URL'nin IP adresini çözme işlemi
        resolved_addresses = socket.getaddrinfo(address, None)
        
        # Çözümlenen IP adreslerini ekrana yazdırma kısmı
        print(Fore.LIGHTCYAN_EX + f"{address} adresinin çözümlenmiş IP adresleri:")
        for item in resolved_addresses:
            print(Fore.LIGHTMAGENTA_EX + item[4][0]) # Çözümlenen IP adreslerini ekrana yazdır
            input("\n" + Fore.LIGHTYELLOW_EX + " [?] " + "Enter'a basarak tekrar ana menüye geçiş yapın.")  # Enter yerine başka tuşları da tıklasa her türlü geçer
    except Exception as e:
        print("Bir hata oluştu:", e)

# Ana program bölümü
if __name__ == "__main__":
    main()  # Ana döngüyü başlatır