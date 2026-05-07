
import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

def scrape_produk(url):
    # Header agar tidak dianggap bot oleh website target
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }

    print(f"Menghubungi: {url}...")
    response = requests.get(url, headers=headers)
    
    if response.status_code != 200:
        print(f"Gagal akses! Status Code: {response.status_code}")
        return []

    soup = BeautifulSoup(response.text, 'html.parser')
    
    # List untuk menampung hasil
    hasil_data = []

    # CONTOH LOGIC (Ini perlu disesuaikan dengan struktur HTML website target)
    # Misal kita mencari elemen produk dalam tag <div> dengan class 'product-item'
    produk_items = soup.find_all('div', class_='product-item') # Ganti class sesuai target

    for item in produk_items:
        try:
            nama = item.find('h2').text.strip() # Ganti tag sesuai target
            harga = item.find('span', class_='price').text.strip() # Ganti tag sesuai target
            
            hasil_data.append({
                'Nama Produk': nama,
                'Harga': harga
            })
        except AttributeError:
            continue

    return hasil_data

if __name__ == "__main__":
    # URL Target (Ganti dengan link marketplace atau web toko yang ingin di-scrape)
    target_url = "https://example-shopping-site.com/products" 
    
    data = scrape_produk(target_url)
    
    if data:
        # Simpan ke Excel/CSV otomatis
        df = pd.DataFrame(data)
        df.to_csv('hasil_scrape.csv', index=False)
        print("Scraping Selesai! Data disimpan di hasil_scrape.csv")
        print(df.head())
    else:
        print("Data tidak ditemukan. Pastikan 'class' atau 'tag' HTML sudah sesuai dengan web target.")
