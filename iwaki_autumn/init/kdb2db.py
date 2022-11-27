import json
import sqlite3
import uuid

# manage.pyと同じディレクトリにあるdb.sqlite3に接続する
conn = sqlite3.connect("db.sqlite3")
cur = conn.cursor()

# kdb.josnを開く
with open("init/kdb.json", "r", encoding="utf-8") as f:
    kdb = json.load(f)

print("講義データベース・スレッド生成プログラム")
print(f"kdb.json Updated at {kdb['updated']}")

print("スレッド生成を開始します。")

# スレッドを生成する
for sub in kdb["subject"]:
    col = [sub[0], sub[1], sub[3], sub[4], sub[5], sub[8], sub[9], sub[13], sub[14], sub[15]]
    # cur.excute()でSQL文を実行する
    cur.execute("insert into yarukikkake_subject("
                + "code,name,unit,grade,semester,teachers,overview,subtype,schools,colleges"
                + ") values (?,?,?,?,?,?,?,?,?,?);", col)

print("スレッド生成が完了しました。")
conn.commit()
conn.close()
