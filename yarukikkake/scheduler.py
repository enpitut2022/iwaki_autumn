from datetime import datetime, date
from apscheduler.schedulers.background import BackgroundScheduler


def periodic_execution():# 任意の関数名
    print("Hello World")

def start():
  scheduler = BackgroundScheduler()
  scheduler.add_job(periodic_execution, 'cron', hour=16, minute=50, second=00)# 毎日23時59分に実行
  scheduler.start()