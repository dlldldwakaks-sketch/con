import sys
from typing import Optional
from .core import Bot
from .handlers import register_default_handlers

class CLIBot:
    """CLI Runner for interactive terminal communication with Bot."""

    def __init__(self, bot: Optional[Bot] = None):
        if bot is None:
            self.bot = Bot(name="مساعد التيرمينال")
            register_default_handlers(self.bot)
        else:
            self.bot = bot

    def start(self) -> None:
        """Start interactive loop in terminal."""
        print(f"=== {self.bot.name} (Interactive CLI) ===")
        print("اكتب رسالتك أو أمرك (مثال: /start أو /help أو /calc 10+20)")
        print("اكتب 'exit' أو 'quit' للخروج.\n")

        context = {'bot_name': self.bot.name}

        while True:
            try:
                user_input = input("أنت: ")
                if user_input.strip().lower() in ['exit', 'quit']:
                    print("تم إنهاء الجلسة. وداعاً! 👋")
                    break
                response = self.bot.process_message(user_input, context=context)
                print(f"البوت: {response}\n")
            except (KeyboardInterrupt, EOFError):
                print("\nتم الخروج.")
                break
