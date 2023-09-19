from aiogram import Bot, Router, F
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery

from keyboards.ex import get_checkin_kb
from middlewares.ex import WeekendMessageMiddleware

router = Router()
router.message.filter(F.chat.type == "private")


@router.message(Command("start"))
async def cmd_checkin(message: Message, bot: Bot):
    channel_invite_link = await bot.create_chat_invite_link(chat_id='-1001859136925', member_limit=1)
    await message.answer(
        f"link: {channel_invite_link.invite_link}",
        # reply_markup=get_checkin_kb()
    )
