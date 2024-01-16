class User:
    def __init__(self, user_name, user_age, user_languages, user_is_active):
        self.user_name = user_name
        self.user_age = user_age
        self.user_languages = user_languages
        self.user_is_active = user_is_active
        self.lang_count = len(user_languages)

    def info(self):
        print(f'Info: {self.user_name}, Age: {self.user_age}, Languages: {self.user_languages}, Active: {self.user_is_active}')

    def update_lang_count(self):
        self.lang_count = len(self.user_languages)
