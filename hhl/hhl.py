class HHL():
    def __init__(self):
        self.test1 = 'hello'
        self.test2 = 49

    def say_hello(self):
        print('Hello,world!')

# テストコード
if __name__ == "__main__":
    h = HHL()
    print(h.__dict__)
    h.say_hello()
