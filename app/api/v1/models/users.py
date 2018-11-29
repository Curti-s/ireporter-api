from instance.db_config import connection


class UserModel():
    """Create the user model"""

    def __init__(self):
        self.db = connection()

    def create_user_database(self):
        try:
            # cusor
            cur = self.db.cursor()
            query = """
                    CREATE TABLE IF NOT EXISTS users (
                    user_id SERIAL PRIMARY KEY NOT NULL,
                    firstname VARCHAR(60) NOT NULL,
                    lastname VARCHAR(60) NOT NULL,
                    username VARCHAR(60) NOT NULL,
                    email VARCHAR(60) NOT NULL,
                    phone_number VARCHAR(60),
                    registered TIMESTAMP DEFAULT now() NOT NULL,
                    is_admin BOOL NOT NULL 
            )"""
            # execute
            cur.execute(query)
            self.db.commit()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if self.db is not None:
                self.db.close()
    

    def get_all_users(self):
        # cursor
        cur = self.db.cursor()
        # execute
        cur.execute("""SELECT * FROM users""")
        data = cur.fetchall()
        for items in enumerate(data):
            users.append(items)
        return users

    def save(self,firstname,lastname,username,email,phone_number,is_admin=False):
        payload = {
            'firstname':firstname,
            'lastname': lastname,
            'username': username,
            'email': email,
            'phone_number': phone_number,
            'is_admin': is_admin
        } 

        query = """INSERT INTO users (firstname, lastname, username,email, phone_number) VALUES
                (%(firstname)s, %(lastname)s, %(username)s, %(email)s, %(phone_number)s)"""

        cur = self.db.cursor()
        cur.execute(query, payload)
        self.db.commit()
        return payload