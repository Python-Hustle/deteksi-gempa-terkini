"""
APLIKASI GEMPA TERKINI WILAYAH INDONESIA
"""
from gempaterkini import ekstrasi_data

if __name__ == '__main__':
    print('Aplikasi utama')
    result = ekstrasi_data()
    tampilkan_data(result)
