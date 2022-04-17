import sqlite3

conn = sqlite3.connect('users_active.db', check_same_thread=False)
cur = conn.cursor()
def create_technocom_db():
    cur.execute("""CREATE TABLE IF NOT EXISTS technocom(
    user TEXT,
    telegram_id INT,
    sub_status TEXT);
    """)
    conn.commit()

def create_technocom_posts_db():
    cur.execute("""CREATE TABLE IF NOT EXISTS technocom_posts(
    post_id TEXT,
    post_text TEXT);
    """)
    conn.commit()

def update_technocom_db(SOME_LIST):
    cur.execute("INSERT INTO technocom VALUES(?, ?, ?);", SOME_LIST)
    conn.commit()

def update_technocom_posts_db(SOME_LIST):
    cur.execute("INSERT INTO technocom_posts VALUES(?, ?);", SOME_LIST)
    conn.commit()


def create_it_fest_2022_db():
    cur.execute("""CREATE TABLE IF NOT EXISTS it_fest_2022(
    user TEXT,
    telegram_id INT,
    sub_status TEXT);
    """)
    conn.commit()

def create_it_fest_2022_posts_db():
    cur.execute("""CREATE TABLE IF NOT EXISTS it_fest_2022_posts(
    post_id TEXT,
    post_text TEXT);
    """)
    conn.commit()

def update_it_fest_2022_db(SOME_LIST):
    cur.execute("INSERT INTO it_fest_2022 VALUES(?, ?, ?);", SOME_LIST)
    conn.commit()

def create_iasf_2022_db():
    cur.execute("""CREATE TABLE IF NOT EXISTS iasf_2022(
    user TEXT,
    telegram_id INT,
    sub_status TEXT);
    """)
    conn.commit()

def create_iasf_2022_posts_db():
    cur.execute("""CREATE TABLE IF NOT EXISTS iasf_2022_posts(
    post_id TEXT,
    post_text TEXT);
    """)
    conn.commit()

def update_iasf_2022_db(SOME_LIST):
    cur.execute("INSERT INTO iasf_2022 VALUES(?, ?, ?);", SOME_LIST)
    conn.commit()

def create_festival_okk_db():
    cur.execute("""CREATE TABLE IF NOT EXISTS festival_okk(
    user TEXT,
    telegram_id INT,
    sub_status TEXT);
    """)
    conn.commit()

def create_festival_okk_posts_db():
    cur.execute("""CREATE TABLE IF NOT EXISTS festival_okk_posts(
    post_id TEXT,
    post_text TEXT);
    """)
    conn.commit()

def update_festival_okk_db(SOME_LIST):
    cur.execute("INSERT INTO festival_okk VALUES(?, ?, ?);", SOME_LIST)
    conn.commit()

def create_neirofest_db():
    cur.execute("""CREATE TABLE IF NOT EXISTS neirofest(
    user TEXT,
    telegram_id INT,
    sub_status TEXT);
    """)
    conn.commit()

def create_neirofest_posts_db():
    cur.execute("""CREATE TABLE IF NOT EXISTS neirofest_posts(
    post_id TEXT,
    post_text TEXT);
    """)
    conn.commit()

def update_neirofest_db(SOME_LIST):
    cur.execute("INSERT INTO technocom VALUES(?, ?, ?);", SOME_LIST)
    conn.commit()


def create_nir_db():
    cur.execute("""CREATE TABLE IF NOT EXISTS nir(
    user TEXT,
    telegram_id INT,
    sub_status TEXT);
    """)
    conn.commit()

def create_nir_posts_db():
    cur.execute("""CREATE TABLE IF NOT EXISTS nir_posts(
    post_id TEXT,
    post_text TEXT);
    """)
    conn.commit()

def update_nir_db(SOME_LIST):
    cur.execute("INSERT INTO technocom VALUES(?, ?, ?);", SOME_LIST)
    conn.commit()


def create_invisible_world_db():
    cur.execute("""CREATE TABLE IF NOT EXISTS invisible_world(
    user TEXT,
    telegram_id INT,
    sub_status TEXT);
    """)
    conn.commit()

def create_invisible_world_posts_db():
    cur.execute("""CREATE TABLE IF NOT EXISTS invisible_world_posts(
    post_id TEXT);
    """)
    conn.commit()

def update_invisible_world_db(SOME_LIST):
    cur.execute("INSERT INTO invisible_world VALUES(?, ?, ?);", SOME_LIST)
    conn.commit()

def create_vrar_fest_db():
    cur.execute("""CREATE TABLE IF NOT EXISTS vrar_fest(
    user TEXT,
    telegram_id INT,
    sub_status TEXT);
    """)
    conn.commit()

def create_vrar_fest_posts_db():
    cur.execute("""CREATE TABLE IF NOT EXISTS vrar_fest_posts(
    post_id TEXT);
    """)
    conn.commit()

def update_vrar_fest_db(SOME_LIST):
    cur.execute("INSERT INTO vrar_fest VALUES(?, ?, ?);", SOME_LIST)
    conn.commit()


def create_all_db():
    create_technocom_db()
    create_technocom_posts_db()
    create_it_fest_2022_db()
    create_it_fest_2022_posts_db()
    create_iasf_2022_db()
    create_iasf_2022_posts_db()
    create_festival_okk_db()
    create_festival_okk_posts_db()
    create_neirofest_db()
    create_neirofest_posts_db()
    create_nir_db()
    create_nir_posts_db()
    create_invisible_world_db()
    create_invisible_world_posts_db()
    create_vrar_fest_db()
    create_vrar_fest_posts_db()

create_all_db()