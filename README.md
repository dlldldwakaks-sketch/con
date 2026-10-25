# Bot Application - تطبيق البوت المساعد 🤖

تطبيق بوت تفاعلي ومرن بلغة بايثون يتيح التواصل التفاعلي عبر واجهة السطر البرمجي (CLI) أو عبر منصة تيليجرام (Telegram Bot).

An interactive and flexible Python Bot application supporting CLI mode and Telegram Bot integration.

---

## 🌟 المميزات / Features

- 💬 **وضع التيرمينال التفاعلي (CLI Mode)**: للتواصل واختبار البوت محلياً بسهولة.
- 📱 **دعم تيليجرام (Telegram Bot Support)**: ربط البوت مباشرة مع منصة Telegram باستخدام Bot API Token.
- ⚡ **أوامر مدمجة جاهزة / Built-in Commands**:
  - `/start`: بدء الجلسة والترحيب.
  - `/help`: عرض قائمة الأوامر المتاحة.
  - `/echo <نص>`: إعادة طباعة النص المدخل.
  - `/calc <تعبير>`: حاسبة رياضية آمنة وسريعة.
  - `/info`: عرض معلومات وإصدار البوت.
- 🧩 **قابلية للتوسيع (Extensible)**: تسجيل أوامر جديدة ومقيدات افتراضية بسهولة.
- 🧪 **اختبارات آلية (Unit Tests)**: حزمة اختبارات لضمان جودة الأداء واستقرار الكود.

---

## 🚀 طريقة التثبيت والتشغيل / Getting Started

### 1. التثبيت / Installation

تأكد من وجود **Python 3.8+** مثبت على جهازك.

```bash
# تثبيت المتطلبات (إن وجدت)
pip install -r requirements.txt
```

---

### 2. التشغيل / Usage

#### أ) وضع التيرمينال التفاعلي (CLI Mode):
```bash
python3 main.py
# أو
python3 main.py --mode cli
```

#### ب) تنفيذ أمر مباشر (Single Message Execution):
```bash
python3 main.py --message "/start"
python3 main.py --message "/calc (15 + 5) * 2"
```

#### ج) ربط بوت تيليجرام (Telegram Mode):
قم بتمرير رمز البوت (Bot Token) الذي حصلت عليه من `@BotFather`:
```bash
python3 main.py --mode telegram --token "YOUR_TELEGRAM_BOT_TOKEN"
```
أو عبر تعيين متغير البيئة:
```bash
export TELEGRAM_BOT_TOKEN="YOUR_TELEGRAM_BOT_TOKEN"
python3 main.py --mode telegram
```

---

## 🧪 تشغيل الاختبارات / Running Tests

يمكنك تشغيل الاختبارات الآلية باستخدام unittest:

```bash
python3 -m unittest discover -s tests
```

---

## 📂 الهيكل التنظيمي للمشروع / Project Structure

```
.
├── bot/
│   ├── __init__.py       # حزمة البوت
│   ├── core.py           # المحرك الرئيسي لمعالجة الأوامر والرسائل
│   ├── handlers.py       # معالجات الأوامر المدمجة (/start, /help, /calc, إلخ)
│   ├── cli_bot.py        # واجهة التيرمينال التفاعلية
│   └── telegram_bot.py   # التكامل مع Telegram API
├── tests/
│   └── test_bot_core.py  # الاختبارات الآلية للبوت
├── main.py               # نقطة التشغيل الرئيسية
├── requirements.txt      # التبعيات والحيود
└── README.md             # وثائق المشروع
```
