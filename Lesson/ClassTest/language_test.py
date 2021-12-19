class Language:
    default_lang = "English"
    
    def __init__(self):
        self.show = '나의 언어는 ' + self.default_lang
    
    @classmethod
    def class_my_language(cls):
        return cls()
    
    @staticmethod
    def static_my_language():
        return Language()
    
    def print_language(self):
        print(self.show)
        

class KoreanLanguage(Language):
    default_lang = "한국어"