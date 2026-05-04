# BOT-SENTRY PRO v1.0
**Advanced Telegram Bot Inspector by SPY-E**

Alat profesional untuk memvalidasi token, mengekstrak metadata, dan melacak interaksi chat bot Telegram.

## 🚀 Instalasi

### **Ubuntu / Xubuntu / Kali Linux**
1. Buka terminal di ThinkPad X280 kamu.
2. Pastikan Python terinstal: `sudo apt update && sudo apt install python3-pip -y`.
3. Masuk ke folder proyek: `cd bot-sentry`.
4. Install library: `pip3 install -r requirements.txt`.
5. Jalankan server: `python3 app.py`.
6. Akses via browser: `http://localhost:5000` atau `http://127.0.0.1:5000`.

### **Termux (Android)**
1. `pkg update && pkg upgrade`.
2. `pkg install python`.
3. `pip install flask requests colorama`.
4. `python app.py`.
5. Buka browser di HP dan ketik: `localhost:5000`.

## 🛡️ Fitur Pro
- **Token Validation**: Cek apakah token aktif atau mati secara instan.
- **Identity Tracker**: Mendapatkan Bot ID, Username, dan Tautan Permanen.
- **Interaction Log**: Menampilkan ID User/Grup yang baru saja mengirim pesan ke bot (Chat ID).
- **Anonymous UI**: Berjalan di localhost IP dengan tampilan Neo-Brutalist.
