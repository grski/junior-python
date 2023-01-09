\pagebreak

# Funkcje

...

## Zwykłe funkcje/metody

Funkcje to podstawowy element programowania, który pozwala na grupowanie kodu w celu jego powtarzalnego wykorzystania. Są one również używane do dzielenia programu na mniejsze, bardziej zrozumiałe fragmenty, co ułatwia jego tworzenie i utrzymanie.

Czym są funkcje i dlaczego są ważne w programowaniu

Funkcje są zestawem poleceń, które można wywołać z dowolnego miejsca w programie. Dzięki temu można uniknąć powtarzania kodu i łatwiej jest go zmieniać i utrzymywać. Funkcje są również używane do dzielenia programu na mniejsze fragmenty, co ułatwia jego czytanie i zrozumienie.

Składnia definiowania funkcji w Pythonie

W Pythonie definicja funkcji rozpoczyna się od słowa kluczowego `def`, po którym następuje nazwa funkcji oraz nawiasy z argumentami. Kod wewnątrz funkcji jest wcięty. Przykład definicji funkcji:

```
def nazwa_funkcji(arg1, arg2):
    # kod funkcji
    return wynik
```

Przekazywanie argumentów do funkcji

Aby wywołać funkcję, należy podać jej nazwę oraz odpowiednie argumenty. W zależności od tego, jakie argumenty są wymagane przez funkcję, należy podać odpowiednią liczbę argumentów.

Zwracanie wartości z funkcji

Funkcje w Pythonie mogą zwracać wartości za pomocą słowa kluczowego `return`. Po wywołaniu funkcji, kod wewnątrz funkcji jest wykonywany, a następnie wartość jest zwracana i przypisywana do zmiennej lub wykorzystywana w inny sposób. Jeśli funkcja nie zwraca żadnej wartości, domyślnie zwraca `None`.

Użycie słowa kluczowego `return` do zwracania wartości z funkcji

Aby zwrócić wartość z funkcji, należy użyć słowa kluczowego `return` wraz z wyrażeniem, które ma zostać zwrócone. Na przykład:

```
Copy codedef powieksz(x):
    return x + 1

a = 5
b = powieksz(a)
print(b)  # Output: 6
```

Możliwość zwracania wielu wartości z funkcji za pomocą tuple lub słownika

W Pythonie możliwe jest zwracanie wielu wartości z funkcji za pomocą tuple lub słownika. Aby zwrócić wiele wartości w formie tuple, należy je po prostu umieścić w nawiasach klamrowych i oddzielić przecinkami. Przykład:

```
Copy codedef min_max(x):
    return min(x), max(x)

a = [1, 2, 3]
min_a, max_a = min_max(a)
print(min_a)  # Output: 1
print(max_a)  # Output: 3
```

Aby zwrócić wiele wartości w formie słownika, należy utworzyć słownik i zwrócić go za pomocą słowa kluczowego `return`. Przykład:

```
Copy codedef min_max(x):
    return {'min': min(x), 'max': max(x)}

a = [1, 2, 3]
min_max_dict = min_max(a)
print(min_max_dict['min'])  # Output: 1
print(min_max_dict['max'])  # Output: 3
```

Domyślne wartości argumentów

W Pythonie możliwe jest określenie domyślnych wartości dla argumentów funkcji. W takim przyp

W Pythonie funkcje są obiektami, co oznacza, że można je przypisywać do zmiennych, przekazywać jako argumenty do innych funkcji oraz używać jako elementów składowych innych obiektów.

Możliwość przypisywania funkcji do zmiennych i przekazywania ich jako argumentów do innych funkcji

Ponieważ funkcje są obiektami, można je przypisywać do zmiennych, tak jak przypisywana jest wartość zmiennej. Można również przekazywać funkcję jako argument do innej funkcji. Przykład:

```
Copy codedef powieksz(x):
    return x + 1

def wykonaj_na_liscie(funkcja, l):
    return [funkcja(x) for x in l]

a = [1, 2, 3]
b = wykonaj_na_liscie(powieksz, a)
print(b)  # Output: [2, 3, 4]
```

Funkcje to ważny element programowania, który pozwala na grupowanie kodu w celu jego powtarzalnego wykorzystania. Są one również używane do dzielenia programu na mniejsze, bardziej zrozumiałe fragmenty, co ułatwia jego tworzenie i utrzymanie. W Pythonie możliwe jest zwracanie wartości z funkcji za pomocą słowa kluczowego `return`, a także przekazywanie funkcji jako argumentów do innych funkcji i używanie ich jako elementów składowych innych obiektów.

Wskazówki dotyczące pisania czytelnego i efektywnego kodu z użyciem funkcji

Aby napisać czytelny i efektywny kod z użyciem funkcji, należy pamiętać o kilku ważnych wskazówkach:

- Dziel kod na mniejsze fragmenty za pomocą funkcji. Dzięki temu łatwiej będzie go czytać i zrozumieć.
- Nazywaj funkcje tak, aby opisywały, co robią. Nazwy powinny być zrozumiałe dla odbiorców kodu.
- Staraj się unikać powtarzania kodu za pomocą funkcji. Dzięki temu kod będzie krótszy i łatwiejszy do zrozumienia.
- Określaj dokładnie, jakie argumenty są wymagane przez funkcję i jakie wartości zwraca. To pomoże innym programistom zrozumieć, jak funkcja działa.
- Staraj się ograniczyć liczbę argumentów przekazywanych do funkcji do minimum. Im mniej argumentów, tym łatwiej będzie ją zrozumieć.
- Pamiętaj o testowaniu funkcji. Przetestuj każdą funkcję, aby upewnić się, że działa poprawnie.

## Argumenty funkcji

### *args, **kwargs

Słowa kluczowe `*args` i `**kwargs` służą do przekazywania dowolnej liczby argumentów do funkcji.

`*args` jest używane do przekazywania dowolnej liczby argumentów niekluczowych (tzw. "positional arguments") do funkcji. Argumenty te są przekazywane do funkcji w postaci tuple.

Przykład:

```python
def func(*args):
    print(args)

func(1, 2, 3)
# Output: (1, 2, 3)
```

`**kwargs` jest używane do przekazywania dowolnej liczby argumentów kluczowych (tzw. "keyword arguments") do funkcji. Argumenty te są przekazywane do funkcji w postaci słownika.

Przykład:

```python
def func(**kwargs):
    print(kwargs)

func(a=1, b=2, c=3)
# Output: {'a': 1, 'b': 2, 'c': 3}
```

Słowa kluczowe `*args` i `**kwargs` są szczególnie przydatne, gdy chcemy przekazać dowolną liczbę argumentów do funkcji, bez konieczności znajomości ich dokładnej liczby lub nazw. Można również użyć obu słów kluczowych jednocześnie, jeśli chcemy przekazać zarówno argumenty pozycyjne, jak i kluczowe.

## Funkcje anonimowe/lambda

Tutaj będzie naprawdę krótko. Funkcje anonimowe/lambda to po prostu jednolinijkowe funkcje, którym nie nadajemy nazwy, gdyż używamy ich tylko w określonym lokalnym miejscu.

Nie jest dobrą praktyką, by ich nadużywać, natomiast w pewnych sytuacjach mają swoje zastosowanie. Zazwyczaj preferuję zwykłe funkcje, gdyż pozwalają mi bardziej rozlegle i opisowo zaznaczyć co dany kod robi. Są oczywiście trywialne przykłady i miejsca, gdzie lambdy mają sens. Warto jednak pamiętać, żeby nie tworzyć potworków, które posiadają milion zagnieżdżonych lambd czy skomplikowaną logikę.

Poniżej przykłady. 

```python
# Zwykła funkcja
def add(x, y):
    return x + y

# Funkcja lambda
add = lambda x, y: x + y
```

Funkcje lambda są często używane w połączeniu z funkcjami takimi jak `map()`, `filter()` i `reduce()`, które przyjmują funkcje jako argumenty.

Oto przykład użycia funkcji lambda z `map()`:

```python
numbers = [1, 2, 3, 4]
doubled = map(lambda x: x * 2, numbers)
# doubled jest teraz [2, 4, 6, 8]
```

Pamiętaj, że funkcje lambda są ograniczone do jednej linii i nie można ich używać do bardziej złożonych zadań. W takich przypadkach lepiej jest użyć zwykłej funkcji.

```python
def sort_timestamp(orders):
    return sorted(orders, key=lambda x: x.timestamp)
# inny przykład
class Foo:
    def _create_transactions(
        self, 
        book_side: dict[(int, list)], 
        new_order: Order, 
        start: int = None
    ) -> Order:
        """Here we take care of creating transaction and 
        fulfilling orders if a match is found in the orderbook.
        When we process the book it's important to reverse the
        ordering based if it's a bid/ask side of orderbook.
        Orders that are fulfilled are removed from the book. 
        If no orders are present for given price
        internally it's removed from the order book. Orders that 
        are filled partly are added to the orderbook with
        the remaining quantity."""
        sorted_prices = sorted(book_side.keys(), reverse=new_order.is_ask)
        sorted_prices = sorted_prices if start is None else sorted_prices[start:]
        for price in sorted_prices:
            if new_order.is_fulfilled or new_order.price_doesnt_match(book_side_price=price):
                break

            orders_at_price: list[Order] = book_side[price]
            sorted_orders_at_price = sorted(
                orders_at_price, 
                key=lambda order: order.timestamp
            )
           	(...)
```

Do poczytania:

1. https://analityk.edu.pl/python-lambda-wszystko-co-trzeba-wiedziec/
2. https://realpython.com/python-lambda/
3. https://www.geeksforgeeks.org/python-lambda-anonymous-functions-filter-map-reduce/
4. https://www.geeksforgeeks.org/intersection-two-arrays-python-lambda-expression-filter-function/?ref=lbp

\pagebreak

