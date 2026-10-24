import time
import urllib.request
import urllib.parse
import json
from typing import Optional, Dict, Any
from .core import Bot
from .handlers import register_default_handlers

class TelegramBot:
    """Telegram Bot wrapper using Telegram HTTP Bot API."""

    def __init__(self, token: str, bot: Optional[Bot] = None):
        self.token = token
        self.api_url = f"https://api.telegram.org/bot{self.token}"
        if bot is None:
            self.bot = Bot(name="Telegram Bot")
            register_default_handlers(self.bot)
        else:
            self.bot = bot

    def send_message(self, chat_id: int, text: str) -> bool:
        """Send message to a Telegram chat."""
        url = f"{self.api_url}/sendMessage"
        payload = json.dumps({"chat_id": chat_id, "text": text}).encode("utf-8")
        req = urllib.request.Request(
            url,
            data=payload,
            headers={"Content-Type": "application/json"}
        )
        try:
            with urllib.request.urlopen(req) as resp:
                data = json.loads(resp.read().decode())
                return data.get("ok", False)
        except Exception as e:
            print(f"Error sending Telegram message: {e}")
            return False

    def get_updates(self, offset: Optional[int] = None, timeout: int = 30) -> list:
        """Get updates from Telegram API (Polling)."""
        url = f"{self.api_url}/getUpdates?timeout={timeout}"
        if offset is not None:
            url += f"&offset={offset}"
        try:
            req = urllib.request.Request(url)
            with urllib.request.urlopen(req, timeout=timeout + 5) as resp:
                data = json.loads(resp.read().decode())
                if data.get("ok"):
                    return data.get("result", [])
        except Exception as e:
            print(f"Error polling Telegram updates: {e}")
        return []

    def run_polling(self) -> None:
        """Run long polling loop to receive messages from Telegram."""
        print(f"Starting Telegram Bot polling for {self.bot.name}...")
        offset = None
        while True:
            try:
                updates = self.get_updates(offset=offset)
                for update in updates:
                    offset = update["update_id"] + 1
                    message = update.get("message") or update.get("edited_message")
                    if not message or "text" not in message:
                        continue

                    chat_id = message["chat"]["id"]
                    text = message["text"]
                    user_info = message.get("from", {})

                    context = {
                        "chat_id": chat_id,
                        "user_info": user_info,
                        "bot_name": self.bot.name
                    }

                    response = self.bot.process_message(text, context=context)
                    self.send_message(chat_id, response)
            except KeyboardInterrupt:
                print("Stopping Telegram bot...")
                break
            except Exception as e:
                print(f"Polling loop exception: {e}")
                time.sleep(3)
