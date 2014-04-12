import sys
import unittest
import hashlib

sys.path.append("..")

import sql_manager


class SqlManagerTests(unittest.TestCase):

    def setUp(self):
        sql_manager.create_clients_table()
        sql_manager.register('Tester', '123haha&HH')

    def tearDown(self):
        sql_manager.cursor.execute('DROP TABLE clients')

    def test_register(self):
        username = 'Dinko'
        password = '123123$$GGhhhh'
        hashed_pass = sql_manager.hash_function(password)
        sql_manager.register(username, password)

        sql_manager.cursor.execute('SELECT Count(*)  FROM clients\
            WHERE username = (?) AND password = (?)', (username,
                                                       hashed_pass))
        users_count = sql_manager.cursor.fetchone()

        self.assertEqual(users_count[0], 1)

    def test_login(self):
        logged_user = sql_manager.login('Tester', '123haha&HH')
        self.assertEqual(logged_user.get_username(), 'Tester')

    def test_login_wrong_password(self):
        logged_user = sql_manager.login('Tester', '123h&HH')
        self.assertFalse(logged_user)

    def test_change_message(self):
        logged_user = sql_manager.login('Tester', '123haha&HH')
        new_message = "podaivinototam"
        sql_manager.change_message(new_message, logged_user)
        self.assertEqual(logged_user.get_message(), new_message)

    def test_change_password(self):
        logged_user = sql_manager.login('Tester', '123haha&HH')
        new_password = "123haha&HHGGG"
        sql_manager.change_pass(new_password, logged_user)

        logged_user_new_password = sql_manager.login('Tester', new_password)
        self.assertEqual(logged_user_new_password.get_username(), 'Tester')

    def test_injection_fail(self):
        self.assertEqual(False, sql_manager.login("' OR 1 == 1 --;", 'hahhah'))

    def test_strong_password_only_numbers(self):
        self.assertFalse(sql_manager.strong_password('Tester', '1234'))

    def test_username_in_password(self):
        self.assertFalse(sql_manager.strong_password('Tester', 'Tester1234'))

    def test_no_special_symbols(self):
        self.assertFalse(sql_manager.strong_password('Tester', 'TttTT1234'))

    def test_no_upper_letters(self):
        self.assertFalse(sql_manager.strong_password('Tester', 'tttt$$$1234'))

    def test_weak_password_only_numbers(self):
        self.assertFalse(sql_manager.register('Tester', '123'))

    def test_hash(self):
        username = 'tdhris'
        password = 'blahblahblah'
        sql_manager.register(username, password)

        sql_manager.cursor.execute("SELECT Count(*) FROM clients\
            WHERE username = ? AND password = ?", (username, password))

        self.assertEqual(0, sql_manager.cursor.fetchone()[0])

if __name__ == '__main__':
    unittest.main()
