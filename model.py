import sqlite3

# データベースの作成とテーブルの初期化
def initialize_db():
    conn = sqlite3.connect('shiritori.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS words
                (id INTEGER PRIMARY KEY, word TEXT UNIQUE)''')
    conn.commit()
    conn.close()

# テキストファイルからデータベースへの単語のインポート
def import_words_from_file(file_path):
    conn = sqlite3.connect('shiritori.db')
    c = conn.cursor()
    with open(file_path, 'r', encoding='utf-8') as file:  # エンコーディングを指定
        for line in file:
            word = line.strip()
            if word:
                try:
                    c.execute("INSERT INTO words (word) VALUES (?)", (word,))
                except sqlite3.IntegrityError:
                    continue  # 重複した単語を無視
    conn.commit()
    conn.close()


# データベースとテーブルの初期化を実行
initialize_db()
# テキストファイルからの単語のインポート（ファイルパスを適宜変更してください）
import_words_from_file('words.txt')

