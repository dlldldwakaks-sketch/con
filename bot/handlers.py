import math
import ast
import operator
from typing import Dict, Any, Callable
from .core import Bot

def start_handler(args: str, context: Dict[str, Any]) -> str:
    """Handler for /start command."""
    bot_name = context.get('bot_name', 'البوت')
    return (
        f"أهلاً بك في {bot_name}! 👋\n"
        "أنا بوت تفاعلي ومساعد ذكي.\n"
        "اكتب /help لرؤية قائمة الأوامر المتاحة."
    )

def help_handler(args: str, context: Dict[str, Any]) -> str:
    """Handler for /help command."""
    return (
        "📋 قائمة الأوامر المتاحة:\n"
        "• /start - بدء التواصل مع البوت\n"
        "• /help - عرض قائمة الأوامر والتعليمات\n"
        "• /echo <نص> - إعادة طباعة النص المدخل\n"
        "• /calc <تعبير> - حاسبة رياضية بسيطة\n"
        "• /info - معلومات عن البوت والتطبيق"
    )

def echo_handler(args: str, context: Dict[str, Any]) -> str:
    """Handler for /echo command."""
    if not args.strip():
        return "الرجاء إدخال نص بعد الأمر /echo (مثال: /echo مرحبا)"
    return f"🗣️ {args.strip()}"

def safe_eval_math(expr: str) -> str:
    """Safely evaluate mathematical expressions using AST."""
    allowed_operators = {
        ast.Add: operator.add,
        ast.Sub: operator.sub,
        ast.Mult: operator.mul,
        ast.Div: operator.truediv,
        ast.Pow: operator.pow,
        ast.USub: operator.neg,
        ast.UAdd: operator.pos,
        ast.Mod: operator.mod,
    }

    def _eval(node):
        if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)):
            return node.value
        elif isinstance(node, ast.BinOp):
            left = _eval(node.left)
            right = _eval(node.right)
            op_type = type(node.op)
            if op_type in allowed_operators:
                return allowed_operators[op_type](left, right)
            raise ValueError(f"مشغل غير مدعوم: {op_type}")
        elif isinstance(node, ast.UnaryOp):
            operand = _eval(node.operand)
            op_type = type(node.op)
            if op_type in allowed_operators:
                return allowed_operators[op_type](operand)
            raise ValueError(f"مشغل غير مدعوم: {op_type}")
        else:
            raise ValueError("تعبير غير صالح")

    try:
        parsed = ast.parse(expr.strip(), mode='eval')
        result = _eval(parsed.body)
        return f"🔢 النتيجة: {result}"
    except Exception as e:
        return f"❌ خطأ بالحساب: {str(e)}"

def calc_handler(args: str, context: Dict[str, Any]) -> str:
    """Handler for /calc command."""
    if not args.strip():
        return "الرجاء إدخال تعبير رياضي لسرعة الحساب (مثال: /calc 5 + 3 * 2)"
    return safe_eval_math(args)

def info_handler(args: str, context: Dict[str, Any]) -> str:
    """Handler for /info command."""
    return (
        "🤖 معلومات البوت:\n"
        "- الاسم: Bot Engine\n"
        "- الإصدار: 1.0.0\n"
        "- اللغة: Python 3\n"
        "- الحالة: يعمل بنجاح ✅"
    )

def register_default_handlers(bot: Bot) -> None:
    """Register all built-in handlers to the bot."""
    bot.register_command("start", start_handler)
    bot.register_command("help", help_handler)
    bot.register_command("echo", echo_handler)
    bot.register_command("calc", calc_handler)
    bot.register_command("info", info_handler)
