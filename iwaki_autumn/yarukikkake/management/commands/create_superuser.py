from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from django.conf import settings

User = get_user_model()

class Command(BaseCommand):
    help = '管理者アカウントの作成'

    def handle(self, *args, **options):
        # settings.pyのグローバル変数から値を取得
        if not User.objects.filter(username=settings.SUPERUSER_NAME).exists():
            User.objects.create_superuser(
                username=settings.SUPERUSER_NAME,
                email=settings.SUPERUSER_EMAIL,
                password=settings.SUPERUSER_PASSWORD,
            )
            print('スーパーユーザーを作成しました')
        else:
            print('スーパーユーザーはすでに存在します')