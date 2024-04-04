import os  # Sistemle ilgili işlemler için
import sys  # Sistemle ilgili işlemler için
import subprocess  # Harici işlemler çağırmak için
import socket  # Ağ işlemleri için
import colorama  # Renkli metinler için kütüphane
from colorama import Fore, Style, init  # Renkli metinler için

# Renkli metinler için colorama'nın başlatılması
init()

# Web pinger başlığı için ASCII sanatını çizen fonksiyon
def web_pinger_art():
    # ASCII sanatı çizimi
    sys.stderr.writelines(Fore.LIGHTCYAN_EX + """
                                     _       __     __    ____  _                      
                                    | |     / /__  / /_  / __ \(_)___  ____ ____  _____
                                    | | /| / / _ \/ __ \/ /_/ / / __ \/ __ `/ _ \/ ___/
                                    | |/ |/ /  __/ /_/ / ____/ / / / / /_/ /  __/ /    
                                    |__/|__/\___/_.___/_/   /_/_/ /_/\__, /\___/_/     
                                                                    /____/             
""")

# Ana menüyü gösteren fonksiyon
def menu():
    # Ekran temizleniyor
    if os.name == "nt":  # Windows işletim sistemi için temizlik işlemi
        os.system("cls")
    else:  # Diğer işletim sistemleri için
        os.system("clear")
    
    # Web pinger başlığını ekrana yazdırma
    web_pinger_art()
    
    # Kullanıcıya seçeneklerin listesini gösterme
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
    # Windows veya diğer işletim sistemleri için temizlik işlemi
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")
    
    # Web pinger başlığını ekrana yazdırma
    web_pinger_art()
    
    # Kullanıcıdan ping atılacak URL'yi al
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

# Girilen URL'nin IP adresini çözen fonksiyon
def resolve_address():
    # Windows veya diğer işletim sistemleri için temizlik işlemi
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")
    
    # Web pinger başlığını ekrana yazdırma
    web_pinger_art()
    
    # Kullanıcıdan çözümlenmek istenen URL'yi al
    address = input(Fore.LIGHTYELLOW_EX + " [>] " + Fore.LIGHTCYAN_EX + "Lütfen çözümlemek istediğiniz URL'yi girin: ")
    
    try:
        # URL'nin IP adresini çözme işlemi
        resolved_addresses = socket.getaddrinfo(address, None)
        
        # Çözümlenen IP adreslerini ekrana yazdırma
        print(Fore.LIGHTCYAN_EX + f"{address} adresinin çözümlenmiş IP adresleri:")
        for item in resolved_addresses:
            print(Fore.LIGHTMAGENTA_EX + item[4][0])
            input("\n" + Fore.LIGHTYELLOW_EX + " [?] " + "Enter'a basarak tekrar ana menüye geçiş yapın.")
    except Exception as e:
        print("Bir hata oluştu:", e)

# Ana program bölümü
if __name__ == "__main__":
    main()  # Ana döngüyü başlatma
