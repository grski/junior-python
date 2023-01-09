\pagebreak

# Przykładowe pytania i zadania

To, z jakimi pytaniami się spotkasz, zależy ściśle od tego, co umieścisz w swoim CV, dla przykładu podam ci tutaj listę pytań, z którymi ja się spotkałem na rozmowach rekrutacyjnych. Dodatkowo dorzucę kilka od siebie. Wszystkie, przynajmniej w kilku słowach, omówię.

## Django

1. Distinct w Django model

1. Django middleware - czym jest, gdzie się używa
   Odp: To kawałek kodu, który na wejściu i przy wyjściu przetwarza naszego requesta w jakiś sposób. Na tym poziomie handlujemy np. autentykacje.

1. Django droga requesta
   Odp: Middleware -> router -> views -> modele/kod/cokolwiek/ -> znowu middleware(opcjonalnie) -> klient

1. Django select related

1. Jak działają migracje w Django

1. Czy makemigrations potrzebuje połączenia z bazą danych?\
    Odp: Nie, nie potrzebuje. Django sobie porównuje modele z ostatnio zapisanym stanem (chyba haszami) i jeśli wykryje zmiany, to zabiera się do działania.

1. Czy migrate potrzebuje połączenia z bazą danych?\
    Odp: Tak – wprowadza zmiany do bazy, więc jak najbardziej.

1. Czy możliwym jest zaimplementowanie logowania/autentykacji bez sesji?\
    Odp: Jak najbardziej. JWT lub Cookies chociażby.

1. Różnica pomiędzy Flaskiem a Django\
    Odp: Wygoogluj sobie, a najlepiej to sprawdź sam i porównaj, bo to banał.

1. Różnica między Django a FastAPI

  Odp: Jak wyżej.

1. Ustawianie unique_together na atrybucie modelu, który posiada `null=True`. Czy django na to pozwala? Jakie jest zagrożenie.
   Odp: w bazie danych null == null jest False, zatem (null, 1) i np. (null, 1) będą dla bazy danych unikalne. Dla pythona też.

## Python

1. 3 ulubione featury Pythona 3 względem Pythona 2
     Odp: Tutaj odpowiedzi oczywiście mocno indywidualne, więc nie podam jakiegoś wzorca, ale ja, o ile pamiętam, wymieniłem: f-stringi, unicode jako domyślne kodowanie, operator przypisania w wyrażeniach (walrus).

1. Co zmieniłbyś w Pythonie – podaj przykład nowego PEP'
     Odp: Kwestia mocno indywidualna. Ja rzuciłem coś o tym, by wywalić GIL’a. A jak już mówimy o GIL’u, to pora na klasyczne pytanie każdej rekrutacji na Python deva.

1. Co to GIL?
     Odp: Global Interpreter Lock, a to, czym jest, to już opisywałem, zatem powinieneś wiedzieć. W skrócie powoduje swego rodzaju blokadę, która sprawia, że tylko jeden wątek może się wykonywać w danej instancji interpretera naraz.

1. Wymień rodzaje comprehensions w Pythonie.
     Odp: Chodzi o np. List Comprehensions, Set Comprehensions, Dict Comprehensions

1. Podaj przykłady powyższych, po jednym na rodzaj.
     Odp: Przykładami mogą być... 

     ```python
     list_comprehension = [x for x in range(10)]
     dict_comprehension = {x: x**2 for x in range(10)}
     set_comprehension = {x for x in range(10)}
     set_comprehension_variation = set(x for x in range 10)
     tuple_comprehension = tuple(x for x in range(10) if x % 2)
     ```

     

1. Jakie są różnice między tuplą(krotką) a listą?
     Odp: Główna różnica to fakt tego, że jedną z nich można mutować, drugą nie – listę można zmieniać po utworzeniu, tuplę, czy jak kto woli po polsku, krotkę, już nie – po zainicjowaniu już jej nie zmienisz. Poza tym jest  duża różnica w wydajności i implementacji ‘pod spodem’. Z racji tego, że tupla jest niemutowalna, to interpreter w chwili inicjalizacji ma dokładną świadomość tego, ile będzie ona zajmowała, zatem alokuje dla niej tylko tyle pamięci, ile potrzebuje i ani grama więcej. Lista natomiast podczas inicjalizacji, jest tworzona w taki sposób, że zawsze alokuje się więcej pamięci niż potrzeba na faktyczne dane z listy użytkownika, by potem operacje dodania czegoś do listy działały szybciej. Jeśli tworzysz listę np. 50 elementową, to pod spodem okazuje się, że twoje lista ma zaalokowane miejsce nie na 50 elementów, a na np. 90. Dokładnych liczb możesz dowiedzieć się sam. 

1. Czym są generatory i czym się różnią od list? 
       Odp: Generatory to coś, co ułatwia nam operowanie na dużych ilościach danych, gdyż, są to takie swego rodzaju ‘funkcje’, które zamiast ładować jakiś cały określony data set do pamięci, przetwarza wartości po kolei i yield’uje kolejne wartości. Od listy różnią się tym, że lista ładuje wszystko do pamięci, generator już nie, upraszczając w dużym stopniu.

1. Czy w Pythonie można programować funkcyjnie?
     Odp:  Tak. Jest to możliwe – Python jest językiem umożliwiającym programowanie w wielu paradygmatach takich jak funkcyjny, zorientowany obiektowo, imperatywny, proceduralny. Można by się sprzeczać, czy to programowanie byłoby ‘czystym’ (raczej nie) funkcyjnie i tak dalej, ale samo w sobie jest to możliwe. Niezbyt popularna opcja i niezbyt promowana. Ogółem niektórzy krzywo patrzą na to połączenie.

1. Enkapsulacja w Pythonie - czy da się?
     Odp: I tak i nie. Z jednej strony w Pythonie brak takich modyfikatorów dostępu jak private czy public, ale mamy umowne określenia, które powodują, że np. zmienne czy funkcje zaczynające się od podkreślenia ‘_’, są raczej prywatne i nie powinno się ich używać poza daną klasą. Niemniej jest to tylko konwencja, a nie element języka, nic nie będzie ci broniło używać metody z podkreśleniem wszędzie.

1. Jak rozwiązać problem GIL'a?\
       Odp: Stackless Python czy też inne implementacje lub wykorzystanie w naszym modelu współbieżności procesów zamiast wątków.

1. Co jest pod spodem dicta, jaka struktura danych teoretyczna?
      Odp: Hash map. 

1. Jak przebiega access do elementów dicta? 
      Odp: Na podstawie klucza liczony jest hash za pomocą określonego algorytmu. Z tego hasha uzyskuje się z kolei offset wskaźnika do referencji.

1. Zachowanie kolejności dodania itemów do słownika w Pythonie, czym?
      Odp: W Pythonie < 3.7: OrderedDict() z collections. W >= 3.7 sam dict() domyślnie zachowuje kolejność.

1. Różnice między listą a setem.
      Odp: W liście elementy mogą się powtarzać. W secie nie. Na secie możemy wykonywać pewne operacje, których na listach już nie możemy – podobnie jak na normalnych zbiorach w matematyce – suma, część wspólna, różnica. W najprostszym przypadku można myśleć o secie jak o liście bez powtórzeń. Warto też pamiętać, że dane w secie są nieuporządkowane z założenia, więc set kompletnie nie nadaje się do porządkowania elementów.

1. Jakiego typu obiekty zwracają funkcje dict.keys(), dict.values(), dict.items()?
      Odp: Dict.items() - oczywiste. Lista tupli. Ale tak nie do końca. Bo jak się bliżej przyjrzeć to jest to klasa dict_items, która nie do końca jest listą – trochę to taka rozszerzona klasa, bo umożliwia nam wykonywanie na niej operacji takich, jak na setach. Podobnie z keys() i values(). Czyli na obiektach zwracanych przez te funkcje można wykonywać operacje sumy, różnicy czy części wspólnej ze zbiorów. Tldr – te funkcje zwracają iterable set-like object.

1. Operatory bitowe w Pythonie. Jakie znasz, do czego służą?
      Odp:  << i >> , przesunięcie bitowe w lewo i w prawo
      & - bitowa koniunkcja, czyli ‘i’
      | - bitowa alternatywa, czyli lub
      ~ - bitowe negacja, czyli ~x = -x – 1
      ^ - bitowa alternatywa wykluczająca

1. Kiedy używać list comprehension, a kiedy normalną pętlą krokową?
      Odp:  Tam, gdzie możemy, powinniśmy używać list comprehensions, gdyż są one czytelniejsze i wydajniejsze, jeśli chodzi o czas wykonania, ponieważ są optymalizowane przez interpreter i lecą z prędkością gdzieś tam w jakimś stopniu zbliżoną do prędkości C, natomiast zwykłe for loopy są wykonywane normalnie przez interpreter z prędkością normalnego kodu Pythona. Jednak jeśli chcemy wykonać coś, co ma efekty uboczne lub skomplikowaną logikę, czasem warto jednak zostać przy zwykłych pętlach.

1. Jakie są różnice między pętlą for i while w Pythonie?
      Odp: Głównie składniowe oraz wydajnościowe. Pętla while będzie zawsze wykonywana przez interpreter Pythona, natomiast pętla for użyta w list comprehension, chociażby, może zostać zoptymalizowana i śmigać o wiele szybciej.

1. Czym jest iterator a iterable? Różnica iterator a iterable.

1. `float("NaN") == float("NaN")` jaki wynik?

1. `True is True` a tu?

1. `1 is 1` a tu?

1. Napisz program, który sprawdzi, czy podany przez użytkownika ciąg znaków jest palindromem (ciągiem, który czytany od początku i od końca brzmi tak samo).

1. Napisz program, który zliczy, ile razy dana cyfra występuje w podanym przez użytkownika ciągu cyfr.

1. Napisz funkcję, która przyjmie listę liczb i zwróci ich sumę oraz średnią arytmetyczną.

1. Napisz program, który utworzy słownik zawierający statystyki dotyczące liter (ile razy dana litera występuje w tekście).

1. Napisz program, który wczyta plik CSV i wyświetli jego zawartość w formie tabeli.

1. Napisz program, który zaimplementuje algorytm sortowania przez scalanie.

1. Napisz program, który zaimplementuje algorytm sortowania szybkiego (QuickSort).

1. Napisz program, który zaimplementuje algorytm Dijkstry do znajdowania najkrótszych ścieżek w grafie.

## Git
1. Czym różni się merge od rebase?
Odp: Merge tworzy nam ‘merge commit’, natomiast ‘rebase’ niejako wkleja nam commity z mergowanego brancha. Poza tym, używając rebase, można nieźle zepsuć git loga. Co jest lepsze? Zależy kogo zapytać, są różne szkoły.
1. Różnice między Gitem a GitHubem.
Odp: Git to narzędzie – system kontroli wersji, natomiast GitHub to serwis, na którym możemy hostować swoje repozytoria Git’a i ogółem współpracować z innymi.
1. Co robi git stash? A git stash pop?


## Http/Rest
1. Czym jest REST?
   Odp: googlaj
1. Co odpowiada za to, jakiego typu treści można przesyłać na/z serwera?
   Odp: Nagłówki, konkretniej chodzi o content-type.
1. Gdzie lecą parametry w requeście?
   Odp: W urlu. ? i &.
1. 403 vs 401
   Odp: Forbidden vs unauthorized. Różnica kiedy user jest niezalogowany czyli nie ma dostępu vs jest zalogowany ale nie ma pozwolenia.
1. Kody responsow http 1xx 2xx 3xx 4xx 5xx
   Odp: Zajrzyjcie na wiki.
1. Czym jest jwt?
   Odp: JWT to po prostu sposób autentykacji, gdzie mamy określony trzy częściowy token wygenerowany za pomocą jakiegoś sekretnego klucza/certyfikatu, który zawiera określony payload. 
1. Czy możliwa jest już autentykacja na poziomie load balancera tak, żeby później aplikacja nie musiała tego robić dodatkowo?
   Odp: Jeszcze jak. JWT ftw.
1. Sposoby autentykacji requesta: basic auth i tokena - opisz i zcharakteryzuj czym się różnią.
   Odp: Googlaj
1. Skąd serwer bierze username i password przy basic auth?
   Odp: Nagłówek. Jaki?
1. Skąd przeglądarka wie, że daną odpowiedź trzeba wyświetlić jako json a nie np. plaintext?
   Odp: Znowu - CONTENTY-TYPE
1. Różnica miedzy PUT a PATCH.
    Odp: Jedno wymaga podanie wszystkich pól serializera, drugie nie. Dlaczego? Która metoda wymaga wszystkich pól, która metoda zaś nie?
1. Dostępne metody/verby HTTP.
    Odp: Googlaj.

## Bazy danych
1. Czym jest join w sql, jak działa, przykład
1. Normalizacja bazy danych - co to, z czym się to je.
1. Rodzaje baz danych. Relacyjne i nierelacyjne, trochę o nich.

## Ogólne koncepty programowania
1. Czym jest OOP.
1. Czym jest SOLID - wymień chociaż jedną
1. Załóżmy, że wpisuję coś w okno przeglądarki i klikam enter by przejść na daną stronę. Co się wtedy dzieje pod spodem?

## Struktury danych
1. Czym jest drzewo/tree?
1. Zbalansowane drzewo binarne?
1. Jak działa hashmapa/słownik?
1. A zbiór?

## Kamień papier nożyce

1. Napisz funkcję rock_paper_scissors(), która zasymuluje losowy przebieg gry w kamień papier nożyce i następnie wyświetli, który gracz, p1 czy p2, wygrał daną rundę. Czy zawsze ktoś wygrywa? Może być remis? Spróbuj uczynić swoje rozwiązanie jak najkrótszym. Spróbuj nie korzystać w ogóle z ifów. Tak, da się to zrobić bez tego.
   Mnie udało się napisać samą funkcję symulującą pojedyńczy losowy przebieg gry w 5 linijkach kodu łącznie, bez ifa.

2. Teraz dopisz kod, która wywoła taką symulacje 10 razy i wyprintuje jej wynik na wyjście.

Przykład mojego rozwiązania:


```python
import random as ra
```


```python
def rock_paper_scissors():
    gestures = ['rock', 'paper', 'scissors'] # order here is important
    p1, p2 = ra.randint(0, 2), ra.randint(0, 2)
    return "P1: {0}, x P2: {1}, Result: {2}".format(
        gestures[p1], 
        gestures[p2],
        {0: 'tie', 1: 'p1', 2: 'p2'}[(p1-p2)%3]
    )
```


```python
for i in range(10):
    print(rock_paper_scissors())
```

## Operacja na liczbach

Tutaj dwa ćwiczonka do zrobienia.

1. Jak można zaimplementować w Pythonie mnożenie przez 2, bez użycia operatora mnożenia, potęgowania, funkcji pow, sqrt?
2. Co z dzieleniem przez dwa biorąc pod uwagę podobne obostrzenia, jak wyżej?
3. Napisz funkcję is_prime(number), sprawdzającą czy podana liczba jest pierwsza.
4. To co wyżej, ale w jednej linijce kodu.


## Statystyki z logów
Tutaj polecimy po angielsku. Treść zadania jak i potencjalne rozwiązanie niżej. Całość można jeszcze uprościć i zrefaktorować, natomiast podaję tutaj rozwiązanie, które naskrobałem na szybko podczas rekrutacji na żywo. 30 minut. 

1. You are given a large log file which stores user interactions with an application. The entries in the log file follow the following schema: `{userId, timestamp, actionType}`. Calculate the average session time across all users. Assume that data yet get is valid and not sorted in any way. Assume that number of records that are `opens` will be equal to `closes`.
2. What if we want to modify the code to also calculate average session time per user?

```python
from collections import defaultdict
from enum import Enum


# User level 1 -> 1512, 2-> 17
events = [
    [1, 1435459573, "Close"], [1, 1435456566, "Open"],
    [1, 1435462567, "Open"], [1, 1435462584, "Close"],
    [1, 1435462567, "Open"], [1, 1435462584, "Close"],
    [2, 1435462567, "Open"], [2, 1435462584, "Close"]
]


class ActionTypeEnum(Enum):
    OPEN = "Open"
    CLOSE = "Close"

    @classmethod
    def opposite(cls, action_type: str) -> str:
        if action_type == cls.OPEN.value:
            return cls.CLOSE.value
        return cls.OPEN.value

class Event:
    def __init__(self, user_id, timestamp, action_type):
        self.user_id = user_id
        self.timestamp = timestamp
        self.action_type = action_type

    def calculate_difference(self, second_event):
        if self.action_type == ActionTypeEnum.CLOSE.value:
            return self.timestamp - second_event.timestamp
        return second_event.timestamp - self.timestamp


def calculate_avg_session_time(events: list) -> tuple:
    time_sum, number_of_sessions = 0, 0
    user_level_sum = defaultdict(int)
    user_level_matches = defaultdict(int)

    user_time_mapping: dict = defaultdict(lambda: defaultdict(list))
    for event in events:
        wrapped_event: Event = Event(*event)
        opposite_action = ActionTypeEnum.opposite(wrapped_event.action_type)
        user_id: int = wrapped_event.user_id
        if first_user_record := user_time_mapping[user_id][opposite_action]:
            first_event = first_user_record.pop()
            user_session_time = wrapped_event.calculate_difference(first_event)
            time_sum += user_session_time
            user_level_sum[user_id] += user_session_time
            user_level_matches[user_id] += 1
            number_of_sessions += 1
            continue
        user_time_mapping[user_id][wrapped_event.action_type].append(wrapped_event)
    user_level_average = {
        user_id: user_level_sum[user_id] / user_level_matches[user_id] 
        for user_id in user_level_sum.keys()
    }
    return time_sum / number_of_sessions, user_level_average
print(calculate_avg_session_time(events=events))
# (1213.0, {1: 1512.0, 2: 17.0})

```

Zadanie bezczelnie podwędzone z rekrutacji.

## Statystyki zapytań

Stwórz klasę, która będzie przechowywać całkowity czas egzekucji danego zapytania. Jako dane wejściowe dostaniesz rekordy, które będą zawierały id zapytania oraz czas trwania. Rekordy mogą być częściowe, czyli jedno id może mieć wiele rekordów. Powinno się takie wartości sumować razem.

Dodatkowo zaimplenetuj w tejże klasie metodę `get_top_k_records`, która zwróci zadaną liczbę zapytań o najdłuższym czasie egzekucji.

```python
from collections import defaultdict
from typing import Iterable

events = [
  {"id": 2, "partial_execution_time": 10},
  {"id": 1, "partial_execution_time": 15},
  {"id": 1, "partial_execution_time": 12},
  {"id": 3, "partial_execution_time": 25},
  {"id": 3, "partial_execution_time": 10},
  {"id": 4, "partial_execution_time": 15},
]

class QueryStats:
  def __init__(self):
    self.query_execution_times: dict = defaultdict(int)
  
  def add(self, event: dict) -> dict:
    self.query_execution_times[event["id"]] += event["partial_execution_time"]
    return event
  
  def get_top_k_records(self, k: int) -> Iterable:
    return sorted(self.query_execution_times.items(), key=lambda record: record[1], reverse=True)


query_stats = QueryStats()
for event in events:
  query_stats.add(event)

print(query_stats.get_top_k_records(5))
```

Zadanie bezczelnie podwędzone z rekrutacji.

## Książka zleceń

Zaimplementuj Książkę Zleceń (ang. Order Book), która obsługuje zlecenia zwykłe, z Limitem Ceny (ang. Limit Order). 

Następnie dodaj obsługę zleceń typu Góra Lodowa (ang. Iceberg Order). Co to jest i z czym to się je poczytać możecie w dokumentacjach technicznych giełd. Dla przykładu: SETSmm and Iceberg Orders, SERVICE &TECHNICAL DESCRIPTION z London Stock Exchange. Albo pogooglajcie.

Dane wczytujemy ze standardowe wejścia kolejne zlecenia i na bieżąco aktualizuje książkę. Jeśli zachodzi transakcja to wypisujemy ją na standardowe wyjście. Po dodaniu każdego zlecenia wypisujemy zaktualizowaną książkę na standardowe wyjście.

### Format danych wejściowych

JSON. Każde zlecenie ma pole "type" oraz "order". Type zawiera typ zlecenia - Icebergo lub Limit. Order to dane o zleceniu.

- "direction" typ zlecenia ("Buy" albo "Sell"), 
- "id" unikalny identyfikator zlecenia (dodatnia liczba całkowita),
- "price" cena (dodatnia liczba całkowita)
-  "quantity" wielkość zlecenia (dodatnia liczba całkowita).

Zlecenia typu Góra Lodowa mają dodatkowe pole - `peak`, oznacza on wierzchołek tegoż zlecenia. 

Zakładamy, ze dane wejściowe są poprawne. 

```json
{"type": "Limit", "order": 
{"direction": "Buy", "id": 1, "price": 14, "quantity": 20}}
{"type": "Iceberg", "order": 
{"direction": "Buy", "id": 2, "price": 15, "quantity": 50, "peak": 20}}
{"type": "Limit", "order": 
 {"direction": "Sell", "id": 3, "price": 16, "quantity": 15}}
{"type": "Limit", "order": 
 {"direction": "Sell", "id": 4, "price": 13, "quantity": 60}}
```

### Format danych wyjściowych

Jak już wczytamy informacje o nowym zlecenu i bedziemy chcieli wypisać zaktualizowany stan książki zleceń, to obiekt JSON, jaki powinniśmy wyprintować powinien mieć następujące właściwości/atrybuty: `buyOrders` oraz `sellOrders`. Każde zlecenie powinno zawierać pola "id", "price" oraz "quantity". Posortowane według ceny. Zlecenia kupna nierosnąco. Sprzedaży niemalejąco. Jeśli cena taka sama to priorytet bierze czas dodania zlecenia. Przykład:

```json
{"buyOrders": [{"id": 2, "price": 15, "quantity": 20}, 
               {"id": 1, "price": 14, "quantity": 20}],
"sellOrders": [{"id": 3, "price": 16, "quantity": 15}]}
```

Przykładowa sesja (sory za brzydkie formatowanie, skopiuj sobie i popraw samodzielnie):

```json
{"type": "Limit", "order": 
 {"direction": "Buy", "id": 1, "price": 14, "quantity": 20}} 
{"buyOrders": [
    {"id": 1, "price": 14, "quantity": 20}], "sellOrders": []
}
{"type": "Iceberg", 
 "order": {
     "direction": "Buy", "id": 2, "price": 15,
     "quantity": 50, "peak": 20
 }}
{"buyOrders": [
    {"id": 2, "price": 15, "quantity": 20},
    {"id": 1, "price": 14, "quantity": 20}
], 
 "sellOrders": []}
{"type": "Limit", 
 "order": {"direction": "Sell", "id": 3, "price": 16, "quantity": 15}}
{"buyOrders": [
    {"id": 2, "price": 15, "quantity": 20}, 
    {"id": 1, "price": 14, "quantity": 20}
],
"sellOrders": [
    {"id": 3, "price": 16, "quantity": 15}]
} 
{"type": "Limit", "order": 
 {"direction": "Sell", "id": 4, "price": 13, "quantity": 60}}
{"buyOrders": [{"id": 1, "price": 14, "quantity": 10}],
 "sellOrders": [{"id": 3, "price": 16,"quantity": 15}]} 
{"buyOrderId": 2, "sellOrderId": 4, "price": 15, "quantity": 20} 
{"buyOrderId": 2, "sellOrderId": 4, "price": 15, "quantity": 20} 
{"buyOrderId": 2, "sellOrderId": 4, "price": 15, "quantity": 10} 
{"buyOrderId": 1, "sellOrderId": 4, "price": 14, "quantity": 10}

```

Inny przykład:
```json
{"type": "Iceberg", "order": 
 {"direction": "Sell", "id": 1, "price": 100, "quantity": 200,
"peak": 100}}
{"type": "Iceberg", "order":
{"direction": "Sell", "id": 2, "price": 100, "quantity": 300,
"peak": 100}}
{"type": "Iceberg", "order": 
{"direction": "Sell", "id": 3, "price": 100, "quantity": 200,
"peak": 100}}
{"type": "Iceberg", "order": 
{"direction": "Buy", "id": 4, "price": 100, "quantity": 500,
"peak": 100}}
daje nam
{"sellOrders": [{"id": 3, "price": 100, quantity: 100}, 
                {"id": 2, "price": 100, quantity:
100}], "buyOrders": []}
```

Przykładowe rozwiązanie na moim githubie - [github.com/grski](https://github.com/grski)

Zadanie bezczelnie podwędzone z rekrutacji.

Nie umieszczam tutaj gdyż jest ono za długie.

## Skracacz adresów

W tym zadaniu stwórz proszę serwis skracający URLe. Użyj Pythona i dowolnego frameworka. Np. django czy fastapi.

Czyli serwis, który skraca urle np. z https://codesubmit.io/library/react zrobi http://short.est/GeAi9

Analogicznie odwrotne działanie też zachodzi.

- Język: **Python**
- Framework: **dowolny**
- Endpointy:
  - /encode - pełny URL koduje na skrócony
  - /decode - skrócony odkodowuje na pełny.

-   Oba zwracają JSON
-   To jak bedzie odbywało się kodowanie to detal implementacyjny. Wybierz jak uważasz. Byle dało się zakodowac a potem odkodować. Nie musisz doklejac bazy danych - możemy trzymać w pamięci.

-   Stwórz dokumentację jak uruchomić i używać.
-   Napisz testy.
-   Korzystaj z GITa i za pomoca historii commitów pokaż swoje rozumowanie
-   Kod pisz tak, jakby miał iść na produkcję. Czyściutki, elegancki, piękniutki.

Przykładowe rozwiązanie na moim githubie - [github.com/grski](https://github.com/grski)

Zadanie bezczelnie podwędzone z rekrutacji.

Nie umieszczam tutaj gdyż jest ono za długie.

## Generator statycznych stron

Co to znaczy? Zerknij w googla pod hasłem `SSG` albo `static site generator`. Generalnie to kawałek kodu, program, który generuje na jakiejś podstawie statyczne strony, coś przeciwnego do obecnego podejścia, czyli tworzenia SPA. W moim wypadku postanowiłem stworzyć bardzo prosty system na potrzeby własnego bloga. Tutaj detale implementacyjne zostawiam Tobie. Niech to będzie część zadania - spisz wymagania, rozpisz funkcjonalności etc. Niech poniesie cię wyobraźnia. Minimum jakiego oczekuje, to dostarczenie funkcjonalności wystarczających do prowadzenia bloga - index z listą wpisów i pojedyncze wpisy.

\pagebreak

```python
def find_all_posts(directory: str = "posts") -> Iterable[str]:
    """ All the md posts - both extensions .markdown and .md"""
    return find_all_markdown_and_md_files(directory=directory)


def find_all_pages(directory: str = "pages") -> Iterable[str]:
    """ Similar to the one above, but searches for 
    posts - another directory. Both .md and .markdown """
    return find_all_markdown_and_md_files(directory=directory)


def find_all_markdown_and_md_files(directory: str) -> Iterable[str]:
    """ Base method that finds both .md and .markdown recursively
    in a given directory and it's children. """
    md_files: Generator = iglob(
        os.path.join(directory, "**", "*.md"), recursive=True
    )
    markdown_files: Generator = iglob(
        os.path.join(directory, "**", "*.markdown")
    )
    return chain(md_files, markdown_files)
```

W kodzie sa komentarze, zatem dodatkowo opisywał raczej nie będę. Kolejny kawałek kodu:

```python
md: Markdown = Markdown(
    extensions=["tables", "fenced_code", "codehilite", "meta", "footnotes"]
)

def render_markdown_to_html(md: Markdown, filename: str) -> str:
    """ Markdown to html. Important here is to keep the reset() method. """
    return md.reset().convert(open(filename).read())

def render_jinja_template(template: Template, context: dict) -> str:
    """ Rendering jinja template with a context and global config. """
    context_with_globals = {**context, **CONFIG}
    return template.render(context_with_globals)

def build_meta_context(md: Markdown) -> Dict[str, str]:
    """
    This builds context that we get from Meta items from markdown like
    post/page Title, Description and so on.
    """
    return {key: "\n".join(value) for key, value in md.Meta.items()}
```

Kolejny fragment:

\pagebreak

```python

def build_article_context(article_html: str, md: Markdown) -> Dict[str, str]:
    """ Contant that'll be used to render template with jinja. """
    return {"content": article_html, **build_meta_context(md=md)}


def add_url_to_context(jinja_context: dict, new_filename: str) -> dict:
    """ Builds and adds url for a given page/post 
    to jinja context. """
    jinja_context["url"] = f"{BASE_URL}{new_filename.replace(f'{DIST_DIR}/', '')}"
    return jinja_context

def save_output(original_file_name: str, output: str) -> str:
    """ Saves a given output based on the original 
    filename in the dist folder"""
    new_location: str = os.path.splitext(
        os.path.join(DIST_DIR, original_file_name)
    )[0] + ".html"
    new_directory, _ = os.path.split(new_location)
    if not os.path.exists(new_directory):
        os.makedirs(new_directory)
    output_file: TextIO = open(new_location, "w")
    output_file.write(output)
    return new_location

def gather_statics() -> None:
    template_statics = os.path.join(TEMPLATE_DIR, "static")
    if os.path.exists(template_statics):
        shutil.copytree(
            template_statics, os.path.join(DIST_DIR, "static"),
            dirs_exist_ok=True
        )
```

Składając wszystko do kupy: 

\pagebreak

```python
def render_blog() -> None:
    """ Renders both pages and posts for the blog 
    and moves them to dist folder."""
    posts: Iterable[dict] = reversed(
        sorted(render_posts(), key=lambda x: x["date"])
    )
    render_all_pages()
    render_index(posts=posts)
    gather_statics()


def render_all_pages() -> None:
    """ Rendering of all the pages for the blog.
    markdown -> html with jinja -> html"""
    template: Template = jinja_environment.get_template("index.html")
    for filename in find_all_pages():
        render_page(filename=filename, md=md, template=template)


def render_page(
    filename: str, 
    md: Markdown, 
    template: Template, 
    additional_context: dict = None
):
    additional_context = additional_context if additional_context else {}
    page_html: str = render_markdown_to_html(md=md, filename=filename)
    jinja_context: dict = {
        "page": {"content": page_html}, **additional_context
    }
    output: str = render_jinja_template(
        template=template, context=jinja_context
    )
    save_output(
        original_file_name=jinja_context.get("slug", filename), output=output
    )


def render_posts() -> Iterable[dict]:
    template: Template = jinja_environment.get_template("detail.html",)
    return [
        render_and_save_post(md=md, filename=filename, template=template)
        for filename in find_all_posts()
    ]


def render_and_save_post(md, filename, template) -> dict:
    """ Renders blog posts and saves the output as 
    html. md -> html with jinja -> html"""
    article_html: str = render_markdown_to_html(md=md, filename=filename)
    jinja_context: dict = build_article_context(article_html=article_html, md=md)
    output: str = render_jinja_template(template=template, context=jinja_context)
    new_filename: str = save_output(
        original_file_name=jinja_context.get("slug", filename), output=output
    )
    return add_url_to_context(
        jinja_context=jinja_context, new_filename=new_filename
    )


def render_markdown_to_html(md: Markdown, filename: str) -> str:
    """ Markdown to html. Important here is to keep the reset() method. """
    return md.reset().convert(open(filename).read())


def render_index(posts: Iterable[dict]) -> None:
    md: Markdown = Markdown(
        extensions=["tables", "fenced_code", "codehilite", "meta", "footnotes"]
    )
    template: Template = jinja_environment.get_template("index.html")
    filename = "index.md"
    additonal_context: dict = {"articles": posts}
    render_page(
        filename=filename,
        md=md, 
        template=template,
        additional_context=additonal_context
    )
```



Szerzej rozpisane jest to we [wpisie na moim blogu](https://grski.pl/braindead.html) a całość kodu źródłowego na githubie - [braindead](https://github.com/grski/braindead). Tam też jest historia commitów, opis etc. Zerknij.



## Jednolinijkowiec

Write a one-line Python generator or iterator expression that returns the sequence of integers generated by repeatedly adding the ascii values of each letter in the word “Close” to itself. The first 10 integers in this sequence are: 67, 175, 286, 401, 502, 569, 677, 788, 903, 1004. Assume any needed Python standard library modules are already imported.

Odpowiedź:

```python
islice(accumulate(cycle("Close"), func=lambda x, y: x + ord(y), initial=0), 1, None)
```

Fajne, 



\pagebreak
