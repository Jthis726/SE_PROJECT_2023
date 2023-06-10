from product import Product

class User:
    user_list = []
    user_ID_list={}
    def __init__(self, id, name, password, coin, won):
        self.id = id
        self.name = name
        self.password = password
        self.isLogged = False;
        self.product_list = []
        self.coin = coin
        self.money = won
    
    @classmethod
    def add_user(cls, name, password):
        for user in cls.user_list:
            if name == user.name and password == user.password:
                return False
        id = len(cls.user_list)
        cls.user_list.append(User(id ,name, password, 0, 0))
        cls.user_ID_list[name]=id;
        return True

    @classmethod
    def login(cls, name, password):
        for user in cls.user_list:
            if name == user.name and password == user.password:
                user.log_instance()
                return user
        return None
    
    @classmethod
    def logout(cls):
        for user in cls.user_list:
            user.logout_instance()

    def log_instance(self):
        self.isLogged = True;
    
    def logout_instance(self):
        self.isLogged = False;
    
    @classmethod
    def add_money(cls, price):
        for user in cls.user_list:
            user.money += price

    @classmethod
    def sub_money(cls, price):
        for user in cls.user_list:
            user.money -= price

    @classmethod
    def add_coin(cls, coin):
        for user in cls.user_list:
            user.coin += coin

    @classmethod
    def sub_coin(cls, coin):
        for user in cls.user_list:
            user.coin -= coin

    def set_product(self, coin, price):
        product_id = Product.add_product(coin, price, self.id)
        self.product_list.append(product_id)
        
    def __repr__(self):
        return self.name