import os
import requests
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Mock Database untuk simulasi riwayat (karena API resmi tidak ada)
# Di dunia nyata, ini akan menembak ke API OSINT luar atau database lokal kamu
MOCK_HISTORY = {
    "12345678": ["@old_user1", "@old_user2", "@current_user"],
    "8097908138": ["@demo_v1", "@demo_beta", "@DemoWebsBot"]
}

def get_owner_info(token):
    """Mencoba melacak owner melalui interaksi pertama atau konfigurasi admin"""
    url = f"https://api.telegram.org/bot{token}/getUpdates"
    try:
        response = requests.get(url, timeout=10).json()
        if response.get("ok") and response["result"]:
            # Biasanya pesan pertama (indeks 0) berasal dari pembuat bot saat testing
            first_msg = response["result"][0].get("message", {})
            from_user = first_msg.get("from", {})
            if from_user:
                return {
                    "owner_id": from_user.get("id"),
                    "owner_user": f"@{from_user.get('username')}" if from_user.get('username') else "N/A",
                    "owner_name": from_user.get("first_name", "N/A")
                }
        return {"owner_id": "Unknown", "owner_user": "Hidden/Not Found", "owner_name": "Unknown"}
    except:
        return {"owner_id": "Error", "owner_user": "Error", "owner_name": "Error"}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/inspect', methods=['POST'])
def inspect():
    token = request.form.get('token')
    url = f"https://api.telegram.org/bot{token}/getMe"
    
    try:
        res = requests.get(url).json()
        if res.get("ok"):
            bot_data = res["result"]
            owner = get_owner_info(token) # Panggil fungsi pelacak owner
            
            return jsonify({
                "status": "success",
                "bot_id": bot_data["id"],
                "name": bot_data["first_name"],
                "username": f"@{bot_data['username']}",
                "owner_id": owner["owner_id"],
                "owner_user": owner["owner_user"],
                "owner_name": owner["owner_name"]
            })
        return jsonify({"status": "error", "msg": "Invalid Token"})
    except Exception as e:
        return jsonify({"status": "error", "msg": str(e)})

@app.route('/history', methods=['POST'])
def history():
    user_id = request.form.get('user_id')
    # Simulasi pencarian riwayat berdasarkan ID Akun
    history_data = MOCK_HISTORY.get(str(user_id), ["No history found for this ID"])
    return jsonify({"status": "success", "history": history_data})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
