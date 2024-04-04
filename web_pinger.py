import subprocess

def ping_url(url):
    # Ping işlemini gerçekleştirme
    process = subprocess.Popen(["ping", "-c", "1", url], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = process.communicate()

    # Ping sonucunu kontrol etme
    if "1 packets transmitted, 1 received" in output.decode():
        return True
    else:
        return False

# Test etmek için bir URL girin
url = input("Lütfen ping atmak istediğiniz URL'yi girin: ")

if ping_url(url):
    print(f"{url} adresine ping başarıyla gönderildi.")
else:
    print(f"{url} adresine ping gönderilirken bir hata oluştu.")
