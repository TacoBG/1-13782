import os, sqlite3

def get_db():
    DATABASE = os.path.join('.','blog.sqlite')
    db = sqlite3.connect(DATABASE, detect_types=sqlite3.PARSE_DECLTYPES)
    db.row_factory = sqlite3.Row
    print('Connection created successfully.')
    return db

db = get_db()

def init_db():
    db.executescript(open('schema.sql').read())

def add_user(username, password, email):
    db.execute('INSERT INTO user (username, password, email) VALUES (?, ?, ?)',
               (username, password, email))
    db.commit()

def get_all_users():
    return db.execute('SELECT * FROM user').fetchall()

def print_users(users_list):
    for user in users_list:
        print('ID: ', user['id'], ', username: ', user['username'], ', password: ', user['password'], ', email: ', user['email'])

if __name__ == '__main__':
    init_db()
    add_user('john', 'ivan567')
    add_user('georgi', 'pythonisfun')
    add_user('dimitar', 'hero123')
    print_users(get_all_users())
    db.close()
