Cara Pakai
Tool ini dijalankan lewat terminal/Termux
Pastikan kamu sudah berada di folder yang berisi file Shell_FinderCinCau.py

Command Dasar 
python Shell_FinderCinCau.py https://target.com
Contoh :
python Shell_FinderCinCau.py https://example.com

Gunakan:
http:// jika target pakai HTTP
https:// jika target pakai HTTPS

Penjelasan Command :
python Shell_FinderCinCau.py https://target.com

Keterangan:
python → menjalankan Python
Shell_FinderCinCau.py → file utama tool
https://target.com → target website yang ingin dicek
Saat dijalankan, tool akan:

membaca payload dari shell_payloads.txt
mengecek satu per satu ke target
menampilkan hasil scan langsung di terminal
Jika Salah Menggunakan Command
Jika target tidak diisi, akan muncul pesan:
Salin kode

Usage : python Shell_FinderCinCau.py https://target.com
Artinya kamu hanya perlu menambahkan URL target di belakang command.
Tips Penggunaan

Jangan gunakan slash (/) di akhir URL
❌ https://target.com/
✅ https://target.com
Payload bisa kamu edit atau tambahkan sendiri di file :
shell_payloads.txt
