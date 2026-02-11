import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart, Command, CommandObject
from aiogram.types import Message, CallbackQuery, LabeledPrice, PreCheckoutQuery
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram import Bot, Dispatcher, types
from aiogram.types import Message

# --- Configuration ---
TOKEN = '8259364164:AAHk461J3YyHbRGkTv0Y_1THSLNwlaEGvdc'
PAYMENT_TOKEN = 'YOUR_PAYMASTER_TOKEN'  # Replace with your payment provider token

bot = Bot(token=TOKEN)
dp = Dispatcher()

# --- Keyboards ---
start_kb = InlineKeyboardBuilder()
start_kb.button(text="Оплатить подписку 🌟", callback_data="subscribe")

payment_kb = InlineKeyboardBuilder()
payment_kb.button(text="Оплатить🌟", pay=True)
payment_kb.button(text="Подписка на месяц за 100⭐", callback_data="subscribe_months")
payment_kb.button(text="Подписка на 3 месяца за 250⭐", callback_data="subscribe_3_months")
payment_kb.button(text="Навсегда за 1000⭐", callback_data="subscribe_permanent")
payment_kb.adjust(1)

# URL картинки для отправки в /start9
WELCOME_IMAGE_URL = 'https://postimg.cc/B8gVPgmH'# <- замените на актуальную ссылку

@dp.message(CommandStart())
async def start(message: Message):
    caption_text = (
        "Привет!\n"
        "Если ты столкнулся с блокировкой Телеграмма от РКН, не огорчайся — у меня есть решение! 🔓🚀\n\n"
        "Почему VPN не помогает?\n"
        "Многие пытаются решать проблему с помощью VPN, но РКН научился обходить такие меры. Простым VPN зачастую недостаточно — блокировки остаются.\n\n"
        "Что я предлагаю?\n"
        "У меня есть уникальный обходчик блокировок, который действительно работает! Хотите выйти из подполья и снова пользоваться всеми фишками Телеграма? Тогда лучше купить у меня специальный доступ.\n\n"
        "Преимущества:\n"
        "- Надежное обходное решение\n"
        "- Быстро и удобно\n"
        "- Безопасно и конфиденциально\n\n"
        "Готовы восстановить доступ?"
        "/help для большей информации"
    )
    # Отправляем фото с подписью и кнопками
    await message.answer_photo(WELCOME_IMAGE_URL, caption=caption_text, reply_markup=start_kb.as_markup())

@dp.message(Command(commands=['help']))
async def handle_help(message: Message):
    help_text = (
        "🤖 Команды бота:\n"
        "/start - Начало работы и информация\n"
        "/help - Подсказки по использованию\n\n"
        "/service - как работает наш бот\n\n"
        "Для оплаты подписки нажмите кнопку 'Оплатить подписку 🌟' после /start или используйте меню."
    )
    await message.answer(help_text)
    
@dp.message(Command(commands=['service']))
async def handle_service(message: Message):
    service_text = (
        "Как работает наш обходчик блокировок и почему стоит своих денег\n\n"
        "**Как это работает?**  \n"
        "Наш бот использует уникальную технологию обхода блокировок — он подключается к специально настроенным серверам и использует сложные маршруты, которые не блокируются РКН. В отличие от обычных VPN, которые могут быть легко обнаружены и заблокированы, наши решения работают на уровне сети и используют инновационные методы защиты, гарантируя стабильный доступ к Телеграмму даже в условиях жестких блокировок.\n\n"
        "**Почему это надежно?**  \n"
        "- Постоянное обновление и настройка серверов для обхода новых методов блокировки.  \n"
        "- Инновационные протоколы, делающие обнаружение и блокировку максимально сложной задачей для Роскомнадзора.  \n"
        "- Простое и быстрое подключение — без сложных настроек и техподдержки.\n\n"
        "**Почему именно цена оправдана?**  \n"
        "- **Высокие технологии**: мы используем эксклюзивные алгоритмы и инфраструктуру, которая стоит дорого в разработке и поддержке.  \n"
        "- **Гарантированный результат**: покупая у нас, вы получаете уверенность в доступе, а это — ценность, которую сложно переплатить.  \n"
        "- **Эксклюзивность**: такой обход не доступен бесплатными методами, а запуск собственных решений требует времени и ресурсов.  \n"
        "- **Безопасность и конфиденциальность**: ваш трафик защищен и не будет отслежен или заблокирован повторно по мере развития технологий цензуры.\n\n"
        "**Итог:**  \n"
        "Платя за доступ к нашему сервису, вы инвестируете в стабильность, безопасность и свободу общения — ценности, которые невозможно оценить деньгами. Наши клиенты уже уверенно пользуются Телеграммом и не переживают о блокировках — а это, согласитесь, стоит своих денег!"
    )
    await message.answer(service_text)
    

# Обработка кнопки "Оплатить подписку 🌟"
@dp.callback_query(F.data == "subscribe")
async def handle_subscribe(call: CallbackQuery):
    price = [LabeledPrice(label='XTR', amount=250)]  # 1 звезда = 100 копеек
    await call.message.answer_invoice(
        title="Подписка на бота",
        description="Возможность пользоваться ботом",
        provider_token=PAYMENT_TOKEN,  # Укажите ваш токен поставщика платежей
        prices=price,
        currency="XTR",
        payload="by_stars",
        reply_markup=payment_kb.as_markup()
    )

@dp.callback_query(F.data == "subscribe_months")
async def handle_subscribe_month(call: CallbackQuery):
    price = [LabeledPrice(label='месяц подписки', amount=100)]  # 100⭐ * 100 копеек
    await call.message.answer_invoice(
        title="Подписка на месяц",
        description="Оформите подписку на месяц",
        provider_token=PAYMENT_TOKEN,
        prices=price,
        currency="XTR",
        payload="month_subscribe",
        reply_markup=payment_kb.as_markup()
    )

@dp.callback_query(F.data == "subscribe_3_months")
async def handle_subscribe_3_months(call: CallbackQuery):
    price = [LabeledPrice(label='3 месяца подписки', amount=250)]  # 250⭐ * 100 копеек
    await call.message.answer_invoice(
        title="Подписка на 3 месяца",
        description="Оформите подписку на 3 месяца",
        provider_token=PAYMENT_TOKEN,
        prices=price,
        currency="XTR",
        payload="3_month_subscribe",
        reply_markup=payment_kb.as_markup()
    )

@dp.callback_query(F.data == "subscribe_permanent")
async def handle_subscribe_permanent(call: CallbackQuery):
    price = [LabeledPrice(label='Навсегда', amount=1000)]  # 1000⭐ * 100 копеек
    await call.message.answer_invoice(
        title="Навсегда",
        description="Пожизненная подписка",
        provider_token=PAYMENT_TOKEN,
        prices=price,
        currency="XTR",
        payload="permanent_subscribe",
        reply_markup=payment_kb.as_markup()
    )

@dp.pre_checkout_query()
async def process_pre_checkout_query(pre_checkout_query: PreCheckoutQuery):
    await bot.answer_pre_checkout_query(pre_checkout_query.id, ok=True)

@dp.message(F.successful_payment)
async def success_payment(message: Message):
    charge_id = message.successful_payment.telegram_payment_charge_id
    await message.answer(f"Спасибо за оплату! ID платежа: <code>{charge_id}</code>", parse_mode="HTML")

# --- Главная функция ---
async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())