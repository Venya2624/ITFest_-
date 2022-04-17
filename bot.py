from threading import Thread
import telebot
from telebot import types

from config import token
import btn
from db import create_all_db
from parser import check_all

bot = telebot.TeleBot(token)


@bot.message_handler(commands = ['start'])
def start(msg):
    markup = types.InlineKeyboardMarkup(row_width = 1)
    to_follow = types.InlineKeyboardButton(text='Подпишитесь на новости!', callback_data='to_follow')
    contacts = types.InlineKeyboardButton(text='Контактные данные организаторов', callback_data='contacts')

    markup.add(to_follow, contacts)
    bot.send_message(msg.chat.id, text='Здравствуйте', reply_markup = markup)
    print(msg)

@bot.message_handler(commands = ['help'])
def start(msg):
    bot.send_message(msg.chat.id, text='Этот бот может осуществлять подписку / отписку на информационные группы ВК.')
    
@bot.message_handler(commands = ['menu'])
def menu(msg):
    markup = types.InlineKeyboardMarkup(row_width = 1)
    to_follow = types.InlineKeyboardButton(text='Подпишитесь на новости!', callback_data='to_follow')
    contacts = types.InlineKeyboardButton(text='Контактные данные организаторов', callback_data='contacts')
    bot.send_message(msg.chat.id, text='Меню', reply_markup=markup)

    
@bot.message_handler(commands = ['get_posts'])
def get_posts(msg):
    bot.send_message(msg.chat.id, text='Новых постов нет')
    
@bot.message_handler(commands = ['follow'])
def follow(msg):
    bot.send_message(msg.chat.id, text='Подпишитесь на группы')
    btn.to_follow_btn()
    

    
    
@bot.callback_query_handler(func=lambda call: True)
def call_data(call):
    if call.data == 'to_follow':
        bot.answer_callback_query(call.id)
        btn.to_follow_btn(call)
        print(call)

    elif call.data == 'to_follow_technocom':
        bot.answer_callback_query(call.id)
        btn.to_follow_technocom(call)

    elif call.data == 'to_unfollow_technocom':
        bot.answer_callback_query(call.id)
        btn.to_unfollow_technocom(call)

    elif call.data == 'to_follow_it_fest_2022':
        bot.answer_callback_query(call.id)
        btn.to_follow_it_fest_2022(call)

    elif call.data == 'to_unfollow_it_fest_2022':
        bot.answer_callback_query(call.id)
        btn.to_unfollow_(call)

    elif call.data == 'to_follow_iasf_2022':
        bot.answer_callback_query(call.id)
        btn.to_follow_iasf_2022(call)

    elif call.data == 'to_unfollow_iasf_2022':
        bot.answer_callback_query(call.id)
        btn.to_unfollow_iasf_2022(call)

    elif call.data == 'to_follow_festival_okk':
        bot.answer_callback_query(call.id)
        btn.to_follow_festival_okk(call)

    elif call.data == 'to_unfollow_festival_okk':
        bot.answer_callback_query(call.id)
        btn.to_unfollow_festival_okk(call)

    elif call.data == 'to_follow_neirofest':
        bot.answer_callback_query(call.id)
        btn.to_follow_neirofest(call)

    elif call.data == 'to_unfollow_neirofest':
        bot.answer_callback_query(call.id)
        btn.to_unfollow_neirofest(call)

    elif call.data == 'to_follow_invisible_world':
        bot.answer_callback_query(call.id)
        btn.to_follow_technocom(call)

    elif call.data == 'to_unfollow_invisible_world':
        bot.answer_callback_query(call.id)
        btn.to_unfollow_invisible_world(call)

    elif call.data == 'to_follow_nir':
        bot.answer_callback_query(call.id)
        btn.to_follow_nir(call)

    elif call.data == 'to_unfollow_nir':
        bot.answer_callback_query(call.id)
        btn.to_unfollow_nir(call)

    elif call.data == 'to_follow_vrar_fest':
        bot.answer_callback_query(call.id)
        btn.to_follow_vrar_fest(call)

    elif call.data == 'to_unfollow_vrar_fest':
        bot.answer_callback_query(call.id)
        btn.to_unfollow_vrar_fest(call)

    elif call.data == 'contacts':
        bot.answer_callback_query(call.id)
        markup = types.InlineKeyboardMarkup(row_width=1)
        back_to_menu_btn = types.InlineKeyboardButton(text='Вернуться назад', callback_data='back_to_menu_btn')
        markup.add(back_to_menu_btn)

        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text='some', reply_markup=markup)

    elif call.data == 'back_btn':
        bot.answer_callback_query(call.id)
        btn.to_follow_btn(call)


print('bot is working...')

create_all_db()

thread_check = Thread(target=check_all)
thread_check.start()

bot.polling(none_stop=True)
