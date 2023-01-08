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

Method Resolution Order (MRO) to sposób, w jaki Python odwzoruje dziedziczenie wielokrotne w klasach. MRO określa kolejność, w jakiej Python szuka metod w klasach podczas wywoływania metody na obiekcie.

Przykładowo, jeśli mamy następujące trzy klasy:

```python
class A:
    def method(self):
        print("This method is from class A")

class B(A):
    def method(self):
        print("This method is from class B")

class C(A):
    def method(self):
        print("This method is from class C")
```

a następnie tworzymy obiekt klasy `D`, która dziedziczy zarówno po klasie `B`, jak i `C`:

```python
class D(B, C):
    pass
```

Jeśli teraz wywołamy metodę `method` na obiekcie `D`, to Python użyje MRO do określenia, która wersja metody zostanie wywołana. W tym przypadku, ponieważ klasa `D` dziedziczy po klasie `B` jako pierwszej, to Python wywoła wersję metody z klasy `B`. Jeśli klasa `B` nie miałaby tej metody, Python przeszukałby klasę `C`, a następnie klasę `A`.

MRO działa według algorytmu C3, który zapewnia spójne i łatwe do przewidzenia wyniki. Można zobaczyć MRO dla danej klasy, używając funkcji `__mro__`:

```python
>>> D.__mro__
(<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>)
```

MRO jest ważne, ponieważ umożliwia kontrolę nad tym, w jaki sposób dziedziczenie wielokrotne jest odwzorowywane w kodzie. Może to być szczególnie przydatne w przypadku klas, które dziedziczą po wielu klasach bazowych i chcą mieć pewność, że metody zostaną odpowiednio wywołane.

Algorytm C3 działa następująco:

1. Wszystkie klasy są umieszczane na liście, w kolejności, w jakiej są podane jako argumenty dziedziczenia. Na przykład, w klasie `D` zdefiniowanej jako `class D(B, C)`, klasa `B` znajduje się przed klasą `C`.
2. Dla każdej klasy na liście, dodaj jej klasę bazową do końca tej samej listy.
3.  (...)

Resztę pominę.

Algorytm C3 jest stosowany w Pythonie od wersji 2.3. Jest on uważany za bardziej elegancki i prosty niż poprzedni algorytm stosowany w Pythonie (algorithmic depth-first search). Algorytm C3 zapewnia spójne i łatwe do przewidzenia wyniki dla MRO, co umożliwia lepszą kontrolę nad dziedziczeniem wielokrotnym w klasach.

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

Type hinting to mechanizm w Pythonie, który pozwala niejako "podpowiedzieć" interpreterowi jakiego typu danych oczekujemy w danym miejscu programu. W Pythonie nie ma konieczności deklarowania typów zmiennych, więc type hinting jest opcjonalnym narzędziem, które można wykorzystać w celu ułatwienia kodowania lub dokumentowania kodu.

Type hinting może być używany w kilku różnych miejscach kodu, takich jak deklaracje funkcji i metod, oraz w komentarzach.

Przykłady użycia type hinting:

```python
def greet(name: str) -> str:
    return "Hello, " + name

def sum_numbers(a: int, b: int) -> int:
    return a + b

class Point:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

```

Zaletą używania type hinting jest to, że może pomóc w dokumentowaniu kodu i ułatwić jego odczytanie dla innych programistów. Type hinting może również pomóc w detekcji błędów w czasie kompilacji, ponieważ interpreter może zgłaszać błędy, jeśli dane oczekiwanego typu nie zostaną przekazane do funkcji lub metody.

Wadą używania type hinting jest to, że może on być uciążliwy w implementacji, zwłaszcza w dużych projektach, gdzie konieczne jest ręczne dodawanie type hinting do wielu miejsc w kodzie. Ponadto, ponieważ type hinting nie jest obowiązkowy w Pythonie, niektórzy programiści mogą nie używać go w swoich projektach, co może utrudnić współpracę i odczytanie kodu przez innych.

Do poczytania: 

1. https://towardsdatascience.com/12-beginner-concepts-about-type-hints-to-improve-your-python-code-90f1ba0ac49
2. https://docs.python.org/3/library/typing.html

## Operator is

##  

\pagebreak