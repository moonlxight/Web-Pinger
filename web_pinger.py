import os
import sys
import subprocess
import colorama
from colorama import Fore, Style, init
init()

def ping_url(url, count):
    # Ping işlemini gerçekleştirme
    result = subprocess.run(["ping", "-c", str(count), url], capture_output=True, text=True)
    
    # Ping sonucunu kontrol etme
    if result.returncode == 0:
        return True, result.stdout.strip()
    else:
        return False, result.stderr.strip()

def main_menu():
    print(Fore.LIGHTGREEN_EX + Style.BRIGHT + "Ping Menüsü")
    print("-----------------")
    print("1. Ping Gönder")
    print(Style.RESET_ALL)

while True:
    main_menu()
    choice = input("Lütfen seçim yapınız: ")

    if choice == "1":
        url = input("Lütfen ping atmak istediğiniz URL'yi girin: ")
        count = int(input("Kaç ping göndermek istiyorsunuz?: "))
        success, result = ping_url(url, count)
        if success:
            print(Fore.LIGHTGREEN_EX + f"{url} adresine ping başarıyla gönderildi.")
            print("Ping sonucu:", result)
        else:
            print(Fore.RED + f"{url} adresine ping gönderilirken bir hata meydana geldi!")
            print("Hata mesajı:", result)
        print(Style.RESET_ALL)
    elif choice == "2":
        print("Programdan çıkılıyor...")
        break
    else:
        print(Fore.LIGHTYELLOW_EX + "Böyle bir seçenek yok.")
        print(Style.RESET_ALL)