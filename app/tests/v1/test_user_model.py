import unittest
from app.api.v1.models.users import UserModel
from instance.db_config import connection

class TestUserModel(unittest.TestCase):
    pass
    # def test_user_database_creation(self):
    #     conn = connection()
    #     query = """
    #             CREATE TABLE IF NOT EXISTS users (
    #                 user_id SERIAL PRIMARY KEY NOT NULL,
    #                 firstname VARCHAR(60) NOT NULL,
    #                 lastname VARCHAR(60) NOT NULL,
    #                 username VARCHAR(60) NOT NULL,
    #                 email VARCHAR(60) NOT NULL,
    #                 phone_number VARCHAR(60),
    #                 registered TIMESTAMP DEFAULT now() NOT NULL,
    #                 is_admin BOOL DEFAULT false
    #         )"""
    #     cur = conn.cursor()
    #     cur.execute(query)
    #     conn.commit()
    #     datar = UserModel()
    #     datar.save('curtis','kirimi','curtis','curtis@gmail.com','074644682')
    #     cur.drop_all()
    #     data = cur.fetchall()
    #     self.assertTrue(type(data) == tuple)

