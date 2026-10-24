import re
from typing import Callable, Dict, Any, Optional

class Bot:
    """Core Bot engine handling command registration and response generation."""

    def __init__(self, name: str = "AssistantBot", default_language: str = "ar"):
        self.name = name
        self.default_language = default_language
        self.command_handlers: Dict[str, Callable[[str, Any], str]] = {}
        self.default_handler: Optional[Callable[[str, Any], str]] = None

    def register_command(self, command: str, handler: Callable[[str, Any], str]) -> None:
        """Register a command handler function. Command names start with '/' or plain names."""
        clean_cmd = command.strip().lstrip('/').lower()
        self.command_handlers[clean_cmd] = handler

    def set_default_handler(self, handler: Callable[[str, Any], str]) -> None:
        """Set a fallback handler for unhandled text messages."""
        self.default_handler = handler

    def process_message(self, message: str, context: Optional[Dict[str, Any]] = None) -> str:
        """Process an incoming string message and return the bot's response."""
        if context is None:
            context = {}

        message_str = message.strip()
        if not message_str:
            return "مرحباً! كيف يمكنني مساعدتك اليوم؟" if self.default_language == "ar" else "Hello! How can I help you today?"

        if message_str.startswith('/'):
            parts = message_str[1:].split(maxsplit=1)
            cmd = parts[0].lower()
            args = parts[1] if len(parts) > 1 else ""

            if cmd in self.command_handlers:
                try:
                    return self.command_handlers[cmd](args, context)
                except Exception as e:
                    return f"حدث خطأ أثناء معالجة الأمر: {str(e)}" if self.default_language == "ar" else f"Error processing command: {str(e)}"
            else:
                return (
                    f"الأمر '{cmd}' غير معروف. اكتب /help لمشاهدة قائمة الأوامر."
                    if self.default_language == "ar"
                    else f"Unknown command '{cmd}'. Type /help for available commands."
                )

        if self.default_handler:
            return self.default_handler(message_str, context)

        return (
            f"وصلتني رسالتك: {message_str}"
            if self.default_language == "ar"
            else f"Received your message: {message_str}"
        )
