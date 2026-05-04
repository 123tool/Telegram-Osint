import os
import requests
from flask import Flask, render_template, request, jsonify
from colorama import Fore, init

init(autoreset=True)
app = Flask(__name__)

# SPY-E
VERSION = "1.0.0"
BRAND = "OSINT TELEGRAM"

def validate_bot(token):
    """Fungsi inti untuk inspeksi Bot Telegram"""
    url = f"https://api.telegram.org/bot{token}/getMe"
    try:
        response = requests.get(url, timeout=10).json()
        if response.get("ok"):
            res = response["result"]
            # Mendapatkan data updates untuk Chat ID
            updates_url = f"https://api.telegram.org/bot{token}/getUpdates"
            updates = requests.get(updates_url, timeout=10).json()
            
            recent_chats = []
            if updates.get("ok"):
                for up in updates["result"]:
                    msg = up.get("message", {})
                    chat = msg.get("chat", {})
                    if chat and chat not in recent_chats:
                        recent_chats.append(chat)

            return {
                "status": "valid",
                "id": res["id"],
                "name": res["first_name"],
                "username": res["username"],
                "link": f"https://t.me/{res['username']}",
                "can_groups": res.get("can_join_groups", False),
                "recent_chats": recent_chats[:5] # Ambil 5 interaksi terakhir
            }
        return {"status": "invalid", "msg": response.get("description")}
    except Exception as e:
        return {"status": "error", "msg": str(e)}

@app.route('/')
def index():
    return render_template('index.html', version=VERSION, brand=BRAND)

@app.route('/inspect', methods=['POST'])
def inspect():
    token = request.form.get('token')
    if not token:
        return jsonify({"status": "error", "msg": "Token is required"})
    
    result = validate_bot(token)
    return jsonify(result)

if __name__ == '__main__':
    # Menjalankan di Localhost / Anonymous IP
    print(f"{Fore.CYAN}[*] {BRAND} Starting...")
    print(f"{Fore.GREEN}[+] Web UI: http://127.0.0.1:5000")
    app.run(host='0.0.0.0', port=5000, debug=True)
