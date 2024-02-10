from flask import Flask, request, jsonify, render_template
import sqlite3
import ctypes

libc = ctypes.cdll.LoadLibrary("return.score.so")

app = Flask(__name__)

def word_exists(word):
    conn = sqlite3.connect('shiritori.db')
    c = conn.cursor()
    c.execute("SELECT word FROM words WHERE word = ?", (word,))
    result = c.fetchone()
    conn.close()
    return result is not None

def check_word(last_word, new_word):
    if not word_exists(new_word):
        return False, "データベースに単語が存在しません。"
    
    if last_word and last_word[-1] != new_word[0]:
        return False, "新しい単語は前の単語の最後の文字から始まる必要があります。"
    
    if new_word[-1] == 'ん':
        return False, "ゲームオーバー。単語が「ん」で終わっています。"
    
    return True, "有効な単語です！"

@app.route('/shiritori', methods=['POST'])
def shiritori():
    data = request.json
    last_word = data.get('last_word', '')
    new_word = data.get('new_word', '')
    
    valid, message = check_word(last_word, new_word)
    if valid:
        return jsonify({"success": True, "message": message}), 200
    else:
        return jsonify({"success": False, "message": message}), 400

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
    print(libc.check_eostr_nn("イオン"))