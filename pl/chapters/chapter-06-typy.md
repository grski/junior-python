\pagebreak

# Typy danych

W poprzednim rozdziale mówiliśmy sobie o zmiennych. Będąc przy tym, siłą rzeczy warto wspomnieć o typach danych jakie nasze zmienne mogą przechowywać w Pythonie. Porozmawiamy sobie o tym konkretnym języku, ale podobny podział występuje w większości języków.

Jak już w poprzednich rozdziałach pisałem, Python nie wymaga od nas definiowania typów dla naszych zmiennych, nie ma w nim statycznego typowania. Przypomnij sobie co to oznaczało i odpowiedz na pytanie - co oznacza brak statycznego typowania? Czym jest dynamiczne typowanie? Jakie są tego wady/zalety. Poszukaj w książce, może w odpowiedziach do poprzednich rozdziałów. Zrób to teraz.

Mimo tego dobrze wiedzieć, na jakie typy zazwyczaj dzielimy sobie różne zmienne. Dlaczego? Bo Python też ich używa, tylko sam niejako zgaduje jakiego typu użyliśmy. Zależnie od typu na zmiennej można wykonywać różne operacje. Jak sobie o tym pomyślimy, to jest to logiczne, bo mimo tego, że pod spodem to wszystko to samo - kod binarny, to na pewnych fragmentach, które interpretujemy jako X, chcemy wykonywać tylko operacje ze zbioru Z, a gdy interpretujemy G, to tylko z F. Mówiąc prościej jak coś oznaczamy jako tekst, to inaczej to potraktujemy, czy inne modyfikacje będziemy mogli zastosować, niż w sytuacji, gdy coś jest liczbą. Na liczbach możemy wykonywać operacje arytmetyczne dla odmiany a w tekście chociażby szukać swojego imienia. Zależnie od typu inne operacje. Logiczne, prawda?

A więc w Pythonie wyróżniamy między innymi następujące podstawowe typy danych:

1. Liczby
2. Napisy
3. Bajty
4. Typ logiczny/boolowski

Z bardziej złożonych mamy:

1. Listy
2. Krotki
3. Słowniki
4. Zbiory

Zaraz je sobie wszystkie po kolei omówimy. Zacznijmy od liczb, bo będzie najdłużej prawdopodobnie.

## Liczby

### Krótka charakterystyka

No to tak moi drodzy, w Pythonie wyróżniamy sobie trzy główne typy liczb: liczby całkowite, liczby zmiennoprzecinkowe i liczby złożone, czyli po kolei tak jakby inty, floaty, complex.

Co to znaczy? 

### Liczby całkowite

Tu sprawa jest chyba prosta, prawda? `1, -1, 5, 0, 938, -24861` to przykłady liczb całkowitych, czyli po prostu `zwykłe` liczby bez żadnych przecinków, udziwnień i wynalazków. Więcej na ich temat rozpisywał się jakoś zbytnio nie będę bo i nie ma po co.

Czy na pewno? 

Zwróć uwagę na to, że w przykładach wyżej pojawia nam się liczba ujemna, mniejsza od zera. W przypadku tekstu zapisać jest ją prosto, stawiamy minus przed i gotowe. Jako ludzie nauczeni jesteśmy, by interpretować to jako liczbę ujemną. Jak natomiast robi to komputer?

### Przykładowy sposób reprezentacji liczb ujemnych

Przypomnijmy sobie poprzednie rozdziały i to, o czym tam mówiliśmy. Pokazywałem między innymi to, jak komputer zapisuje sobie liczby w pamięci i jak je reprezentuje, a mianowicie za pomocą systemu binarnego, bity, bajty, te sprawy. Teraz tak, pojawia się pytanie: jak w takim razie komputer oznacza, że dana liczba jest ujemna? Przecież `minusa` sobie nie postawi w pamięci w jakiś sposób. 

Otóż przedstawię wam, jak to wygląda, znowu, w C. Sposobów i pomysłów jak rozwiązać ten problem było wiele, dalej jest, ale my omówmy tylko jeden. Załóżmy, że operujemy sobie jakimś typem, który jest akurat wielkości 1 bajta. Znaczy to tyle, że ma 8 bitów długości. Ile w takim razie obsługuje maksymalnie wartości/liczb? Odpowiedz na to pytanie proszę, przelicz.

Dobrze, mając 8 bitów, mamy do dyspozycji 8 zer i/lub jedynek. Czyli możemy maksymalnie przedstawić 256 wartości, prawda? Czyli na przykład liczby od 0, do 255. A no nie do końca! 

W domyślnym przypadku będziemy mieć do dyspozycji 256 wartości, prawda, ale z innego zakresu: od **-128** do **127**. Można to określić wzorem: od $-2^{n-1}$ do $2^{n-1}-1$, gdzie n to liczba bitów, czyli dla 8 bitów: od $-2^7$ do $2^7-1$

Skąd ta zmiana? A no stąd, że zabieramy sobie jeden bit by oznaczyć czy dana liczba jest dodatnia, czy ujemna, tak w dużym skrócie. W C, jeśli wiemy, że nie interesują nas wartości ujemne, możemy powiedzieć kompilatorowi, żeby przesunął zakres ujemny na dodatki. Zmienne ze znakiem vs zmienne bez. Signed variables vs unsigned variables. 

Swoją drogą jak już jesteśmy przy tym to dorzucę jeszcze jedną ciekawostkę. Wiesz, że nawet sposób zapisu kolejności bitów w pamięci jest umowny? Co to znaczy? Otóż niektórzy ludzie nie byli w stanie dogadać się co jest lepsze, zapisywanie bita o najwyższej wartości pierwszego czy ostatniego. Stąd też mamy dwa standardy: big endian (grubokońcowość) i little endian (cienkokońcowość). Co to znaczy i jak wygląda w praktyce? Prosta rzecz.

Załóżmy, że rozmawiamy o Big Endian. Chcemy pod adresem 100 wpisać wartość np. 0x4A3B2C1D. Wyglądałoby to tak.

| 100  | 101  | 102  | 103  |
| ---- | ---- | ---- | ---- |
| 4A   | 3B   | 2C   | 1D   |

A Little Endian?

| 100  | 101  | 102  | 103  |
| ---- | ---- | ---- | ---- |
| 1D   | 2C   | 3B   | 4A   |

Czyli odwrotnie. Chodzi generalnie o to, który zapisać gdzie. Robi nam to różnicę przy przeliczaniu/odczytywaniu tych wartości. Która lepsza? Łatwiejsze do ogarnięcia będzie pewnie Big Endian, gdyż jest analogiczna do zapisu jakiego używamy na co dzień w systemie dziesiętnym.

Różne procesory mają różne konwencje, całe szczęście ty nie musisz się tym martwić w swoim kodzie - interpreter Pythona zrobi to za ciebie.

### Liczby zmiennoprzecinkowe i niedokładność ich reprezentacji 

Z czym do czynienia mamy tutaj? Nic innego aniżeli liczby z `częścią po przecinku` mówiąc prostym językiem. I w zasadzie tyle. Jeśli widzimy gdzieś w Pythonie liczbę, gdzie występuje sobie kropeczka - np. `1.0`, to musimy wiedzieć, że mamy do czynienia z liczbą zmiennoprzecinkową. Dlaczego to ważna wiedza? Otóż...

Tutaj, w przeciwieństwie do liczb całkowitych, udziwnienia są i to duże, ale pod spodem. Dłuższy temat, ale generalnie sprowadza się to do tak zwanej niedokładności reprezentacji liczb zmiennoprzecinkowych w systemie binarnym. Tak tak. Jasne, prawda? Powiem tylko tajemniczo, żebyście pamiętali zawsze i wszędzie, że używanie zwykłych floatów/doublów do dokładnych obliczeń czy przechowywania informacji o pieniądzach, to niezbyt dobry pomysł, gdyż czasami `0.1+0.2 != 0.3`. Dlaczego? Bo spróbuj za pomocą potęg dwójki dokładnie przedstawić np. 1/3. Ciężko, co? Ale o co mi w sumie chodzi?

Rozważmy prosty program w C(sprawa dotyczy praktycznie każdego języka):

```c
    #include <stdio.h>

    int main()
    {
        float example_float = 0.1;
        if(example_float == 0.1)
        {
            printf("Equal");
        }
        return 0;
    }
```

Prosty kod, prawda? Myślę, że każdy powinien go zrozumieć, jeśli zna choćby podstawy programowania. Oczekiwanym przez sporą część wynikiem działania tego kodu byłoby wydrukowanie 'Equal' w konsoli, racja? Ja też oczywiście tak myślałem na początku. Sprawdźcie jednak sami, co się stanie gdy kod skompilujecie i uruchomicie.

O dziwo "Equal" się nie wyświetliło. Dlaczego? Coś się pomyliło? Liczby pozornie te same, no bo i tu 0.1 i tu 0.1, co jest? Hm, może zmienną nam źle zapisało. Wypiszmy ją sobie i zobaczmy.

```c
    printf("%f", example_float);
```

Dodajcie sobie tę linijkę kodu po zakończonym ifie. Uruchomcie kod... I co? Oto wynik:

```
0.100000
```

Chwila. Czyli jednak coś źle działa w naszym programie, prawda? No bo `example_float` jest przecież równy 0.1, prawda? A no nie.

Tutaj tego nie widać, bo precyzja jest zbyt niska, ale poprawny to, zmuśmy funkcję `printf` do wyświetlenia naszego floata z większą dokładnością niż domyślna, bo jak widzicie, printf domyślnie wyświetla tylko 6 cyfr po przecinku.

```c
    #include <stdio.h>

    int main()
    {
        float example_float = 0.1;
        if(example_float == 0.1)
        {
            printf("Equal");
        }
        printf("%.16f", example_float);
        return 0;
    }
```

Daje nam

```
0.1000000014901161
```

Lekka modyfikacja naszego kodu i wszystko jasne. Nasz `example_float` nie jest równy dokładnie 0.1, tylko troszkę więcej. Dlaczego?

Wszystko wynika stąd, że komputer 'operuje' na języku binarnym. Oznacza to, że przy tworzeniu liczb dostępne są jedynie potęgi dwójki, mnożone odpowiednio przez 1 lub 0, które można sumować(tak w dużym uproszczeniu, mówiliśmy o tym już). Nic zatem dziwnego, że nasz float tak wygląda. No bo spróbujcie z takich liczb `{..., 1/128, 1/64, 1/32, 1/16, 1/8, 1/4, 1/2, 0, 1, 2, 4, 8, 16, ...}` zbudować dokładnie 0.1. Nie da się tego zazwyczaj zrobić idealnie. Teoretycznie w wyimaginowanym świecie, gdzie mielibyśmy nieskończoną ilość pamięci do dyspozycji i nieskończoną ilość czasu, to moglibyśmy zbliżyć się nieskończenie blisko, nawet ją osiągnąć czasem, do dowolnej liczby. Ale o tym jak chcecie więcej, to poczytajcie sobie o limitach albo przypomnijcie z liceum i z matematyki.

Stąd ta niedokładność - wynika ona jedynie z tego jak reprezentowane są liczby zmiennoprzecinkowe w pamięci komputera. O ile w większości przypadków, za pomocą skończonej ilości pamięci można uzyskać zadowalającą dokładność, tak są takie przypadki, gdzie niestety ta dokładność nie będzie wystarczająca.

Do takich przypadków mamy specjalne biblioteki czy też może specjalne podejście, które inaczej zajmuje się tematem, niemniej jednak warto o tym wiedzieć. Dlatego też, jeśli piszemy jakiś program, który cokolwiek ma wspólnego z pieniędzmi, warto zastanowić się dwa razy zanim użyjemy floata czy doubla. Może lepiej złotówki trzymać w oddzielnym incie, a grosze w oddzielnym? Who knows.

Rozwiązanie wielu problemów związanych z liczbami zmiennoprzecinkowymi znajdziemy w modułach `decimal` i `fractions`. 

Do poczytania: 

1. https://docs.python.org/3/library/decimal.html
2. https://docs.python.org/3/library/fractions.html

### Liczby złożone

Bardzo rzadko spotykane, ale czasem jak ktoś robi obliczenia naukowe jakieś albo inne dziwne rzeczy, to może mu się ta wiedza przydać - otóż są to liczby składające się z części rzeczywistej i urojonej. Matematyczne tematy. Jak nie wiesz o co chodzi, to nie przejmuj się.

Definiujemy je tak: `test = 21 +3j` albo `some_complex_number = complex(32, 3)`. I możemy wykonywać na nich takie same operacje jak na liczbach - dzielenie, mnożenie, dodawanie i tak dalej. Czasami przydatne.

I tyle. Na razie tyle potrzeba ci wiedzieć jeśli idzie o rzeczy, którymi kwalifikujemy jako liczby w Pythonie. Są jeszcze np. decimale czy rationalsy, ale o nich innych razem!

### Operacje na liczbach

Jak wspomniałem przy okazji liczb złożonych, na liczbach możemy wykonywać wszelakie podstawowe operacje matematyczne i zadziałają one plus minus tak, jak byśmy tego oczekiwali. Mówię tutaj o dodawaniu, odejmowaniu, mnożeniu, dzieleniu, dzieleniu całkowitym, operacji modulo i innych podstawowych operacjach arytmetycznych.

Operatory, jakie Python rozumie, to:

| Operator | Akcja                                                        |
| -------- | ------------------------------------------------------------ |
| *        | Mnożenie                                                     |
| **       | Potęgowanie, czyli 2 ** 3, znaczy dwa do potęgi trzeciej.    |
| /        | Zwykłe dzielenie zmiennoprzecinkowe                          |
| +        | Dodawanie                                                    |
| -        | Odejmowanie                                                  |
| //       | Dzielenie bez reszty, czyli 5 // 2 równa się 2,  -11 //  3 równa się -4 (zwróć uwagę na negatywne liczby) |
| %        | Reszta z, czyli np. 5 % 2, to nic innego jak reszta z dzielenia 5 przez 2, czyli 1 |

Warto też pamiętać o tym, że jeśli w jednym wyrażeniu mamy kilka różnych typów liczb, to Python zrzuci wynik całego wyrażenia do najbardziej złożonego typu. Co to znaczy? Wynikiem `1.0 + 1` będzie nie `2` a `2.0`, wynikiem `1 + 1.0 + 3 +0j` będzie `5+0j`. Kolejność złożoności jest zatem taka:

Całkowite -> Zmiennoprzecinkowe -> Złożone. 

Warto o tym pamiętać, gdyż niesie to za sobą pewne konsekwencje - po prostu uważaj na te kropeczki, bo czasami można się naciąć. 

Dodatkowo wspomnę jeszcze o lukrze składniowym, który pozwala nam na skrócenie zapisu popularnych operacji. Wygląda to tak:

```python
foo = 2
foo = foo + 2 # ta linijka będzie równoważna z tą niżej
foo += 2
```



### Konwersje liczbowe

Liczby można pomiędzy sobą 'konwertować', czy też dokonywać swego rodzaju `rzutowania typów` jakbyśmy powiedzieli w innych silnie typowanych statycznych językach. Jak? Niżej przykłady. Przeanalizuj je sobie kapkę sam.

```python
>>> int(1.3)
1
>>> int(1.6)
1
>>> int(1.9)
1
>>> int(1.4444)
1
>>> int("1")
1
>>> int("5")
5
>>> int("52")
52
>>> int("-52")
-52
>>> float(1)
1.0
>>> float(3)
3.0
>>> float("2")
2.0
>>> complex(2)
(2+0j)
>>> int("1.3")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: invalid literal for int() with base 10: '1.3'
```

Pobaw się funkcjami `int`, `float`, `complex`. Następnie opisz co każda z nich robi. Jakie przyjmuje wartości, co powoduje błędy. Ostatni przykład `int("1.3")` spowodował błąd. Przetłumacz go i spróbuj wyjaśnić co tu się stało.

Warto zaznaczyć jedną ważną rzecz, którą Python dostarcza od ręki, a niekoniecznie każdy język tak ma. Otóż wszystkie te funkcje rozumieją, że `"1"` to 1. W innych językach bywa inaczej. Dlaczego. Otóż podczas rzutowania typów następuje operacja często bezpośrednio na wartości w pamięci. Przypomnijmy sobie ten fragment o tym, jak komputer przechowuje tekst w pamięci. ASCII, UTF-8, Unicode i tak dalej. Wróć do poprzednich rozdziałów jak potrzebujesz.

No właśnie, zatem jak? Jako liczby odpowiednio później mapowane. A zatem, w innych językach bywa tak, że zamiast interpretować `"1"` jako 1, to często rzutuje się to do numerycznej wartości która kryje się za znakiem `1` w danym zestawie znaków/kodowaniu. W naszym przypadku `"1"`, czyli jedynka w tekście jest oznaczana nie jako `0b1` ale jako `49` czyli `0b110001` lub `0x31`.

Przy okazji - mała notka. Do szybkiego przeliczania mogą zainteresować cię funkcje, które widać w kawałku niżej.

```python
>>> ord('1')
49
>>> bin(49)
'0b110001'
>>> hex(49)
'0x31'
>>> oct(49)
'0o61'
>>> chr(49)
'1'
```

Czyli `ord`, `bin`, `hex`, `oct`, `chr`. Pobaw się i poczytaj. Gdzie? W dokumentacji [Pythona(https://docs.python.org/3/)](https://docs.python.org/3/). Najlepiej po angielsku. Swoje wnioski i efekty zabawy podsumuj pisząc artykuł, w którym opisujesz o co chodzi z którą funkcją, po krótce scharakteryzujesz każdy z typów. Podasz przykłady dla których funkcje nie działają i domysły dlaczego. Ewentualnie skorzystaj z funkcji `help` np. `help(int)` 

Do tego pokażę ci mały trik:

```python
>>> dir(float)  # alternatywnie: dir(1.0)
['__abs__', '__add__', '__bool__', '__ceil__', '__class__',
 '__delattr__', '__divmod__', '__doc__', '__eq__', '__float__',
 '__floor__', '__floordiv__', '__format__', '__ge__',
 '__getattribute__', '__getnewargs__', '__getstate__', '__gt__',
 '__hash__', '__init__', '__init_subclass__', '__int__', '__le__',
 '__lt__', '__mod__', '__mul__', '__ne__', '__neg__', '__new__',
 '__pos__', '__pow__', '__radd__', '__rdivmod__', '__reduce__',
 '__reduce_ex__', '__repr__', '__rfloordiv__', '__rmod__', '__rmul__',
 '__round__', '__rpow__', '__rsub__', '__rtruediv__', '__setattr__',
 '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__truediv__',
 '__trunc__', 'as_integer_ratio', 'conjugate', 'fromhex', 'hex',
 'imag', 'is_integer', 'real']
>>> dir(str)  # alternatywnie: dir("text")
['__add__', '__class__', '__contains__', '__delattr__', '__dir__',
 '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__',
 '__getitem__', '__getnewargs__', '__getstate__', '__gt__',
 '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__',
 '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__',
 '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__',
 '__setattr__', '__sizeof__', '__str__', '__subclasshook__',
 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith',
 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum',
 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier',
 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle',
 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans',
 'partition', 'removeprefix', 'removesuffix', 'replace', 'rfind',
 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split',
 'splitlines', 'startswith', 'strip', 'swapcase', 'title',
 'translate', 'upper', 'zfill']
```

Otóż funkcję `dir`. Funkcja dir to funkcja, która zwraca wszystkie dostępne metody/atrybuty danego obiektu. 

Póki co nie zajmuj się tymi, które zaczynają się od `__` czy `_` a skup na tych, które zaczynają się od normalnych liter. Czym jednak one są? Metody zaczynające się od `__` to tak zwane Python Magic Methods/Dunder Methods/Metody Magiczne. To coś o czym porozmawiamy później, ale to takie specjalne rodzaje metod/funkcji danego obiektu, które mają spełniać określone role. Te, które zaczynają się od pojedynczego podkreślenia `_`, są metodami prywatnymi.

W Pythonie nie ma enkapsulacji, co znaczy, że generalnie jak dodamy jakiś atrybut/metodę do klasy/obiektu, to nie możemy jakoś bardzo skutecznie zabronić innym wołać, nawet jeśli chcemy by użytkownik nie miał możliwości tego zrobić, gdyż np. dana metoda jest tylko pomocnicza, **prywatna**. Konwencja zatem mówi, byśmy dawali podkreślenie przed prywatnymi zmiennymi, metodami a my jako programiści nie powinniśmy używać takowych o ile nie jest to wewnątrz definicji. Porozmawiamy o tym jeszcze później. W międzyczasie możesz sobie pogooglować o tej całej enkapsulacji.

Podsumowując: za pomocą `dir` możesz sprawdzić, co na danym obiekcie można robić, jakie ma metody/funkcje etc. Przydatne.

Pobaw się tym teraz znanych ci typach.

### Przykłady podstawowych operacji na liczbach

```python
>>> integer = 4
>>> second_integer = 9
>>> first_float = 2.0
>>> second_float = 6.0
>>> help(integer.conjugate)
>>> help(integer.numerator)
>>> integer.numerator
4
>>> integer.numerator
4
>>> integer.as_integer_ratio
<built-in method as_integer_ratio of int object at 0x7f5443904150>
>>> integer.as_integer_ratio()
(4, 1)
>>> integer.bit_count()
1
>>> integer.bit_length()
3
>>> integer.imag
0
>>> integer.real
4
>>> 4 * 2
8
>>> 4 ** 2
16
>>> 4 // 3
1
>>> 4 / 3
1.3333333333333333
>>> 5 // 3
1
>>> 5 % 3
2
>>> first_float.is_integer()
True
>>> first_float.as_integer_ratio()
(2, 1)
```



## Łańcuch znaków

### Krótka charakterystyka

Napisy/tekst, łańcuch znaków, czyli tak zwane stringi. To po prostu tekst. Zazwyczaj przynajmniej, bo mogą to też być jakieś tam zbiory bajtów tak jakby, ale o tym też przy innej okazji.

W Pythonie3 dla zwykłych stringów króluje UNICODE i zazwyczaj utf-8. Oczywiście można używać innych kodowań korzystając z odpowiednich metod, ale póki co chyba nie mamy się co tym martwić. W Pythonie 2 było nieco inaczej, więc tylko i wyłącznie dla wiedzy historycznej o tym wspomnę i nie będę się zbytnio rozwodził nad tym jak proces tam wyglądał, gdyż jest to już nieco archaiczne podejście a wszystkie nowoczesne języki programowania zakładają wykorzystanie UNICODE i utf-8. 

Stringi w pythonie deklarujemy w następujący sposób 

```python
some_text = "foo"  # pierwszy sposób
another_text = 'bar'  # drugi sposób z użyciem ' zamiast "
longer_text = """hahah
another line """
```

A zatem jest to po prostu tekst otoczony `"` lub `'`. Python zezwala na użycie zarówno podwójnego jak i pojedynczego 'ciapka'. Moją praktyką jest, by preferować `"`. Technicznie rzecz ujmując standard pozwala na to by używać zarówno jednego jak i drugiego, byle nie mieszać ich ze sobą w jednym projekcie. Co to znaczy?

Jeśli mamy już jakiś codebase/kod/projekt, i postanowimy używać `'` zamiast `"` to okej, niechże tak będzie, chociaż nie jest to moja preferencja, ale nie mieszajmy stylów. Konwencją jest, by trzymać się jednego i mieć ujednolicony styl w całym kodzie. To znaczy, że jak gdzieś zaczniemy używać pojedynczych ciapków, to używajmy ich już wszędzie w danym projekcie. Jak podwójnych to podwójnych. Wspominałem już, że preferuje podwójne i uważam je za lepsze? Tak samo uważają twórcy narzędzia do formatowania kodu - `black` plus obiektywnie podwójne ciapki mają swoje zalety typu lepsza czytelność czy też łatwiejsze używanie razem z językiem angielskim gdzie mamy sporo znaków `'` w tekście. Nie trzeba dodawać znaku ucieczki.

A no właśnie, znak ucieczki. Porozmawiajmy sobie o znakach specjalnych. Co jeśli w naszym tekście, który zdefiniowaliśmy za pomocą `"`, będziemy potrzebowali użyć też tego znaku? Spróbujmy.

```python
quote = "chciałbym tutaj zacytować "paula coelho" ale nie wiem czy moge"
```

 Podany kod nie zadziała. Dlaczego? Python nie potrafi domyśleć się, że chcesz akurat tutaj cytować i ten znak powinien traktowany być specjalnie, a nie tak jak zwykle. Trzeba mu o tym powiedzieć. Jak? Prosta rzecz.

```python
quote = "chciałbym tutaj zacytować \"paula coelho\" i wiem, że mogę"
```

Zwyczajnie wystarczy dodać `\` przed danym znakiem, który chcemy traktować w specjalny sposób. Teraz może ci kapkę zaświtać dlaczego `"` > `'`. Otóż w języku angielskim często występuje pojedynczy ciapek. Jeśli używamy go do definiowania stringów to pojawia się problem w postaci tego, że musimy często stosować znak ucieczki. Jak użyjemy podwójnego to już rzadziej. A zatem powodem jest lenistwo i czytelność kodu, czyli w sumie też lenistwo. Yay!

Anyway, wróćmy do głównego tematu.

Tak definiowane stringi muszą się mieścić w jednej linijce. Jeśli chcemy, by nasz tekst był wielolinijkowy w kodzie, to musimy użyć Potrójnego znaku - zatem albo `"""` albo `'''` zamiast jednego. To spowoduje, ze python będzie czytał nie tylko do końca linii ale aż do znalezienia znaku zamykającego, który może być już w innej linii.

Warto też zaznaczyć, że do komentowania w kodzie używamy do jednolinijkowych komentarzy używamy `#` a wielolinijkowych stringów jako wielolinijkowych komentarzy.

```python
class RedirectMixin:
    """
    Mixin that is used for the purpose of...
    """
```

Przykład tego wyżej.

Pamiętaj o tym, by użyć `dir` na stringach i przejrzeć sobie podstawowe metody jakie Python posiada w bibliotece standardowej, które pozwalają nam manipulować stringami.

### Pojedyncze znaki

Hm, skoro stringi to łańcuchy znaków to co z pojedynczymi ogniwami tychże łańcuchów? Otóż wyobraź sobie, że po łańcuchach tekstów można iterować jak po liście, plus mamy dostęp do jej poszczególnych elementów, do slicingu etc. NEAT!

### Zmienne w tekście

Oprócz prostych stringów, które po prostu zawierają hardcodowany tekst, czyli dla przykładu:

```python
name = "Aryo"
```

Istnieje możliwość przeprowadzania operacji na stringach, które umożliwiają nam wstawianie do tekstu zmiennych, dodawania stringów etc. Istnieje kilka sposobów by to osiągnąć. Zamiast się rozpisywać, po prostu zaprezentuję.

```python
age = 23
name_and_age = f"Olaf {age}"
name_and_age = "Olaf {}".format(age)
name_and_age = "Olaf " + str(age)
```

Pierwszy sposób nazywamy f-stringami. Są eleganckie. Piękne. Kozackie. Prawilne.

Druga opcja, to funkcja format.

Trzecia zaś to tak zwana konkatenacja. 

Którego używać i kiedy? F-stringi ftw. Format spoko, jak nie można inaczej to konkatenacja.

### Używanie zmiennych w tekście - wydajność

Jestem dość dużym zwolennikiem f-stringów w Pythonie. Podobają mi się one, są eleganckie, czytelne i proste w użyciu. Ciekawiło mnie jednak, jak wypadają jeśli chodzi o wydajność pod spodem, gdyż cóż, ta elegancja pewnie musi mieć jakiś ukryty koszt. Nic w życiu nie ma za darmo, prawda? Postanowiłem to sprawdzić i zestawić ze sobą różne metody manipulacji stringów w Pythonie pod względem wydajności.

W konkurencji znalazły się: f-stringi, konkatenacja (dodawanie) stringów, metoda join(), metoda format(). W zestawieniu nie znalazł się operator %. Dlaczego? Nie przepadam za nim tak szczerze. Moja osobista preferencja. Uważam, że powinno się go raczej unikać z pewnych względów. Relikt przeszłości, mamy dziś lepsze rozwiązania.

#### Metodyka testowania

Testował będę za pomocą modułu timeit wbudowanego w Pythona, wywołując polecenia z terminala. Wszystkie zmienne wykorzystywane w modyfikowanym stringu, będą definiowane i ładowane zanim rozpocznie się mierzenie czasu.
Każde polecenie będzie uruchamiane pętlach o 1000000 iteracjach, każda taka pętla będzie uruchomiona 3 razy. Z tejże pętli wyłoniony zostanie najkrótszy przebieg pojedynczej iteracji. Przejdźmy do samego testowania.

#### Porównanie.

Zaczynajmy zatem. Poniżej kod, jakiego użyłem. Wybaczcie prymitywne nazwy zmiennych, ale pisałem go kompletnie na kolanie.

``` bash
python3 -m timeit -s "x = 'f'; y = 'z'" "f'{x} {y}'" # f-string
python3 -m timeit -s "x = 'f'; y = 'z'" "x + ' ' + y" # konkatenacja
python3 -m timeit -s "x = 'f'; y = 'z'" "' '.join((x,y))" # join
python3 -m timeit -s "x = 'f'; y = 'z'; t = ' '.join" "t((x,y))" # join2
python3 -m timeit -s "x = 'f'; y = 'z'" "'{} {}'.format(x,y)" # format
python3 -m timeit -s "x = 'f'; y = 'z'; t = '{} {}'.format" "t(x,y)" # format2
```

Wszystko raczej proste. Rozważyłem dwie opcje, jedną standardową drugą taką, gdzie znalezienie metody nastąpi w setupie, a w czasie mierzonym tylko i wyłącznie jej wywołanie.

Co mam na myśli, kiedy mówię, że metoda zostanie znaleziona za pomocą operatora .? Otóż Python tam pod spodem robi sobie tak, że atrybuty danej klasy/nazwy metod i tak dalej, trzyma sobie zhashowane w słowniku. Zatem gdy piszemy `obiekt.atrybut`, pod spodem leci sobie szukanie w słowniku/dictionary lookup czy coś takiego jest w tej klasie. To oczywiście dodaje to czasu wykonania bo same instrukcje lookupu zajmują czas, co prawda niedużo, prawie nic, ale wciąż, do tego dochodzi jeszcze czas potrzebny na zaalokowanie pamięci i dodanie elementów do dicta pod spodem przy konstruowaniu instancji. Dla pewności zatem przebadałem różne przypadki. Zaznaczę jednak, że w przypadku produkcyjnego kodu raczej wzbraniaj się przed tego typu optymalizacjami, dobrze? Na juniorskim poziomie to raczej rzadko zdarzy się, iż będziesz przetwarzał tak duże zbiory danych i twój kod będzie wymagał takiej wydajności, by takowe rzeczy odwalać. Tak ku przestrodze. Anyway.

Podobnie zrobiłem z joinem i formatem. Tu rozważyłem dwie opcje - normalne wywołanie z lookupem i to bez niego.

A oto wyniki:

```
f-string: 10000000 loops, best of 3: 0.0791 usec per loop
konkatenacja: 10000000 loops, best of 3: 0.0985 usec per loop
join bez lookupu: 10000000 loops, best of 3: 0.112 usec per loop
join: 10000000 loops, best of 3: 0.144 usec per loop
format bez lookupu: 1000000 loops, best of 3: 0.232 usec per loop
format: 1000000 loops, best of 3: 0.264 usec per loop
```

#### Zaskoczenie

Powiem szczerze, że nie spodziewałem się tego, że f-stringi są nie tylko eleganckim rozwiązaniem, ale i najszybszym! Bardzo mnie to cieszy.
Na drugim miejscu uplasowała się konkatenacja, join bez lookupu, join, format bez lookupu, format, a na samym końcu template string. Z racji tego, że optymalizacja, którą poczyniłem, jest dość niepraktyczna i raczej w kodzie nikt takich potworów nie będzie tworzył poza pewnymi wyjątkami, które być może powinny być napisane w C a nie w Pythonie, to nie umieszczam wyników bez lookupów w rankingu, który wygląda tak:

1. f-string
2. Konkatenacja
3. join()
4. format()

#### Nieco bardziej skomplikowany przykład

Pokazałem prosty przykład - wstawienie dwóch zmiennych oddzielonych spacją. Co jeśli zmiennych mamy nieco więcej niż 2? Załóżmy przypadek z 13 zmiennymi, które chcemy połączyć spacją. Kod:

```python
a, b, c, d, e, f, g, h, i, j, k, l, m = [str(s) for s in range(13)]
# f-string
f"{a} {b} {c} {d} {e} {f} {g} {h} {i} {j} {k} {l} {m}" 
# konkatenacja
"a + ' ' + b + ' ' + c + ' ' + d + ' ' + e + ' ' + f + \
' ' + g + ' ' + h + ' ' + i + ' ' + j + ' ' + k + ' ' + l + ' ' + m"
# format
"{} {} {} {} {} {} {} {} {} {} {} {} {}".format(
    a, b, c, d, e, f, g, h, i, j, k, l, m
)
# join
" ".join((a, b, c, d, e, f, g, h, i, j, k, l, m))
```

Kod wyżej uruchomiłem analogicznie do poprzedniego razu.

Ciekawi mnie jak tutaj sytuacja będzie wyglądała.

Wyniki:

```
join: 1000000 loops, best of 3: 0.352 usec per loop
f string: 1000000 loops, best of 3: 0.399 usec per loop
format: 1000000 loops, best of 3: 0.872 usec per loop
concat: 1000000 loops, best of 3: 1.13 usec per loop
```

Bazując na poprzednich wynikach, nie zdziwiły mnie one za bardzo. Dlaczego?
Zacznijmy od tego, co się zmieniło. Join wskoczył z 3. miejsca na 1. Konkatenacja spadła z 2. na przedostatnie. Format na 3. z czwartego. W sumie dość zasadne, dlaczego.

Pierwsze miejsce join w takiej sytuacji jest oczywiste - popatrzmy co tam robimy - joinujemy tak jakby ze sobą wiele stringów ze wspólnym stringiem, czyli dokładnie to, do czego join został stworzony. Jestem niemalże pewnym, iż pod spodem na poziomie implementacji metody czy nawet interpretera są zrobione pod to optymalizacje, dzięki czemu join świetnie poradzi sobie z dużą ilością argumentów. Cieszy mnie to - ponownie rozwiązanie, które w tym przypadku wygląda najbardziej elegancko, wypada pierwsze.

Drugie miejsce f-string. Tutaj też się nie zdziwiłem. Dlaczego? Otóż f-stringi, pierwotnie co prawda były wolne, bardzo wolne, - w pierwszej implementacji były one "kompilowane" na nic innego jak zbiór odpowiednich joinów albo formatów, nie pamiętam. Niemniej jednak w kolejnej implementacji f-stringi doczekały się własnego, zoptymalizowanego OPCODE w CPythonie, co pozwoliło poczynić znaczne oszczędności i lepiej dostosować kod C, który jest pod spodem.

Dlaczego format wyprzedził konkatenacje? Cóż, domyślam się. Wydaje mi się, iż chodzi o ewaluację. Być może Python, z racji tego, że stringi są niemutowalne w Pythonie, za każdym razem, kiedy wykonywał operacje dodania na dwóch stringach, musiał zaalokować nowy kawałek pamięci, który pomieści X znaków, gdzie X to suma długości dwóch stringów, potem je tam przekopiować, by otrzymać finalną wartość. Z racji doświadczenia tego, jak python działa, to założę się, że w naszym wypadku, kiedy mieliśmy kod w postacie a + ' ' + b + ..., Python wykonywał każdą operacje dodawania oddzielnie. To znaczy, prawdopodobnie instrukcje pod spodem wyglądały tak:

1. Zaalokuj pamięć, która pomieści zmienną a oraz string ' '.
2. Przekopiuj wartość a
3. Przekopiuj wartość ' '
4. Otrzymany wynik dodaj do zmiennej b.
5. Zaalokuj pamięć, która pomieści poprzedni wynik oraz zmienną b.
6. ...

I tak dalej. A to wszystko kosztuje czas - nowe alokacje, kopiowanie. Tak mi się przynajmniej wydaje, że to zadziałało w ten sposób, nie jestem jednak pewien, czy developerzy pythona nie poczynili jakiś optymalizacji na ten przypadek i może robią to inaczej? Nie wiem, aż tak głęboko nie zaglądałem, ale patrząc po wynikach, nie sądzę.

#### Podsumowanie - o wydajności

W pythonie mechanizmy, które zdają się wyglądać elegancko w danej sytuacji, zazwyczaj są pod takową zoptymalizowane i przygotowane, stąd warto ich używać. Piękny ten wąż po prostu. Elegancki kod.

Używajcie zatem f-stringów gdziekolwiek tylko możecie i cieszcie się z życia, tam gdzie dużo stringów do połączenia w przewidywalny sposób, join. Dzięki temu wasz kod będzie ładniejszy ale i szybszy!



### Przykłady podstawowych operacji na stringach

```python
>>> dir(str)
['__add__', '__class__', '__contains__', '__delattr__', '__dir__',
 '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__',
 '__getitem__', '__getnewargs__', '__getstate__', '__gt__',
 '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__',
 '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__',
 '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__',
 '__setattr__', '__sizeof__', '__str__', '__subclasshook__',
 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith',
 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum',
 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier',
 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle',
 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans',
 'partition', 'removeprefix', 'removesuffix', 'replace', 'rfind',
 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split',
 'splitlines', 'startswith', 'strip', 'swapcase', 'title',
 'translate', 'upper', 'zfill']
>>> text = "some text"
>>> text.capitalize()
'Some text'
>>> text.count("t")
2
>>> text.replace("t", "f")
'some fexf'
>>> coolest_org = "NAFO"
>>> coolest_org.lower()
'nafo'
>>> coolest_org_lower = coolest_org.lower()
>>> coolest_org + coolest_org_lower
'NAFOnafo'
>>> "RuSSia" + "HATE" "CLUB"
'RuSSiaHATECLUB'
>>> 'test' * 10
'testtesttesttesttesttesttesttesttesttest'
>>> coolest_org = "nafo"
>>> coolest_org = coolest_org.upper()
>>> coolest_org
>>> 'NAFO'
>>> coolest_org.swapcase()
>>> 'nafo'
>>> coolest_org.isalpha()
>>> True
>>> coolest_org.find("F")
>>> 2
>>> "AaBbCcDd"[::2]
>>> 'ABCD'
```

Zauważ, że stringi są niemutowalne. Znaczy, to, że nie możemy ich modyfikować a każda modyfikacja powoduje, że w efekcie powstaje nowy string. Pomówimy o mutowalności jeszcze nieco później kiedy będziemy omawiać listy i krotki.

## Bajty 

### Krótka charakterystyka

Hmmm, bajty. To owszem, podstawowy i prosty typ w Pythonie, to po prostu ciąg bajtów jak sama nazwa wskazuje. Przydatne przy operacjach na plikach. Poczytaj samodzielnie.

## Typ logiczny/Boolowski

### Krótka charakterystyka

Tutaj sprawa wygląda prosto - typ logiczny to tak zwany bool - albo prawda, albo fałsz. Typ o długości 1 bita. Albo 0 albo 1, albo `True` albo `False`.

### Wartości prawdziwe vs wartości fałszywe 

Zazwyczaj używany przy warunkach, ustawianiu jakichś flag i tak dalej. Warto zaznaczyć, że w Pythonie typ logiczny jest nieco rozszerzony. To znaczy, że cokolwiek co można zewaluować do pewnych rzeczy, będzie traktowane jak typ logiczny. Mówiąc prościej, Fałsz jest zerem lub czymś pustym. Prawda jest zaś dowolną liczbą inną niż zero lub czymś niepustym. Pusty string to Fałsz, jakiś tekst to Prawda. Pusta lista to Fałsz. Niepusta przeciwnie.

```python
>>> bool(1)
True
>>> bool(0)
False
>>> bool(0.1)
True
>>> bool([])
False
>>> bool(["f"])
True
>>> bool("String")
True
>>> bool("")
False
```

Mała notka. Funkcja `bool` to w Pythonie coś, co próbuje 'przekonwertować' zadaną wartość do `booleana` czyli typu logicznego/boolowskiego. Zasady Przedstawiłem ci wyżej. Inne typy również mają swoje odpowiedniki, pobaw się nimi.

### Przykłady podstawowych operacji na typie boolowskim

## Listy

### Krótka charakterystyka

Czym jest lista? Lista to nic innego jak mutowalny zbiór elementów. Swego rodzaju 'tablica'. Możesz sobie pomyśleć o tym w kategoriach stringa. Dlaczego? A bo czymże jest string, aniżeli listą znaków? To po prostu pewien obszar w pamięci, który jest mutowalny. Co to znaczy? Otóż oznacza to, że lista jest zbiorem elementów, który po zadeklarowaniu można dowolnie modyfikować. Listę można zmniejszać, kasować z niej elementy. Można dodawać do niej elementy. Można znowu je usunąć. Rozmiar listy można zmienić. Poszczególne elementy można nadpisać. Co chcesz, to masz.

Lista może składać się z praktycznie dowolnych elementów, oznacza to, że do listy można włożyć prawie każdy obiekt z Pythona. Nie zawsze tak jest. W innych językach programowania często jest tak, że jak definiujemy tablicę, to po pierwsze z góry znana jest jej długość, chyba, że używamy tablic dynamicznych, dwa, jej elementy często są ograniczone do jednego tylko typu z różnych powodów. Dlaczego?

### Lista od strony niskopoziomowej

Jednym z powodów będzie coś, co nawiązuje do samego początku tej książki, gdzie opisywaliśmy sobie zagadnienie związane z tym, kiedy program wie, gdzie przestać czytać pamięć w przypadku odczytu zmiennej spod danego adresu.

Otóż tutaj zastosowanie ma podobna analogia. Np. w C deklarując tablicę/listę, podajesz jej długość i typ. Po co? Po to by kompilator/program mógł sobie ogarnąć ile pamięci zaalokować i jak poradzić sobie z adresami, gdzie przestać czytać etc. 

Zatem 10 elementowa tablica charów zaalokuje nam w C pamięć o rozmiarze `10 * size(char)`. Komputer będzie wiedział gdzie, i co, i jak czytać, kiedy skończyć.

Załóżmy, że nasza tablica znajduje się pod adresem `0x1` i w jej środku znajdują się 4 elementy, każdy z nich o wielkości jednego bajta:

| Bit (hex)   | 0x01 | 0x02 | 0x03 | 0x04 |
| ----------- | ---- | ---- | ---- | ---- |
| **Wartość** | A    | B    | C    | D    |

Tutaj przypomnij sobie jak wygląda pamięć, ile bitów używamy standardowo do zapisu pojedynczego znaku, załóżmy ASCII w tym wypadku i jak liczyć z szesnastkowego na dziesiętny/binarny.

Mamy już zobrazowane nieco jak to wygląda w przypadku np. C i tablicy/listy o jednakowym typie i znanej długości. Co w przypadku Pythona?

### Referencje i wartości

W Pythonie jest nieco inaczej, ale podobnie. Otóż można by się zapytać: to skąd Pythonie wie kiedy przestać czytać dany adres, skoro tam pod spodem to też najczęściej jest C, w przypadku CPythona przynajmniej? Otóż lista w pythonie tak naprawdę nie jest listą wartości z danymi typami a listą referencji niejako. Cóż to takie? Otóż Python tak naprawdę, kiedy tworzymy listę, to przechowuje on sobie zbiór referencji do danych wartości, a nie same wartości. Zatem wracając do naszej wcześniejszej analogii i porównania z C, gdzie musieliśmy zadeklarować typ wartości w tablicy, nagle wszystko ma sens. Okazuje się, że w Pythonie, tam pod spodem, też mamy w pewnym sensie jeden rodzaj wartości - referencje. Referencje to, w uproszczeniu, odniesienia do jakichś obiektów. Obiekt może być np. inną listą czy instancją jakiejś klasy.

Czyli w Pythonie, w pamięci nasza tablica będzie wyglądała +/- w taki sposób:

| Bit (hex)   | 0x01        | 0x09        | 0x11        | 0x19        |
| ----------- | ----------- | ----------- | ----------- | ----------- |
| **Wartość** | Referencja1 | Referencja3 | Referencja2 | Referencja4 |

Kolejność losowa.  Teraz kiedy odczytujemy sobie wartość z listy python przejdzie sobie do tego co skrywa np. `Referencja1` i weźmie sobie co potrzebuje, niezależnie od typu. Takim oto sposobem pozornie różne typy mogą być w pythonie w jednej liście i nie powoduje to problemów.

Jedna zawiłość wyjaśniona. Pora na drugą -> dynamiczny rozmiar.

### Dynamiczny rozmiar list

Okej, pora wyjaśnić jak to się magicznie dzieje, że w listy w Pythonie mają dynamiczny rozmiar, mimo tego, że np. w C, póki co, pisałem o tym, że wypada podać  rozmiar. Otóż sprawa ma się tak, że w Pythonie, pod spodem, jest tak samo. Interpreter Pythona patrzy na to z iloma elementami utworzyliśmy listę i następnie sam się 'domyśla' ile elementową tablicę zaalokować. 

Co się dzieje gdy zmieniamy rozmiar listy/dodajemy nowe elementy?

### Alokowanie ponad potrzeby - chciwy i przebiegły wąż

Generalnie przypadek tutaj mamy taki, że Python podczas deklaracji jakiejś listy alokuje więcej pamięci niż nam potrzeba! CZO?! JAK TO? 

Ano tak. Generalnie zazwyczaj jest to około $2n$ zakładając, że $2n>=2$ gdzie n to liczba elementów. Zatem nawet kiedy inicjalizujemy pustą listę Python pod spodem alokuje sobie miejsce na przynajmniej dwa elementy, albo więcej. Nie pamiętam już nawet. Po co? A no po to, że interpreter spodziewa się tego, iż będziemy dodawać kolejne elementy. Jeśli osiągniemy zadaną wielkość i spróbujemy dodać kolejny element nastąpi wtedy alokacja nowej pamięci, znowu zachodzi proces opisany przed chwilą i nadalokacja pamięci, po czym wartości ze starego miejsca w pamięci/starej listy są kopiowane w nowe miejsce gdzie mamy zaalokowany większy fragment pamięci, a całość jest dynamicznie podmieniana gdzie trzeba w taki sposób, że my, jako programista/użytkownik końcowy, nawet nie zauważymy.

Jak widzisz Python robi za nas wiele rzeczy byśmy nie musieli się tym martwić. Oczywiście, ma to swój koszt w postaci wydajności czy to komputacyjnej czy pamięciowej, ale niestety, coś za coś. Python szybki nie jest, ale jest wystarczająco szybki, ale tę rozprawkę już czytałeś - w rozdziale o wadach i zaletach Pythona.

Opisuję tutaj cały proces w bardzo dużym uproszczeniu, ale plus minus tak to wygląda.

### Dostęp do elementów listy 

Dostęp do elementów listy zachodzi za pomocą podania indeksu elementu jaki chcemy dosięgnąć. Z racji tego, że znamy rozmiar referencji to wiemy o ile zrobić offset w pamięci. Mówiliśmy już o tym. W kodzie wygląda to tak:

```python
war_crimes = ["Russia on Ukraine", "Israel on Palestine"]
>>> war_crimes[0]
'Russia on Ukraine'
>>> war_crimes[1]
'Israel on Palestine'
>>> war_crimes[2]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: list index out of range
```

Dosyć logiczne. Przekroczenie długości tablicy spowoduje błąd. Jedna ważna notatka. W programowaniu zazwyczaj indeksujemy od zera. Dlaczego? Podstawy odpowiedzi znajdziesz w rozdziale 4. i 5., ale dla pewności wytłumaczę. Oczywiście są wyjątki od reguły, niektóre języki indeksują od 1, bo tak i cześć, ale my o prawilnych językach rozmawiamy jak C, Python czy Rust.

### Negatywne indeksy

O ile zazwyczaj w innych językach niekoniecznie istnieje taka instytucja jak negatywne indeksy w przypadku list, tak w przypadku Pythona jak najbardziej tak. Używanie negatywnych indeksów powoduje, że Python zaczyna liczyć od końca listy w górę. Dość prosty koncept.

```python
>>> numbers = [1,2,3,4]
>>> numbers[-1]
4
>>> numbers[-2]
3
```

### Cięcie list

Czyli tak zwany slicing. O cóż chodzi? A no mając sobie jakąś listę może najść nas potrzeba, by operować na jej kawałku czy coś. Kto wie, dziwne potrzeby ludzie mają. No i cóż teraz? Kopiować, iterować samemu po danej liście? Absolutnie nie. Python posiada, jak zawsze, wbudowane rozwiązanie, które pozwala nam w prosty i przyjemny sposób osiągnąć tenże efekt. Slicing się to po angielskiemu nazywa. Jak działa?

```python
>>> numbers = [1,2,3,4, 5, 6, 7, 8]
>>> numbers[3:6]
[4, 5, 6]
# od pierwszego do piątego
>>> numbers[:4]
[1, 2, 3, 4]
# od czwartego do końca
>>> numbers[3:] 
[4, 5, 6, 7, 8]
# od pierwszego do ostatniego
>>> numbers[::]
[1, 2, 3, 4, 5, 6, 7, 8]
# od pierwszego elementu listy, zaznaczając co drugi element -> 2n+1
>>> numbers[::2]  
[1, 3, 5, 7]
# od drugiego elementu listy, zaznaczając potem co drugi element -> 2n 
>>> numbers[1::2]  
[2, 4, 6, 8]
 # od ostatniego elementu listy do końca zaznaczając po tem co drugi element
>>> numbers[-1::2]
[8]
 # od ostatniego elementu listy do końca czyli po prostu ostatni element
>>> numbers[-1:] 
[8]
>>> numbers[-4:]
[5, 6, 7, 8]
>>> numbers[:-4]
[1, 2, 3, 4]
>>> numbers[::-1]  # łatwy sposób odwrócenia listy
[8, 7, 6, 5, 4, 3, 2, 1]
```

Slicing ma następującą składnię

```python
zadana_lista[początkowy_element:końcowy_element:skok]
```

Początkowy czy końcowy element to raczej znany koncept. Skok to po prostu informacja, co który element mamy zabierać.

Ważna informacja: slicing tworzy kopie listy, świeżutką, nowiutką kopię listy. Jest to jednak płytka kopia, a nie głęboka. Co to znaczy, opiszę nieco dalej. Dowód:

```python
>>> numbers is numbers[:]
False
```

Jak widać slicing powoduje skopiowanie i utworzenie nowej listy pod spodem. Albo inaczej. Pamięć zostanie skopiowana w drugie miejsce i zduplikowana w ten sposób, natomiast referencje w środku będę te same. Jeśli lista zawiera referencje do obiektu, który jest pass-by-reference, to modyfikacja tego obiektu spowoduje zmianę wartości w obu listach, tej skopiowanej też, natomiast jeśli coś jest   pass-by-value (niemutowalne typy w większości przypadków), to modyfikacja będzie dotyczyła tylko tej listy której element modyfikowaliśmy. 

```python
>>> pass_by_reference = [[1,2,3], 1, 2, 3]
>>> new_pass_by_reference = pass_by_reference[:]
>>> pass_by_reference
[[1, 2, 3], 1, 2, 3]
>>> new_pass_by_reference
[[1, 2, 3], 1, 2, 3]
>>> pass_by_reference is new_pass_by_reference  # dwie różne listy
False
# pierwszym elementem listy jest inna lista
# listy są mutowalne i przekazujemy je przez referencje
>>> pass_by_reference[0]  
[1, 2, 3]
# modyfikujemy tutaj drugi element tej wewnętrznej listy z oryginału
>>> pass_by_reference[0][1] = "test"
>>> pass_by_reference[0]
[1, 'test', 3]
# jakimś sposobem lista w kopii też uległa zmianie
>>> new_pass_by_reference
[[1, 'test', 3], 1, 2, 3]
>>> new_pass_by_reference[0]
[1, 'test', 3]
```

Pomyśl o tym. Pogadamy pewnie jeszcze na ten temat przy omawianiu kluczy w słownikach.

### Dlaczego indeksujemy od zera

Stwierdziłem kiedyś gdzieś, że indeksowanie od zera jest logiczne i ma swoje powody, to naturalne i jest tak, jak w RHC przykazali. Padł jednak komentarz, że jest w zasadzie na odwrót a my, programiści, indeksujemy sobie od 0 tak po prostu, bo się przyzwyczailiśmy.

Otóż nie. [Mimo tego, że sam kiedyś podobnie myślałem](https://4programmers.net/Mikroblogi/View/8661#entry-8661), to indeksowanie od 0 jest logiczne i ma swoją zasadność. Jaką?

```C
#include <stdio.h>

int main(void) {
    int numbers[] = {1,2,3,4};
    printf("numbers in general: %p -- %p\n", &numbers, numbers+0);
    for (int i = 0; i < sizeof(numbers)/sizeof(numbers[0]); i++) {
        printf("number no. %i: %p -- %p -- value: %d\n",
               i, &numbers[i], numbers+i, *(numbers+i));
    }
    printf("int size: %d\n", sizeof(int));
    return 0;
}
```

Kod wyżej skompilowany i uruchomiony da nam:

```bash
numbers in general: 0x7ffc9f728f20 -- 0x7ffc9f728f20
number no. 0: 0x7ffc9f728f20 -- 0x7ffc9f728f20 -- value: 1
number no. 1: 0x7ffc9f728f24 -- 0x7ffc9f728f24 -- value: 2
number no. 2: 0x7ffc9f728f28 -- 0x7ffc9f728f28 -- value: 3
number no. 3: 0x7ffc9f728f2c -- 0x7ffc9f728f2c -- value: 4
int size: 4
```

Przeanalizujmy troszkę o cóż tu chodzi.

Zanim to zrobimy, zaznaczę tylko, że Ty, jeśli uruchomiłeś ten kod u siebie, mogłeś dostać nieco inne wyniki. To normalne.

Dla większości osób nieznajomych z C/C++ ten kod może wydawać się nieco kryptyczny, ale w gruncie rzeczy jest dość prosty.

Zacznijmy może od linijki

```c
printf("numbers in general: %p -- %p\n", &numbers, numbers+0);
```

Zakładam, że pierwsza część printa jest zrozumiała dla każdego, może poza `%p` - to po prostu nam mówi, że argument do wyprintowania będzie specyficznym typem danych.

A co to to całe `&numbers` - operator & mówi, że chcę otrzymać adres danej zmiennej - czyli jej lokację w pamięci. Bo jak dobrze wiemy, zmienne alokowane są w pamięci, w pewnym miejscu wybranym przez komputer. Ponownie - mówiliśmy już o tym w rozdziałach 4. i 5. 

To miejsce zazwyczaj opisuje się jako 'adres' - czyli liczba bajtów/bitów od 'początku' pamięci, którą procesor musi 'przeskoczyć', by dotrzeć do danej zmiennej.

Nasza tablica (czyli taka jakby lista z Pythona, ale nie do końca), znajduje się pod adresem: 0x7ffc9f728f20 (zapis szesnastkowy), i jest to tym samym adres naszego pierwszego elementu.

Kompilator musi musi jednak wiedzieć, pod jakim adresem znajduje się następny element naszej tablicy. Skąd? To już wyjaśniałem i liczę na twoją odpowiedź. Moją znajdziesz poniżej.

Zadeklarowaliśmy, że elementy naszej tablicy będą typu `int`. Typ `int` na komputerze, z którego korzystam, jest akurat 4 bajtowy, czyli 32 bitowy. Jest to w zasadzie standard (chociaż oficjalnie standard mówi o tym, że int ma być po prostu przynajmniej 16 bitowy, nie specyfikuje jego rozmiaru dokładnie), ale czasami są odstępstwa od reguły, zależnie od architektury, stąd też ten `sizeof(int)` w kodzie - zwraca on rozmiar danego typu w obecnym środowisku.

Dlatego też, jeśli 0x7ffc9f728f20 jest adresem pierwszego elementu, który zajmuje w pamięci 4 bajty o adresach: 

- `0x7ffc9f728f20`, 
- `0x7ffc9f728f21`, 
- `0x7ffc9f728f22`, 
- `0x7ffc9f728f23`, 

to możemy wnioskować, że następny element tej tablicy będzie po nim, pod adresem `0x7ffc9f728f24`, czyli 4 bajty dalej. Następny znowu kolejne 4 bajty i tak dalej, aż do ostatniego elementu. Można stąd wyekstrahować prosty wzór zatem.

Adres konkretnego elementu tablicy można określić wzorem:

$adres\_pierwszego\_elementu+(index*rozmiar\_typu)$. 

*Z takiego też wzoru korzysta komputer - za każdym razem, gdy piszesz `numbers[index]` kompilator tłumaczy to sobie wewnętrznie na *

$(numbers+(index*rozmiar\_typu))$. 

Co znaczy dla kompilatora `*`? Nic innego, jak 'idź pod dany adres i weź wartość znajdującą się pod tym adresem.'

Zatem gdy napiszemy numbers[0], to nasz kompilator przetłumaczy to na 

$(0x7ffc9f728f20+0)$=$(0x7ffc9f728f20)$,

co z kolei znaczy: weź wartość z tego adresu i wstaw ją tutaj.

W przypadku np. numbers[1], będzie to 

$0x7ffc9f728f20+(1*sizeof(int))$ = $0x7ffc9f728f20+(1*4)$

$0x7ffc9f728f20+(1*4)$ = $0x7ffc9f728f20+4$

czyli 

`0x7ffc9f728f24`. 

Jasne? Jak dla mnie tak. Jeśli masz problem ze zrozumieniem tego konceptu, nie przejmuj się, wiele osób nie do końca rozumie wskaźniki, adres i pamięć. Ja też miałem z tym problem. Przynajmniej na początku.

Możesz wspomóc się [filmikami Gynvaela - Gynvael's Code: Pointery #1](https://www.youtube.com/watch?v=bewTJaboGIw) czy [wykładami z CS50 - kursu z Harvardu](https://www.youtube.com/watch?v=PYJYiBlto5M) oni, jako osoby o znacznie większej wiedzy, tłumaczą całe zagadnienie znacznie lepiej niż ja.

### Jakby to wyglądało, gdybyśmy indeksowali od 1?

Załóżmy, że indeksujemy od 1. Wtedy wzór musiałby ulec modyfikacji - i wyglądałby on tak:

$adres\_pierwszego\_elementu+((index-1)*rozmiar\_typu)$

Innym rozwiązaniem byłoby przesunięcie lokacji pierwszego elementu tablicy o 4 bajty do przodu względem adresu samej tablicy, ale wtedy nasza tablica zajmowała by dodatkowe miejsce w pamięci i to niepotrzebnie, gdyż te pierwsze x bajtów, gdzie x to rozmiar danego typu danych, byłoby po prostu puste. To raz, dwa, że trzeba by pamiętać, że adres tablicy nie jest adresem pierwszego jej elementu.

Oba te rozwiązania są bezsensowne, bo o ile nie jest to niby dużo - kilka bajtów na każdej tablicy, czy jedna operacja odejmowania, to gdy pomnożymy to sobie przez ilość takich zmiennych, które mamy w pamięci, to już wyjdzie całkiem pokaźna sumka bajtów/operacji, które w istocie rzeczy, są zbędnie zajmowane.

Dodatkowo ileż kodu bazuje już na indeksowaniu od 0. Niemożliwym by było to wszystko zmienić.

Oczywiście, są również inne argumenty, by indeksować czy liczyć elementy od zera, jak chociażby [te, głoszone przez Dijsktrę - Why numbering should start at zero](https://www.cs.utexas.edu/users/EWD/transcriptions/EWD08xx/EWD831.html)]. To taki raczej znany i ważny Pan, dla tych, którzy nie kojarzą ;)

Ogółem użyłem tutaj trochę uproszczeń i skrótów myślowych, ale generalny koncept przekazany.

### Przykłady podstawowych operacji na listach

## Krotki/Tuple

### Krótka charakterystyka

Krotka to tak naprawdę nic innego niż niemutowalna lista. Co to znaczy? Mniej więcej tyle, że po zadeklarowaniu krotki nie można już modyfikować. Deklarujemy raz i koniec. Niesie to ze sobą wiele konsekwencji o których zaraz opowiem. 

Jedyne co z krotką można zrobić to odczytać ją, skopiować czy też ponownie zadeklarować zmienną o danej nazwie. Przykłady niżej.

Po co nam te krotki/tuple? Ogółem niemutowalnośc danych często sprawia, że z pewnymi rzeczami trudniej sobie strzelić w stopę. Do tego jest to podejście bardziej podobne do programowania funkcyjnego, powiedzmy. Niemutowalność jest całkiem spoko.

Oprócz tego mamy tutaj jeszcze jedną zaletę. Wydajność.

### Wydajna bestia

Otóż jeśli jest to niemutowalna struktura danych to interpreter pythona wie dokładnie ile pamięci zaalokować plus z pewnych względów proces ten zachodzi szybciej. Czyli tutaj alokacja ponad potrzeby nie ma miejsca plus do tego instrukcja wykonuje się niejako szybciej, python wie jakie typy są użyte, zna konkretne dane które wykorzystaliśmy etc.

Jako anegdotkę przytoczę historię, gdy zastosowanie tupli zmniejszyło nam zużycie pamięci z 4 GB do ~2.1 GB w pewnej niedużej webappce. W innych wypadkach redukcja bywała nawet bardziej drastyczna.

### Przykłady podstawowych operacji na krotkach

```python
dir(tuple)
['__add__', '__class__', '__class_getitem__', '__contains__',
 '__delattr__', '__dir__', '__doc__', '__eq__', '__format__',
 '__ge__', '__getattribute__', '__getitem__', '__getnewargs__',
 '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__',
 '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__',
 '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmul__',
 '__setattr__', '__sizeof__', '__str__', '__subclasshook__',
 'count', 'index']
In [9]: some_tuple = ("f", 1, 2)
In [10]: some_tuple[1]
Out[10]: 1
In [11]: some_tuple[1] = 2
In [13]: some_tuple.count(1)
Out[13]: 1
In [14]: some_tuple.count(2)
Out[14]: 1
In [15]: some_tuple.count(3)
Out[15]: 0
```



## Słowniki

### Krótka charakterystyka

Czymże jest magicznie brzmiący słownik zwany także Dictem/HashMapą? Otóż jest to nic innego jak swego rodzaju słownik/mapowanie. Tak jak w zwykłym słowniku mamy pewnego rodzaju mapowanie **kluczy** do **wartości** w postaci słowa i jego znaczenia, tak podobnie jest w pythonowym słowniku/hashmapie.

Do rzeczy.

Słownik w Pythonie to struktura danych, która pozwala nam przechowywać dowolne wartości pod określonymi kluczami. Wyobraź sobie listę, ale zamiast indeksu w postaci liczbowej masz indeks w postaci określonego klucza.

W praktyce wygląda to tak:

```python
>>> test_dict = {"test": "some_string", 1: "hehe", 2: 3}
>>> test_dict["test"]
'some_string'
>>> test_dict[1]
'hehe'
>>> test_dict[2]
3
```

Przewidywalne. Reszta działa również podobnie jak w liście.

Co jest różnego od działania listy jest to, że o ile w liście zapewniona jest gwarancja tego, że elementy zawsze będą w tej kolejności w jakiej je do listy włożyliśmy. Tak hashmapa z definicji takiego czegoś nie przewiduje. Obecna implementacja CPythona, od wersji 3.7, mimo wszystko zapewnia coś takiego dodatkowo, czyli ze zwykłego `Dicta` zrobił nam się `OrderedDict`, natomiast lepiej się nie nastawiać na to, gdyż wersja pythona typu 3.6 jest dość stara, ale wciąż jest mnóstwo projektów w niej napisanych. Co z tego? A no to, że kod, który będziesz pisał prawdopodobnie może być odpalany na wersji Pythona, która nie bierze pod uwagę i nie gwarantuje zachowania kolejności insercji elementów, zatem lepiej na tym zbytnio nie polegać, bo w większości przypadków ta kolejność będzie zachowana mimo wszystko, ale nie jest ona gwarantowana implementacyjnie, czyli zawsze znajdzie się ten 1%, gdzie jednak coś pójdzie nie tak. Potem weź takiego buga dostań do inwestygacji.

Oczywiście jeśli jesteś świadom i wiesz co robisz, plus masz gwarancje tego, na jakich wersjach pythona twój kod będzie banglał, to śmiało. Natomiast pamiętaj, W najnowszej wersji pythona -> spoko, poniżej 3.8 albo 3.7 już niekoniecznie. Sprawdź dokładnie w której wersji wprowadzono `OrderedDict` jako domyślny.

### Jak przebiega proces dodawania elementów do dicta?

Otóż generalnie tak jak w przypadku listy mieliśmy numeryczny indeks, za pomocą którego Python liczył sobie offset w pamięci, tak w przypadku dicta mamy coś takiego jak funkcja hashująca. Ta funkcja bierze sobie za argument klucz jakiego używamy i na jego podstawie próbuje generować w miarę unikalny hash. Potem na podstawie hashu, zazwyczaj poprzez operacje modolu, ogarniamy sobie adres/offset gdzie trzymana jest dana wartość.

Logiczne? Czyli tak, za każdym razem jak ktoś wpisuje `some_dict["key"]` to pod spodem dzieje się coś takiego, że interpreter Pythona, by uzyskać adres z jakiego odczytać ma wartość dla danego klucza, bierze tenże klucz, wrzuca go w funkcję hashującą, nie wiem, załóżmy `hash("key")`, ta funkcja zaś zwraca nam jakiś tam możliwie unikalny hash wygenerowany/obliczony na podstawie danego klucza. Z hasha wyczarowujemy sobie adres/offset. Jakoś tak.

Dlaczego w miarę unikalny?

### Kolizja hashy

Hash collision to coś co się czasami zdarza. Dlaczego? Otóż funkcja hashująca nie może być kompletnie losowa. Musi być stabilna i powtarzalna. To znaczy, dla zadanego argumentu musi zawsze zwracać to samo, generacja hashu musi odbywać się w sposób przewidywalny. Dlaczego? Otóż gdyby było inaczej, a dla jednego klucza dałoby się wygenerować kilka hashy, to powstałby problem w postaci takiej, że nigdy nie moglibyśmy, albo czasem byśmy nie mogli, trafić do dokładnego adresu, gdzie pierwotnie przypisaliśmy wartość. Co to oznacza?

Brak kompletnej losowości sprawia to, że algorytmy hashujące są w jakimś tam stopniu ograniczone. Ograniczone są też wydajnością i czasem jaki komputer może poświęcić na hashowanie, które dzieje się dość często jednak, bez kosztów dla użytkownika. Trzeba było zatem znaleźć kompromis pomiędzy skomplikowaniem funkcji hashującej i jej zasobożernością, czasem wykonywania a unikalnością dostarczanych hashy dla różnych kluczy.

Obecnie mądre głowy jakiś złoty środek wymyśliły, natomiast w dzisiejszych czasach zdarza się operować na zbiorach danych tak dużych, że kolizja hashu się zdarza i funkcja hashująca wygeneruje taki sam hash dla dwóch różnych kluczy, przez co jeden klucz nadpisze drugi. Bardzo, bardzo rzadki przypadek. Natomiast jeśli masz do przetworzenia milion trylionów rekordów, to nagle bardzo rzadkie przypadki mają jakieś 100% szansy się pojawić. 

### Co może być kluczem?

Kluczem w słowniku może być dowolna wartość/zmienna/obiekt, który jest hashowalny. Co to znaczy? A no to, że w swojej definicji zawiera implementację metody `__hash__`. Tak w dużym skrócie. Czyli te obiekty, dla których zaimplementowana została funkcja hashująca, mogą być kluczami. W sumie logiczne, bo jeśli nie mamy metody hashującej dany obiekt to nie policzymy hashu. Nie policzymy hashu z klucza to nie ogarniemy adresu/offsetu. Bez tego niewiadomo gdzie w pamięci przechować wartość. A zatem musimy mieć tę metodę zaimplementowaną. Logiczne.

### Pass by value & Pass by reference

O co tutaj chodzi? O przekazywanie zawartości poprzez referencje lub poprzez wartość. Dokładniej mówiąc chodzi o to, że niektóre obiekty Python skopiuje, tak jak ma to miejsce w przypadku slicingu listy i otrzymania jej kopii w sposób, który wewnętrzne elementy tegoż obiektu uwspólni dla kopii jak i dla oryginału. Troszkę rozpisywałem się już o tym podczas pisania o listach. 

Wydaje mi się, że zostało to tam w miarę jasno wytłumaczone. Teraz tak - dlaczego wspominam o tym w kontekście dictów? Otóż mutowalne typy danych często przekazywane są przez referencje, czyli zamiast samego obiektu, dostajemy referencję doń. Z tego też powodu np. lista nie może być kluczem w słowniku - jest ona mutowalna, przekazywana przez referencję a z tego też powodu nie implementuje metody `__hash__` przez co jest niehashowalna, a zatem implementacja słownika w pythonie, przy próbie ustanowienia nowego klucza będącego listą, wyrzuci błąd.

Przypomnijmy sobie kod, którym ilustrowałem przekazywanie przez referencje vs przez wartość.

```python
>>> pass_by_reference = [[1,2,3], 1, 2, 3]
>>> new_pass_by_reference = pass_by_reference[:]
>>> pass_by_reference
[[1, 2, 3], 1, 2, 3]
>>> new_pass_by_reference
[[1, 2, 3], 1, 2, 3]
>>> pass_by_reference is new_pass_by_reference  # dwie różne listy
False
# pierwszym elementem listy jest inna lista
# listy są mutowalne i przekazujemy je przez referencje
>>> pass_by_reference[0]  
[1, 2, 3]
# modyfikujemy tutaj drugi element tej wewnętrznej listy z oryginału
>>> pass_by_reference[0][1] = "test"
>>> pass_by_reference[0]
[1, 'test', 3]
# jakimś sposobem lista w kopii też uległa zmianie
>>> new_pass_by_reference
[[1, 'test', 3], 1, 2, 3]
>>> new_pass_by_reference[0]
[1, 'test', 3]
```

Warto na to uważać, zwłaszcza przy np. wybieraniu argumentów dla funkcji czy ustanawianiu wartości domyślnych. Pass by reference -> zwracamy adres i tam następuje modyfikacja danego obiektu. Pass by value -> zwracamy samą wartość i następuje jej 'skopiowanie' na świeżo zamiast modyfikować zmienną pod danym adresem, otrzymujemy nową. Kolejny przykład:
```python
student = {"Putler": 10}
def test(student):
    new = {"Wołodia": 20, "CzłowiekMałpa": 21}
    student.update(new)
    print("Wewnątrz funkcji", student)
test(student)
print("Poza funkcją:", student)
```

Jak widać wyżej dict przekazywany jest poprzez referencje, czyli adres tak jakby. Python zatem idzie pod dany adres i modyfikuje obiekt przez co zmiany są rozpowszechnione w miejscach, gdzie niewprawiony programista mógłby się nie spodziewać. W przypadku przekazania wartości sprawa ma się inaczej. Oryginalny obiekt nie jest modyfikowany, jedynie jego kopia.

```python
>>> student_name = "NAFO"
>>> def test(name_name):
...     student_name = name_name + " <3"
...     print("Wewnątrz: ", student_name)
>>> student_name
'NAFO'
>>> test(student_name)
('Wewnątrz: ', 'NAFO <3')
>>> student_name
'NAFO'
```

Nie wiem, czy ma to sens, może wrócimy do tego jeszcze. Przeanalizuj i poszukaj troszeczkę w necie samodzielnie na ten temat by dodatkowo rozjaśnić sytuację.

### Kopia płytka i kopia głęboka a klucze w słowniku

Mamy te całe przekazywanie referencji, wartości etc. Pomówmy teraz zatem o kopiach płytkich i głębokich. Krótko bo krótko, ale warto wspomnieć.

Kiedy użyliśmy slicingu jako metody kopiowania listy, otrzymaliśmy tak zwaną płytką kopię tejże listy. Co to znaczy płytką? Mianowicie skopiowany został tylko początkowy obiekt, obiekt z samej góry. Wszystko co w środku a co było przekazywane przez referencje, nie zostało zduplikowane. Skopiowane zostały jedynie referencje. To jest płytka kopia.

Głęboka kopia to kopia, gdzie interpreter 'wchodzi' do obiektu, który kopiujemy i kopiuje wszystko przez wartość, nie przez referencje. Sprawia to, że otrzymujemy faktyczny, samodzielny i niezależny duplikat danego obiektu a nie tylko jego 'top levelu' jak w przypadku kopii płytkiej.

Czasami potrzebne. Warto wiedzieć, gdyż w niektórych przypadkach myślimy, że mamy dwa różne obiekty po skopiowaniu używając kopii płytkiej, modyfikujemy jeden obiekt a tu bam, zmiany w obu. Potrafi to spowodować naprawdę brzydkie do debugowania błędy. Nie polecam.

### dict.values() keys() items()

Zwróć uwagę na te trzy metody. Pobaw się nimi i podsumuj swoje wnioski. Ja zwrócę tylko uwagę na jedną rzecz.

Jakiego typu obiekty zwracają funkcje dict.keys(), dict.values(), dict.items()? dict.items() - oczywiste. Lista tupli. Ale tak nie do końca. Bo jak się bliżej przyjrzeć to jest to klasa dict_items, która nie do końca jest listą – trochę to taka rozszerzona klasa, bo umożliwia nam wykonywanie na niej operacji takich, jak na setach. Podobnie z keys() i values(). Czyli na obiektach zwracanych przez te funkcje można wykonywać operacje sumy, różnicy czy części wspólnej ze zbiorów. Tldr – te funkcje zwracają iterable set-like object.

### Przykłady podstawowych operacji na słownikach

```python
In [17]: dir(dict)
Out[17]:
[(...)
 'clear',
 'copy',
 'fromkeys',
 'get',
 'items',
 'keys',
 'pop',
 'popitem',
 'setdefault',
 'update',
 'values']
In [18]: some_dict = {"NAFO": "OK", "SS": "NOT OK"}
""" dict_values to set-like obiekt, na którym
można wykonywać takie operacje jak na zbiorach"""
In [19]: some_dict.values()  
Out[19]: dict_values(['OK', 'NOT OK'])
# dict_keys podobnie
In [20]: some_dict.keys()
Out[20]: dict_keys(['NAFO', 'SS'])

In [21]: some_dict.items()
Out[21]: dict_items([('NAFO', 'OK'), ('SS', 'NOT OK')])
```



## Zbiory

### Krótka charakterystyka

Czym są zbiory? Analogicznie jak w matematyce. To taka jakby lista, ale bez powtórzeń. Przynajmniej pozornie. Pod spodem jest nieco inaczej, bo pod spodem zbiorom/setom bliżej do hash mapy. W sumie to jest niejako hashmapa. Po co na co i dlaczego? Otóż zadajmy sobie pytanie, jakie są atrybuty zbiorów. Każdy element występuje tylko raz. Niekoniecznie zachowana kolejność insercji. Zaczyna brzmieć znajomo? Yup. Sety to tak jakby hashmapy gdzie wartości są też i kluczami niejako.

Jaka jest zaleta zbioru? Pierwsze to deduplikacja elementów -> każdy występuje dokładnie raz. Możemy wyciągnąć 'statystyki' z danego elementu, ile razy został dodany do seta, ale w samym secie pojawi się on tylko raz. Druga jest wydajnościowa. 

### Przeszukanie szybsze niż na warszawskiej Woli

Wyszukiwanie/przeszukiwanie w zbiorze ma złożoność obliczeniową na poziomie O(1) - czas stały. Co to znaczy? Niezależnie od rozmiaru zbioru by sprawdzić przynależność danego elementu do zbioru wykonujemy operację, która cechuje się stałym czasem wykonania niezależnym od rozmiaru. Czyli nawet dla bardzo bardzo dużych zbiorów, jeśli zmieszczą się w pamięci, mega szybko możemy stwierdzić, czy znajdują się one w danym zbiorze. 

W przypadku listy nie ma aż tak łatwo, zwłaszcza jeśli dane są nieposortowane.

Dlaczego tak jest? Otóż przez to, że pod spodem jest niejako hashmapa, by sprawdzić czy element przynależy do zbioru wystarczy jedynie policzyć hash tegoż elementu a potem sprawdzić czy wszystko się zgadza. Stąd O(1) niezależnie od wielkości zbioru.

To zaś wymusza nam ograniczenia odnośnie tego, co możemy do zbioru wrzucić. Jakie? Takie same jak przy kluczach w słownikach.

Do tego zbiór pythonowy obsługuje też podobne operacje jak zbiór matematyczny. Koniunkcje, alternatywę, różnicę. Zwykła lista nie wszystko z tego potrafi ogarnąć. 

### Przykłady podstawowych operacji na zbiorach

```python
In [22]: some_set = {1,2,3,4}
In [23]: another_set = {3, 4, 5}
In [24]: some_set
Out[24]: {1, 2, 3, 4}
In [25]: some_set | another_set
Out[25]: {1, 2, 3, 4, 5}
In [26]: some_set & another_set
Out[26]: {3, 4}
In [27]: some_set - another_set
Out[27]: {1, 2}
In [30]: dir(set)
Out[30]:
[(...),
 'add', 'clear', 'copy',
 'difference', 'difference_update', 'discard', 'intersection',
 'intersection_update', 'isdisjoint', 'issubset', 'issuperset',
 'pop', 'remove', 'symmetric_difference',
 'symmetric_difference_update', 'union', 'update']
In [31]: some_set.add(7)
In [32]: some_set
Out[32]: {1, 2, 3, 4, 7}
In [33]: some_set.add(7)
In [34]: some_set
Out[34]: {1, 2, 3, 4, 7}

```

## Podsumowanie

Uf, nareszcie. Kawał tekstu, co? A to tylko wybrane z Pythonowych typów.

Warto je dobrze znać, pobawić się z nimi i oswoić. Dlaczego? Otóż w standardowej bibliotece Pythona jest już tyle cudeniek, tyle różnych rzeczy, które ułatwiają życie, że głowa mała. Szkoda wymyślać koło na nowo i implementować coś samemu, skoro język udostępnia swoją wersję.

Mało tego, implementacja od zera jest często też bezsensowna z pewnego bardzo ważnego względu. Otóż twoja własna implementacja może być dziurawa, bo sprawdzasz ją ty, może ludzie na Code Review i tyle. Natomiast jeśli idzie o kod, który znajduje się w standardowej bibliotece Pythona i implementacje kontrybutorów, to sprawa ma się tak, że jest to kod przetestowany i przejrzany przez tysiące osób. Wpadki się zdarzają, to prawda. Natomiast gdzie prędzej znajdziemy buga? W kodzie, który przejrzało tysiące osób, który jest przetestowany w milionach produkcyjnych aplikacji jak i pokryty wieloma testami? Czy w kodzie, który przejrzałeś ty i być może twój zespół? Nie ma porównania. 

Do tego dam sobie rękę uciąć, wierząc w to, że dzięki wysiłkowi tysięcy kontrybutorów kod z biblioteki standardowej Pythona będzie lepiej zoptymalizowany. Korzystaj z tego, co zbudowano i nie wynajduj koła na nowo tworząc własne naiwne implementacje algorytmu sortowania czy coś. Czasami zdarza się taka potrzeba, prawda, ale wątpię, byś ty takowe miewał jako junior wannabe. 

Dlatego koniecznością jest dobra znajomość biblioteki standardowej Pythona. Własne implementacje zostaw na cele związane z nauką czy zabawą, by zrozumieć jak coś działa. W kodzie produkcyjnym starajmy się tego unikać zaś na rzecz sprawdzonych rozwiązań z biblioteki standardowej.

To nie tylko ułatwia zadanie, ale sprawia, że kod  będzie solidniejszy, bardziej zoptymalizowany i prawdopodobnie szybciej dostarczony. Łatwiej poskładać coś z gotowych klocków niż samemu budować dom zaczynając od wydobycia gliny i wypalenia cegieł. 

## Pytania i zadania

1. Czy w Pythonie jest dynamiczne typowanie? A może statyczne?
2. Co to oznacza? Jakie są tego wady, jakie zalety. 
3. Wymień podstawowe typy danych w Pythonie.
4. A te bardziej złożone? 
5. Jakie są różnice pomiędzy podstawowymi typami liczbowymi?
6. Co to znaczy, że wartość jest `truthy` albo `falsy` w Pythonie? Podaj przykłady z rozróżnieniem co jest czym.
7. Jakie są sposoby deklarowania tekstu w Pythonie?
8. Co to jest znak ucieczki i dlaczego go używamy?
9. Jakie funkcje ułatwiające przeliczanie znaków na liczby, na inne kodowania, o których wspomniałem?
10. Przygotuj artykuł w którym opiszesz o co chodzi z którą funkcją, po krótce zcharakteryzujesz każdy z podstawowych typów. Podasz przykłady dla których funkcje nie działają i domysły dlaczego. Docelową audiencją są inne osoby początkujące. Niech będzie to rozbudowany artykuł pełny twoich osobistych uwag a nie tylko Copi Pasta z dokumentacji. Podaj żywe przykłady. 
11. Przygotuj podsumowującą listę dla znanych ci podstawowych typów danych w których przedstawisz i po krótce opiszesz jakie poszczególne typy mają metody/atrybuty i co dana metoda robi. Pomiń te, które zaczynają się od `__`. Jakiego polecenia musisz tu użyć?
12. To samo co w 11., ale dla typów złożonych. Bardzo dokładnie opisz. Artykuły możesz połączyć. Skup się na pokazaniu praktycznego użycia. Okomentuj kod i pokaż przykłady inne niż tutaj.
13. Artykuły z 12. i 11. podeślij na olafgorski@pm.me a ja je sprawdzę i dam feedback :) 
14. Przygotuj tabelkę porównawczą: lista vs krotka vs zbiór.
15. Poeksperymentuj z naprawdę dużymi liczbami. Opisz swoje wnioski.
16. Stwórz kod, który pobierze liczbę od użytkownika a następnie powie, czy jest parzysta, czy nie. Jak pobrać coś od usera? Wygooluj jeśli nie pamiętasz.
17. Utwórz stringa a potem zamień jego ostatnią literę z pierwszą.

Pamiętaj, że Twoje odpowiedzi możesz wrzucić na GH o tutaj -  https://github.com/grski/junior-python-exercises, a sprawdzę twoje rozwiązania i dam feedback. Więcej o tym podrozdziale 'Część interaktywna'.

\pagebreak