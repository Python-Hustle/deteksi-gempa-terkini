import requests
from bs4 import BeautifulSoup

url = 'http://www.google.com'
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6)'
                         'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}


def ekstrasi_data():
    try:
        content = requests.get('https://www.bmkg.go.id', headers=headers)
    except Exception:
        return None

    if content.status_code == 200:
        print(content.status_code)
        soup = BeautifulSoup(content.text, 'html.parser')

        # CARA PERTAMA ------
        result = soup.find('span', {"class": "waktu"})
        result = result.text.split(',')
        waktu = result[0]
        tanggal = result[1]


        # #CARA ALTERNATIF 2
        # result = soup.find('ul', {"class": "list-unstyled"})


        #CARA ALTERNATIF 3
        result = soup.find('div', {"class":"col-md-6 col-xs-6 gempabumi-detail no-padding" })
        result = result.findChildren('li')

        i = 0
        magnitudo = None
        kedalaman = None
        lokasi = None
        ls = None
        bt = None
        pusat = None
        dirasakan = None

        for res in result:
            print(i, res)
            if i == 1:
                magnitudo = res.text

            elif i == 2:
                kedalaman = res.text

            elif i == 4:
                lokasi = res.text

            elif i == 3:
                koordinat = res.text.split(' - ')
                ls = koordinat[0]
                bt = koordinat[1]

            elif i == 5:
                dirasakan = res.text
            i = i + 1



        hasil = dict()


        hasil['waktu'] = waktu
        hasil['tanggal'] = tanggal
        hasil['magnitudo'] = magnitudo
        hasil['kedalaman'] = kedalaman
        hasil['lokasi'] = lokasi
        hasil['koordinat'] = {'ls': ls, 'bt': bt}
        hasil['dirasakan'] = dirasakan

        return hasil
    else:
        return None


def tampilkan_data(result):
    if result is None:
        print("tidak bisa menemukan data gempa terkini")
        return

    print("Gempa terkini berdasarkan BMKG")
    print(f"Waktu : {result['waktu']}")
    print(f"Tanggal : {result['tanggal']}")
    print(f"Magnitudo : {result['magnitudo']}")
    print(f"Kedalaman : {result['kedalaman']}")
    print(f"Lokasi : {result['lokasi']}")
    print(f"Koordinat : {result['koordinat']['ls']} - {result['koordinat']['bt']}")
    print(f"Dirasakan : {result['dirasakan']}")

