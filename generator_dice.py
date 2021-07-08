import random 


class Dice:
    def __init__(self, side_cnt):
        self.max_side = side_cnt
        
    def roll(self):
        return random.randint(1, self.max_side)
   
class Dice2:
    def __init__(self, side_cnt):
        self.max_side = side_cnt
        
    def __iter__(self):
        while True:
            yield random.randint(1, self.max_side) 

if __name__=='__main__':
    dice = Dice(6)
    print(dice.roll())
    print(dice.roll())
    dice2 = iter(Dice2(6))
    for _ in range(10):
        print(next(dice2))
