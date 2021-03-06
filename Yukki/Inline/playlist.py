from pyrogram.types import (CallbackQuery, InlineKeyboardButton,
                            InlineKeyboardMarkup, InputMediaPhoto, Message)


def check_markup(user_name, user_id, videoid):
    buttons = [
        [
            InlineKeyboardButton(
                text="๐ฌ๐ผ๐๐ฟ ๐ฃ๐น๐ฎ๐๐๐ถ๐๐",
                callback_data=f"show_genre {user_id}|Personal|{videoid}",
            ),
        ],
        [
            InlineKeyboardButton(text="๐ ๐๐น๐ผ๐๐ฒ", callback_data="close")
        ],
    ]
    return buttons


def playlist_markup(user_name, user_id, videoid):
    buttons = [
        [   InlineKeyboardButton(
                text=f"โจแดแดแดแดแดษดแดsโก",
                url="https://telegra.ph/AnsiMusic-02-23",
            ),
        ],
        [
            InlineKeyboardButton(text="๐ ๐๐น๐ผ๐๐ฒ", callback_data="close")
        ],
    ]
    return buttons


def play_genre_playlist(user_id, type, videoid):
    buttons = [
        [
            InlineKeyboardButton(
                text=f"สแดสสสแดกแดแดแด",
                callback_data=f"play_playlist {user_id}|{type}|Bollywood",
            ),
            InlineKeyboardButton(
                text=f"สแดสสสแดกแดแดแด",
                callback_data=f"play_playlist {user_id}|{type}|Hollywood",
            ),
        ],
        [
            InlineKeyboardButton(
                text=f"แดแดสแดส",
                callback_data=f"play_playlist {user_id}|{type}|Party",
            ),
            InlineKeyboardButton(
                text=f"สแด๊ฐษช",
                callback_data=f"play_playlist {user_id}|{type}|Lofi",
            ),
        ],
        [
            InlineKeyboardButton(
                text=f"sแดแด",
                callback_data=f"play_playlist {user_id}|{type}|Sad",
            ),
            InlineKeyboardButton(
                text=f"แดกแดแดส",
                callback_data=f"play_playlist {user_id}|{type}|Weeb",
            ),
        ],
        [
            InlineKeyboardButton(
                text=f"แดแดษดแดแดสษช",
                callback_data=f"play_playlist {user_id}|{type}|Punjabi",
            ),
            InlineKeyboardButton(
                text=f"แดแดสแดสs",
                callback_data=f"play_playlist {user_id}|{type}|Others",
            ),
        ],
        [
            InlineKeyboardButton(
                text="โฌ๏ธ๐๐ผ ๐๐ฎ๐ฐ๐ธ",
                callback_data=f"main_playlist {videoid}|{type}|{user_id}",
            ),
            InlineKeyboardButton(text="๐ ๐๐น๐ผ๐๐ฒ", callback_data="close"),
        ],
    ]
    return buttons


def add_genre_markup(user_id, type, videoid):
    buttons = [
        [
            InlineKeyboardButton(
                text=f"โ แดกแดแดส",
                callback_data=f"add_playlist {videoid}|{type}|Weeb",
            ),
            InlineKeyboardButton(
                text=f"โ sแดแด",
                callback_data=f"add_playlist {videoid}|{type}|Sad",
            ),
        ],
        [
            InlineKeyboardButton(
                text=f"โ แดแดสแดส",
                callback_data=f"add_playlist {videoid}|{type}|Party",
            ),
            InlineKeyboardButton(
                text=f"โ สแด๊ฐษช",
                callback_data=f"add_playlist {videoid}|{type}|Lofi",
            ),
        ],
        [
            InlineKeyboardButton(
                text=f"โ สแดสสสแดกแดแดแด",
                callback_data=f"add_playlist {videoid}|{type}|Bollywood",
            ),
            InlineKeyboardButton(
                text=f"โ สแดสสสแดกแดแดแด",
                callback_data=f"add_playlist {videoid}|{type}|Hollywood",
            ),
        ],
        [
            InlineKeyboardButton(
                text=f"โ แดแดษดแดแดสษช",
                callback_data=f"add_playlist {videoid}|{type}|Punjabi",
            ),
            InlineKeyboardButton(
                text=f"โ แดแดสแดสs",
                callback_data=f"add_playlist {videoid}|{type}|Others",
            ),
        ],
        [
            InlineKeyboardButton(
                text="โฌ๏ธ๐๐ผ ๐๐ฎ๐ฐ๐ธ", callback_data=f"goback {videoid}|{user_id}"
            ),
            InlineKeyboardButton(text="๐ ๐๐น๐ผ๐๐ฒ", callback_data="close"),
        ],
    ]
    return buttons


def check_genre_markup(type, videoid, user_id):
    buttons = [
        [
            InlineKeyboardButton(
                text=f"แดกแดแดส", callback_data=f"check_playlist {type}|Weeb"
            ),
            InlineKeyboardButton(
                text=f"sแดแด", callback_data=f"check_playlist {type}|Sad"
            ),
        ],
        [
            InlineKeyboardButton(
                text=f"แดแดสแดส", callback_data=f"check_playlist {type}|Party"
            ),
            InlineKeyboardButton(
                text=f"สแด๊ฐษช", callback_data=f"check_playlist {type}|Lofi"
            ),
        ],
        [
            InlineKeyboardButton(
                text=f"สแดสสสแดกแดแดแด",
                callback_data=f"check_playlist {type}|Bollywood",
            ),
            InlineKeyboardButton(
                text=f"สแดสสสแดกแดแดแด",
                callback_data=f"check_playlist {type}|Hollywood",
            ),
        ],
        [
            InlineKeyboardButton(
                text=f"แดแดษดแดแดสษช",
                callback_data=f"check_playlist {type}|Punjabi",
            ),
            InlineKeyboardButton(
                text=f"แดแดสแดสs", callback_data=f"check_playlist {type}|Others"
            ),
        ],
        [InlineKeyboardButton(text="๐ ๐๐น๐ผ๐๐ฒ", callback_data="close")],
    ]
    return buttons


def third_playlist_markup(user_name, user_id, third_name, userid, videoid):
    buttons = [
        [
            InlineKeyboardButton(
                text=f"๐๐ฟ๐ผ๐๐ฝ'๐",
                callback_data=f"show_genre {user_id}|Group|{videoid}",
            ),
            InlineKeyboardButton(
                text=f"{user_name[:8]}'s Playlist",
                callback_data=f"show_genre {user_id}|Personal|{videoid}",
            ),
        ],
        [
            InlineKeyboardButton(
                text=f"{third_name[:16]}'s Playlist",
                callback_data=f"show_genre {userid}|third|{videoid}",
            ),
        ],
        [InlineKeyboardButton(text="๐ ๐๐น๐ผ๐๐ฒ", callback_data="close")],
    ]
    return buttons


def paste_queue_markup(url):
    buttons = [
        [
            InlineKeyboardButton(text="โถ๏ธ", callback_data=f"resumecb"),
            InlineKeyboardButton(text="โธ๏ธ", callback_data=f"pausecb"),
            InlineKeyboardButton(text="โญ๏ธ", callback_data=f"skipcb"),
            InlineKeyboardButton(text="โน๏ธ", callback_data=f"stopcb"),
        ],
        [InlineKeyboardButton(text="๐ค๐๐ฒ๐๐ฒ๐ฑ ๐ฃ๐น๐ฎ๐๐๐ถ๐๐", url=f"{url}")],
        [InlineKeyboardButton(text="๐ ๐๐น๐ผ๐๐ฒ", callback_data=f"close")],
    ]
    return buttons


def fetch_playlist(user_name, type, genre, user_id, url):
    buttons = [
        [
            InlineKeyboardButton(
                text=f"Play {user_name[:10]}'s {genre} Playlist",
                callback_data=f"play_playlist {user_id}|{type}|{genre}",
            ),
        ],
        [InlineKeyboardButton(text="๐๐ต๐ฒ๐ฐ๐ธ๐ผ๐๐ ๐ฃ๐น๐ฎ๐๐๐ถ๐๐", url=f"{url}")],
        [InlineKeyboardButton(text="๐ ๐๐น๐ผ๐๐ฒ", callback_data=f"close")],
    ]
    return buttons


def delete_playlist_markuup(type, genre):
    buttons = [
        [
            InlineKeyboardButton(
                text=f"Yes! Delete",
                callback_data=f"delete_playlist {type}|{genre}",
            ),
            InlineKeyboardButton(text="No!", callback_data=f"close"),
        ],
    ]
    return buttons
