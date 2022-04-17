import telebot
from telebot import types

from config import token
from db import update_technocom_db, update_it_fest_2022_db, update_iasf_2022_db, update_festival_okk_db, update_neirofest_db, update_invisible_world_db, update_nir_db, update_vrar_fest_db, cur, conn

bot = telebot.TeleBot(token)

def to_follow_btn(some):
    markup = types.InlineKeyboardMarkup(row_width=1)
    check = cur.execute('SELECT * FROM technocom WHERE telegram_id=?', (some.message.from_user.id, ))
    if check.fetchone() is not None:
        to_follow_technocom = types.InlineKeyboardButton(text='Отписаться от новостей technocom', callback_data='to_unfollow_technocom')
    else:
        to_follow_technocom = types.InlineKeyboardButton(text='Подпишитесь на новости technocom!', callback_data='to_follow_technocom')

    check = cur.execute('SELECT * FROM it_fest_2022 WHERE telegram_id=?', (some.message.from_user.id, ))
    if check.fetchone() is not None:
        to_follow_it_fest_2022 = types.InlineKeyboardButton(text='Отписаться от новостей IT-fest_2022', callback_data='to_unfollow_it_fest_2022')
    else:
        to_follow_it_fest_2022 = types.InlineKeyboardButton(text='Подпишитесь на новости IT-fest_2022!', callback_data='to_follow_it_fest_2022')

    check = cur.execute('SELECT * FROM iasf_2022 WHERE telegram_id=?', (some.message.from_user.id, ))
    if check.fetchone() is not None:
        to_follow_iasf_2022 = types.InlineKeyboardButton(text='Отписаться от новостей IASF2022', callback_data='to_unfollow_iasf_2022')
    else:
        to_follow_iasf_2022 = types.InlineKeyboardButton(text='Подпишитесь на новости IASF2022!', callback_data='to_follow_iasf_2022')

    check = cur.execute('SELECT * FROM festival_okk WHERE telegram_id=?', (some.message.from_user.id, ))
    if check.fetchone() is not None:
        to_follow_festival_okk = types.InlineKeyboardButton(text='Отписаться от новостей ФестивальОКК', callback_data='to_unfollow_festival_okk')
    else:
        to_follow_festival_okk = types.InlineKeyboardButton(text='Подпишитесь на новости ФестивальОКК!', callback_data='to_follow_festival_okk')

    check = cur.execute('SELECT * FROM neirofest WHERE telegram_id=?', (some.message.from_user.id, ))
    if check.fetchone() is not None:
        to_follow_neirofest = types.InlineKeyboardButton(text='Отписаться от новостей Нейрофест', callback_data='to_unfollow_neirofest')
    else:
        to_follow_neirofest = types.InlineKeyboardButton(text='Подпишитесь на новости Нейрофест!', callback_data='to_follow_neirofest')

    check = cur.execute('SELECT * FROM invisible_world WHERE telegram_id=?', (some.message.from_user.id, ))
    if check.fetchone() is not None:
        to_follow_invisible_world = types.InlineKeyboardButton(text='Отписаться от новостей НевидимыйМир', callback_data='to_unfollow_invisible_world')
    else:
        to_follow_invisible_world = types.InlineKeyboardButton(text='Подпишитесь на новости НевидимыйМир!', callback_data='to_follow_invisible_world')

    check = cur.execute('SELECT * FROM nir WHERE telegram_id=?', (some.message.from_user.id, ))
    if check.fetchone() is not None:
        to_follow_nir = types.InlineKeyboardButton(text='Отписаться от новостей КонкурсНИР', callback_data='to_unfollow_nir')
    else:
        to_follow_nir = types.InlineKeyboardButton(text='Подпишитесь на новости КонкурсНИР!', callback_data='to_follow_nir')

    check = cur.execute('SELECT * FROM vrar_fest WHERE telegram_id=?', (some.message.from_user.id, ))
    if check.fetchone() is not None:
        to_follow_vrar_fest = types.InlineKeyboardButton(text='Отписаться от новостей VRARFest3D', callback_data='to_unfollow_vrar_fest')
    else:
        to_follow_vrar_fest = types.InlineKeyboardButton(text='Подпишитесь на новости VRARFest3D!', callback_data='to_follow_vrar_fest')

    global user_id
    user_id = some.message.from_user.id

    markup.add(to_follow_technocom, to_follow_it_fest_2022, to_follow_iasf_2022, to_follow_festival_okk, to_follow_neirofest, to_follow_invisible_world, to_follow_nir, to_follow_vrar_fest)

    bot.edit_message_text(chat_id=some.message.chat.id, message_id=some.message.id, text='Выберете мерероприятие для подписки / отписки', reply_markup = markup)

def to_follow_technocom(some):
    markup = types.InlineKeyboardMarkup(row_width=1)
    back_btn = types.InlineKeyboardButton(text='Вернуться назад', callback_data='back_btn')
    markup.add(back_btn)

    check = cur.execute('SELECT * FROM technocom WHERE telegram_id=?', (some.from_user.id, ))
    if check.fetchone() is None:
        db_list= [some.chat.username, some.from_user.id, 'Active']
        update_technocom_db(db_list)

    bot.edit_message_text(chat_id=some.message.chat.id, message_id=some.message.id, text='Отлично, вы подписались на новости TechnoCom!', reply_markup=markup)

def to_unfollow_technocom(some):
    markup = types.InlineKeyboardMarkup(row_width=1)
    back_btn = types.InlineKeyboardButton(text='Вернуться назад', callback_data='back_btn')
    markup.add(back_btn)

    bot.edit_message_text(chat_id=some.message.chat.id, message_id=some.message.id, text='Хорошо, вы отписались от новостей TechnoCom!', reply_markup=markup)

    check = cur.execute('SELECT * FROM technocom WHERE telegram_id=?', (some.message.from_user.id, ))
    if check.fetchone() is not None:
        delete = """DELETE from technocom where telegram_id = ?"""
        cur.execute(delete, (some.message.from_user.id, ))
        conn.commit()

def to_follow_it_fest_2022(some):
    markup = types.InlineKeyboardMarkup(row_width=1)
    back_btn = types.InlineKeyboardButton(text='Вернуться назад', callback_data='back_btn')
    markup.add(back_btn)

    check = cur.execute('SELECT * FROM it_fest_2022 WHERE telegram_id=?', (some.message.from_user.id, ))
    if check.fetchone() is None:
        db_list= [some.message.chat.username, some.message.from_user.id, 'Active']
        update_it_fest_2022_db(db_list)

    bot.edit_message_text(chat_id=some.message.chat.id, message_id=some.message.id, text='Отлично, вы подписались на новости itfest2022!', reply_markup=markup)

def to_unfollow_it_fest_2022(some):
    markup = types.InlineKeyboardMarkup(row_width=1)
    back_btn = types.InlineKeyboardButton(text='Вернуться назад', callback_data='back_btn')
    markup.add(back_btn)

    bot.edit_message_text(chat_id=some.message.chat.id, message_id=some.message.id, text='Хорошо, вы отписались от новостей itfest2022!', reply_markup=markup)

    check = cur.execute('SELECT * FROM it_fest_2022 WHERE telegram_id=?', (some.message.from_user.id, ))
    if check.fetchone() is not None:
        delete = """DELETE from it_fest_2022 where telegram_id = ?"""
        cur.execute(delete, (some.message.from_user.id, ))
        conn.commit()

def to_follow_iasf_2022(some):
    markup = types.InlineKeyboardMarkup(row_width=1)
    back_btn = types.InlineKeyboardButton(text='Вернуться назад', callback_data='back_btn')
    markup.add(back_btn)

    check = cur.execute('SELECT * FROM iasf_2022 WHERE telegram_id=?', (some.message.from_user.id, ))
    if check.fetchone() is None:
        db_list= [some.message.chat.username, some.message.from_user.id, 'Active']
        update_iasf_2022_db(db_list)

    bot.edit_message_text(chat_id=some.message.chat.id, message_id=some.message.id, text='Отлично, вы подписались на новости iasf2022!', reply_markup=markup)

def to_unfollow_iasf_2022(some):
    markup = types.InlineKeyboardMarkup(row_width=1)
    back_btn = types.InlineKeyboardButton(text='Вернуться назад', callback_data='back_btn')
    markup.add(back_btn)

    bot.edit_message_text(chat_id=some.message.chat.id, message_id=some.message.id, text='Хорошо, вы отписались от новостей iasf_2022!', reply_markup=markup)

    check = cur.execute('SELECT * FROM iasf_2022 WHERE telegram_id=?', (some.message.from_user.id, ))
    if check.fetchone() is not None:
        delete = """DELETE from iasf_2022 where telegram_id = ?"""
        cur.execute(delete, (some.message.from_user.id, ))
        conn.commit()


def to_follow_festival_okk(some):
    markup = types.InlineKeyboardMarkup(row_width=1)
    back_btn = types.InlineKeyboardButton(text='Вернуться назад', callback_data='back_btn')
    markup.add(back_btn)

    check = cur.execute('SELECT * FROM festival_okk WHERE telegram_id=?', (some.message.from_user.id, ))
    if check.fetchone() is None:
        db_list= [some.message.chat.username, some.message.from_user.id, 'Active']
        update_festival_okk_db(db_list)

    bot.edit_message_text(chat_id=some.message.chat.id, message_id=some.message.id, text='Отлично, вы подписались на новости festival_okk!', reply_markup=markup)

def to_unfollow_festival_okk(some):
    markup = types.InlineKeyboardMarkup(row_width=1)
    back_btn = types.InlineKeyboardButton(text='Вернуться назад', callback_data='back_btn')
    markup.add(back_btn)

    bot.edit_message_text(chat_id=some.message.chat.id, message_id=some.message.id, text='Хорошо, вы отписались от новостей festival_okk!', reply_markup=markup)

    check = cur.execute('SELECT * FROM festival_okk WHERE telegram_id=?', (some.message.from_user.id, ))
    if check.fetchone() is not None:
        delete = """DELETE from festival_okk where telegram_id = ?"""
        cur.execute(delete, (some.message.from_user.id, ))
        conn.commit()


def to_follow_neirofest(some):
    markup = types.InlineKeyboardMarkup(row_width=1)
    back_btn = types.InlineKeyboardButton(text='Вернуться назад', callback_data='back_btn')
    markup.add(back_btn)

    check = cur.execute('SELECT * FROM neirofest WHERE telegram_id=?', (some.message.from_user.id, ))
    if check.fetchone() is None:
        db_list= [some.message.chat.username, some.message.from_user.id, 'Active']
        update_neirofest_db(db_list)

    bot.edit_message_text(chat_id=some.message.chat.id, message_id=some.message.id, text='Отлично, вы подписались на новости neirofest!', reply_markup=markup)

def to_unfollow_neirofest(some):
    markup = types.InlineKeyboardMarkup(row_width=1)
    back_btn = types.InlineKeyboardButton(text='Вернуться назад', callback_data='back_btn')
    markup.add(back_btn)

    bot.edit_message_text(chat_id=some.message.chat.id, message_id=some.message.id, text='Хорошо, вы отписались от новостей neirofest!', reply_markup=markup)

    check = cur.execute('SELECT * FROM neirofest WHERE telegram_id=?', (some.message.from_user.id, ))
    if check.fetchone() is not None:
        delete = """DELETE from neirofest where telegram_id = ?"""
        cur.execute(delete, (some.message.from_user.id, ))
        conn.commit()


def to_follow_nir(some):
    markup = types.InlineKeyboardMarkup(row_width=1)
    back_btn = types.InlineKeyboardButton(text='Вернуться назад', callback_data='back_btn')
    markup.add(back_btn)

    check = cur.execute('SELECT * FROM nir WHERE telegram_id=?', (some.message.from_user.id, ))
    if check.fetchone() is None:
        db_list= [some.message.chat.username, some.message.from_user.id, 'Active']
        update_nir_db(db_list)

    bot.edit_message_text(chat_id=some.message.chat.id, message_id=some.message.id, text='Отлично, вы подписались на новости nir!', reply_markup=markup)

def to_unfollow_nir(some):
    markup = types.InlineKeyboardMarkup(row_width=1)
    back_btn = types.InlineKeyboardButton(text='Вернуться назад', callback_data='back_btn')
    markup.add(back_btn)

    bot.edit_message_text(chat_id=some.message.chat.id, message_id=some.message.id, text='Хорошо, вы отписались от новостей nir!', reply_markup=markup)

    check = cur.execute('SELECT * FROM nir WHERE telegram_id=?', (some.message.from_user.id, ))
    if check.fetchone() is not None:
        delete = """DELETE from nir where telegram_id = ?"""
        cur.execute(delete, (some.message.from_user.id, ))
        conn.commit()


def to_follow_invisible_world(some):
    markup = types.InlineKeyboardMarkup(row_width=1)
    back_btn = types.InlineKeyboardButton(text='Вернуться назад', callback_data='back_btn')
    markup.add(back_btn)

    check = cur.execute('SELECT * FROM invisible_world WHERE telegram_id=?', (some.message.from_user.id, ))
    if check.fetchone() is None:
        db_list= [some.message.chat.username, some.message.from_user.id, 'Active']
        update_invisible_world_db(db_list)

    bot.edit_message_text(chat_id=some.message.chat.id, message_id=some.message.id, text='Отлично, вы подписались на новости invisible_world!', reply_markup=markup)

def to_unfollow_invisible_world(some):
    markup = types.InlineKeyboardMarkup(row_width=1)
    back_btn = types.InlineKeyboardButton(text='Вернуться назад', callback_data='back_btn')
    markup.add(back_btn)

    bot.edit_message_text(chat_id=some.message.chat.id, message_id=some.message.id, text='Хорошо, вы отписались от новостей invisible_world!', reply_markup=markup)

    check = cur.execute('SELECT * FROM invisible_world WHERE telegram_id=?', (some.message.from_user.id, ))
    if check.fetchone() is not None:
        delete = """DELETE from invisible_world where telegram_id = ?"""
        cur.execute(delete, (some.message.from_user.id, ))
        conn.commit()


def to_follow_vrar_fest(some):
    markup = types.InlineKeyboardMarkup(row_width=1)
    back_btn = types.InlineKeyboardButton(text='Вернуться назад', callback_data='back_btn')
    markup.add(back_btn)

    check = cur.execute('SELECT * FROM vrar_fest WHERE telegram_id=?', (some.message.from_user.id, ))
    if check.fetchone() is None:
        db_list= [some.message.chat.username, some.message.from_user.id, 'Active']
        update_vrar_fest_db(db_list)

    bot.edit_message_text(chat_id=some.message.chat.id, message_id=some.message.id, text='Отлично, вы подписались на новости vrar_fest!', reply_markup=markup)

def to_unfollow_vrar_fest(some):
    markup = types.InlineKeyboardMarkup(row_width=1)
    back_btn = types.InlineKeyboardButton(text='Вернуться назад', callback_data='back_btn')
    markup.add(back_btn)

    bot.edit_message_text(chat_id=some.message.chat.id, message_id=some.message.id, text='Хорошо, вы отписались от новостей vrar_fest!', reply_markup=markup)

    check = cur.execute('SELECT * FROM vrar_fest WHERE telegram_id=?', (some.message.from_user.id, ))
    if check.fetchone() is not None:
        delete = """DELETE from vrar_fest where telegram_id = ?"""
        cur.execute(delete, (some.message.from_user.id, ))
        conn.commit()