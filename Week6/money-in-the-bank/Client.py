import time
FIVE_MINUTE_SEC = 5 * 60


class Client():
    def __init__(self, id, username, balance, message,
                 email, failed_attempts=0, time_blocked=0):
        self.__username = username
        self.__balance = balance
        self.__id = id
        self.__message = message
        self._email = email
        self._failed_attempts = failed_attempts
        self.time_blocked = time_blocked
        self.tans = []

    def delete_tan(self, tan):
        self.tans.remove(tan)

    def get_username(self):
        return self.__username

    def get_balance(self):
        return self.__balance

    def deposit_money(self, amount):
        self.__balance += amount

    def withdraw_money(self, amount):
        if amount < self.__balance:
            self.__balance -= amount

    def get_id(self):
        return self.__id

    def get_message(self):
        return self.__message

    def get_email(self):
        return self._email

    def set_message(self, new_message):
        self.__message = new_message

    def get_failed_attempts(self):
        return self._failed_attempts

    def null_failed_attempts(self):
        self._failed_attempts = 0

    @property
    def is_blocked(self):
        current_time = int(time.time())
        return not current_time > self.time_blocked + FIVE_MINUTE_SEC

    # @property
    # def is_changepass_valid(self):
    #     current_time = int(time.time())
    #     return current_time > self.changepass_generated + FIVE_MINUTE_SEC
