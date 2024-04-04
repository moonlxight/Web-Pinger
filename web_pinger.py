import subprocess
from colorama import Fore, Style, init
init()

def ping_simple(url, count, timeout):
    try:
        # Ping işlemini gerçekleştirme
        result = subprocess.run(["ping", "-c", str(count), url], capture_output=True, text=True, timeout=timeout)
    
        # Ping sonucunu kontrol etme
        if result.returncode == 0:
            return True, result.stdout.strip()
        else:
            return False, result.stderr.strip()
    except subprocess.TimeoutExpired:
        return False, "Ping işlemi zaman aşımına uğradı."
    except Exception as e:
        return False, f"Ping işlemi sırasında bir hata meydana geldi: {str(e)}"

def ping_with_size(url, count, size, timeout):
    try:
        # Ping işlemini gerçekleştirme
        result = subprocess.run(["ping", "-c", str(count), "-s", str(size), url], capture_output=True, text=True, timeout=timeout)
    
        # Ping sonucunu kontrol etme
        if result.returncode == 0:
            return True, result.stdout.strip()
        else:
            return False, result.stderr.strip()
    except subprocess.TimeoutExpired:
        return False, "Ping işlemi zaman aşımına uğradı."
    except Exception as e:
        return False, f"Ping işlemi sırasında bir hata meydana geldi: {str(e)}"

def ping_with_timeout(url, count, timeout, size=56):
    try:
        # Ping işlemini gerçekleştirme
        result = subprocess.run(["ping", "-c", str(count), "-s", str(size), "-W", str(timeout), url], capture_output=True, text=True, timeout=timeout)
    
        # Ping sonucunu kontrol etme
        if result.returncode == 0:
            return True, result.stdout.strip()
        else:
            return False, result.stderr.strip()
    except subprocess.TimeoutExpired:
        return False, "Ping işlemi zaman aşımına uğradı."
    except Exception as e:
        return False, f"Ping işlemi sırasında bir hata meydana geldi: {str(e)}"

def main_menu():
    print(Fore.LIGHTGREEN_EX + Style.BRIGHT + "Ping Menüsü")
    print("-----------------")
    print("1: Basit ping gönder")
    print("2: Paket boyutunu belirterek ping gönder")
    print("3: Ping gönderme süresini ayarla")
    print("4: Programı kapat")
    print(Style.RESET_ALL)

while True:
    main_menu()
    choice = input("Lütfen seçim yapınız: ")

    if choice == "1":
        url = input("Lütfen ping atmak istediğiniz URL'yi girin: ")
        count = int(input("Kaç ping göndermek istiyorsunuz?: "))
        timeout = int(input("Ping gönderme süresini belirleyin (saniye cinsinden): "))
        success, result = ping_simple(url, count, timeout)
        if success:
            print(Fore.LIGHTGREEN_EX + f"{url} adresine ping başarıyla gönderildi!")
            print("Ping sonucu:", result)
        else:
            print(Fore.RED + f"{url} adresine ping gönderilirken bir hata meydana geldi!")
            print("Hata mesajı:", result)
        print(Style.RESET_ALL)
    elif choice == "2":
        url = input("Lütfen ping atmak istediğiniz URL'yi girin: ")
        count = int(input("Kaç ping göndermek istiyorsunuz?: "))
        size = int(input("Paket boyutunu belirleyin (varsayılan 56 byte): "))
        timeout = int(input("Ping gönderme süresini belirleyin (saniye cinsinden): "))
        success, result = ping_with_size(url, count, size, timeout)
        if success:
            print(Fore.LIGHTGREEN_EX + f"{url} adresine ping başarıyla gönderildi!")
            print("Ping sonucu:", result)
        else:
            print(Fore.RED + f"{url} adresine ping gönderilirken bir hata meydana geldi!")
            print("Hata mesajı:", result)
        print(Style.RESET_ALL)
    elif choice == "3":
        url = input("Lütfen ping atmak istediğiniz URL'yi girin: ")
        count = int(input("Kaç ping göndermek istiyorsunuz?: "))
        timeout = int(input("Ping gönderme süresini belirleyin (saniye cinsinden): "))
        success, result = ping_with_timeout(url, count, timeout)
        if success:
            print(Fore.LIGHTGREEN_EX + f"{url} adresine ping başarıyla gönderildi!")
            print("Ping sonucu:", result)
        else:
            print(Fore.RED + f"{url} adresine ping gönderilirken bir hata meydana geldi!")
            print("Hata mesajı:", result)
        print(Style.RESET_ALL)
    elif choice == "4":
        print("Programdan çıkılıyor...")
        break
    else:
        print(Fore.LIGHTYELLOW_EX + "Böyle bir seçenek yok.")
        print(Style.RESET_ALL)
