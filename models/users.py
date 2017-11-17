from pass_hash import *
from local_settings import connect_to_db

class Users:

    __id = None
    username = None
    __hashed_password = None
    emeil = None

    def __init__(self):
        self.__id = -1
        self.username = ""
        self.email = ""
        self.__hashed_password = ""

    @property
    def id(self):
        return self.__id

    @property
    def hashed_password(self):
        return self.__hashed_password

    def set_password(self, password, salt):
        self.__hashed_password = password_hash(password, salt)

    def save_to_db(self, cursor):
        if self.__id == -1:
            sql = 'INSERT INTO Users (emeil, username,hashed_password) VALUES (%s,%s,%s)'
            values = (self.email, self.username, self.hashed_password)
            cursor.execute(sql, values)
            self.__id = cursor.lastrowid
            return True
        else:
            sql = 'UPDATE Users SET emeil=%s, username=%s, hashed_password=%s WHERE id=%s'
            values = (self.email, self.username, self.hashed_password, self.id)
            cursor.execute(sql, values)
            return True

    @staticmethod
    def load_user_by_id(cursor, id):
        sql = 'SELECT id, emeil, username, hashed_password FROM Users WHERE id = {}'.format(id)
        result = cursor.execute(sql)
        data = cursor.fetchone()
        if data is not None:
            loaded_user = Users()
            loaded_user.__id = data[0]
            loaded_user.email = data[1]
            loaded_user.username = data[2]
            loaded_user.__hashed_password = data[3]
            return loaded_user
        else:
            return None

    @staticmethod
    def load_user_by_login(cursor, login):
        sql = 'SELECT id, emeil, username, hashed_password FROM Users WHERE username = %s'
        result = cursor.execute(sql, (login,))
        data = cursor.fetchone()
        if data is not None:
            loaded_user = Users()
            loaded_user.__id = data[0]
            loaded_user.email = data[1]
            loaded_user.username = data[2]
            loaded_user.__hashed_password = data[3]
            return loaded_user
        else:
            return None

    @staticmethod
    def load_all_users(cursor):
        sql = 'SELECT id, emeil, username, hashed_password FROM Users'
        ret = []
        result = cursor.execute(sql)
        data = cursor.fetchall()
        for row in data:
            loaded_user = Users()
            loaded_user.__id = row[0]
            loaded_user.email = row[1]
            loaded_user.username = row[2]
            loaded_user.__hashed_password = row[3]
            ret.append(loaded_user)
        return ret

    def delete_user(self, cursor):
        sql = 'DELETE FROM Users WHERE id=%s'
        cursor.execute(sql, (self.__id,))
        self.__id = -1
        return True






'''#nowyuser = Users()
#nowyuser.email = 'trellcia@poczta.onet.pl'
#nowyuser.username = 'marcin'
#nowyuser.set_password('marcin123','')
inny = Users()
inny.email = 'mala@malpa.pl'
inny.username = 'paparapa12'
inny.set_password('hasloo','moje')

try:
    con = connect_to_db('warsztat1')
    cursor = con.cursor()
    print('OK')
    inny = Users.load_user_by_id(cursor, 3)
    inny.email = 'mala@mapl.pl'
    inny.save_to_db(cursor)
    print(inny.username,inny.id)
    cos = Users.load_all_users(cursor)
    for row in cos:
        print(row.username, row.email, row.id, row.hashed_password)
    marcin = Users.load_user_by_login(cursor, 'marcin')
    print(marcin.id, marcin.hashed_password,marcin.username, marcin.email)
except:
    raise Exception('coś nie tak')
finally:
    cursor.close()
    con.close()'''