\pagebreak

# Klasy i OOP



## Klasy

Można o klasach myśleć jak o po prostu pewnych zbieraninach funkcji. Funkcje tworzone wewnątrz klasy nazywają się nagle `metodami`. 

Klasy można 'łączyć', co nazywa się dziedziczeniem. Przykład klasy:

\pagebreak

```python
from collections import defaultdict
from queue import Queue

from orderbook.transaction import Transaction

class BaseOrderBook:
    pass


class OrderBook(BaseOrderBook):
    """
    This very simple order book implementation works 
    within certain constrictions provided in the requirements.
    These constrictions in some aspects assume the 'happy path'
    hence the implementation will do the same and
    cover just these scenarios. Stubs may be provided in a place or
    two just for interface's sake or my sanity.
    We only implement two types of orders: Limit Order & Iceberg Order.
    """

    def __init__(self) -> None:
        self.asks = defaultdict(list)
        self.bids = defaultdict(list)
        self.order_ids = set()
        self.transactions: Queue[Transaction] = Queue()
        self.last_accessed_transaction_index = self.transactions.qsize() - 1

    def show_new_transactions(self):
        while not self.transactions.empty():
            if transaction := self.transactions.get():
                print(transaction)

    @property
    def maximum_bid(self) -> int:
        return min(self.bids.keys()) if self.bids else float("-inf")

    @property
    def minimum_ask(self) -> int:
        return min(self.asks.keys()) if self.asks else float("inf")

```

Do poczytania:

1. https://realpython.com/inheritance-composition-python/

### super() i MRO

`super()` to nic innego jak sposób wywołania metody z klasy po której dziedziczymy. Tylko tyle i aż tyle. Czyli coś a'la jak matka krzyczy 'zawołaj starego'. 

Jeśli dziedziczymy po kilku klasach, co w Pythonie jest dozwolone, które implementują tę samą metodę, to to, która metoda zostanie użyta, jest decydowane przez MRO. Method resolution order. 

```python
class IcebergOrder(Order):
    def __init__(self, peak: int, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.peak = peak
        self.timestamp = datetime.datetime.now()
```

Do poczytania: https://www.educative.io/answers/what-is-mro-in-python

## Classmethods, staticmethods

Koncept, jaki warto kojarzyć, by tworzyć ładne interfejsy i sensowne klasy to metoda klasowa i metoda statyczna.

Co to znaczy? Metoda klasowa/classmethod to taka metoda, która nie potrzebuje instancji danej klasy, jedynie samej klasy. Znaczy to tyle, że nie będziemy mieli dostępu do zainicjalizowanego obiektu i jego atrybutów, które definiujemy w `__ini__` a jedynie do zmiennych na poziomie samej klasy, czyli w jej scopie.

Metoda statyczna, to metoda, która nie potrzebuje nawet zmiennych z klasy i się do nich nie odnosi, nie odnosi się też do innych metod z danej klasy.

Czyli tak w skrócie: jeśli potrzebujemy stanu obiektu albo samego obiektu, zwykłe metody. Jeśli tylko rzeczy z danej klasy, to metoda klasowa, jeśli nic z powyższych to po prostu metoda statyczna. Przykłady na dole.

```python
from datetime import date
 
 
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    # zwykła metoda korzystająca z atrybutów instancji
    def print_name(self):
        print(self.name)
 
    # metoda klasowa tworząca instancje danej klasy
    # na podstawie roku
    @classmethod
    def from_birth_year(cls, name, year):
        return cls(name, date.today().year - year)
 
    # statyczna metoda do sprawdzania dorosłości
    @staticmethod
    def is_adult(age):
        return age > 18
 
 
person1 = Person('hejto', 21)
person2 = Person.from_birth_year('Sasin', 1996)
 
print(person1.age)
print(person2.age)
 
print(Person.is_adult(22))
```



Do poczytania: https://www.geeksforgeeks.org/class-method-vs-static-method-python/?ref=lbp

## Menadżery kontekstu

Menadżery kontekstu to takie klasy, które definiują `__enter__` oraz `__exit__`. To te cosie, których używamy razem z klauzulą `with`. W skrócie, te klasy po prostu definiują magiczne metody, które są odpalane przy wejściu do bloku kodu z with oraz po ukończeniu przetwarzania tego bloku. Pozwalają one nam, cóż, ustawić jakiś określony kontekst a potem po nim posprzatać.

Przykładem dobrym są tu operacje na plikach. Najpierw chcemy plik otworzyć, ustawić odpowiednio kursor etc a dopiero na nim pracować. Jak skończymy pracę na pliku to chcielibyśmy go zamknąć, żeby nic nie wisiało w pamięci. Zamiast robić to ręcznie za każdym razem, używamy kontekst menadżera, który wchodzi cały na biało.

```python
class File(object):
    def __init__(self, file_name, method):
        self.file_obj = open(file_name, method)
    def __enter__(self):
        return self.file_obj
    def __exit__(self, type, value, traceback):
        self.file_obj.close()

with File('demo.txt', 'w') as opened_file:
    opened_file.write('Hola!')
    
    
# context manager jako generator
from contextlib import contextmanager

@contextmanager
def open_file(name):
    f = open(name, 'w')
    try:
        yield f
    finally:
        f.close()
with open_file('some_file') as f:
    f.write('hola!')
```

Do poczytania: https://realpython.com/python-with-statement/

## Typehints

Do poczytania: 

1. https://towardsdatascience.com/12-beginner-concepts-about-type-hints-to-improve-your-python-code-90f1ba0ac49
2. https://docs.python.org/3/library/typing.html

## Operator is

##  

\pagebreak