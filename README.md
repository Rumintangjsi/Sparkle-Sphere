![Sparkle Sphere Header](https://i.pinimg.com/564x/4f/1f/85/4f1f8588100c09ee126be1e66483ade8.jpg)
# Tugas 2
### Nama: Rumintang Jessica H <br>
### Kelas: PBP A <br> 
### Nama App : [Sparkle Sphere](https://sparkle-sphere.adaptable.app/main/) 🔮💍 <br>

## 1. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial)
Djanggo sendiri merupakan suatu framework yang cukup umum dalam pengembangan webdev dengan bahasa pemrograman Python.<br>

### Membuat Direktori dan Mengaktifkan _Virtual Environment_
* Untuk membuat proyek Django baru, kita perlu membuat direktori baru yang saya namakan ```sparkle_sphere```. Setelah itu saya membuat _virtual environment_ dengan menjalankan perintah <br> 
    ```
    python -m venv env
    ```
    Setelah itu saya mengaktifkan _virtual environment_ yang telah dibuat sebelumnya dengan menjalankan perintah <br> 

    * Unix (Mac/Linux): <br>

        ```
        source env/bin/activate
        ```
    _Virtual environment_ yang aktif akan ditandai dengan ```(env)``` pada baris _input terminal_. <br> <br>

### Menyiapkan _Dependencies_ dan Membuat Proyek Django    
Selanjutnya saya menyiapkan _depedencies_ dan membuat proyek django. _Dependencies_ adalah bagian penting dalam perangkat lunak yang memastikan komponen bekerja bersama. Mereka bisa berupa _library_, _framework_, atau _package_ yang dibutuhkan. Dependencies mempercepat pengembangan, tetapi perlu manajemen versi yang hati-hati. Lingkungan virtual membantu mengisolasi dependencies antar proyek. <br>
* Di dalam direktori ```sparkle_sphere``` saya membuat berkas yang bernama ```requirements.txt``` dan menambahkan beberapa _dependencies_. <br>
    ```python
    django
    gunicorn
    whitenoise
    psycopg2-binary
    requests
    urllib3 
    ```
* Kita dapat memasang _dependencies_ dengan menjalankan perintah berikut. Namun, sebelumnya kita harus mengaktifkan _virtual environment_ terlebih dahulu sebelum menjalankan perintah pada terminal. <br>
    ```
    pip install -r requirements.txt
    ```
* Kemudian saya membuat proyek Django yang bernama ```sparkle_sphere``` dengan perintah sebagai berikut.<br>

    ```
    django-admin startproject shopping_list .
    ```
    Kita harus memastikan bahwa karakter ```.``` tertulis di akhir perintah. <br><br>

### Konfigurasi Proyek dan Menjalankan _Server_
Sekarang, kita sampai pada tahan konfigurasi proyek dan menjalankan server.
* Pada file ```settings.py``` kita perlu menambahkan ```*``` pada ```ALLOWED_HOSTS``` untuk keperluan _deployment_:
    ```
    ...
    ALLOWED_HOSTS = ["*"]
    ...
    ```
* Dalam konteks deployment, ALLOWED_HOSTS adalah daftar host yang diizinkan untuk mengakses aplikasi web. Jika saya mengatur nilai ALLOWED_HOSTS menjadi ["*"], ini akan memberikan izin akses kepada semua host, yang berarti aplikasi dapat diakses secara luas. Namun, kita harus berhati-hati saat menggunakan pengaturan ini, dan sebaiknya hanya digunakan dalam situasi tertentu, seperti saat melakukan uji coba atau tahap awal pengembangan. <br>
    
* Sebelum menjalankan perintah untuk mengetes server sudah berjalan atau belum, kita harus memastikan bahwa berkas ```manage.py``` ada pada direktori yang aktif pada _shell_ saat ini.<br>
    ```
    ./manage.py runserver
    ```
    Kita bisa membuka http://localhost:8000 pada peramban web untuk dapat melihat animasi roket yang menandakan aplikasi Django berhasil dibuat. <br>

### Menghentikan _Server_ dan Menonaktifkan _Virtual Environment_
* Untuk menghentikan _server_, saya menekan ```Control+C``` pada _shell_ sebagai pengguna Mac.
    Untuk menonaktifkan _virtual environment_ dengan menjalankan perintah: <br>

    ```
    deactivate
    ```
**Dengan demikian aplikasi Django telah dibuat!**

### Unggah Proyek ke Repositori GitHub
* Saya membuat repositori GitHub yang bernama ```Sparkle-Sphere``` dengan visibilitas _public_.<br>
* Selanjutnya saya menginisiasi direktori ```sparkle_sphere``` sebagai repositori Git yang terdapat pada tutorial sebelumnya.
* Setelah itu saya menambahkan berkas ```.gitignore``` <br>
    * Berkas ```.gitignore``` adalah konfigurasi di Git yang menginstruksikan Git untuk mengabaikan berkas dan direktori tertentu, seperti berkas hasil kompilasi, berkas sementara, atau konfigurasi pribadi. Ini untuk memastikan Git tidak melacak berkas-berkas tersebut dalam versi kontrol.
* Kemudian saya melakukan ```add```, ```commit```, dan ```pnush``` dari direktori repositori lokal.<br>

### Membuat Aplikasi ```main``` dalam Proyek Sparkle Sphere
Pada langkah ini saya membuat aplikasi baru bernama main dalam proyek yang telah saya buat sebelumnya yang bernama Sparkle Sphere.<br>
* Sebelum kita membuat aplikasi main, kita perlu mengaktifkan _virtual environment_ dengan menjalankan perintah seperti diatas.<br>
* Selanjutnya kita menjalankan perintah berikut untuk membuat aplikasi baru.<br>
    ```
    python manage.py startapp main
    ```
    setelah perintah tersebut dijalankan, akan terbentuk direktori baru dengan nama ```main```.<br>
* Selanjutnya kita perlu mendaftarkan aplikasi ```main``` kedalam proyek Sparkle Sphere dengan cara menambahkan ```'main'``` pada variabel ```INSTALLED_APPS``` yang terdapat pada berkas ```settings.py``` dalam direktori ```sparkle_sphere```.<br>
    ```
    INSTALLED_APPS = [
    ...,
    'main',
    ...
    ]
    ```
**Maka aplikasi ```main``` telah terdaftar dalam proyek Sparkle Sphere**

### Mengonfigurasi _Routing_ URL Aplikasi ```main```
Untuk dapat membuat routing pada aplikasi ```main```, kita harus membuat berkas ```urls.py``` pada direktori ```main```. <br><br>
Selanjutnya kita perlu mengisi ```urls.py``` dengan kode berikut. <br>
```
from django.urls import path
from main.views import show_main

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
]
```
**Penjelasan kode:**
Berkas ```urls.py``` dalam aplikasi ```"main"``` mengatur rute URL khusus untuk aplikasi tersebut. Dalam pengaturan ini, kita menggunakan path dari ```django.urls``` untuk menentukan pola URL. Fungsi ```show_main``` dari modul ```main.views``` digunakan sebagai tampilan yang akan ditampilkan saat URL terkait diakses.<br>

### Membuat Model pada Aplikasi Main
Sebelum menjelaskan lengkah-langkah membuat model pada aplikasi Main. Apa itu Model? Model dalam konsep MVT bertanggung jawab atas pengaturan dan manajemen data aplikasi. Model mencerminkan struktur data dan logika aplikasi yang berada di latar belakang tampilan. Model menghubungkan aplikasi dengan basis data serta mengelola interaksi data tersebut. <br>

Untuk dapat membuat models baru, kita perlu mengubah berkas ```models.py``` yang terdapat dalam direktori aplikasi ```main``` yang sebelumnya telah kita buat.<br>
* Kita harus mengisi berkas ```models.py``` dengan kode sebagai berikut.<br>
    ```
    from django.db import models

    class Item(models.Model):
        name = models.CharField(max_length=255)
        date_added = models.DateField(auto_now_add=True)
        amount = models.IntegerField()
        description = models.TextField()
    ```
    **Penjelasan Kode:**
    * ```models.Model``` adalah kelas dasar yang digunakan untuk mendefinisikan model dalam Django.
    * Itemns merupakan nama model yang kita definisikan dan memiliki beberapa atribut seperti:<br>
        * ```name``` sebagai nama _item_ dengan tipe ```CharField```.
        * ```amount``` sebagai jumlah _item_ dengan tipe ```IntegerField```.
        * ```description``` sebagai deskripsi _item_ dengan tipe ```TextField```.
### Menghubungkan _View_ dengan _Template_ 
* Pertama-tama kita harus mengimpor modul yang nantinya akan dibutuhkan untuk membuat fungsi view ```show_main```. Kemudian, kita membuka berkas ```views.py``` yang terletak dalam berkas aplikasi ```main```.<br>
    Kita perlu menambahkan baris impor berikut di bagian paling atas berkas yang bergunak untuk me-_render_ tampilan HTML dengan menggunakan data yang diberikan.<br>
    ```
    from django.shortcuts import render
    ```
    Selanjutnya kita menambahkan fungsi ```show_main``` di bawah impor yang nantinya akan berguna untuk me-_render_ tampilan ```main.html``` dan mengatur permintaan HTTP dan me-_return_ tampilan yang sesuai.<br>
    ```
    def show_main(request):
        context = {
            'name': 'Rumintang Jessica H',
            'app' : 'Sparkle Sphere',
            'class': 'PBP A'
        }

    return render(request, "main.html", context)
    ```
    **Penjelasan Kode:**
    * Pada kode tersebut terdapat ```context``` yang merupakan suatu _dictionary_ yang berisi data yang akan di tunjukan pada tampilan.
* Selanjutnya kita harus mengubah _template_ ```main.html``` agar dapat menampilkan data yang sebelumnya telah diambil dari _model_. Pertana-tama, kita membuka berkas  ```main.html``` yang sebelumnya telah dibuat dalam direktori ```templates```.<br>
* Kemudian kita akan mengubah isinya menjadi kode Django yang sesuai untuk menampilkan data.
    ```
    <h1>Sparkle Sphere Page</h1>

    <h5>Name: </h5>
    <p>{{ name }}<p>
    <h5>App: </h5>
    <p>{{ app }}<p>
    <h5>Class: </h5>
    <p>{{ class }}<p>
    ```

### Mengonfigurasi _Routing_ URL Proyek
Untuk dapat melakukan routing pada proyek agar dapat menjalankan aplikasi ```main``` kita perlu menghubungkan rute URL ke dalam ```urls.py``` proyek untuk menghubungkan ke tampilan ```main```. <br>
* Kita harus membuka berkas ```urls.py``` yang terdapat pada ```sparkle_sphere```, bukan yang ada di dalam ```main```.<br>
    Kemudian kita perlu mengimpor fungsi ```include``` dari ```django.urls``` <br>
    ```
    from django.urls import path, include
    ```
    Selanjutnya, kita perlu menambahkan rute URL untuk mengarahkan ke tampilan ```main``` di dalam variabel ```urlpatterns```.<br>
    ```
    urlpatterns = [
    ...
    path('main/', include('main.urls')),
    ...
    ]
    ```
    **Penjelasan:** <br>
    Berkas ```urls.py``` dalam proyek mengatur rute URL tingkat proyek. Fungsi include digunakan untuk mengimpor rute URL dari aplikasi lain, seperti ```"main,"``` ke dalamnya. Sebagai contoh, path URL ```'main/'``` akan diarahkan ke rute yang telah didefinisikan dalam ```urls.py``` aplikasi ```"main."``` Dengan cara ini, kita mengatur rute URL proyek secara terstruktur dan mengintegrasikan berbagai bagian proyek dengan efisien. <br><br>

### Melakukan _deployment_ ke Adaptable terhadap aplikasi yang sudah dibuat sehingga nantinya dapat diakses oleh teman-temanmu melalui Internet
Sebelum melakukan _deployment_, kita perlu menghubungkan repositori di GitHub dengan direktori lokal kita yaitu ```sparkle_sphere```. Setelah itu, kita melakukan ```add```, ```commit```, dan ```push``` kode yang ada di direktori lokal ke dalam repositori kita. Setelah di-push, kita harus menyambungkan akun Adaptable dengan GitHub. Jika sudah tersambung, maka kita bisa langsung membuat ```New App``` di App Dashboard. Di situ, akan ada pilihan untuk mengkoneksikan dengan repositori GitHub. Kita akan mengkoneksikan dengan repositori yang telah dibuat sebelumnya yakni ```Sparkle-Sphere```. Jika sudah, maka kita pilih template ```Python App Template```. Untuk tipe database, pilih ```PostgreSQL```. Setelahnya, saya memilih versi Python 3.10. Lalu, pada bagian ```Start Command``` saya memasukkan perintah ```python manage.py migrate && gunicorn sparkle_sphere.wsgi```. Masukkan nama aplikasi lalu centang ```HTTP Listener on PORT```. Jika sudah, klik ```Deploy App``` dan tunggu sampai selesai. Jika sudah terlihat tanda centang di seluruh proses, maka proses deployment aplikasi selesai.<br><br>

## 2. Buatlah bagan yang berisi _request client_ ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara ```urls.py```, ```views.py```, ```models.py```, dan berkas ```html```.
![Stucture MVT](https://i.pinimg.com/564x/07/e3/e6/07e3e6b34198ef0c1bd22075009646de.jpg)

## 3. Jelaskan mengapa kita menggunakan _virtual environment_? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan _virtual environment_?
Kita menggunakan _virtual environment_ dalam pengembangan aplikasi web, termasuk yang sedang dipelajari sekarang yaitu aplikasi berbasis Django. _Virtual environment_ membantu kita dalam menjaga dan mengolola proyek yang kita sedang kembangkan dengan lebih baik. _Virtual environment_ membantu kita menghindari masalah seperti konflik antar-paket dan memudahkan instalasi dan pemeliharaan paket yang diperlukan.<br><br> 
Ya, kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan _virtual environment_, namun terdapat kemungkinan adanya konflik antar-paket dan masalah managemen dependensi yang dapat muncul ketika Anda mengembangkan beberapa proyek Django atau saat bekerja dengan berbagai versi paket yang berbeda.

## 4. Jelaskan apakah itu MVC, MVT, MVVM dan perbedaan dari ketiganya.
* MVC (Model-View-Controller):
    * Model: Bertanggung jawab untuk memproses, menyimpan, dan megelola data aplikasi dan logika bisnis. Ini adalah bagian yang berurusan dengan pemrosesan data dan interaksi dengan basis data jika diperlukan.
    * View: Merupakan tampilan yang digunakan untuk menampilkan data ke pengguna. Ini adalah bagian yang berurusan dengan antarmuka pengguna dan tampilan visual
    * Controller: Bertindak sebagai perantara antara Model dan View. Controller akan menerima input dari user, memprosesnya, dan memperbarui model. Setelah itu, model memberi tahu pengontrol yang kemudian memperbarui tampilan. Controller bertanggung jawab untuk menjaga sinkronisasi antara model dan tampilan, dan ini merupakan salah satu prinsip utama dalam arsitektur MVC yang meningkatkan pemeliharaan dan pengujian aplikasi.<br><br>

* MVT (Model-View-Template):
    * Model: Sama halnya dengan model MVC, serta mengelola data dan juga logika bisnis. 
    * View: Bertanggung jawab untuk menampilkan data kepada pengguna, tetapi tidak memiliki logika bisnis di dalamnya. Template yang digunakan untuk merender data dalam tampilan.
    * Template: _Presentation layer_ yang menangani seluruh bagian antarmuka pengguna (User Interface) sepenuhnya. <br><br>

* MVVM (Model-View-ViewModel): 
    * Model:Sama halnya dengan MVC dan juga MVT, serta mengelola data dan juga logika bisnis.
    * View: Merupakan representasi _User Interface_ dan menampilkan data. Dalam MVVM, tampilan sering dibangun menggunakan bahasa markup seperti XAML, memisahkan dengan jelas desain UI dan kode.
    * ViewModel: Bekerja sebagai penghubung antara Model dan View, memiliki tanggung jawab untuk menyimpan kondisi View dan melaksanakan segala tindakan yang diperlukan untuk mengubah data dalam Model ke dalam bentuk yang dapat ditampilkan oleh View. <br><br>

* **Perbedaan MCV, MVT, MVVM:**

|                   | MVC                                       | MVVM                                                  |
|-------------------|-------------------------------------------|-------------------------------------------------------|
| Controller/ViewModel | Menghubungkan Model dan View              | Menggunakan ViewModel sebagai penghubung antara Model dan View melalui binding |
| Cocok untuk       | Cocok digunakan pada aplikasi dengan kompleksitas yang tinggi dan interaksi pengguna yang rumit | Cocok digunakan pada aplikasi dengan tampilan yang kompleks dan dipengaruhi oleh banyak perubahan data |<br>

|                   | MVC                                       | MVP                                                  |
|-------------------|-------------------------------------------|-------------------------------------------------------|
| Perantara        | Controller sebagai perantara antara Model dan View | Presenter sebagai perantara antara Model dan View   |
| Cocok untuk       | Mendukung pengembangan aplikasi dengan tim yang besar | Lebih sesuai untuk aplikasi dengan kompleksitas yang rendah dan tim yang kecil |
| Keunggulan       | Cocok digunakan untuk aplikasi yang memiliki banyak kontrol inputan pengguna | Cocok digunakan untuk aplikasi yang menekankan interaksi dengan pengguna dan menampilkan data dalam bentuk kontrol tampilan |

