# Untuk Magang APTRG, Soal GCS

## 1. Buat mock up tampilan interface untuk wahana (bebas menggunakan software apapun, diutamakan menggunakan figma)

![](images/control.jpg)
[Link Figma](https://www.figma.com/file/lHuazjbyPE4oDXG0WzFQX0/Magang_APTRG?type=design&node-id=0%3A1&mode=design&t=kvRCQyH0sAFT5Scx-1) 

## 2. Buatlah program website sederhana (bebas menggunakan bahasa apapun)

![](images/website.jpg)

[Source code ada di sini](website_sederhana)

#### Cara menjalankan

```bash
git clone https://github.com/mhafiz03/testing
cd testing/website_sederhana
pip install aiohttp
python main.py
```

Buka http://localhost:8000 di web browser


#### Cara mengubah data saat server jalan

```bash
curl 127.0.0.1:8000/update?air_speed=30
curl 127.0.0.1:8000/update?motor_rpm=9000
curl 127.0.0.1:8000/update?vert_speed=600
curl 127.0.0.1:8000/update?air_speed=50&motor_rpm=7500&vert_speed=1000
```

Refresh web page untuk melihat data yang baru di-update, karena saya belum mengimplementasi polling di javascript :/

## 3. Buatkan program crud menggunakan bahasa python

![](images/crud.png)

[Source code ada di sini](simple_crud_python)

#### Cara menjalankan

```bash
git clone https://github.com/mhafiz03/testing
cd testing
pip install PyQt5
python simple_crud_python/main.py
```

-Hatur nuhun