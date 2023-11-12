\pagebreak

# Pętle i iteracja

Opowiemy sobie trochę o pętlach w Pythonie, o iteracji też słów kilka. Co to, po co to i na co to komu. Porozmawiamy o różnych pętlach, `for`, czyli pętli krokowej, `while`, czyli zwykłej pętli. O iteracji i obiektach iterowalnych. 

Co to jednak w ogóle znaczy? 

 Pętle to koncept w programowaniu służący wykonaniu jakieś czynności, jakiegoś kawałka kodu, zadaną ilość razy. Otóż wyobraź sobie, że musisz przetworzyć 10 elementów z tablicy. Na każdej z nich wykonać jakieś operacje. Załóżmy, że te operacje to nie jest jedna linijka a skomplikowane przetwarzanie. Chociaż nie, dla naszego przykładu nawet mnożenie weźmy. I co teraz?
Naiwne rozwiązanie wyglądałoby tak:

```python
>>> elements = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
>>> elements[0] *= 2
>>> elements[1] *= 2
>>> elements[2] *= 3
(...)
>>> elements[9] *= 3
```

Koszmar. Teraz pomyślcie, że tych elementów jest więcej. Na przykład milion, bo tylu użytkowników masz. Ręcznie tego nie idzie wyedytować, chyba, że zatrudnimy skończoną liczbę studentów albo Hindusów. Natomiast wciąż, potrwa to niezmiernie długo. No i tutaj właśnie wchodzą pętle całe na biało.

## Pętla krokowa

### Krótka charakterystyka

Zacznijmy od czegoś, co nazywa się pętla krokowa. Jest to pętla, która pozwala nam 'przejść się' po elementach zadanego obiektu i umożliwia, krok po kroku, czyli element po elemencie, przetwarzanie danego elementu. To znaczy, że słowo kluczowe `for` umożliwia nam iterację po elementach obiektu iterowalnego.

### Obiekt iterowalny

Czymże jest obiekt iterowalny? To taki obiekt, który po wrzuceniu do funkcji `iter()` zwróci nam iterator. A iterator to coś, na czym wołamy `next()`Widziałeś już kilka przykładów iterowalnych obiektów. Listy, Dicty, Tuple. 

To takie obiekty, które mają zaimplementowaną metodę `__iter__` i kolejno `__next__`, czyli w skrócie programista powiedział pythonowi jak ma brać kolejne elementy z danego obiektu/danej struktury i która zwraca obiekt iteratora. 

W listach, dictach, tuplach mamy to domyślnie jako część języka. Jeśli sami tworzymy jakieś wyspecjalizowane klasy, to również możemy uczynić je iterowalnymi poprzez zaimplementowanie tejże metody. Czyli tak w skrócie to takie coś po czym można iterować. 

Iterować znaczy przechodzić krok po kroku po elementach danej struktury. Zrozumiałe? Oby tak. Jak nie to googlaj albo patrz kod niżej.

Jak to wygląda w praktyce? Zmodyfikujmy nasz przykład wyżej. 

```python
>>> elements = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
>>> for index, element in enumerate(elements):
...     elements[index] *= 2
...
>>> elements
[2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
```

Zamiast miliona linii mamy dwie. Fajne, co? Ale chwila, co to za magiczna funkcja `enumerate`? To wbudowana funkcja Pythona, która pozwala nam na ponumerowanie elementów danego obiektu. Mówiąc prościej to taki wrapper, taka nakładka na nasz dany obiekt, np. listę, która oprócz danego elementu z obiektu zwróci też jego indeks.

Całość, przekuta na instrukcję w języku polskim, wygląda tak.

1. Weź obiekt elements. Elements to lista.
2. Przekaż obiekt elements jako argument dla funkcji enumerate.
3. Funkcja enumerate zwraca nowy obiekt. Obiekt ten jest czymś z kolei, co zwraca nam kolejne elementy oryginalnego obiektu i dokleja do nich niejako indeks/numerek

Następnie kiedy mamy ten nowo zwrócony obiekt, pętla for wchodzi do życia i jedzie z tematem.

1. Weź nowo zwrócony obiekt 
2. Pod spodem zawołaj `__iter__()`, który zwróci nam iterator dla tej listy, chyba, że domyślnie mamy przekazany iterator.
3. Zawołaj `next()` jako argument podając otrzymany iterator. 
4. Next zwróci następny element, jaki ma do przekazania iterator
5. Kiedy nie będzie już elementów iterator rzuci wyjątkiem StopIteration, co jest poprawnym zachowaniem dla iteratorów, które nie mają już elementów do przekazania.  

```python
>>> l = elements.__iter__()
>>> next(l)
2
>>> next(l)
4
>>> next(l)
6
>>> next(l)
8
>>> next(l)
10
>>> next(l)
12
>>> next(l)
14
>>>
>>> next(l)
16
>>> next(l)
18
>>>
>>> next(l)
20
>>> next(l)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
StopIteration
```

Tak to wygląda w praktyce i to plus minus pod spodem się dzieje, kiedy używamy pętli for i iterujemy sobie po danym obiekcie. W skrócie, tak jak pisałem, po prostu przechodzimy krokowo przez wszystkie elementy, otrzymując pojedynczy element do dyspozycji i mogąc go przetwarzać w jakiś sposób.

Ma to wiele zastosowań i pętla krokowa to taki chleb powszedni często w pythonie. Będziesz widział/widziała ją jeszcze nie raz. Oswój się z nią dość dobrze, bo to będzie prawdopodobnie twój przyjaciel.

## Zwykła pętla

### Krótka charakterystyka

Zwykła pętla jak to ją nazywam, to po prostu pętla `while`. O ile pętla krokowa wykonuje się przechodząc po elementach danego iterowalnego obiektu, tak pętla `while` wykonuje się dopóki zadany warunek jest prawdziwy. Koncept nieco podobny co w pętli krokowej, ale kapkę inny.

### Przykłady użycia pętli

```python
counter = 0
while True:
    counter += 1
    if counter >= 10:
        break
```

I chyba tyle. Reszta do samodzielnej analizy.

## Składanie

Składanie, czy też `comprehensions` i struktury składane to nic innego jak swego rodzaju lukier składniowy, który sprawia, że pewne typowe zachowania można opisać w Pythonie krócej. Zachowania te dotyczą pętli for i tworzenia za jej pomocą nowych obiektów, list, tupli etc. 

Przykład tego, jak używać comprehensions:

```python
list_comprehension = [x for x in range(10)]
dict_comprehension = {x: x**2 for x in range(10)}
set_comprehension = {x for x in range(10)}
set_comprehension_variation = set(x for x in range 10)
tuple_comprehension = tuple(x for x in range(10) if x % 2)
```

Poczytaj kapkę więcej i poeksperymentuj sobie samodzielnie. Pamiętaj, że comprehensions można zagnieżdżać, czyli mieć listę składaną składaną z listy składanej. Book. Incepcja.

Wspomnę tylko dodatkowo o tym, że ja osobiście lubię dłuższe listy składane rozpisywać w następujący sposób:

```python
list_comprehension = [
    value
    for value in range(10)
    if value % 2
]
```

Czyli na trzy linijki, w każdej mamy kolejne elementy. Jeśli comprehension jest krótkie, to tego nie robię, w przypadku bardziej złożonych już tak. Poprawia to moim zdaniem czytelność.

## Generatory

Jak już o pętlach i iteracji mówimy, to wspomnę o generatorach. Cóż to takiego?

Generalnie są to funkcje, które coś `yield`ują zamiast zwracać. Co to znaczy w praktyce i o co chodzi, po co to? 

Mówiąc prostym językiem, to zwyczajnie chodzi o to, że czasami mamy zbiory danych, które są za duże by jednorazowo załadować je do RAMu, gdyż ten jest skończony, duży, ale skończony i ograniczony. Co zrobić wtedy? Generator jest jedną ze strategii radzenia sobie w takiej sytuacji. Otóż generatory pozwalają nam przetwarzać duże zbiory danych krok po kroku.

Generatory to pod spodem tak naprawdę zwykłe pętle, opakowane w funkcje, które `yield`ują jakąś wartość. Co to znaczy? Zamiast zwracać dany element i kończyć egzekucje, generator yielduje daną wartość, 'zapisuje' czy 'zapamiętuje' sobie swój obecny stan i czeka na sygnał, by zwrócić kolejny element. W międzyczasie my możemy sobie przetwarzać i robić coś z danymi wartościami.

Generatory mogą działać na skończonych zbiorach, mogą być nieskończone. Wiele wariacji.

```python
def infinite_sequence():
    num = 0
    while True:
        yield num
        num += 1
for i in infinite_sequence():
    print(i, end=" ")
0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29
30 31 32 33 34 35 36 37 38 39 40 41 42
[...]
6157818 6157819 6157820 6157821 6157822 6157823 6157824 6157825 6157826 6157827
6157828 6157829 6157830 6157831 6157832 6157833 6157834 6157835 6157836 6157837
6157838 6157839 6157840 6157841 6157842
KeyboardInterrupt
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
```

 Generatory mają też to do siebie, że są jednorazowe. To znaczy, że raz zainicjalizowany generator można przejść tylko raz. To plus fakt, iż nie ładujemy danych do pamięci na raz to główna różnica między generatorami a tradycyjnymi listami czy krotkami.

## Walrus 

Od Pythona 3.8 mamy do dyspozycji coś, co nazywane jest Walrusem lub operatorem przypisania w wyrażenia. Pozwala on nam na przypisywanie zmiennych nie tylko w stwierdzeniach, ale również i wyrażeniach, za pomocą operatora `NAME := expr`.

No dobrze, ale co to znaczy w praktyce. Spójrzmy na kod.

```python
data = None
if our_function_getting_json(some_arg) is not None:
    data = our_function_getting_json(some_arg)
    data.do_stuff()
```

Raczej proste do zrozumienia, zasadne, racja? Przykład z pewnego kodu wzięty. Przykład brzydki. Powyższy kod ssie w tym kontekście. Jak można by go poprawić?

```python
data = our_function_getting_json(some_arg)
if data is not None:
    data.do_stuff()
```

Możemy zrobić coś takiego, ale czy to najkrócej jak się da, najlepiej jak się da? Obecnie raczej tak, ale...

Fajnie by było, gdyby można było zadeklarować tą zmienną tam w tym ifie - zapisać po prostu wynik funkcji tam, gdzie jest ona pierwotnie używana. Ważne jest to tam, gdzie chcemy później np. wykonać jakieś operacje na wyniku wyrażenia, które wykonaliśmy, np. w warunku, ale przez to, że w wyrażeniach obecnie nie można zapisywać zmiennych, to musimy zapisać ją sobie sami, wcześniej. Czy to w pętlach, czy w list comprehensions, lambda functions czy w innych.

Chyba, że użyjemy walrusa.

```python
if (data := our_function_gettin_json(some_arg)) is not None:
    data.do_stuff()
```

Inne przykłady użycia:

```python
if (match := pattern.search(data)) is not None:
    match.do_stuff()

while (value := read_next_item()) is not None:
    ...

filtered_data = [y for x in data if (y := f(x)) is not None]
results = [(x, y, x/y) for x in input_data if (y := f(x)) > 0] 
# lub też coś takiego jak niżej
stuff = [[y := f(x), x/y] for x in range(5)]
y = y1 := f(x) # BŁĄD
bar(x = y := f(x)) # BŁĄD
bar(x = (y := f(x))) # OK
something := 'lalala' # BŁĄD
something2 = 'hey' # OK	
```



## Podsumowanie

Pętle, generatory, listy składane etc to przydatne narzędzia dla każdego programisty i podstawowe bloki budulcowe każdego kodu. Dobrze jest być z nimi świetnie zaznajomionym.

## Pytania i zadania

1. Napisz przykłady pętli for, while. Po 3 różne.
2. Napisz artykuł porównujący pętlę for z pętlą while.
3. Do tego charakterystyka porównawcza pętli for i `składania`.
4. Napisz kod, który znajduje największą i najmniejszą liczbę na liście.
5. Napisz kod, który zliczy wyrazy w zadanym stringu.
6. Następnie litery.
7. I częstotliwość ich występowania.
8. Zbadaj czy na zadanej liście, znajdują się dwie liczby – a i b, których suma wynosi zadaną liczbę.
9. Napisz kod, który z dowolnej listy(same liczby) wyświetli tylko te, które są mniejsze od 5.
10. Poproś usera o liczbę a następnie wypisz wszystkie dzielniki tejże liczby.
11. Pobierz od usera dwie liczby a następnie zwróć kwadrat ich sumy.
12. Napisz kod, który wczyta od użytkownika jakiegoś stringa a następnie wyświetli trzy pierwsze litery tego stringa, kolejno po sobie, bez nowych linii. Np. "MelonTusk" -> "MelMelMel"
13. Pobierz od użytkownika stringa a następnie wyświetl go w odwróconej kolejności liter
14. Bazując na kodzie benchmarkującym f-stringi z poprzedniego rozdziału, przeprowadź analizę tego, co jest szybsze. list(), [] czy listy składane. wszystkich niech zawiera liczby naturalne od 1 do 10. Czy jest 

Pamiętaj, że Twoje odpowiedzi możesz wrzucić na GH o tutaj -  https://github.com/grski/junior-python-exercises, a sprawdzę twoje rozwiązania i dam feedback. Więcej o tym podrozdziale 'Część interaktywna'.

\pagebreak
