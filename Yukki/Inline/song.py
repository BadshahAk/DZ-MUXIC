from pyrogram.types import (CallbackQuery, InlineKeyboardButton,
                            InlineKeyboardMarkup, InputMediaPhoto, Message)


def song_markup(videoid, duration, user_id, query, query_type):
    buttons = [
        [
            InlineKeyboardButton(
                text="๐๐ข๐ช๐ก๐๐ข๐๐",
                callback_data=f"qwertyuiopasdfghjkl {videoid}|{user_id}",),
        ],
        [
            InlineKeyboardButton(
                text="แดสแดแด ",
                callback_data=f"song_right B|{query_type}|{query}|{user_id}",
            ),
            InlineKeyboardButton(
                text="ษดแดxแด",
                callback_data=f"song_right F|{query_type}|{query}|{user_id}",
            ),
        ],
        [
            InlineKeyboardButton(
                text="๐๐๐๐ข๐ฆ๐๐ข",
                callback_data=f"forceclose {query}|{user_id}",
            )
        ],
    ]
    return buttons


def song_download_markup(videoid, user_id):
    buttons = [
        [
            InlineKeyboardButton(
                text="โฌ๏ธ ๐๐จ๐๐๐ข!!",
                callback_data=f"gets audio|{videoid}|{user_id}",
            ),
            InlineKeyboardButton(
                text="โฌ๏ธ ๐ฉ๐๐๐๐ข!!",
                callback_data=f"gets video|{videoid}|{user_id}",
            ),
        ],
        [
            InlineKeyboardButton(
                text="๐ ๐๐๐ข๐ฆ๐",
                callback_data=f"forceclose {videoid}|{user_id}",
            )
        ],
    ]
    return buttons
