## TELEGRAM OSINT
**Osint Telegram Inspector by SPY-E**

Alat untuk memvalidasi token, mengekstrak metadata, dan melacak interaksi chat bot Telegram.

## 🚀 Instalasi

## **Ubuntu / Xubuntu / Kali Linux**
1. Buka terminal.
2. Pastikan Python terinstal: `sudo apt update && sudo apt install python3-pip -y`.
3. Clone Proyek: `git clone https://github.com/123tool/Telegram-Osint.git`
4. Masuk ke folder proyek: `Telegram-Osint`.
5. Install library: `pip3 install -r requirements.txt`.
6. Jalankan server: `python3 app.py`.
7. Akses via browser: `http://localhost:5000` atau `http://127.0.0.1:5000`.

### **Termux (Android)**
1. `pkg update && pkg upgrade`.
2. `pkg install python`.
3. `git clone https://github.com/123tool/Telegram-Osint.git`.
4. `cd Telegram-Osint`
5. `pip install flask requests colorama`.
6. `python app.py`.
7. Buka browser di HP dan ketik: `localhost:5000`.

## 🛡️ Fitur
- **Token Validation**: Cek apakah token aktif atau mati secara instan.
- **Identity Tracker**: Mendapatkan Bot ID, Username, dan Tautan Permanen.
- **Interaction Log**: Menampilkan ID User/Grup yang baru saja mengirim pesan ke bot (Chat ID).
