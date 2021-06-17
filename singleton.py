### Task 5.3

# A singleton is a class that allows only a single instance of itself to be created and gives access to that created instance.
# Implement a singleton class in two different ways:
# * write a class decorator "singleton" to decorate any class and make it singleton
# * implement singleton logic inside your custom class using a method to initialise class instance

# Example:

# ```python
# >>> @singleton
 #    class Moon:
  #       pass


# >>> m = Moon()
# >>> s = Moon()
# >>> d = Moon()
# >>> m is s is d
# True
# >>> id(m)
# 140020147190584
# >>> id(s)
# 140020147190584
# >>> id(d)


# >>> p = Sun.inst()
# >>> f = Sun.inst()
# >>> p is f
# True
# ```


class Singleton:
  instance = None
  def __new__(cls):
      if not cls.instance:
          cls.instance = super().__new__(cls)
      return cls.instance


def singleton(cls):
    instance = [0]
    def inner(*args, **kwargs):
      if not instance[0]:
        print('creating object')
        instance[0] = cls(*args, **kwargs)
      return instance[0]
    return inner


@singleton
class Moon():
  pass


@singleton
class Sun():
  pass


if __name__=='__main__':
  a = Singleton()
  b = Singleton()
  print(a is b)
  a = Moon()
  b = Moon()
  c = Moon()
  d = Sun()
  e = Sun()
  print(a is b is c)
  print(d is e)
  print(id(a))
  print(id(e))
  print(a is d)
