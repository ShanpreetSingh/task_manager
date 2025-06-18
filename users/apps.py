from django.apps import AppConfig

class UsersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'users'

    def ready(self):
        if not hasattr(self, 'telegram_bot_started'):
            from .telegram_bot import setup_bot
            import threading
            
            bot_thread = threading.Thread(target=setup_bot)
            bot_thread.daemon = True
            bot_thread.start()
            
            self.telegram_bot_started = True