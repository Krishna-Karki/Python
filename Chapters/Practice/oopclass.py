class cars:
    wheel = 4
    country =  "Germany"
    speed = 304.55

    def __init__(self) :
        print(f"The wheels of car is {self.wheel} and the country is {self.country}")

    def speed1(self):
        print(f"The speed is {self.speed}")

c1 = cars()
print(c1.wheel)

print(c1.speed)
c1.speed1()