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
    _Virtual environment_ yang aktif akan ditandai dengan `(env)` pada baris _input terminal_. <br> <br>

### Menyiapkan _Dependencies_ dan Membuat Proyek Django    
Selanjutnya saya menyiapkan _depedencies_ dan membuat proyek django. _Dependencies_ adalah bagian penting dalam perangkat lunak yang memastikan komponen bekerja bersama. Mereka bisa berupa _library_, _framework_, atau _package_ yang dibutuhkan. Dependencies mempercepat pengembangan, tetapi perlu manajemen versi yang hati-hati. Lingkungan virtual membantu mengisolasi dependencies antar proyek. <br>
* Di dalam direktori `sparkle_sphere` saya membuat berkas yang bernama `requirements.txt` dan menambahkan beberapa _dependencies_. <br>
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
* Kemudian saya membuat proyek Django yang bernama `sparkle_sphere` dengan perintah sebagai berikut.<br>

    ```
    django-admin startproject shopping_list .
    ```
    Kita harus memastikan bahwa karakter `.` tertulis di akhir perintah. <br><br>

### Konfigurasi Proyek dan Menjalankan _Server_
Sekarang, kita sampai pada tahan konfigurasi proyek dan menjalankan server.
* Pada file `settings.py` kita perlu menambahkan `*` pada `ALLOWED_HOSTS` untuk keperluan _deployment_:
    ```
    ...
    ALLOWED_HOSTS = ["*"]
    ...
    ```
* Dalam konteks deployment, ALLOWED_HOSTS adalah daftar host yang diizinkan untuk mengakses aplikasi web. Jika saya mengatur nilai ALLOWED_HOSTS menjadi ["*"], ini akan memberikan izin akses kepada semua host, yang berarti aplikasi dapat diakses secara luas. Namun, kita harus berhati-hati saat menggunakan pengaturan ini, dan sebaiknya hanya digunakan dalam situasi tertentu, seperti saat melakukan uji coba atau tahap awal pengembangan. <br>
    
* Sebelum menjalankan perintah untuk mengetes server sudah berjalan atau belum, kita harus memastikan bahwa berkas `manage.py` ada pada direktori yang aktif pada _shell_ saat ini.<br>
    ```
    ./manage.py runserver
    ```
    Kita bisa membuka http://localhost:8000 pada peramban web untuk dapat melihat animasi roket yang menandakan aplikasi Django berhasil dibuat. <br>

### Menghentikan _Server_ dan Menonaktifkan _Virtual Environment_
* Untuk menghentikan _server_, saya menekan `Control+C` pada _shell_ sebagai pengguna Mac.
    Untuk menonaktifkan _virtual environment_ dengan menjalankan perintah: <br>

    ```
    deactivate
    ```
**Dengan demikian aplikasi Django telah dibuat!**

### Unggah Proyek ke Repositori GitHub
* Saya membuat repositori GitHub yang bernama `Sparkle-Sphere` dengan visibilitas _public_.<br>
* Selanjutnya saya menginisiasi direktori `sparkle_sphere` sebagai repositori Git yang terdapat pada tutorial sebelumnya.
* Setelah itu saya menambahkan berkas `.gitignore`. <br>
    * Berkas `.gitignore` adalah konfigurasi di Git yang menginstruksikan Git untuk mengabaikan berkas dan direktori tertentu, seperti berkas hasil kompilasi, berkas sementara, atau konfigurasi pribadi. Ini untuk memastikan Git tidak melacak berkas-berkas tersebut dalam versi kontrol.
* Kemudian saya melakukan `add`, `commit`, dan `pnush` dari direktori repositori lokal.<br>

### Membuat Aplikasi `main` dalam Proyek Sparkle Sphere
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

# Tugas 3

## 1. Apa perbedaan antara form `POST` dan form `GET` dalam Django?
|                           | Metode POST (HTTP POST)  | Metode GET (HTTP GET)   |
|---------------------------|---------------------------|--------------------------|
| **Keamanan**              | Lebih aman                | Kurang aman              |
| **Ketentuan Data**        | Data tidak ditampilkan di URL, disimpan di dalam badan permintaan HTTP | Data ditambahkan ke URL, terlihat oleh semua orang |
| **Ketentuan Panjang URL** | Tidak terbatas panjang URL | Batasan panjang URL lebih ketat |
| **Kegunaan**              | Biasanya digunakan untuk input data melalui form | Biasanya digunakan untuk input data melalui link |


## 2. Apa perbedaan utama antara XML, JSON, dan HTML dalam konteks pengiriman data?
|               | XML (eXtensible Markup Language) | JSON (JavaScript Object Notation) | HTML (Hypertext Markup Language) |
|---------------|----------------------------------|-----------------------------------|--------------------------------|
| **Struktur**  | Terspesifikasi                   | Ringkas                           | Spesifik                       |
| **Pemrosesan**| Dapat diurai dan diproses        | Dapat diurai dan diproses         | Tidak dapat diurai              |
| **Human-Readable** | Ya                         | Ya                                | Ya                             |
| **Lintas Bahasa Pemrograman** | Ya           | Ya                                | Tidak                          |
| **Tujuan Utama** | Pertukaran data antar aplikasi | Pertukaran data antar aplikasi    | Tampilan halaman web           |

**Penjelasan singkat:**  XML digunakan untuk pertukaran data yang sangat terstruktur, JSON digunakan untuk pertukaran data yang lebih ringkas dan mudah dimengerti, sementara HTML digunakan untuk membuat tampilan halaman web dan bukan untuk pemrosesan data. Pemilihan format tergantung pada kebutuhan dan konteks penggunaannya. <br>

## 3. Mengapa JSON sering digunakan dalam pertukaran data antara aplikasi web modern?
JSON (JavaScript Object Notation) sangat populer dalam komunikasi antara aplikasi web modern karena kemudahan penggunaannya, efisiensi, dan fleksibilitas. JSON menggunakan format yang sederhana, seperti objek dan array, sehingga data dapat dipahami dengan cepat. Keuntungannya tidak berhenti di situ; JSON juga bisa digunakan dalam berbagai bahasa pemrograman, sehingga berbagai aplikasi dapat berbicara satu sama lain tanpa masalah. JSON juga mudah diurai oleh komputer, bahkan dengan perpustakaan yang berbeda-beda.

Selain itu, JSON efisien dalam pengiriman data melalui jaringan. Data yang dikirim dalam format JSON ringan, sehingga mengurangi waktu dan sumber daya yang dibutuhkan untuk mentransfernya. Di samping itu, JSON memiliki fleksibilitas yang sangat berguna; Kita bisa menggunakan format ini untuk merepresentasikan berbagai jenis data dengan mudah. Selain itu, JSON dianggap aman untuk digunakan dalam pertukaran data web. Berbeda dengan beberapa format lain yang bisa menghadapi risiko keamanan, JSON cenderung lebih aman. Itulah mengapa banyak aplikasi web modern memilih JSON sebagai cara utama untuk berkomunikasi.

## 4. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
Sebelum kita masuk ke checklist yang pertama yaitu membuat input form kita perlu menngubah routing `main/` menjadi `/`. Pertama-tama kita perlu mengaktifkan _virtual environment_ seperti tutorial yang bisa dilihat diatas. Selanjutna kita perlu mengganti path yang terdapat pada `urls.py` yang ada pada folder `sparkle_spehere` yaitu mengubah `main/` menjadi `''` pada `urlpatterns`. Kita dapat menjalankan runserver dan melihatnya pada http://localhost:8000/. <br>

### Implementasi Skeleton sebagai Kerangka _Views_
Sebelum kita membuat form untuk menambahkan objek model pada app yang telah dibuat sebelumnya yaitu Sparkle Sphere. Kita perlu membuat suatu _skeleton_ agar terdapat konsistemsi dalam desain situs web kita dan juga berfungsi sebagai kerangka view dari web yang kita buat. 
* Kita harus membuat folder `templates` pada main folder yaitu `sparkle_sphere` kemudian kita perlu membuat berkas HTML yang bernama `base.html` yang akan berfungsi sebagai template dasar untuk halaman web lainnya dalam proyek ini. <br>
* Kemudian, buka `settings.py` yang terdapat pada subdirektori `sparkle_sphere` kemudian kita perlu menambahkan baris berikut pada `TEMPLATES`.<br><br>
    ```
    ...
    TEMPLATES = [
        {
            ...
            'DIRS': [BASE_DIR / 'templates'], # Tambahkan kode ini
            ...
        }
    ]
    ...
    ```
* Selanjutnya, kita perlu mengganti berkas `main.html` yang terdapat pada subdirektori `tempaltes` pada direktori `main` menjadi sebagai berikut.<br><br>
    ```
    {% extends 'base.html' %}

    {% block content %}
        <h1>Sparkle Sphere Page</h1>

        <h5>Name:</h5>
        <p>{{name}}</p>

        <h5>App:</h5>
        <p>{{app}}</p>

        <h5>Class:</h5>
        <p>{{class}}</p>
    {% endblock content %}
    ```
### Membuat Input `form` untuk menambahkan objek model pada app
Form akan digunakan untuk menginput Items pada aplikasi Sparkle Sphere yang nantinya akan ditambahkan pada halaman utama.<br>
* Kita perlu membuat berkas `forms.py` pada direktori main untuk menerima data produk baru sebagai berikut.<br><br>
    ```
    from django.forms import ModelForm
    from main.models import Item

    class ItemForm(ModelForm):
        class Meta:
            model = Item
            fields = ["name", "amount", "description"]
    ```
    **Penjelasan Kode:**
    * `model = Item` digunakan untuk menunjukan model yang akan digunakan untuk _form_ dan ketika disimpan, isi _form_ akan disimpan menjasi object `Item`.<br>
    * `fields = ["name", "amount", "description"]` akaan menunjukan _field_ dari model Items yang digunakan untuk _form_.
* Tambahkan beberapa import pada `views.py` pada folder `main` sebagai berikut.<br><br>
    ```
    from django.http import HttpResponseRedirect
    from main.forms import ItemForm
    from django.urls import reverse
    ```
* Kemudian kita perlu menambahkan fungsi baru dengan nama `create_item` yang akan menerima input dengan parameter `request` untuk menambahkan data produk yang kita _submit_ pada _form_. <br><br>
    ```
    def create_item(request):
        form = ItemForm(request.POST or None)

        if form.is_valid() and request.method == "POST":
            form.save()
            return HttpResponseRedirect(reverse('main:show_main'))

        context = {'form': form}
        return render(request, "create_item.html", context)
    ```
    **Penjelasan Kode:** Kita membuat formulir baru dengan ItemForm(request.POST or None), memvalidasi input dengan form.is_valid(), dan menyimpan data dengan form.save(). Setelah berhasil, kita menggunakan return HttpResponseRedirect(reverse('main:show_main')) untuk mengarahkan pengguna ke halaman lain.<br><br>
* Selanjutnya, kita perlu menambahkan beberapa hal pada ```show_main``` dalma berkas ```views.py``` sebagai berikut.<br><br>
    ```
    def show_main(request):
    items = Item.objects.all()
    
    context = {
        'name': 'Rumintang Jessica H',
        'app' : 'Sparkle Sphere',
        'class': 'PBP A',
        'items' : items
    }
    return render(request, "main.html", context)
    ```
    Fungsi `Item.objects.all()` akan digunakan untuk mengambai semua Items yang tersimpan pada database.<br><br>
* Tambahkan _import_ fungsi `create_item` pada `views.py`
    ```
    from main.views import show_main, create_item
    ```
* Kemudian, tambahkan _path url_ ke dalam `urlpatterns` yang terdapat pada `urls.py` unruk dapat mengakses fungsi yang sebelumnya telah kita import. <br><br>
    ```
    ...
    path('create-item', create_item, name='create_item'),
    ...
    ```
* Setelah itu, kita perlu membuat berkas HTML baru yang bernama `create_item.html` pada direktori `template` yang terdapat di dalam `main`.<br><br>
    ```
    {% extends 'base.html' %} 

    {% block content %}
    <h1>Add New Item</h1>

    <form method="POST">
        {% csrf_token %}
        <table>
            {{ form.as_table }}
            <tr>
                <td></td>
                <td>
                    <input type="submit" value="Add Item"/>
                </td>
            </tr>
        </table>
    </form>

    {% endblock %}
    ```
    **Penjelasan Kode:**
    `<form method="POST">` digunakan untuk menandai formulir dengan metode POST, `{% csrf_token %}` adalah token keamanan, dan `{{ form.as_table }}` digunakan untuk menampilkan field-form sebagai tabel. Tombol "Submit" `<input type="submit" value="Add Item"/>` digunakan untuk mengirimkan data ke view `create_item(request)`. Ini adalah langkah dasar dalam membuat formulir Django yang aman dan efisien.

* Kita perlu menambahkan kode berikut ke dalam `{% block content %}` yang terdapat di dalam berkas `main.html` yang akan menampilkan data produk dalam bentuk tabel.<br><br>
    ```
    ...
    {% with total_items=items|length %}
        <p>Kamu menyimpan {{ total_items }} jewelry pada Sparkle Sphere </p>
    {% endwith %}

    {% comment %} Tambahan kode untuk nilai bonus {% endcomment %}

    <table>
        <tr>
            <th>Name</th>
            <th>Amount</th>
            <th>Description</th>
            <th>Date Added</th>
        </tr>

        {% comment %} Berikut cara memperlihatkan data produk di bawah baris ini {% endcomment %}

        {% for item in items %}
            <tr>
                <td>{{item.name}}</td>
                <td>{{item.amount}}</td>
                <td>{{item.description}}</td>
                <td>{{item.date_added}}</td>
            </tr>
        {% endfor %}
    </table>

    <br />

    <a href="{% url 'main:create_item' %}">
        <button>
            Add New Item
        </button>
    </a>

    {% endblock content %}
    ```
* Selanjutnya, kita dapat mencoba menjalankan web dengan `python manage.py runserver` dan membuka link http://localhost:8000/ di browser. Setelah menambahkan Items pada forms, seharysnya kita dapat melihat data barang yang baru saja ditambahkan pada halaman utama aplikasi.<br><br>

### Menampilkan Data Produk dalam Bentuk HTML, XML, JSON,XML by ID, dan JSON by ID.
Penjelasan untuk menampilkan data produk dalam bentuk HTML sudah dijelaskan bersamaan dengan pembuatan form. <br><br>

* Pertama-tama kita perlu menambahkan beberapa _import_ sebagai berikut.
    ```
    from django.http import HttpResponse
    from django.core import serializers
    ```
* Kemudian kita perlu menambahkan fungsi yang menerima parameter _request_ dengan nama `show_xml`, `show_json`. Setelah itu tambahkan _return function_ dalam bentuk `HttpResponse`.
    * XML
        ```
        def show_xml(request):
            data = Item.objects.all()
            return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")
        ```
    * JSON
        ```
        def show_json(request):
            data = Item.objects.all()
            return HttpResponse(serializers.serialize("json", data), content_type="application/json")
        ```
* Untuk fungsi yang mengembalikan data produk berdasarkan id kita memerlukan parameter _request_ dan juga _id_
    * XML
        ```
        def show_xml_by_id(request, id):
            data = Item.objects.filter(pk=id)
            return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")
        ```
    * JSON
        ```
        def show_json_by_id(request, id):
            data = Item.objects.filter(pk=id)
            return HttpResponse(serializers.serialize("json", data), content_type="application/json")
        ```
### Membuat _Routing_ URL untuk Masing-masing `Views`
* Langkah pertama dalam membuat _routing_ URL adalam dengan mengimport beberapa fungsi yang telah dibuat sebelumnya sebagai berikut.<br><br>
    ```
    from main.views import show_main, create_item, show_xml, show_json, show_xml_by_id, show_json_by_id 
    ```
* Setelah itu, kita perlu menambahkan _path url_ ke dalam `urlpatterns`. <br><br>
    ```
    ...
    path('xml/', show_xml, name='show_xml'), 
    path('json/', show_json, name='show_json'), 
    path('xml/<int:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<int:id>/', show_json_by_id, name='show_json_by_id'), 
    ...
    ```

Kita dapat melihat hasilnya dengan menjalankan server `python manage.py runserver` dan membuka http://localhost:8000/xml, http://localhost:8000/json,  http://localhost:8000/xml/[id] atau http://localhost:8000/json/[id] pada browser.

![HTML at Postman](image-2.png)
![XML at Postman](image-3.png)
![JSON at Postman](image-4.png)
![XML (id:2)](image-5.png)
![JSON (id:3)](image-6.png)

# Tugas 4
## 1. Apa itu Django UserCreationForm, dan jelaskan apa kelebihan dan kekurangannya?
'Django UserCreationForm' adalah sebuah impor formulir bawaan yang disediakan oleh Django untuk memudahkan proses pembuatan pengguna (user) dalam aplikasi web. Form ini digunakan untuk mengumpulkan data yang diperlukan saat membuat akun pengguna, seperti nama pengguna (username), kata sandi (password), dan lain-lain. Dengan adanya formulir ini, pengguna baru dapat mendaftar dengan mudah di situs web Anda tanpa harus menulis kode dari awal. <br>
**Kelebihan:** <br>
* Mudah Digunakan: Form ini sudah disiakan dengan baik dan dengan mudah dapat digunakan yaitu dengan mengimport dan menambahkannya pada view.
* Validasi Otomatis: Form telah dilengkapi dengan validasi default yang berguna untuk memeriksa daya yang dimasukan oleh pengguna sudah memenuhi persyaratan atau belum.
* _Customable_: Tampilan pada form ini dapat kita sesuaikan sengan kebutuhan.
**Kekurangan:** <br>
* Tampilan default yang terbatas: Form ini menyediakan tampilan (UI/UX) yang mungkin tidak sesuai dengan kebutuhan spesifik kita. Oleh karena itu, kita perlu mengkustomisasi tampilan jika diperlukan.
* Keterbatasan Fungsionalsitas: Form ini tidak mendukung layanan seperti verifikasi email atau ontegrasi dengan layanan pihak ketiga.
* Ketergantungan pada Django: 

## 2. Apa perbedaan antara autentikasi dan otorisasi dalam konteks Django, dan mengapa keduanya penting?
Autentikasi adalah proses verifikasi identitas pengguna. Dalam Django, autentikasi mencakup pengenalan pengguna (login) seperti pengecekan nama pengguna dan kata sandi. Sedangkan otorisasi merupakan proses untuk verifikasi bahwa suatu pengguna memiliki hak untuk mengakses suatu sistem atau program. <br>
Keduanya merupakan hal yang penting dilakukan, pada tahap autentikasi keamanan dipastikan dengan memverifikasi identitas dari pengguna, mencegak akses tanpa izin, dan melindungi data sensitif.<br>
Sedangkan otorisasi memastikan bahwa user hanya memiliki akses ke sistem yang sesuai dengan peran mereka.

## 3. Apa itu _cookies_ dalam konteks aplikasi web, dan bagaimana Django menggunakan _cookies_ untuk mengelola data sesi pengguna?
Cookies adalah sejenis data yang disimpan di sisi klien (biasanya dalam browser web) oleh server aplikasi web. Cookies digunakan untuk menyimpan informasi spesifik yang dapat diakses kembali oleh server ketika pengguna melakukan permintaan selanjutnya. Dalam Django _cookies_ digunakan untuk mengidentfikasi sesi pengguna dan menyimpam data sesi yang terkait. Berikut adalah bagaimana Django menggunakan cookie untuk mengelola data sesi pengguna:
* Kita perlu mengaktifkan dan mengonfigurasi framework sesi Django
* Ketika kita menyimpan data (Seperti ID pengguna), Django akan membuat cookie sesi baru di sesi pengguna dan menyimpan data sesi sesuai dengan server.
* Setiap pengguna meminta _request_ ke server, cookie yang terdapat pada sesi tersebut akan dikirimkan ke server, dan Django akan menggunakan _cookie_ untuk melakukan pengidentifikasian, data tersebut diambil dari sever dan digunakan dalam pemrosesan permintaan.
* Django akan _refresh_ _cookie_ secara otomatis untuk mencegah kadaluarsa terlalu cepaat.

## 4. Apakah penggunaan _cookies_ aman secara _default_ dalam pengembangan web, atau apakah ada risiko potensial yang harus diwaspadai?
Penggunaan cookies dalam pengembangan web dapat menjadi aman secara default, tetapi ada beberapa risiko potensial yang harus diwaspadai dan dipertimbangkan:
* Keamanan Data: Cookies dapat menyimpan data pengguna seperti ID sesi dan preferensi. Tetapi jika tidak diatur dengan benar, data sensitif seperti informasi login bisa dicuri. Maka, enkripsi data dalam cookies penting untuk melindungi privasi pengguna.
* Privasi Pengguna: Cookies dapat digunakan untuk melacak pengguna. Namun, jika pelacakan dilakukan dengan tidak etis hal ini dapat melanggar data privasi pengguna 
* Serangan Terhadap _Cookies_: Dalam serangan XSS, penyerang dapat mencuri atau memanipulasi cookies pengguna, mengancam keamanan sesi. Sedangkan CSRF bisa memanfaatkan cookies untuk melakukan tindakan yang tidak diinginkan pada nama pengguna yang sudah terotentikasi.

## 5. Jelaskan bagaimana cara kamu mengimplementasikan _checklist_ di atas secara _step-by-step_ (bukan hanya sekadar mengikuti tutorial).

### Membuat Fungsi Registrasi
* Untuk dapat membuat fungsi registrasi kita perlu menambahkan beberapa import ke dalam berkas `views.py` yang terdapat pada subdirektori `main`.<br><br>
```
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages  
```
* Kemudian kita perlu membuat fungsi dengan nama ```register``` yang berfungsi untuk membuat formulir registrasi secara otomatis dan menghasilkan akun pengguna ketika data di-_submit_. <br><br>
    ```
    def register(request):
        form = UserCreationForm()

        if request.method == "POST":
            form = UserCreationForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'Your account has been successfully created!')
                return redirect('main:login')
        context = {'form':form}
        return render(request, 'register.html', context)
    ```
    **Penjelasan Kode:**
    * `UserCreationForm(request.POST)` digunakan untuk membuat instance baru dari `UserCreationForm` dengan menggunakan data dari `request.POST`, yang berasal dari input pengguna.
    * `form.is_valid()` digunakan untuk mengecek apakah data yang dimasukkan ke dalam form valid atau tidak.
    * `form.save()` digunakan untuk membuat dan menyimpan data dari form ke dalam database.
    * `messages.success(request, 'Your account has been successfully created!')` digunakan untuk memberikan pesan sukses kepada pengguna setelah suatu tindakan berhasil dilakukan.
    * `return redirect('main:show_main')` digunakan untuk mengarahkan pengguna ke halaman yang tepat setelah data dari form berhasil disimpan.
* Selanjutnya kita akan membuat berkas HTML baru dengan nama `register.html` pada folder `template` dalam subdirektori `main`. Kemudian kita perlu menambahkan _template_ berikut. <br><br>
    ```
    {% extends 'base.html' %}

    {% block meta %}
        <title>Register</title>
    {% endblock meta %}

    {% block content %}  

    <div class = "login">
        
        <h1>Register</h1>  

            <form method="POST" >  
                {% csrf_token %}  
                <table>  
                    {{ form.as_table }}  
                    <tr>  
                        <td></td>
                        <td><input type="submit" name="submit" value="Daftar"/></td>  
                    </tr>  
                </table>  
            </form>

        {% if messages %}  
            <ul>   
                {% for message in messages %}  
                    <li>{{ message }}</li>  
                    {% endfor %}  
            </ul>   
        {% endif %}

    </div>  

    {% endblock content %}
    ```
* Setelah menambahkan template pada `register.html`, kita akan menambahkan impor fungsi yang telah dibuat pada berkas `urls.py` pada subdirektori `main`.<br><br>
    ```
    from main.views import register
    ```
* Kemudian kita akan menambahkan _path url_ ke dalam `urlpatterns` agar kita dapat mengakses fungsi yang kita buat sebelumnya.<br><br>
    ```
    ...
    path('register/', register, name='register'),
    ...
    ```
### Membuat Fungsi Login
* Pertama-tama kita perlu menambahkan fungsi import pada berkas `view.py` yang terdapat dalam subdirektori `main`. <br><br>
    ```
    from django.contrib.auth import authenticate, login
    ```
    **Penjelasan Kode:**
    Fungsi `authenticate` dan `login` yang diimport akan digunakan untuk melakukan autentikasi dan akan menjalankan login ketika autentikasi berhasil. <br><br>
* Selanjutnya kita perlu menambahkan kode di bawah ini ke dalam fungsi login yang telah dibuat sebelumnya. <br><br>
    ```
    def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('main:show_main')
        else:
            messages.info(request, 'Sorry, incorrect username or password. Please try again.')
    context = {}
    return render(request, 'login.html', context)
    ```
    **Penjelasan Kode:**
    `authenticate(request, username=username, password=password)` digunakan untuk memeriksa identitas pengguna dengan menggunakan informasi login yang diterima dari permintaan pengguna saat mereka mencoba masuk ke sistem. <br><br>
* Setelah itu, buat berkas HTML baru pada folder `template` dalam subdirektori `main` dengan nama `login.html`.<br><br>
    ```
    {% extends 'base.html' %}

    {% block meta %}
        <title>Login</title>
    {% endblock meta %}

    {% block content %}

    <div class = "login">

        <h1>Login</h1>

        <form method="POST" action="">
            {% csrf_token %}
            <table>
                <tr>
                    <td>Username: </td>
                    <td><input type="text" name="username" placeholder="Username" class="form-control"></td>
                </tr>
                        
                <tr>
                    <td>Password: </td>
                    <td><input type="password" name="password" placeholder="Password" class="form-control"></td>
                </tr>

                <tr>
                    <td></td>
                    <td><input class="btn login_btn" type="submit" value="Login"></td>
                </tr>
            </table>
        </form>

        {% if messages %}
            <ul>
                {% for message in messages %}
                    <li>{{ message }}</li>
                {% endfor %}
            </ul>
        {% endif %}     
            
        Don't have an account yet? <a href="{% url 'main:register' %}">Register Now</a>

    </div>

    {% endblock content %}
    ```
* Selanjutnya kita perlu menambahkan impor fungsi yang sudah kita buat tadi pada berkas `urls.py` yang terdapat pada subdirektori `main`. <br><br>
    ```
    from main.views import login_user
    ```
* Kita juga perlu menambahkan _path url_ ke dalam `urlpatterns` agar kita dapat mengakses fungsi login. <br><br>
    ```
    ...
    path('login/', login_user, name='login'),
    ...
    ```
### Membuat Fungsi Logout
* Sama hal nya dengan fungsi registrasi dan login, sebelum membuat fungsi logout kita perlu menambahkan import fungsi logout pada berkas `view.py` yang terdapat pada subdirektori `main`. <br><br>
    ```
    from django.contrib.auth import logout
    ```
* Selanjutnya kita membuat fungsi yang bernama `logout_user` dan menambahkan potongan kode dibawah ini ke dalam fungsi tersebut.<br><br>
    ```
    def logout_user(request):
        logout(request)
        return redirect('main:login')
    ```
    **Penjelasan Kode:**
    * `logout(request)` digunakan untuk mengakhiri sesi pengguna yang sedang aktif saat ini, sehingga mereka tidak lagi dianggap masuk.
    * `return redirect('main:login')` mengarahkan pengguna ke halaman login dalam aplikasi Django setelah mereka keluar atau logout dari sesi mereka.
* Selanjutnya kita akan menambahkan kode berikut pada berkas `main.html` pada forlder templates yang terdapat di subdirektori main. <br><br>
    ```
    ...
    <a href="{% url 'main:logout' %}">
        <button>
            Logout
        </button>
    </a>
    ...
    ```
* Kemudian kita akan menambahkan impor fungsi yang sebelumnya telah kita buat kedalam `urls.py` yang terletak pada subdirektori `main`. <br><br>
    ```
    from main.views import logout_user
    ```
* Kita juga akan menambahkan _path url_ ke dalam `urlpatterns` untuk menambahkan fungsi yang telah di impor. <br><br>
    ```
    ...
    path('logout/', logout_user, name='logout'),
    ...
    ```

### Contoh Akun Pengguna (beserta dummy item)
Akun 1:
* Username: rumintang
* pw : cloud123
* Items: 
    - rings	    (4)	  gold rings with diamond	
    - necklace	(2)	  Necklace with red ruby stone
    - bracelet	(10)  White pearl bracelet

Akun 2:
* Username: Drake
* pw : hello987
* Items: 
    - rings	    (3)	  Silver rings
    - necklace	(4)	  Necklace with skull chain
    - earrings	(7)   Drop hoop earrings

Sebelum menghubungkan `item` dan `user` kita perlu merestriksi akses halaman main:
* Di dalam berkas `views.py` pada subdirektori `main`, tambahkan perintah dibawah ini pada bagian paling atas. Ini digunakan untuk mewajibkan pengguna untuk melakukan login sebelum mengakses halaman web tertentu.<br><br>
    ```
    from django.contrib.auth.decorators import login_required
    ``` 
* Selanjutnya, beri kode berikut di atas fungsi `show_main` dalam berkas tersebut. Ini akan memastikan bahwa halaman `main` hanya dapat diakses oleh pengguna yang sudah login (terautentikasi).<br><br>
    ```
    ...
    @login_required(login_url='/login')
    def show_main(request):
    ...
    ``` 
* Setelah menerapkan pembatasan akses, jalankan proyek Django dengan menggunakan perintah `python manage.py runserver`. Ketika mencoba membuka http://localhost:8000/ di browser, user akan mengalami pengalihan (redirect) ke halaman login, bukan melihat daftar produk di halaman "main".

### Menghubungkan Model `Item` dengan `User`
* Pertama-tama kita perlu mengimpor kode dibaawah ini pada `models.py` yang terdapat di dalam subdirektori `main`. <br><br>
    ```
    ...
    from django.contrib.auth.models import User
    ...
    ```
* Selanjutnya pada model `Item` yang telah kita buat sebelumnya, kita perlu menambahkan kode berikut:
    ```
    class Item(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ...
    ```
    Kode di atas digunakan untuk mengaitkan satu produk dengan satu pengguna melalui hubungan tertentu, di mana setiap produk selalu terasosiasi dengan satu pengguna. <br><br>
* Selanjutnya kita perlu mengubah fungsi `create_item` yang terdapat pada subdirektori `main` di dalam `views.py`. <br><br>
    ```
    def create_item(request):
    form = ItemForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        item = form.save(commit=False)
        item.user = request.user
        item.save()
        return HttpResponseRedirect(reverse('main:show_main'))
    ...
    ```
    Parameter `commit=False` digunakan untuk menunda penyimpanan objek formulir ke database, memungkinkan modifikasi sebelum disimpan. Contohnya, kita mengisi field `user` dengan objek `User` yang sesuai dengan pengguna yang sedang login.
* Untuk dapat mengupdate hal yang telah kita lakukan sebelumnya, kita perlu mengubah fungsi `show_main` sebagai berikut. <br><br>
    ```
    def show_main(request):
        item = Item.objects.filter(user=request.user)

        context = {
            'name': request.user.username,
        ...
    ...
    ```
    Kode di atas digunakan untuk menampilkan `item` yang berhubungan dengan pengguna yang sedang login. Ini dilakukan dengan memfilter semua `item` dan hanya mengambil `item` yang memiliki pengguna yang sama dengan pengguna yang saat ini masuk. Kode `request.user.username` digunakan untuk menampilkan nama pengguna yang login di halaman utama.
* Setelah semua perubahan dilakukan, kita perlu melakukan migrasi model dengan menjalankan `python manage.py makemigrations` pada terminal.

### Menerapkan _Cookies_ pada Sparkle Sphere
* Pertama-tama kita perlu menambahkan beberapa import ke dalam `views.py` yang terletak pada subdirektori `main`.<br><br>
    ```
    import datetime
    from django.http import HttpResponseRedirect
    from django.urls import reverse
    ```
* Pada fungsi `login_user`, kita akan menambahkan fungsi untuk membuat sebuah _cookie_ bernama `last_login` yang akan digunakan untuk melacak kapan terakhir kali pengguna melakukan login. Caranya adalah dengan mengganti kode yang ada dalam blok `if user is not None` dengan kode berikut: <br><br>
    ```
    ...
    if user is not None:
        login(request, user)
        response = HttpResponseRedirect(reverse("main:show_main")) 
        response.set_cookie('last_login', str(datetime.datetime.now()))
        return response
    ...
    ```
    **Penjelasan Kode:**
    * `login(request, user)` berguna untuk melakukan proses login terlebih dahulu.
    * `response = HttpResponseRedirect(reverse("main:show_main"))` berguna untuk membuat respons atau halaman yang akan ditampilkan.
    * `response.set_cookie('last_login', str(datetime.datetime.now()))` berguna menciptakan _cookie_ bernama `'last_login'` dan menyelipkannya ke dalam respons yang sedang dibuat.
* Kita akan menambahkan potongan kode `'last_login': request.COOKIES['last_login']` yang berguna untuk menambahkan informasi cookie last_login yang akan ditampilkan pada halaman web pada fungsi `show_main` ke dalam variabel `context`, seperti berikut:
    ```
    context = {
    'name': 'Rumintang Jessica Hutagaol',
    'class': 'PBP A',
    'items' : items,
    'last_login': request.COOKIES['last_login'],
    }
    ```
* Kemudian kita perlu mengubah fungsi `logout_user` sebagai berikut.<br><br>
    ```
    def logout_user(request):
        logout(request)
        response = HttpResponseRedirect(reverse('main:login'))
        response.delete_cookie('last_login')
        return response
    ```
    `response.delete_cookie('last_login')` berperan dalam menghilangkan `cookie` `last_login` ketika pengguna melakukan proses _logout_.

* Kemudian kita akan menambahkan potongan kode berikut pada berkas `main.html` di antara tabel dan tombol _logout_ untuk menampilkan data _last login_.<br><br>
    ```
    ...
    <h5>Sesi terakhir login: {{ last_login }}</h5>
    ...
    ```
Kita dapet menjalankan perintah `python manage.py runserver` maka kita dapat melihat data _last login_ akan muncul di halaman _main_.

# Tugas 5

## 1. Jelaskan manfaat dari setiap element _selector_ dan kapan waktu yang tepat untuk menggunakannya.
BElement Selector digunakan untuk memilih semua elemen dengan tag yang sama di dalam dokumen HTML. Berikut merupakan penjelasan tiga jenis _selector_: **Element Selector**, **ID Selector**, dan **Class Selector**. <br><br>

* **Element Selector:**
   Element Selector digunakan untuk memilih semua elemen dengan tag yang sama di dalam dokumen HTML. Contohnya, jika kita ingin memilih semua elemen `<p>` dalam dokumen HTML yang telah kita buat, kita dapat menggunakan selector ini. Berikut merupakan manfaat dari Element Selector:
   - Mengganti gaya atau menerapkan aturan CSS secara umum (elemen dengan tag yang sama).
   - Kita dapat menggunakan Element Selector dalam JavaScript untuk memanipulasi elemen-elemen tersebut. Ini berguna ketika kita ingin menambahkan event listener atau mengubah isi elemen-elemen tersebut.
   
   Waktu yang tepat untuk menggunakan Element Selector adalah ketika kita ingin memilih semua elemen dengan tag yang sama dan menerapkan aturan CSS atau operasi JavaScript pada semua elemen tersebut.<br><br>
   **Contoh penggunaan Element Selector:**

        ```
        p {
            color: blue;
        }
        ```
* **ID Selector:**
    ID Selector digunakan untuk memilih elemen dengan atribut id yang cocok dengan nilai yang ditentukan. Setiap id harus unik di dalam dokumen HTML, sehingga ID Selector akan memilih satu elemen tertentu. Manfaat dari ID Selector adalah:<br>
    - Mengganti gaya atau menerapkan aturan CSS pada suatu elemen tertentu.
    - ID Selector dapat digunakan dalam JavaScript untuk memilih dan memanipulasi elemen tertentu.
    
    Waktu yang tepat untuk menggunakan ID Selector adalah ketika kita perlu memilih atau memanipulasi satu elemen tertentu di dalam dokumen HTML.<br><br>
    **Contoh penggunaan ID Selector:**

        ```
        #header {
            background-color: gray;
        }
        ```
* **Class Selector:**
    Class Selector digunakan untuk memilih semua elemen yang memiliki kelas tertentu (atribut class) yang sesuai dengan nilai yang ditentukan. Dalam dokumen HTML, kita dapat memberikan banyak elemen kelas yang sama. Manfaat dari Class Selector adalah:
    - Kita dapat menggabungkan beberapa elemen yang berbeda dengan kelas yang sama dan menerapkan aturan CSS yang sama pada mereka.
    - Class Selector dapat berguna untuk memilih dan memanipulasi semua elemen kelas tertentu. Selector ini berguna ketika kita ingein melakukan operasi yang sama pada beberapa elemen terkait.

    Waktu yang tepat untuk menggunakan Class Selector adalah ketika Anda ingin memilih dan memanipulasi elemen-elemen yang memiliki kelas tertentu atau saat Anda ingin menerapkan aturan CSS yang sama pada kelompok elemen tertentu. <br><br>
    **Contoh penggunaan Class Selector:**

        ```
        .button {
            background-color: green;
        }
        ```
## 2. Jelaskan HTML5 Tag yang kamu ketahui.
 - `<header>`: Digunakan untuk mendefinisikan bagian atas halaman web atau kepala dokumen. Biasanya berisi elemen-elemen seperti judul situs, logo, dan menu navigasi.

 - `<nav>`: Digunakan untuk mengelompokkan tautan navigasi, seperti menu utama atau menu samping.

 - `<section>`: Digunakan untuk mengelompokkan konten yang terkait tematik dalam halaman. Setiap bagian dapat memiliki judul yang diidentifikasi oleh elemen `<h1>` - `<h6>`.

 - `<time>`: Digunakan untuk menandai waktu atau tanggal dalam teks, dan dapat membantu mesin pencari dan layanan aksesibilitas untuk mengenali konten waktu.

 - `<main>`: Digunakan untuk mendefinisikan konten utama halaman web. Biasanya, hanya ada satu elemen `<main>` dalam satu halaman.

## 3. Jelaskan perbedaan antara _margin_ dan _padding_.
**Margin** adalah ruang kosong di sekitar elemen HTML. Ini adalah jarak antara elemen dan elemen lainnya atau tepi browser. Margin dapat digunakan untuk menambahkan ruang kosong di sekitar elemen HTML atau untuk mengubah posisi elemen relatif terhadap elemen lainnya. Margin tidak memengaruhi isi elemen itu sendiri, namun hanya memengaruhi jarak di sekitarnya.

**Padding** adalah ruang kosong atau space antar content pada website. Dengan padding, kita bisa memisahkan satu content dengan content lainnya pada website, sehingga layout akan tertata rapi. Ketika kita mengatur padding, elemen akan memengaruhi ruang di sekitar isi elemen, tetapi tidak akan memengaruhi elemen-elemen di luarnya

## 4. Jelaskan perbedaan antara _framework_ CSS Tailwind dan Bootstrap. Kapan sebaiknya kita menggunakan Bootstrap daripada Tailwind, dan sebaliknya?
Tailwind CSS dan Bootstrap adalah dua framework CSS populer yang digunakan dalam pengembangan web untuk memudahkan desain dan pengembangan tampilan halaman web. Mereka memiliki beberapa perbedaan utama, dan pemilihan antara keduanya tergantung pada kebutuhan proyek dan preferensi pengembang.
| Kriteria                        | Tailwind CSS                             | Bootstrap                                 |
|---------------------------------|-----------------------------------------|-------------------------------------------|
| Pendekatan Desain              | Utility-first: Membangun tampilan dengan menggabungkan kelas-kelas utilitas. | Opiniated: Menyediakan komponen-komponen UI siap pakai. |
| Ukuran Framework                | Relatif kecil, hanya memuat apa yang kita gunakan. | Lebih besar, karena banyak komponen dan gaya bawaan. |
| Kustomisasi                     | Sangat mendalam, dapat menyesuaikan secara ekstensif. | Dapat disesuaikan tetapi memerlukan lebih banyak pekerjaan. |
| Kecepatan Memulai               | Mungkin memerlukan lebih banyak waktu untuk memulai, karena memerlukan penulisan lebih banyak kode. | Cepat untuk memulai dengan komponen-komponen UI siap pakai. |
| Komponen UI Siap Pakai          | Tidak menyediakan komponen UI siap pakai, kita harus membangunnya sendiri. | Menyediakan berbagai komponen UI seperti tombol, formulir, dll. |
| Kendali atas Tampilan           | Tinggi, kita memiliki kontrol penuh atas tampilan. | Lebih terbatas karena mengikuti tampilan Bootstrap yang bawaan. |
| Ukuran File                     | Ringan jika kita hanya menggunakan bagian-bagian yang Anda butuhkan. | Lebih besar karena banyak komponen yang disertakan. |

## 5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
Untuk memulai menkostumisasi page project yang sudah kita buat sebelumnya, kita perlu menambahkan Bootstrap ke dalam Aplikasi.

### Menambahkan Bootstrap ke Aplikasi
* Pertama-tama kita perlu menambahkan tag `<meta name="viewport">` ke dalam file `base.html` di dalam subdirektori `templates`.
    ```
    <head>
        {% block meta %}
            <meta charset="UTF-8" />
            <meta name="viewport" content="width=device-width, initial-scale=1">
        {% endblock meta %}
    </head>
    ```
* Kita juga perlu menambahkan Bootstrap CSS dan juga JS.
    * **CSS:**
    ```
    <head>
        {% block meta %}
            ...
        {% endblock meta %}
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-T3c6CoIi6uLrA9TneNEoa7RxnatzjcDSCmG1MXxSR1GAsXEV/Dwwykc2MPK8M2HN" crossorigin="anonymous">
    </head>
    ```
    * **JS:**
    ```
    <head>
        ...
        <script src="https://code.jquery.com/jquery-3.6.0.min.js" integrity="sha384-KyZXEAg3QhqLMpG8r+J4jsl5c9zdLKaUk5Ae5f5b1bw6AUn5f5v8FZJoMxm6f5cH1" crossorigin="anonymous"></script>
    </head>
    ```

### Menambahkan _navbar_ pada Aplikasi
* Pertama-tama kita perlu menambuat berkas `navbar.html` pada direktori `main/template`.
* Selanjutnya saya menambahkan code berikut: <br><br>
    ```
    <nav class="navbar navbar-expand-lg navbar-dark custom-navbar">
        <a class="navbar-brand" href="#"> Rumintang Jessica </a>
        <div class="navbar-nav ml-auto">
            <a class="nav-item nav-link" href="{% url 'main:logout' %}">Logout</a>
        </div>
        <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav"
            aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
            <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarNav">
            <ul class="navbar-nav">
                <li class="nav-item active">
                    <a class="nav-link" href="/">Home <span class="sr-only">(current)</span></a>
                </li>
            </ul>
        </div>
        <img src="https://i.pinimg.com/564x/c6/a7/05/c6a70583464b8be1ba6060a892df5ed0.jpg" alt="Your Logo" class="navbar-logo">
    </nav>
    ```
    Dapat dilihat dari kode diatas, saya menambahkan juga logo dari Aplikasi saya yang bernama sparkle sphere, serta menambahkan button untuk _logout_ dan _home_.<br><br>
    Untuk dapat menambahkan pengaturan pada navbar yang telah kita buat, maka kita perlu menambahkan `styles` sebagai berikut.<br><br>
    ```
    {% block navbar_styles %}
    <style>
        .custom-navbar {
            background-color:#aa8d74; 
            color: #ffffff; /* White text color */
        }

        .custom-heading {
            font-family: 'Font Name', sans-serif;
            font-weight: bold; 
            color: #333; 
            margin-left: 30px;
        }

        .navbar-logo {
            max-width: 80px;
            height: auto; 
            margin-right: 20px;
        }

        .navbar-brand {
            margin-left: 20px;
        }

        body {
        font-family: 'Roboto', sans-serif;here */
        }

        h1, h2, h3, h4, h5, h6, p {
            font-family: 'Roboto', sans-serif;
        }
    </style>

    {% endblock navbar_styles %}
    ```
    Pada kode diatas saya menambahkan beberapa _arrangement_ untuk menentukan posisi yang sesuai untuk gambar serta tulisan dalam navbar, dan juga memberikan warna untuk background dan tulisan. <br><br>

### Menambahkan Fitur _Edit_ pada Aplikasi
* Pada subdirektori `main` kita perlu menambahkan fungsi baru bernama `edit_item` dalam berkas `views.py`.
    ```
    def edit_product(request, id):
        # Get product berdasarkan ID
        item = Item.objects.get(pk = id)

        # Set product sebagai instance dari form
        form = ItemForm(request.POST or None, instance=product)

        if form.is_valid() and request.method == "POST":
            # Simpan form dan kembali ke halaman awal
            form.save()
            return HttpResponseRedirect(reverse('main:show_main'))

        context = {'form': form}
        return render(request, "edit_item.html", context)
    ```
* Selanjutnya kita akan membuat berkas HTML baru yang bernama `edit_item.html` pada subdirektori `main/templates` dan menambahkan kode berikut.
    ```
    {% extends 'base.html' %}

    {% load static %}

    {% block content %}

    <h1>Edit Item</h1>

    <form method="POST">
        {% csrf_token %}
        <table>
            {{ form.as_table }}
            <tr>
                <td></td>
                <td>
                    <input type="submit" value="Edit Item"/>
                </td>
            </tr>
        </table>
    </form>

    {% endblock %}
    ```
* Setelah itu kita perlu menambahkan _path_ url untuk dapat mengakses fungsi yang telah kita buat. Tentunya kita harus mengimport fungsi yang telah dibuat terlebih dahulu.<br><br>
    ```
    from main.views import edit_item
    ```

    ```
    ...
    path('edit-item/<int:id>', edit_item, name='edit_item'),
    ...
    ```
* Selanjutnya kita juga akan menambahkan kode pada `main.html` agar tombol `edit` dapat muncul pada halaman main
    ```
    ...
    <tr>
        ...
        <td>
            <a href="{% url 'main:edit_item' item.pk %}">
                <button>
                    Edit
                </button>
            </a>
        </td>
    </tr>
    ...
    ```
### Menambahkan Fitur _Delete_ pada Aplikasi
* Sama halnya dengan `edit` kita juga perlu melakukan hal yang sama dengan tombol delete. Pertama, kita akan membuat fungsi `delete_item` pada berkas `views.py` yang terdapat pada subdirektori `main`.<br><br>
    ```
    def delete_item(request, id):
        # Get data berdasarkan ID
        item = Item.objects.get(pk = id)
        # Hapus data
        item.delete()
        # Kembali ke halaman awal
        return HttpResponseRedirect(reverse('main:show_main'))
    ```
* Selanjutnya, kita akan mengimpor fungsi yang telah kita buat.<br><br>
    ```
    from main.views import delete_item
    ```
* Setelah itu, kita akan menambahkan path url ke dalam `urlpatterns` agar fungsi dapat diakses.
    ```
    ...
    path('delete/<int:id>', delete_item, name='delete_item'), # sesuaikan dengan nama fungsi yang dibuat
    ...
    ```
* Kemudian, kita akan menambahkan tombol pada `main.html`
    ```
    ...
    <tr>
        ...
        <td>
            <a href="{% url 'main:edit_item' item.pk %}">
                <button>
                    Edit
                </button>
            </a>
            <a href="{% url 'main:delete_item' item.pk %}">
                <button>
                    Delete
                </button>
            </a>
        </td>
    </tr>
    ...
    ```
### Styles pada Aplikasi Main
Pada aplikasi main, saya menambahkan beberapa kustomisasi sebagai berikut
```
<style>

    table {
        margin-top: 20px;
        border-collapse: collapse; /* Added to merge cell borders */
        width: 100%; /* Added to make the table full-width */
    }

    table, th, td {
        border: 2px solid black; /* Added to set border style */
    }

    th, td {
        padding: 8px; /* Added for cell padding */
        text-align: left; /* Added for cell text alignment */
    }
    
    .header-cell {
        background-color: #c4a884;
    }

    h1, h2, h3, h4, h5, h6, p {
        font-family: 'Calibri', sans-serif; /* Use the same font for headings and paragraphs */
    }

    h1 {
        margin-top: 30px;
    }

    h5 {
        margin-top: 20px;
        font-size: medium;
    }

    button{
        background-color: #c19e6d;
    }

</style>
```
Pada kode diatas, saya mengatur backgroud color menggunakan `background-color` serta mengatur padding dan juga margin untuk menyesuaikan penempatan dari tiap elemen, maupun keseluruhan elemen. Selain itu, saya juga menambahkan border untuk membuat tabel, serta mengatur ketebalan dari border yang saya gunakan. Saya juga menambahkan warna pada header dari tabel yang ada.

# Tugas 6
## 1. Jelaskan perbedaan antara asynchronous programming dengan synchronous programming.
| Fitur / Aspek                   | Synchronous Programming   | Asynchronous Programming   |
|----------------------------------|--------------------------|------------------------|
| Alur Eksekusi                   | Satu persatu secara berurutan      | Bersamaan tanpa menunggu satu sama lain |
| Responsifitas                  | Tidak Responsif         | Responsif              |
| Kasus Penggunaan                | Tugas Sederhana, I/O     | I/O, Penundaan, Paralel|
| Penanganan Kesalahan            | Mudah                    | Kompleks                |
| Struktur Kode                   | Linear                   | Kompleks (Callback/Promise/Async-Await) |


## 2. Dalam penerapan JavaScript dan AJAX, terdapat penerapan paradigma event-driven programming. Jelaskan maksud dari paradigma tersebut dan sebutkan salah satu contoh penerapannya pada tugas ini.
Paradigma "event-driven programming" adalah pendekatan pemrograman di mana alur eksekusi program ditentukan oleh peristiwa (event) yang terjadi, bukan oleh aliran eksekusi berurutan. Ini berarti program menunggu peristiwa tertentu terjadi, dan ketika peristiwa tersebut terjadi, program akan merespons secara sesuai.

Contoh penerapannya pada tugas ini adalah dengan penggunaan AJAX (Asynchronous JavaScript and XML) untuk mengambil atau mengirim data ke server secara asinkron. Dalam kasus ini, "event" adalah peristiwa yang terkait dengan permintaan HTTP, seperti permintaan data dari server atau pengiriman data ke server. Anda menentukan peristiwa-peristiwa ini, seperti mengklik tombol "Tambah Item" atau "Edit Item," dan kemudian menentukan bagaimana program harus merespons ketika peristiwa-peristiwa tersebut terjadi.

Contoh konkretnya adalah ketika user mengklik tombol "Tambah Item" pada halaman web Sparkle Sphere. Dengan paradigma event-driven, Saya akan mendefinisikan apa yang harus terjadi ketika tombol ini diklik. Saya menerapkan kode JavaScript yang akan memicu permintaan AJAX untuk menambahkan item baru ke server dan memperbarui tampilan tanpa harus me-refresh seluruh halaman. Inilah salah satu contoh  penggunaan paradigma event-driven dalam pemrograman JavaScript dan AJAX, di mana program yang saya buat merespons peristiwa (klik tombol) dengan mengirim permintaan ke server dan mengupdate tampilan ketika respon dari server diterima.


## 3. Jelaskan penerapan asynchronous programming pada AJAX.
Berikut merupakan beberapa penerapan asynchronous programming pada AJAX:
1. Asynchronous Request
Saat kita membuat permintaan AJAX, seperti mengambil data dari server atau mengirim data ke server, permintaan ini dikirim secara asinkron. Artinya, permintaan ini tidak menghentikan eksekusi kode JavaScript lainnya. Ini sangat penting dalam lingkungan web, di mana responsifitas dan kinerja aplikasi adalah prioritas.

2. Callback Functions
Untuk mengelola permintaan AJAX secara asinkron, kita menggunakan callback functions. Ini adalah fungsi-fungsi JavaScript yang akan dipanggil ketika permintaan selesai. Ada dua callback utama yang digunakan dalam AJAX:
* `onreadystatechange`: Ini adalah callback yang dipanggil setiap kali ada perubahan dalam status permintaan AJAX. Dengan ini, kita dapat memantau status permintaan dan mengambil tindakan sesuai ketika permintaan berubah.
* `onload`: Ini adalah callback yang dipanggil ketika permintaan selesai dengan sukses. kita akan menangani respons dari server di sini dan memperbarui tampilan atau melakukan tindakan lain yang diperlukan.

3. Promises dan async/await
Selain callback functions, kita juga dapat menggunakan fitur `async` dan `await` dalam JavaScript. Fitur ini memungkinkan kita untuk menulis kode yang lebih bersih dan mudah dipahami saat mengelola permintaan AJAX yang asinkron.

4. Error Handling
Kita dapat mengelola kesalahan yang mungkin terjadi dalam permintaan AJAX secara asinkron. Dengan menambahkan callback `onerror`, kita dapat menangani error ketika _request_ gagal.


## 4. Pada PBP kali ini, penerapan AJAX dilakukan dengan menggunakan Fetch API daripada library jQuery. Bandingkanlah kedua teknologi tersebut dan tuliskan pendapat kamu teknologi manakah yang lebih baik untuk digunakan.
Berikut perbandingan antara Fetch API dan jQuery untuk permintaan AJAX:

| Kriteria                   | Fetch API                                   | jQuery                                    |
|----------------------------|--------------------------------------------|-------------------------------------------|
| Kompatibilitas Browser     | Mendukung browser modern dan standar ES6.  | Dirancang untuk kompatibilitas lintas browser termasuk yang lebih lama.         |
| Ketergantungan Eksternal   | Zero-dependency (tidak memerlukan library eksternal). | Memerlukan library eksternal (jQuery library). |
| Kode JavaScript            | Menggunakan Promises untuk mengelola permintaan asinkron. | Menggunakan callback functions untuk menangani respons.    |
| Fleksibilitas              | Memberikan kontrol penuh atas permintaan HTTP dengan dukungan untuk method, header, body, dan opsi lainnya. | Lebih terbatas dalam hal konfigurasi permintaan. |
| Kompleksitas Kode          | Lebih sedikit boilerplate code, membuat kode bersih dan lebih mudah dipahami. | Memiliki lebih banyak boilerplate code, yang dapat menghasilkan callback hell dalam proyek yang lebih besar. |
| Populeritas                | Populer di pengembangan web modern.       | Populer dalam proyek yang lebih tua atau yang memerlukan kompatibilitas lintas browser yang ketat. |

## 6. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
* Membuat function yang bernama `get_product_json` untuk mereturn data sebagai JSON:
    ```
    def get_product_json(request):
    product_item = Item.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize('json', product_item))
    ```
    kemudian lakukan _routing_ pada `urls.py`

* Membuat function yang bernama `add_item_ajax` untuk melakukan Add Items menggunakan AJAX:
    ```
    @csrf_exempt
    def add_item_ajax(request):
        if request.method == 'POST':
            name = request.POST.get("name")
            amount= request.POST.get("amount")
            description = request.POST.get("description")
            categories = request.POST.get("categories")
            user = request.user     
            new_item = Item(name=name, amount=amount, description=description, user=user, categories=categories)
            new_item.save()

            return HttpResponse(b"CREATED", status=201)

        return HttpResponseNotFound()
    ```
    kemudian lakukan _routing_ pada `urls.py` <br><br>
    ```
    path('create-ajax/', add_item_ajax, name='add_item_ajax'),
    ```

* Menunjukan items yang ada menggunakan `fetch()` API, kita perlu memasukan kode dibawah ini didalam `<script>`:
    ```
    <script>
        async function getProducts() {
            return fetch("{% url 'main:get_product_json' %}").then((res) => res.json())
        }
    </script>
    ```

    Kemudian masih didalm blok `<script>` kita akan menambahkan `refreshItems()` yang diggunakan untuk _merefresh_ items yang ada secara _asynchronous_.<br><br>
    ```
    ...
        async function refreshItems() {
            const cardContainer = document.getElementById("item-container");
            cardContainer.innerHTML = "";

            const items = await getItems();

            items.forEach((item) => {
                cardContainer.innerHTML += `
                <div class="card-item">
                    <div class="card mx-auto p-3" style="width: 18rem;">
                        <div class="card-body">
                            <h4 class="card-title">${item.fields.name}</h4>
                            <p class="card-text">Amount: ${item.fields.amount} 
                                <button class="btn increment btn-sm rounded-full" onclick="incrementAmount(${item.pk})">+</button> 
                                <button class="btn decrement btn-sm rounded-full" onclick="decrementAmount(${item.pk})">-</button>
                            </p>
                            <p class="card-text">${item.fields.description}</p>
                            <a style="justify-content: baseline;" href='edit-item/${item.pk}' class="btn edit_item" onclick="editItem(${item.pk})">Edit</a>
                            <button style="justify-content: baseline;" class="btn delete_item" onclick="deleteItem(${item.pk})">Delete</button>
                        </div>
                    </div>
                </div>`; 
            });
            document.getElementById("item-container").innerHTML = cardContainer.innerHTML;
        }
        refreshItems()
    </script>
    ```

* Setelah itu saya mengimplementasikan card dan bootstrap pada aplikasi yang saya buat berserta tambahan beberapa button.
    ```
     <div class="modal fade" id="exampleModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
            <div class="modal-dialog">
                <div class="modal-content">
                    <div class="modal-header">
                        <h1 class="modal-title fs-5" id="exampleModalLabel">Add New Item</h1>
                        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                    </div>
                    <div class="modal-body">
                        <form id="form" onsubmit="return false;">
                            {% csrf_token %}
                            <div class="mb-3">
                                <label for="name" class="col-form-label">Name:</label>
                                <input type="text" class="form-control" id="name" name="name"></input>
                            </div>
                            <div class="mb-3">
                                <label for="amount" class="col-form-label">Amount:</label>
                                <input type="number" class="form-control" id="amount" name="amount"></input>
                            </div>
                            <div class="mb-3">
                                <label for="description" class="col-form-label">Description:</label>
                                <textarea class="form-control" id="description" name="description"></textarea>
                            </div>
                        </form>
                    </div>
                    <div class="modal-footer">
                        <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
                        <button type="button" class="btn btn-primary" data-bs-dismiss="modal" data-bs-toggle="modal" data-bs-target="#exampleModal" id="button_add">Add Item</button>
                    </div>
                </div>
            </div>
        </div>
    ```

* Tambahkan fungsi onclick pada button "Add Item" pada modal untuk menjalankan fungsi addItem():

    ```
    <script>
        ...
        document.getElementById("button_add").onclick = addItem
    </script>
    ```
* Berikut merupakan beberapa update pada `login.html`, `edit_item.html` dan `register.html`
    * `login.html`:
        ```
        {% extends 'base.html' %}

        {% block meta %}
            <title>Login</title>
        {% endblock meta %}

        {% block content %}
        {% include 'navbar.html' %}

        <style>
            .login-container {
                text-align: center;
                font-family: Georgia, serif;
                margin-top: 50px;
            }

            .login-box {
                max-width: 400px;
                margin: 0 auto;
                padding: 20px;
                background: #efe1cf;
                border-radius: 5px;
                box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.1);
            }

            .form-group {
                text-align: left;
                margin: 10px 0;
            }

            .form-group label {
                display: block;
                text-align: left;
                margin-bottom: 5px;
                font-family: Georgia, serif;
            }

            .form-control {
                display: block;
                width: 100%;
                padding: 10px;
                margin: 10px 0;
            }

            .login_btn {
                background-color: #a27a55;
                color: #fff;
                padding: 10px 20px;
                border: none;
                cursor: pointer;
                display: block;
                margin: 10px auto;
            }

            .login_btn:hover {
                background-color: rgb(207, 161, 97);
                color: #ffffff;
            }

            h1{
                font-family: "Lucia Bright", serif; 
            }

            p{
                font-family: Georgia, serif;
            }


        </style>

        <div class="login-container">
            <div class="login-box">
                <h1>Login</h1>

                <form method="POST" action="">
                    {% csrf_token %}
                    <div class="form-group">
                        <label for="username">Username:</label>
                        <input type="text" name="username" id="username" placeholder="Username" class="form-control">
                    </div>

                    <div class="form-group">
                        <label for="password">Password:</label>
                        <input type="password" name="password" id="password" placeholder="Password" class="form-control">
                    </div>

                    <div class="form-group">
                        <input class="btn login_btn" type="submit" value="Login">
                    </div>
                </form>

                {% if messages %}
                    <ul>
                        {% for message in messages %}
                            <li>{{ message }}</li>
                        {% endfor %}
                    </ul>
                {% endif %}

                <p>Don't have an account yet? <a href="{% url 'main:register' %}">Register Now</a></p>
            </div>
        </div>

        {% endblock content %}

        ```

        * `edit_item.html`:
        ```
        {% extends 'base.html' %}

        {% load static %}

        {% block content %}

        {% include 'navbar.html' %}

        <style>
            .edit-container {
                max-width: 400px;
                margin: 0 auto;
                padding: 20px;
                background: #efe1cf;
                border-radius: 5px;
                box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.1);
                font-family: Georgia, serif;
                margin-top: 40px;
            }

            .form-group {
                text-align: left;
                margin: 10px 0;
            }

            .form-group label {
                display: block;
                text-align: left;
                margin-bottom: 5px;
                font-family: Georgia, serif;
            }

            .form-control {
                display: block;
                width: 100%;
                padding: 10px;
                margin: 10px 0;
            }

            .btn {
                background-color: #a27a55;
                color: #fff;
                padding: 10px 20px;
                border: none;
                cursor: pointer;
                display: block;
                margin: 10px auto;
                font-family: Georgia, serif;
            }

            .btn:hover {
                background-color: rgb(207, 161, 97);
                color: #fff;
            }

            h1 {
                font-family: "Lucia Bright", serif;
                text-align: center;
                margin-bottom: 30px;
            }
        </style>

        <div class="edit-container">
            <h1>Edit Product</h1>

            <form method="POST">
                {% csrf_token %}
                <div class="form-group">
                    <label for="{{ form.name.id_for_label }}">Name:</label>
                    {{ form.name }}
                </div>
                <div class="form-group">
                    <label for="{{ form.amount.id_for_label }}">Amount:</label>
                    {{ form.amount }}
                </div>
                <div class="form-group">
                    <label for="{{ form.description.id_for_label }}">Description:</label>
                    {{ form.description }}
                </div>
                <div class="form-group">
                    <input type="submit" class="btn" value="Done Edit">
                </div>
            </form>
        </div>

        {% endblock %}

        ```

        * `register.html`:
        ```
        {% extends 'base.html' %}

        {% block meta %}
            <title>Register</title>
        {% endblock meta %}

        {% block content %}
        {% include 'navbar.html' %}

        <style>
            .register-container {
                font-family: Georgia, serif;
                margin-top: 50px;
            }

            .register-box {
                max-width: 400px;
                margin: 0 auto;
                padding: 20px;
                background: #efe1cf;
                border-radius: 5px;
                box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.1);
            }

            .form-group {
                text-align: left;
                margin: 10px 0;
            }

            .form-group label {
                text-align: left;
                display: block;
                margin-bottom: 5px;
                font-family: Georgia, serif;
            }

            .form-control {
                display: block;
                width: 100%;
                padding: 10px;
                margin: 10px 0;
            }

            .register-btn {
                background-color: #a27a55;
                color: #fff;
                padding: 10px 20px;
                border: none;
                cursor: pointer;
                display: block;
                margin: 10px auto;
                font-family: Georgia, serif;
            }

            .register-btn:hover {
                background-color: rgb(207, 161, 97);
                color: #fff;
            }

            h1 {
                font-family: "Lucia Bright", serif;
                text-align: center;
                margin-bottom: 30px;
            }

        </style>

        <div class="register-container">
            <div class="register-box">
                <h1>Register</h1>
                
                <form method="POST">
                    {% csrf_token %}
                    {{ form.username.label_tag }}
                        <input type="text" name="{{ form.username.name }}" class="form-control" id="{{ form.username.id_for_label }}" required>
                    {{ form.password1.label_tag }}
                        <input type="password" name="{{ form.password1.name }}" class="form-control" id="{{ form.password1.id_for_label }}" required>
                    {{ form.password2.label_tag }}
                        <input type="password" name="{{ form.password2.name }}" class="form-control" id="{{ form.password2.id_for_label }}" required>
                    <div class="form-group">
                        <input class="btn register-btn" type="submit" name="submit" value="Register">
                    </div>
                </form>

                {% if messages %}
                    <ul>
                        {% for message in messages %}
                            <li>{{ message }}</li>
                        {% endfor %}
                    </ul>
                {% endif %}
            </div>
        </div>

        {% endblock content %}
        ```



