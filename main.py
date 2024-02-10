from flask import Flask, request, jsonify, render_template
import sqlite3
import ctypes

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

def find_cpu_word(last_char):
    conn = sqlite3.connect('shiritori.db')
    c = conn.cursor()
    c.execute("SELECT word FROM words WHERE word LIKE ? ORDER BY RANDOM() LIMIT 1", (last_char + '%',))
    result = c.fetchone()
    conn.close()
    if result:
        return True, result[0]
    else:
        return False, "見つかりませんでした。私の負けです。"

def check_word(last_word, new_word):
    # 既存のチェックロジック...
    # 新しい単語が「ん」で終わっていないかチェック
    if new_word[-1] == 'ん':
        cpu_loses = True
        return False, "ゲームオーバー。単語が「ん」で終わっています。", cpu_loses
    
    # CPUの単語を探す
    cpu_loses = False
    valid, cpu_word = find_cpu_word(new_word[-1])
    if not valid:
        cpu_loses = True  # CPUが単語を見つけられなかった場合
    return True, f"有効な単語です！ CPUのターン: {cpu_word}", cpu_loses


@app.route('/shiritori', methods=['POST'])
def shiritori():
    data = request.json
    last_word = data.get('last_word', '')
    new_word = data.get('new_word', '')
    
    valid, message, cpu_loses = check_word(last_word, new_word)
    if valid:
        if cpu_loses:
            return jsonify({"success": True, "message": message, "cpu_loses": True}), 200
        return jsonify({"success": True, "message": message, "cpu_loses": False}), 200
    else:
        return jsonify({"success": False, "message": message}), 400


@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)