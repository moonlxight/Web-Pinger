import subprocess

def main():
    print("Ping Programına Hoş Geldiniz!")
    print("-----------------------------")

    while True:
        print("Seçenekler:")
        print("1: Belirli bir URL'e sürekli ping gönderme")
        print("2: Adresleri ana bilgisayarlara çözme")
        print("3: Echo isteği sayısı belirleme")
        print("4: Gönderilen veri paketi boyutunu belirleme")
        print("5: İnternet Protokolü sürümünü belirleme")
        print("6: Paketlerin Parçalanmasını Engelleyin")
        print("7: Zaman Aşımı Belirleme")
        print("8: Programı Kapat")

        choice = input("Lütfen bir seçenek numarası girin: ")

        if choice == "1":
            ping_continuous()
        elif choice == "2":
            resolve_addresses()
        elif choice == "3":
            set_echo_count()
        elif choice == "4":
            set_packet_size()
        elif choice == "5":
            set_ip_version()
        elif choice == "6":
            set_fragmentation()
        elif choice == "7":
            set_timeout()
        elif choice == "8":
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
    pass

def set_echo_count():
    # Echo isteği sayısını belirleyin
    pass

def set_packet_size():
    # Gönderilen veri paketi boyutunu belirleyin
    pass

def set_ip_version():
    # İnternet Protokolü sürümünü belirleyin
    pass

def set_fragmentation():
    # Paketlerin Parçalanmasını Engelleyin
    pass

def set_timeout():
    # Zaman aşımını belirleyin
    pass

if __name__ == "__main__":
    main()