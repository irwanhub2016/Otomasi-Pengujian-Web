# Otomasi-Pengujian-Web
Projek ini berisi script untuk melakukan otomasi pengujian pada website http://automationpractice.com/index

Tools :
- Python3
- pip3
- Selenium binding python
- Chromedriver
- HtmlTestRunner

How to :
- git clone https://github.com/irwanhub2016/Otomasi-Pengujian-Web.git
- Install paket yang diperlukan dengan pip3 
- pip3 install -r requirements.txt
- Buat file .env dan isi variable 'URL' didalam .env dengan link url website (Abaikan step ini jika sudah ada file .env, dalam Repo ini sudah tersedia file .env)
- Aktivasi environment venv :
  - source env/bin/activate
- Jalankan test :
  - python3 [test_case_name.py]
- Secara otomatis Report test akan ter-generate setelah jalankan test -> Cek folder reports
