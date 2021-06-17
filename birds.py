##############################################################################################################################################

# Create birds hierarchy.
#Implement 4 classes:
#* Birds abstract class with an attribute "name" and methods "fly" and "walk".
#* flying bird class with same attribute "name" and with the same methods.
#Implement the method "eat" which will describe it's typical ration.
#* nonflying bird class with same characteristics but which obviously will not have the "fly".
#Add same "eat" method but with other implementation regarding the swimming bird tastes.
#* a bird class which can do all of it: walk, fly, swim and eat.
#But be careful which "eat" method you inherit.

#Implement str() function call for each class.

#Example:

#```python
#>>> b = Bird("Any")
#>>> b.walk()
#"Any bird can walk"

#p = Penguin("Penguin")
#>> p.swim()
#"Penguin bird can swim"
#>>> p.fly()
#AttributeError: 'Penguin' object has no attribute 'fly'
#>>> p.eat()
#"It eats mostly fish"

#c = Canary("Canary")
#>>> str(c)
#"Canary can walk and fly"
#>>> c.eat()
#"It eats mostly grains"

#s = SeaGull("Gull")
#>>> str(s)
#"Gull bird can walk, swim and fly"
#>>> s.eat()
#"It eats fish"
#```

#Have a look at `__mro__` method of your last class.


import abc


class BaseBird(abc.ABC):
    def __init__(self, name):
        self.name = name

    @abc.abstractmethod
    def walks(self):
        pass

    @abc.abstractmethod
    def eats(self):
        pass


class Bird(BaseBird):
    def __init__(self, name):
        super().__init__(name)

    def walks(self):
        return 'on the ground'

    def eats(self):
        return ['bread']


class FlyingBird(Bird):
    def flies(self):
        return 'in the sky'
    
    def eats(self):
        return super().eats() + ['grains']


class NonFlyingBird(Bird):
    def eats(self):
        return super().eats() + ['fish']

    def swims(self):
        return 'in the sea'


class SuperBird(FlyingBird, NonFlyingBird):
    def eats(self):
        return super().eats() + ['sweats']


#NOTE: method resolution order for SuperBird by steps 1-5
# 1: SuperBird, FlyingBird, Bird, BaseBird, object
# 2: SuperBird, NonFlyingBird, Bird, BaseBird, object
# 3: SuperBird, FlyingBird, Bird, BaseBird, object, NonFlyingBird, Bird, BaseBird, object
# 4: SuperBird, FlyingBird, Bird, BaseBird, object, NonFlyingBird
# 5: SuperBird, FlyingBird, NonFlyingBird, Bird, BaseBird, object


if __name__=='__main__':
    s = SuperBird('SeaGul')
    print(f'{s.name}', s.eats()) # ['bread', 'fish', 'grains', 'sweats']
    print('Walks ', s.walks())
    print('Flies', s.flies())
    print('Swims', s.swims())

    # MRO: FlyingBird, Bird, BaseBird
    f = FlyingBird('Canary')
    print(f'{f.name}', f.eats()) # ['bread', 'grains']
    print('Walks ', f.walks())
    print('Flies', f.flies())
    #print('Swims', f.swims())

    # MRO: NonFlyingBird, Bird, BaseBird
    p = NonFlyingBird('Penguin')
    print(f'{p.name}', p.eats()) #  ['bread', 'fish']
    print('Walks ', p.walks())
    print('Swims', p.swims())
    #print('Flies', p.flies())

    # MRO: Bird, BaseBird
    any_bird = Bird('Crow')
    print(f'{any_bird.name}', any_bird.eats())
    print('Walks ',any_bird.walks())
    print('Eats ',any_bird.eats()) # Eats  ['bread']
    #print('Swims', any_bird.swims())

