import random

class Animal:
    live = True
    sound = None
    _DEGREE_OF_DANGER = 0
    def __init__(self, speed):
        self._cords = [0, 0, 0]
        self.speed = speed
    def move(self, dx, dy, dz):
        if self. _cords[2] + dz * self.speed < 0:
            print("It's too deep, i can't dive :(")
        else:
            self._cords[0] += dx * self.speed
            self._cords[1] += dy * self.speed
            self._cords[2] += dz * self.speed
    def get_cords(self):
            print(f'X: {self._cords[0]}, Y: {self._cords[1]}, Z: {self._cords[2]}')
    def attack(self):
        if self._DEGREE_OF_DANGER < 5:
            print("Sorry, i'm peaceful :)")
        else:
            print("Be careful, i'm attacking you 0_0" )
    def speak(self):
            print(self.sound)
class Bird(Animal):
    def __init__(self, speed):
        super().__init__(speed)
    beak = True
    def lay_eggs(self):
        num_eggs = random.randint(1, 4)
        print(f"Here are(is) {num_eggs} eggs for you")
class AquaticAnimal(Animal):
    def __init__(self, speed):
        super().__init__(speed)
    _DEGREE_OF_DANGER = 3
    def dive_in(self, dz):
        z_change = abs(dz) * self.speed / 2
        if self._cords[2] - z_change < 0:
            print("It's too deep, i can't dive :(")
        else:
            self._cords[2] = self._cords[2] - z_change
class PoisonousAnimal(Animal):
    def __init__(self, speed):
        super().__init__(speed)
    _DEGREE_OF_DANGER = 8
class Duckbill(PoisonousAnimal,AquaticAnimal, Bird):
    sound = "Click-click-click"


db = Duckbill(10)

print(db.live)
print(db.beak)

db.speak()
db.attack()

db.move(1, 2, 3)
db.get_cords()
db.dive_in(6)
db.get_cords()

db.lay_eggs()
