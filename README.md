# Otomasi-Pengujian-Web
Projek ini berisi script untuk melakukan otomasi pengujian pada website http://automationpractice.com

Tools :
- Python3 (Versi python yang digunakan Python 3.7.1)
- pip3
- Selenium binding python
- Chromedriver

How to :
```bash 
git clone https://github.com/irwanhub2016/Otomasi-Pengujian-Web.git
```
- Masuk ke folder Otomasi-Pengujian-Web
- Install paket yang diperlukan dengan pip3 dengan cara :
```bash
 pip3 install -r requirements.txt
```
- Apabila terdapat error pada chrome driver, ikuti langkah alternatif berikut :
```bash
 git clone https://github.com/peterhudec/chromedriver_installer.git
```
- Kemudian jalankan :
```bash
python3 chromedriver_installer/setup.py install --chromedriver-version=2.10
```
- Buat file .env dan isi variable 'URL' didalam .env dengan link url website (Abaikan step ini jika sudah ada file .env, dalam Repo ini sudah tersedia file .env)
- Aktivasi environment venv :
```bash
source env/bin/activate
```
- Jalankan test :
```bash
python3 [test_case_name.py] ( dalam repo ini terdapat 5 test case untuk automation test )
```

Proses eksekusi test berjalan dalam mode headless atau tanpa GUI.
```python

    options = webdriver.ChromeOptions()
		options.add_argument("--incognito")
		options.add_argument("--headless")
		options.add_argument("--no-sandbox")
		options.headless = True
    self.driver = webdriver.Chrome(chrome_options=options)
```
