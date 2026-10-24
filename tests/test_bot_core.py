import unittest
from bot.core import Bot
from bot.handlers import (
    register_default_handlers,
    start_handler,
    help_handler,
    echo_handler,
    calc_handler,
    info_handler,
    safe_eval_math
)

class TestBotCore(unittest.TestCase):

    def setUp(self):
        self.bot = Bot(name="TestBot")
        register_default_handlers(self.bot)

    def test_empty_message(self):
        res = self.bot.process_message("")
        self.assertIn("مرحباً", res)

    def test_start_command(self):
        res = self.bot.process_message("/start")
        self.assertIn("أهلاً بك", res)

    def test_help_command(self):
        res = self.bot.process_message("/help")
        self.assertIn("قائمة الأوامر", res)

    def test_echo_command(self):
        res = self.bot.process_message("/echo مرحبا بالعالم")
        self.assertEqual(res, "🗣️ مرحبا بالعالم")

        res_empty = self.bot.process_message("/echo")
        self.assertIn("الرجاء إدخال نص", res_empty)

    def test_calc_command(self):
        res = self.bot.process_message("/calc 12 + 8 * 2")
        self.assertIn("28", res)

        res_err = self.bot.process_message("/calc 10 / 0")
        self.assertIn("خطأ", res_err)

    def test_info_command(self):
        res = self.bot.process_message("/info")
        self.assertIn("معلومات البوت", res)

    def test_unknown_command(self):
        res = self.bot.process_message("/unknown_cmd")
        self.assertIn("غير معروف", res)

    def test_custom_handler(self):
        def ping_handler(args, context):
            return "pong!"

        self.bot.register_command("ping", ping_handler)
        res = self.bot.process_message("/ping")
        self.assertEqual(res, "pong!")

    def test_default_handler(self):
        def fallback(msg, ctx):
            return f"معالجة: {msg}"

        self.bot.set_default_handler(fallback)
        res = self.bot.process_message("مرحبا كيف الحال")
        self.assertEqual(res, "معالجة: مرحبا كيف الحال")

if __name__ == "__main__":
    unittest.main()
