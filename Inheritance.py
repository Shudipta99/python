class Phone:#create base/super /parent class
    def call(self):
        print("you can call")

    def message(self):
        print("you can message")

class Samsung(Phone):# Here samsung is the sub/derived/child class of phone class and this way sub class is use super class and it's called inheritance
    def photo(self):
        print("you can take photo")

s= Samsung()
s.message()
s.call()
s.photo()
print(issubclass(Phone,Samsung))# for checking which is sub-class & super class