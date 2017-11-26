
class Message():

    __id = None
    from_user = None
    to_user = None
    text_message = None
    create_date = None

    def __init__(self):
        self.__id = -1
        self.from_user = ''
        self.to_user = ''
        self.text_message = ''
        self.create_date = ''


    @property
    def id(self):
        return self.__id


    def save_to_db(self, cursor):
        if self.__id == -1:
            sql = 'INSERT INTO Message (from_user, to_user, text_message, create_date) VALUES (%s,%s,%s,%s)'
            values = (self.from_user, self.to_user, self.text_message, self.create_date)
            cursor.execute(sql, values)
            self.__id = cursor.lastrowid
            return True
        else:
            sql = 'UPDATE Message SET form_user=%s, to_user=%s, text_message=%s, create_date=%s WHERE id=%s'
            values = (self.from_user, self.to_user, self.text_message, self.create_date, self.id)
            cursor.execute(sql, values)
            return True

    @staticmethod
    def load_message_by_id(cursor, id):
        sql = 'SELECT id, from_user, to_user, text_message FROM Message WHERE id = {}'.format(id)
        cursor.execute(sql)
        data = cursor.fetchone()
        if data is not None:
            loaded_message = Message()
            loaded_message.__id = data[0]
            loaded_message.from_user = data[1]
            loaded_message.to_user = data[2]
            loaded_message.text_message = data[3]
            return loaded_message
        else:
            return None


    @staticmethod
    def load_all_message_for_user(cursor, id):
        sql = 'SELECT from_user, text_message, create_date FROM Message JOIN Users ON Message.to_user=Users.id WHERE Users.id = %s'
        ret = []
        cursor.execute(sql, (id,))
        data = cursor.fetchall()
        for row in data:
            loaded_message = Message()
            loaded_message.from_user = row[0]
            loaded_message.text_message = row[1]
            loaded_message.create_date = row[2]
            ret.append(loaded_message)
        return ret

    @staticmethod
    def load_all_message(cursor):
        sql = 'SELECT id, from_user, to_user, text_message, create_date FROM Message'
        ret = []
        cursor.execute(sql)
        data = cursor.fetchall()
        for row in data:
            loaded_message = Message()
            loaded_message.__id = row[0]
            loaded_message.from_user = row[1]
            loaded_message.to_user = row[2]
            loaded_message.text_message = row[3]
            loaded_message.create_date = row[4]
            ret.append(loaded_message)
        return ret


