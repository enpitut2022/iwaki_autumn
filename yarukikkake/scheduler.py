from datetime import datetime, date
from apscheduler.schedulers.background import BackgroundScheduler
from django_apscheduler.jobstores import DjangoJobStore, register_events, register_job, DjangoJob
from django_apscheduler.models import DjangoJobExecution
from linebot import LineBotApi
from linebot.models import TextSendMessage
import datetime
import pytz

def _20221209_1800():# 12/09金・授業後・プログラム言語処理
    line_bot_api = LineBotApi("XtWv3Sv/BEkhMqI9hOFCQCDI2FNEZ7ic14xnPxs7Oe+zhZdfrg6BB8f2iOlWgrEfOL0ecfe5MQp+MG4zAuzhZfn0GzoIXSJdOQ9yUmXZOCdia7AFNN+apGdqulruV5WLcFPMXhh1uLa2jt+MW4rFCQdB04t89/1O/w1cDnyilFU=")
    line_bot_api.broadcast(TextSendMessage("やるきっかけの予定が生成されました!\n【題名】:プログラム言語処理#9をやっつける会\n【対象学類】:情報科学類生(他学類も可)\n【日時】:12/9 20時から1時間程度(途中入退出OK)\n好きなところのURLから参加しよう!\n\n【Discord(音声)】https://discord.com/channels/963633143317938176/997416162218483782 \n"))

def _20221212_0830():# 12/12月・朝・情報線形代数
    line_bot_api = LineBotApi("XtWv3Sv/BEkhMqI9hOFCQCDI2FNEZ7ic14xnPxs7Oe+zhZdfrg6BB8f2iOlWgrEfOL0ecfe5MQp+MG4zAuzhZfn0GzoIXSJdOQ9yUmXZOCdia7AFNN+apGdqulruV5WLcFPMXhh1uLa2jt+MW4rFCQdB04t89/1O/w1cDnyilFU=")
    line_bot_api.broadcast(TextSendMessage("やるきっかけの予定が生成されました!\n【題名】:情報線形代数#9をやっつける会\n【対象学類】:情報科学類生(他学類も可)\n【日時】:12/12 20時から1時間程度(途中入退出OK)\n好きなところのURLから参加しよう!\n\n【Discord(音声)】https://discord.com/channels/963633143317938176/997416162218483782 \n"))

def _20221212_1800():# 12/12月・授業後・情報線形代数
    line_bot_api = LineBotApi("XtWv3Sv/BEkhMqI9hOFCQCDI2FNEZ7ic14xnPxs7Oe+zhZdfrg6BB8f2iOlWgrEfOL0ecfe5MQp+MG4zAuzhZfn0GzoIXSJdOQ9yUmXZOCdia7AFNN+apGdqulruV5WLcFPMXhh1uLa2jt+MW4rFCQdB04t89/1O/w1cDnyilFU=")
    line_bot_api.broadcast(TextSendMessage("やるきっかけの予定が生成されました!\n【題名】:情報線形代数#9をやっつける会\n【対象学類】:情報科学類生(他学類も可)\n【日時】:12/12 20時から1時間程度(途中入退出OK)\n好きなところのURLから参加しよう!\n\n【Discord(音声)】https://discord.com/channels/963633143317938176/997416162218483782 \n"))

def _20221213_0830():# 12/13火・朝・ソフトウェア工学
    line_bot_api = LineBotApi("XtWv3Sv/BEkhMqI9hOFCQCDI2FNEZ7ic14xnPxs7Oe+zhZdfrg6BB8f2iOlWgrEfOL0ecfe5MQp+MG4zAuzhZfn0GzoIXSJdOQ9yUmXZOCdia7AFNN+apGdqulruV5WLcFPMXhh1uLa2jt+MW4rFCQdB04t89/1O/w1cDnyilFU=")
    line_bot_api.broadcast(TextSendMessage("やるきっかけの予定が生成されました!\n【題名】:ソフトウェア工学#9をやっつける会\n【対象学類】:情報科学類生(他学類も可)\n【日時】:12/13 20時から1時間程度(途中入退出OK)\n好きなところのURLから参加しよう!\n\n【Discord(音声)】https://discord.com/channels/963633143317938176/997416162218483782 \n"))

def _20221213_1800():# 12/13火・授業後・ソフトウェア工学
    line_bot_api = LineBotApi("XtWv3Sv/BEkhMqI9hOFCQCDI2FNEZ7ic14xnPxs7Oe+zhZdfrg6BB8f2iOlWgrEfOL0ecfe5MQp+MG4zAuzhZfn0GzoIXSJdOQ9yUmXZOCdia7AFNN+apGdqulruV5WLcFPMXhh1uLa2jt+MW4rFCQdB04t89/1O/w1cDnyilFU=")
    line_bot_api.broadcast(TextSendMessage("やるきっかけの予定が生成されました!\n【題名】:ソフトウェア工学#9をやっつける会\n【対象学類】:情報科学類生(他学類も可)\n【日時】:12/13 20時から1時間程度(途中入退出OK)\n好きなところのURLから参加しよう!\n\n【Discord(音声)】https://discord.com/channels/963633143317938176/997416162218483782 \n"))

def _20221213_2230():
    line_bot_api = LineBotApi("XtWv3Sv/BEkhMqI9hOFCQCDI2FNEZ7ic14xnPxs7Oe+zhZdfrg6BB8f2iOlWgrEfOL0ecfe5MQp+MG4zAuzhZfn0GzoIXSJdOQ9yUmXZOCdia7AFNN+apGdqulruV5WLcFPMXhh1uLa2jt+MW4rFCQdB04t89/1O/w1cDnyilFU=")
    line_bot_api.broadcast(TextSendMessage("This is a test"))
    
def _20221213_2255():
    line_bot_api = LineBotApi("XtWv3Sv/BEkhMqI9hOFCQCDI2FNEZ7ic14xnPxs7Oe+zhZdfrg6BB8f2iOlWgrEfOL0ecfe5MQp+MG4zAuzhZfn0GzoIXSJdOQ9yUmXZOCdia7AFNN+apGdqulruV5WLcFPMXhh1uLa2jt+MW4rFCQdB04t89/1O/w1cDnyilFU=")
    line_bot_api.broadcast(TextSendMessage("This is a test2"))
    
def _20221214_0600():
    line_bot_api = LineBotApi("XtWv3Sv/BEkhMqI9hOFCQCDI2FNEZ7ic14xnPxs7Oe+zhZdfrg6BB8f2iOlWgrEfOL0ecfe5MQp+MG4zAuzhZfn0GzoIXSJdOQ9yUmXZOCdia7AFNN+apGdqulruV5WLcFPMXhh1uLa2jt+MW4rFCQdB04t89/1O/w1cDnyilFU=")
    line_bot_api.broadcast(TextSendMessage("This is a test3"))

def start():
    scheduler = BackgroundScheduler()
    django_job_store = DjangoJobStore()
    scheduler.add_jobstore(django_job_store, "default")
    print("---")
    try :
        django_job_store.remove_all_jobs()
    except :
        pass
    print("---")
    scheduler.add_job(_20221209_1800, 'cron', year=2022, month=12, day=9, hour=18, minute=00, id="test1")
    scheduler.add_job(_20221212_0830, 'cron', year=2022, month=12, day=12, hour=8, minute=30, id="test2")
    scheduler.add_job(_20221212_1800, 'cron', year=2022, month=12, day=12, hour=18, minute=00, id="test3")
    scheduler.add_job(_20221213_0830, 'cron', year=2022, month=12, day=13, hour=8, minute=30, id="test4")
    scheduler.add_job(_20221213_1800, 'cron', year=2022, month=12, day=13, hour=18, minute=00, id="test5")
    scheduler.add_job(_20221213_2230, 'cron', year=2022, month=12, day=13, hour=22, minute=30, id="test6")
    scheduler.add_job(_20221213_2255, 'cron', year=2022, month=12, day=13, hour=22, minute=55, id="test7")
    scheduler.add_job(_20221214_0600, 'cron', year=2022, month=12, day=14, hour=6, minute=00, id="test8")
    scheduler.start()
    pass