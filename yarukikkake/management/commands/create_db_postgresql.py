from django.core.management.base import BaseCommand
from django.conf import settings
import json
import uuid
import sqlite3
import psycopg2
from django.utils import timezone



class Command(BaseCommand):
    help = 'デプロイ用データベース生成プログラム'

    def handle(self, *args, **options):
        # デプロイ先のに接続する
        conn = psycopg2.connect("postgres://yarukikkake:pfhb0YyJ8RqevUVdhzoQN3W4leSIyVPM@dpg-ce1hp7en6mpu84o18v3g-a/yarukikkake_test_db")
        cur = conn.cursor()

        # kdb.josnを開く
        with open("kdb.json", "r", encoding="utf-8") as f:
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
                + ") values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);", col)

        print("スレッド生成が完了しました。")
        conn.commit()
        conn.close()
