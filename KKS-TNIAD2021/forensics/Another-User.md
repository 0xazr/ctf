# Another-User
Kami menyita sebuah mesin dari terduga pelaku perentasan pada website sebuah perusahaan, di situ diberikan sebuah akun yang dapat masuk ke dalam sebuah mesinnya, dapatkah kamu mendapatkan akun selain **guest**? KKST2021{username:password}

Password VM : **4d1b54eeaceb5277ea022f7b42b53113**

##  Penjelasan
Diberikan sebuah soal dengan format zip yang terkunci, dan didalamnya terdapat file OVA. Temukan akun selain user **guest** untuk mendapatkan flag.

## How to Solve

1. Ekstrak zip dengan masukkan password yang telah diberikan dan didapatkan file berekstensi **.ova**.
2. Jalankan file OVA. (bisa menggunakan VirtualBox atau VMWare)
3. Login menggunakan username dan password **guest::guest**.
4. Lihat isi file **/etc/passwd** untuk melihat list user. Didapatkan username lain yaitu **ellen**.<br/>
    ``cat /etc/passwd``
5. Lihat isi file **/etc/shadow** untuk melihat list password user.<br/>
    ``cat /etc/shadow``
6. Bruteforce password dengan menggunakan tools **John The Ripper** dan wordlist rockyou.txt.
	Karena user **guest** tidak bisa menginstall package, maka kita harus mengcopy manual username dan password ke terminal milik kita.
	Command :<br/>
	``john --wordlist=wordlist/rockyou.txt pass``<br/>
	
	dengan isi file pass :<br/>
	``ellen:$6$2MEFal4T$iq0DtS8CD4CXEdST5MT6hmhK2ERdgPqJs6kzHImiFgnE34UwNdAwgig/XsyLRzRnxxtNGKLWMCzpTlAHO2l0k/:1002:1002::/home/ellen:/bin/bash``<br/>
7. Didapatkan password **ellen** adalah **ihateyou**

## Flag
KKST2021{ellen:ihateyou}

