class cars:
    wheel = 4
    country =  "Germany"
    speed = 304.55

    def __init__(self) :
        print(f"The wheels of car is {self.wheel} and the country is {self.country}")

    def speed1(self):
        print(f"The speed is {self.speed}")


class Audi(cars):
    price = 200000

a = Audi()
b = cars()

print(a.wheel)
print(b.speed)