### Task 5.4

# Implement a class Money to represent value and currency.
# You need to implement methods to use all basic arithmetics expressions (comparison, division, multiplication, addition and subtraction).
# To use this methods on different currencies implement an exchange_rate attribute.
# This attribute you should be able to change according to the currency or even delete.

# Example:
# ```python
# >>> usd = Money(12, "usd")
# >>> usd_t = Money(42, "usd")
# >>> usd + usd_t
# Money(54, "usd")

# >>> usd = Money(100, "usd")
# >>> eur = Money(42, "eur")
# >>> usd.exchange_rate = 0.89
# >>> usd - eur
# Money(47, "usd")

# >>> del usd.exchange_rate
# ```

class Money():
    USD_RATE = 2.511
    EURO_RATE = 3.002
    currency_dict = {
            'usd': (USD_RATE, 'USD'),
            'eur': (EURO_RATE, 'Euro'),
            '$': (USD_RATE, 'USD'),
            '€': (EURO_RATE, 'Euro'),
        }

    def __init__(self, value, currency = 'usd'):
        self.__if_currency_valid(currency)
        self.value = value
        self.currency = currency
        self.exchange_rate = None

    def __if_currency_valid(self, currency):
        if currency.lower() not in self.currency_dict:
            raise Exception('The currency is not valid!')

    def __calc_rate(self):
        res = self.USD_RATE / self.EURO_RATE
        try:
            res = self.exchange_rate if self.exchange_rate else res
        except AttributeError:
            pass
        return res

    def convert_to(self, currency):
        self.__if_currency_valid(currency)
        if self.currency_dict[self.currency][1] == self.currency_dict[currency][1]:
            return self.value
        rate = self.__calc_rate()
        if self.currency_dict[self.currency] < self.currency_dict[currency]:
            res = self.value * rate
        else:
            res = self.value / rate
        return res

    def __delattr__(self, attr):
        if attr == 'exchange_rate':
            if attr in self.__dict__:
                del self.__dict__[attr]
            return
        return super().__delattr__(attr)

    def __sub__(self, other):
        return Money(self.convert_to('usd') - other.convert_to('usd'))

    def __add__(self, other):
        return Money(self.convert_to('usd') + other.convert_to('usd'))
    
    def __mul__(self, other):
        return Money(self.convert_to('usd') + other.convert_to('usd'))

    def __truediv__(self, other):
        return Money(self.convert_to('usd') / other.convert_to('usd'))

    def __floordiv__(self, other):
        return Money(self.convert_to('usd') // other.convert_to('usd'))

    def __lt__(self, other):
        return self.convert_to('usd') < other.convert_to('usd')

    def __gt__(self, other):
        return self.convert_to('usd') > other.convert_to('usd')
    
    def __le__(self, other):
        return self.convert_to('usd') <= other.convert_to('usd')

    def __ge__(self, other):
        return self.convert_to('usd') <= other.convert_to('usd')

    def __eq__(self, other):
        return self.convert_to('usd') == other.convert_to('usd')
    
    def __ne__(self, other):
        return self.convert_to('usd') != other.convert_to('usd')

    def __str__(self):
        currency_name = self.currency_dict[self.currency][1]
        return f'{self.value:.2f} {currency_name}'


if __name__=='__main__':
    m = Money(123, '$')
    n = Money(5, '€')
    print(m-n)
    print((m - n).convert_to('eur'))
    print(m+n)
    print(m*n)
    print(m/n)
    print(m//n)
    print(m<n)
    print(m>n)
    print(m<=n)
    print(m==n)
    print(m!=n)
    del m.exchange_rate
    del n.exchange_rate
    print(m-n)


