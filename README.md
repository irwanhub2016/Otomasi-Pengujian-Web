# Otomasi-Pengujian-Web
Projek ini berisi script untuk melakukan otomasi pengujian pada website http://automationpractice.com

Tools :
- Python3
- pip3
- Selenium binding python
- Chromedriver
- HtmlTestRunner

How to :
- git clone https://github.com/irwanhub2016/Otomasi-Pengujian-Web.git
- Masuk ke folder Otomasi-Pengujian-Web
- Install paket yang diperlukan dengan pip3 dengan cara :
  - pip3 install -r requirements.txt
- Apabila terdapat error pada chrome driver, ikuti langkah alternatif berikut :
  - git clone https://github.com/peterhudec/chromedriver_installer.git
  - python3 chromedriver_installer/setup.py install --chromedriver-version=2.10
- Buat file .env dan isi variable 'URL' didalam .env dengan link url website (Abaikan step ini jika sudah ada file .env, dalam Repo ini sudah tersedia file .env)
- Aktivasi environment venv :
  - source env/bin/activate
- Jalankan test :
  - python3 [test_case_name.py] ( dalam repo ini terdapat 5 test case untuk automation test )
- Secara otomatis Report test akan ter-generate setelah jalankan test -> Cek folder reports
