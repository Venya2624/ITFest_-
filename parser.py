from time import sleep
import requests
import telebot
from bs4 import BeautifulSoup as bs
import lxml

import db
from config import token

bot = telebot.TeleBot(token)

# href = f"/ + {technocom_last_wall_post_id}"

technocom_html = requests.get('https://vk.com/wall-210998761?own=1')

technocom_soup = bs(technocom_html.text, 'lxml')

technocom_last_wall_post_text = technocom_soup.find('div', class_='pi_text').text

# idx = str(technocom_last_wall_post).index('/')
# subs1 = str(technocom_last_wall_post_text)[idx+1:]
# idx2 = str(subs1).index('"')
# subs2 = subs1[:idx2]
# print(technocom_last_wall_post_text)
technocom_users = db.cur.execute('SELECT telegram_id FROM technocom').fetchall()



technocom_last_wall_post_id_find = technocom_soup.find(f'a', class_='wi_date')
technocom_last_wall_post_id = str(technocom_last_wall_post_id_find['href'])[1:]
print(technocom_last_wall_post_id)

def send_to_user_technocom_post():
    global technocom_last_wall_post_text, technocom_users
    for i in technocom_users:
        global technocom_last_wall_post_text
        print(i)  
        bot.send_message(i, text=technocom_last_wall_post_text)
        
#print(send_to_user_technocom_post())


def check_technocom_posts():
        check = db.cur.execute('SELECT * FROM technocom_posts WHERE post_id=?', (technocom_last_wall_post_id, ))
        if check.fetchone() is None:
            db.update_technocom_posts_db((technocom_last_wall_post_id, ))
            send_to_user_technocom_post()

    #################################################################################

itfest_html = requests.get('https://vk.com/wall-210985709?own=1')

itfest_soup = bs(itfest_html.text, 'lxml')

itfest_last_wall_post_text = itfest_soup.find('div', class_='pi_text').text

# idx = str(technocom_last_wall_post).index('/')
# subs1 = str(technocom_last_wall_post_text)[idx+1:]
# idx2 = str(subs1).index('"')
# subs2 = subs1[:idx2]

print(itfest_last_wall_post_text)


itfest_last_wall_post_id_find = itfest_soup.find(f'a', class_='wi_date')
itfest_last_wall_post_id = str(itfest_last_wall_post_id_find['href'])[1:]
print(itfest_last_wall_post_id)


        ################################################################################

def check_all():
    while True:
        check_technocom_posts()
        sleep(300)
