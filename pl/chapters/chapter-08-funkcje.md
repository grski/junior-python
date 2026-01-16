\pagebreak

# Funkcje

Funkcje to podstawowy element programowania, który pozwala na grupowanie kodu w celu jego powtarzalnego wykorzystania. Są one również używane do dzielenia programu na mniejsze, bardziej zrozumiałe fragmenty, co ułatwia jego tworzenie i utrzymanie, czytelność. A o tym już wspominałem, że jest krytycznie ważne, prawda? W końcu kod piszesz raz, a czytasz dziesiątki razy czasami. Ty i inni ludzie.

Czym są funkcje i dlaczego są ważne w programowaniu? Zaraz pomówimy o tym szerzej. Zacznijmy od zwykłych funkcji.

## Zwykłe funkcje/metody

Najpierw omówmy tradycyjne funkcje, czy jeśli mówimy o funkcjach definiowanych w klasach, metody.

#### Składnia definiowania funkcji w Pythonie.

W Pythonie definicja funkcji rozpoczyna się od słowa kluczowego `def`, po którym następuje nazwa funkcji oraz nawiasy z argumentami. Kod wewnątrz funkcji jest wcięty. Przykład definicji funkcji:

```python
def nazwa_funkcji(arg1, arg2):
    # kod funkcji
    return wynik
```

#### Przekazywanie argumentów do funkcji

Aby wywołać funkcję, należy podać jej nazwę oraz odpowiednie argumenty. W zależności od tego, jakie argumenty są wymagane przez funkcję, należy podać odpowiednią liczbę argumentów.

#### Zwracanie wartości z funkcji

Funkcje w Pythonie mogą zwracać wartości za pomocą słowa kluczowego `return`. Po wywołaniu funkcji, kod wewnątrz funkcji jest wykonywany, a następnie wartość jest zwracana i przypisywana do zmiennej lub wykorzystywana w inny sposób. Jeśli funkcja nie zwraca żadnej wartości, domyślnie zwraca `None`.

#### Użycie słowa kluczowego `return` do zwracania wartości z funkcji

Aby zwrócić wartość z funkcji, należy użyć słowa kluczowego `return` wraz z wyrażeniem, które ma zostać zwrócone. Na przykład:

```python
def powieksz(x):
    return x + 1

a = 5
b = powieksz(a)
print(b)  # Output: 6
```

#### Wincyj wartości do zwrotu

W Pythonie możliwe jest zwracanie wielu wartości z funkcji za pomocą krotki lub słownika. Aby zwrócić wiele wartości w formie krotki, należy je po prostu oddzielić przecinkami. Przykład: 

```python
def min_max(x):
    return min(x), max(x), x

a = [1, 2, 3]
min_a, max_a, _ = min_max(a)
# alternatywnie:
result = min_max(a)
min_a = result[0]
max_a = result[1]
print(min_a)  # Output: 1
print(max_a)  # Output: 3
```

Przy okazji linijka z wywołania tejże funkcji, to przykład tak zwanego tuple unpacking - rozpakowywania krotki. 

Przydatna i ważna rzecz.

Jeśli stwierdzamy, że drugi argument zwracany przez funkcję jest nam zbędny albo, że w funkcji, która zwraca trzy argumenty, chcemy tylko pierwszy, albo tylko drugi, lub może ostatni, to też się da. Jak? Przeanalizuj kod niżej.

```python
def min_max(x):
    return min(x), max(x), x

a = [1, 2, 3]
min_a, max_a, _ = min_max(a) 
# trzeci argument zostanie olany i nieprzypisany do 
# żadnej zmiennej _ to placeholder, który python rozpoznaje
*_, last_argument = min_max(a)
first, *all_the_rest = min_max(a)
first, _, the_third = min_max(a)
first, *_, the_third = min_max(a)
```

Pobaw się kodem powyżej i zobacz jakie wnioski wyciągniesz. Dodatkowo polecam spróbować stworzyć funkcje z większą ilością argumentów, które zwraca. 

Aby zwrócić wiele wartości w formie słownika, należy utworzyć słownik i zwrócić go za pomocą słowa kluczowego `return`. Nic odkrywczego.

```python
def min_max(x):
    return {'min': min(x), 'max': max(x)}

a = [1, 2, 3]
min_max_dict = min_max(a)
print(min_max_dict['min'])  # Output: 1
print(min_max_dict['max'])  # Output: 3
```

#### Domyślne wartości argumentów

W Pythonie możesz zdefiniować domyślne wartości argumentów funkcji, co oznacza, że argumenty te nie muszą być przekazywane do funkcji w momencie jej wywołania. Wartość domyślna jest używana w przypadku, gdy argument nie został przekazany do funkcji. Natomiast trzeba pamiętać  tutaj o jednej ważnej rzeczy, przy definiowaniu wartości domyślnych, o czym zaraz.

Oto przykład funkcji z domyślnymi argumentami:

```python
def greet(name, greeting='Hello'):
  print(f'{greeting}, {name}!')

greet('Alice')  # wypisze "Hello, Alice!"
greet('Bob', 'Hi')  # wypisze "Hi, Bob!"
```

W powyższym przykładzie argument `name` nie ma wartości domyślnej, więc musi być przekazany do funkcji podczas jej wywołania. Natomiast argument `greeting` ma wartość domyślną `'Hello'`, więc może być pominięty podczas wywołania funkcji. Jeśli jednak przekazujesz drugi argument do funkcji, to jego wartość zostanie użyta zamiast wartości domyślnej.

Drugi argument można przekazać na dwa sposoby.

```python
greet('Bob', 'Hi')  # wypisze "Hi, Bob!"
greet('Bob', greeting='Hi')  # wypisze "Hi, Bob!"
```

Ten drugi sposób to używanie keyword arguments - argumentów z domyślnymi wartościami, które są opcjonalne. Argumenty bez domyślnych wartości też można przekazywać jako keyword arguments.

```python
greet('Bob', 'Hi')  # wypisze "Hi, Bob!"
greet(name='Bob', greeting='Hi')  # wypisze "Hi, Bob!"
```

Nazwa argumentu jest używana jako klucz. Możesz używać keyword arguments, aby przekazywać argumenty do funkcji w dowolnej kolejności, niezależnie od kolejności, w jakiej zostały zdefiniowane w definicji funkcji, ale lepiej trzymać się konwencjonalnej kolejności. To, że można, nie znaczy, że wypada.

Oto przykład użycia keyword arguments:

```python
def greet(name, greeting='Hello'):
  print(f'{greeting}, {name}!')

greet(name='Alice')  # wypisze "Hello, Alice!"
greet(greeting='Hi', name='Bob')  # wypisze "Hi, Bob!"
```

W powyższym przykładzie argument `name` jest przekazywany do funkcji za pomocą keyword argument `name`, a argument `greeting` jest przekazywany za pomocą keyword argument `greeting`. Możesz zamienić kolejność tych argumentów podczas wywołania funkcji, a funkcja nadal będzie działać poprawnie.

Uwaga: keyword arguments muszą być umieszczone po argumentach pozycyjnych (czyli takich, które nie są określone przez nazwę) podczas wywołania funkcji i podczas jej definicji. 

```python
def greet(name, greeting='Hello'):
  print(f'{greeting}, {name}!')

greet('Alice', greeting='Hi')  # poprawne
greet(greeting='Hi', 'Alice')  # błąd SyntaxError
def greet(greeting='Hello', name):
  print(f'{greeting}, {name}!')  # błąd
```

### Śledzik na raz

Wartości domyślne argumentów są jak śledzik na raz - interpreter Pythona zerknie na nie tylko raz, chluśnie i więcej nie będzie się zajmował. Co to znaczy? Ano to, że interpreter działa w taki sposób, że jak może, inicjuje domyślne argumenty tylko raz. O ile przy stringach, liczbach to nie ma problemu, tak przy obiektach mutowalnych pojawia się problem. Jak sądzisz, jaki?

Otóż każde kolejne wywołanie funkcji, wbrew temu czego by się można spodziewać, nie będzie powodować stworzenia nowej instancji elementu domyślnego a po prostu użyje referencji do na początku zainicjowanego obiektu np. listy. Rozważ przykład niżej.

 ```python
 >>> def xd(default_list=[]):
         default_list.append(1)
         return default_list
 >>> xd()
 [1]
 >>> xd
 <function xd at 0x7fd52a695510>
 >>> xd()
 [1, 1]
 >>> xd([1,2,3])
 [1, 2, 3, 1]
 ```

Zajrzyj do tego kodu i przemyśl. Często pojawia się to na rekrutacjach jako haczyk :-).

#### Funkcje jako obiekty

W Pythonie istnieje możliwość przypisywania funkcji do zmiennych i przekazywania ich jako argumentów do innych funkcji.

Ponieważ funkcje są obiektami, można je przypisywać do zmiennych, tak jak przypisywana jest wartość zmiennej. Można również przekazywać funkcję jako argument do innej funkcji. Przykład:

```python
def powieksz(x):
    return x + 1

def wykonaj_na_liscie(funkcja, l):
    return [funkcja(x) for x in l]

a = [1, 2, 3]
b = wykonaj_na_liscie(powieksz, a)
print(b)  # Output: [2, 3, 4]
```

#### Czysta funkcjowo Eur---- sieć

Pure functions/czyste funkcje to funkcje, które zawsze zwracają tę samą wartość dla danych wejściowych i nie wpływają na stan programu poza swoim zasięgiem. Innymi słowy, pure functions nie modyfikują stanu globalnego, nie wywołują żadnych efektów ubocznych (takich jak zmiana zmiennej globalnej lub wyświetlenie czegoś na ekranie) i zawsze zwracają tę samą wartość dla danego zestawu wejściowych. To trochę takie odwzorowanie funkcji znanej nam z matematyki. Mapowanie wartości dla każdego argumentu.

Oto przykład czystej funkcji:

```python
def add(x, y):
  return x + y

print(add(1, 2))  # wypisze 3
print(add(1, 2))  # wypisze 3
print(add(1, 2))  # wypisze 3
```

Powyższa funkcja `add` jest czysta, ponieważ zawsze zwraca tę samą wartość dla danego zestawu wejściowych (tutaj 1 i 2) i nie ma żadnych efektów ubocznych.

Pure functions są często używane w programowaniu funkcyjnym, ponieważ są one łatwe do testowania i łatwe do zrozumienia. Ponadto pure functions są często bardziej niezawodne niż funkcje, które wywołują efekty uboczne, ponieważ nie występuje ryzyko, że ich działanie będzie zależało od stanu globalnego lub innych niezdefiniowanych zmiennych. 

Ja osobiście całkiem lubię. Pewne aspekty programowania funkcyjnego są mi dość bliskie, plus nawet używane w OOP, poprawiają jakość kodu. Kiedy staram się pisać w miarę czyste funkcje, zauważam często, że kod wychodzi lepszy. Oczywiście wszystko z głową, nie polecam bycia purystą i fanatykiem. Wiedz, kiedy zrobić wyjątek.

#### *args, **kwargs

Słowa kluczowe `*args` i `**kwargs` służą do przekazywania dowolnej liczby argumentów do funkcji.

`*args` jest używane do przekazywania dowolnej liczby argumentów niekluczowych (tzw. "positional arguments") do funkcji. Argumenty te są przekazywane w postaci krotki.

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

Słowa kluczowe `*args` i `**kwargs` są szczególnie przydatne, gdy chcemy przekazać dowolną liczbę argumentów do funkcji, bez konieczności znajomości ich dokładnej liczby lub nazw. Można również użyć obu słów kluczowych jednocześnie, jeśli chcemy przekazać zarówno argumenty pozycyjne, jak i kluczowe. Można używać ich razem - `*args, **kwargs`.

#### Wskazówki 

Aby napisać czytelny i efektywny kod z użyciem funkcji, należy pamiętać o kilku ważnych wskazówkach:

- Dziel kod na mniejsze fragmenty za pomocą funkcji. Dzięki temu łatwiej będzie go czytać i zrozumieć.
- Nazywaj funkcje tak, aby opisywały, co robią. Nazwy powinny być zrozumiałe dla odbiorców kodu.
- Staraj się unikać powtarzania kodu i metody copiego pasty. Twórz atomiczne, małe i reużywalne funkcje.
- Określaj dokładnie, jakie argumenty są wymagane przez funkcję i jakie wartości zwraca. Type Hinting i Docstringi twoimi przyjaciółmi.
- Idealnie jest kiedy funkcja ma jak najmniej efektów ubocznych - nie zależy od rzeczy z zewnątrz, poza nią. 
- Staraj się ograniczyć liczbę argumentów przekazywanych do funkcji do minimum. Im mniej argumentów, tym łatwiej będzie ją zrozumieć.
- Funkcja z jednym argumentem jest ideolo. Dwa prawie tak samo dobra. Powyżej już się zastanów. Może warto opakować te argumenty w jakąś klasę/obiekt?
- Pamiętaj o testowaniu funkcji. Przetestuj każdą funkcję, aby upewnić się, że działa poprawnie. Małe, krótkie, czyste funkcje łatwo testować.

## Funkcje anonimowe/lambda

Tutaj będzie naprawdę krótko. Funkcje anonimowe/lambda to po prostu jednolinijkowe funkcje, którym nie nadajemy nazwy, gdyż używamy ich tylko w określonym lokalnym miejscu lub do przekazywania funkcji jako argumentu do innej funkcji.

Nie jest dobrą praktyką, by ich nadużywać, natomiast w pewnych sytuacjach mają swoje zastosowanie. Zazwyczaj preferuję zwykłe funkcje, gdyż pozwalają mi bardziej rozlegle i opisowo zaznaczyć co dany kod robi, nadać nazwę. Są oczywiście trywialne przykłady i miejsca, gdzie lambdy mają sens. Warto jednak pamiętać, żeby nie tworzyć potworków, które posiadają milion zagnieżdżonych lambd czy skomplikowaną logikę.

Poniżej przykłady. 

```python
# Zwykła funkcja
def add(x, y):
    return x + y

# Funkcja lambda
add = lambda x, y: x + y
```

### Gdzie używamy lambd najczęściej?

Funkcje lambda są często używane w połączeniu z funkcjami takimi jak `map()`, `filter()` i `reduce()`, które przyjmują funkcje jako argumenty, `sorted()` etc. 

### Przykłady

Oto przykład użycia funkcji lambda z `map()` jak i kilka innych przykładów:

```python
numbers = [1, 2, 3, 4]
doubled = map(lambda x: x * 2, numbers)
# doubled jest teraz [2, 4, 6, 8]

# funkcja lambda zwracająca kwadrat danej liczby
square = lambda x: x**2
print(square(5))  # wypisze 25

# funkcja lambda zwracająca większą z dwóch liczb
max_number = lambda x, y: x if x > y else y
print(max_number(4, 5))  # wypisze 5

# funkcja lambda przyjmująca listę i zwracająca sumę jej elementów
sum_list = lambda lst: sum(lst)
print(sum_list([1, 2, 3]))  # wypisze 6

# funkcja lambda przyjmująca listę i zwracająca listę złożoną z elementów parzystych
even_elements = lambda lst: [x for x in lst if x % 2 == 0]
print(even_elements([1, 2, 3, 4, 5]))  # wypisze [2, 4]
```

W powyższym kodzie użyto funkcji lambda do stworzenia krótkich funkcji zwracających kwadrat danej liczby, większą z dwóch liczb, sumę elementów listy oraz listę złożoną z elementów parzystych.

Pamiętaj, że funkcje lambda są ograniczone do jednej linii i nie można ich używać do bardziej złożonych zadań. W takich przypadkach lepiej jest użyć zwykłej funkcji. 

Przykład z nieco bardziej życiowego kodu:

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

Kod powyżej sortuje obiekty po jednym z jego atrybutów.

Do poczytania:

1. https://analityk.edu.pl/python-lambda-wszystko-co-trzeba-wiedziec/
2. https://realpython.com/python-lambda/
3. https://www.geeksforgeeks.org/python-lambda-anonymous-functions-filter-map-reduce/
4. https://www.geeksforgeeks.org/intersection-two-arrays-python-lambda-expression-filter-function/?ref=lbp

\pagebreak

