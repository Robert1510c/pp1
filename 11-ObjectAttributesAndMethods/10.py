class Phone:
    def __init__(self,brand,model,phone_number):
        self.brand=brand
        self.model=model
        self.phone_number=phone_number

    def call(self,number):
        print(f"{self.brand} {self.model} {self.phone_number} is calling to {number}")

    def pick_up(self,new_number):
        print(f"{self.brand} {self.model} {self.phone_number} picks up the call from: {new_number}")
    
    def __str__(self):
        return (f"{self.phone_number} {self.brand} {self.model}")

phone1=Phone("Samsung","s10", 123123123)
phone2=Phone("Samsung",'S20',312321321)
print(phone1)
print(phone2)
phone1.call(321321321)
phone2.pick_up(123123123)