Cara Pakai
Tool ini dijalankan lewat terminal / Termux.
Pastikan kamu sudah ada di folder tempat file Shell_FinderCinCau.py berada.
Command dasar
Salin kode
Bash
python Shell_FinderCinCau.py https://target.com
Contoh
Salin kode
Bash
python Shell_FinderCinCau.py https://example.com
Kalau target pakai http, ya pakai http.
Kalau https, pakai https.
Penjelasan Command
Salin kode
Bash
python Shell_FinderCinCau.py https://target.com
python → menjalankan Python
Shell_FinderCinCau.py → file utama tool
https://target.com → target website yang mau dicek
Tool bakal otomatis:
ambil daftar payload dari shell_payloads.txt
cek satu-satu ke target
nampilin hasil di terminal
Kalau Salah Pakai
Kalau command kurang target, bakal keluar pesan:
Salin kode

Usage : python Shell_FinderCinCau.py https://target.com
Artinya tinggal tambahin URL target aja.
Tips
Jangan pakai slash di akhir URL
❌ https://target.com/
✅ https://target.com
Payload bisa kamu edit sendiri di:
Salin kode

shell_payloads.txt
Catatan
Tool ini cuma ngecek shell yang sudah ada.
Bukan upload, bukan exploit.
Gunakan hanya di target yang kamu punya izin.
