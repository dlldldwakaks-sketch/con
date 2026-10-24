"""
Bot Package - A flexible and extensible Bot framework.
"""

from .core import Bot
from .cli_bot import CLIBot
from .telegram_bot import TelegramBot

__all__ = ["Bot", "CLIBot", "TelegramBot"]
