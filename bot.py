import asyncio
from aiogram import Bot, Dispatcher

import config_reader
from handlers import ex, common


# Запуск бота
async def main():
    bot = Bot(token=config_reader.config.bot_token.get_secret_value())
    dp = Dispatcher()

    dp.include_routers(common.router)

    # Запускаем бота и пропускаем все накопленные входящие
    # Да, этот метод можно вызвать даже если у вас поллинг
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
