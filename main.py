#!/usr/bin/env python3
import sys
import os
import argparse
from bot.core import Bot
from bot.handlers import register_default_handlers
from bot.cli_bot import CLIBot
from bot.telegram_bot import TelegramBot

def main():
    parser = argparse.ArgumentParser(description="Bot Application - برنامج البوت المساعد")
    parser.add_argument("--mode", choices=["cli", "telegram"], default="cli", help="Mode of operation (cli or telegram)")
    parser.add_argument("--token", type=str, default=os.getenv("TELEGRAM_BOT_TOKEN"), help="Telegram Bot Token (for telegram mode)")
    parser.add_argument("--message", type=str, help="Process a single message and print response directly")

    args = parser.parse_args()

    bot = Bot(name="مساعدك الذكي")
    register_default_handlers(bot)

    if args.message:
        response = bot.process_message(args.message)
        print(response)
        return

    if args.mode == "cli":
        cli = CLIBot(bot=bot)
        cli.start()
    elif args.mode == "telegram":
        if not args.token:
            print("❌ خطأ: يرجى توفير --token أو تعيين متغير البيئة TELEGRAM_BOT_TOKEN")
            sys.exit(1)
        tg_bot = TelegramBot(token=args.token, bot=bot)
        tg_bot.run_polling()

if __name__ == "__main__":
    main()
