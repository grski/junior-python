\pagebreak

# Bazy danych

Trochę o tym, co czym warto poczytać i o co chodzi z bazami danych.

Co to w ogóle są bazy danych? To po prostu miejsce, gdzie w sposób w miarę trwały chcemy przechowywać jakieś dane. 

Bazy danych są różnorakie i rozmaite, dzielą się na różne kategorie. My pomówimy sobie o tych Relacyjnych oraz na języku, do robienia zapytań, który króluje od dziesięcioleci w systemach bazodanowych - SQLu. Są bazy, które z niego nie korzystają, ale to nie w scopie tej książki.

Od razu zaznaczę, że przez to, iż istnieją różne rodzaje baz danych, to czasami powstają gównoburze. Która lepsza etc. Coś jak Linux vs Windows, które distro Linuxa najlepsze, Jabłka czy Śliwki, etc.

Prawda jest taka, że kretynizmem jest wychwalać w każdej sytuacji tylko jedno rozwiązanie. Każda baza ma własne zastosowanie i pewne nisze, do których nadaje się najlepiej. No, może poza OracleDB, która powinna już dawno umrzeć i przestać ludzi katować swoim istnieniem.  Anyway.

## SQL

SQL to po prostu język baz danych pozwalający robić zapytania na danych. Tyle musisz wiedzieć. Do tego poczytaj o prostych zapytaniach: SELECT, UPDATE, INSERT, klauzula WHERE i inny.

Przykłady do analizy jeśli nie chce ci się samodzielnie googlować:

```sql
SELECT column1, column2, ... FROM table_name;
SELECT * FROM table_name;
SELECT DISTINCT column1, column2, ... FROM table_name;

DELETE FROM table_name WHERE condition;
SELECT column1, column2, ... FROM table_name WHERE condition;

SELECT column1, column2, ... FROM table_name 
ORDER BY column1, column2, ... ASC|DESC;

INSERT INTO table_name (column1, column2, column3, ...) 
VALUES (value1, value2, value3, ...);
```

## Relacyjne bazy danych

To generalnie bazy danych, gdzie posiadamy jakąś strukturę formalną powiedzmy poprzez zdefiniowane tabele (najczęściej) oraz gdzie między tabelami możemy definiować relacje. 

### Tabele

Tabele to po prostu coś, gdzie przechowujemy dane. Tabele mają kolumny i rekordy/wiersze.

Kolumny to takie jakby 'klucze' w słowniku w Pythonie, a rekordy to faktyczne wartości.

Do poczytania: https://www.plukasiewicz.net/SQL/Introduction (trochę formalnie wszystko opisane, ale może być)

### Indeksy

Czym są indeksy? Indeksy to takie specjalne tabele wyszukujące, które pozwalają nam przyśpieszyć zwracanie danych. Takie jakby wskaźniki, co jest gdzie, dzięki którym sql wie gdzie przeskoczyć i skąd odczytać daną wartość. Taki jakby spis treści w książce.

Dzięki nim SELECTy, klauzule WHERE są znacznie szybsze. Wolniejsze za to będą operacje dodawania i aktualizowania danych - przy dodawaniu danych oprócz samej tabeli trzeba jeszcze zaktualizować indeks co powoduje dodatkowy narzut. 

Indeksy można tworzyć na jednej lub więcej kolumn, można je łączyć.

Kiedy warto zastanowić się dwa razy zanim stworzymy indeks?

- w przypadku małych tabel
- w bardzo często aktualizowanych tabelach, gdzie dane się zmieniają nierzadko
- kiedy mamy bardzo dużo NULLi w jakiejś kolumnie

### Relacje

Relacje to opis powiązań pomiędzy parą tabel. Istnieje wtedy, kiedy dwie tabelki są połączone przez klucz podstawowy lub obcy. 

Każda relacja jest opisana określonym typem relacji, więzi między tymi dwoma tabelami. Pierwszym przykładem będzie **jeden do wielu** (one to many/foreign key). Przykładem takiego czegoś może być relacja kupujący <-> faktura. Faktura ma tylko jednego kupującego z definicji natomiast jeden kupujący może mieć wiele faktur. 

Inny przykład to **wiele do wielu**. Tutaj jako przykład niech posłuży fan artysty. Jeden artysta może mieć wielu fanów. Jeden fan może lubić wielu artystów. 

Do poczytania: 

1. https://developeronthego.pl/sql-schemat-bazy-danych/
2. https://analityk.edu.pl/relacyjna-baza-danych-o-co-chodzi-z-tymi-relacjami-sql/

### Normalizacja

Normalizacja to proces w którym pozbywamy się zbędnych danych oraz ustanawiamy relacje między tabelami. 

Pomaga to uniknąć duplikacji danych i bałaganu w nich.

### Transakcje i współbieżność

Z transakcjami chodzi o to, że czasami chcemy pewne operacje grupować i wykonywać je razem. Np. wyobraź sobie przykład z linku niżej - przelew bankowy.

Co jeśli podczas wykonywania operacji, którą można podzielić na następujące kroki:

1. Pobierz środki z konta A i zaktualizuj stan konta A.
2. Dodaj pobrane środki do konta B i zaktualizuj stan konta B.

...nastąpi odcięcie prądu, błąd dysku, whatever? A no właśnie, klient B nie dostałby hajsu a klient A by go stracił. Niefajnie. Tu wchodzą transakcje całe na biało, pozwalając nam na to, by w sposób trwały, przed zakończeniem danej grupy operacji, zapisać je. Wszystko albo nic. 

Jeśli po drodze coś się nie uda to transakcja jest cofana jakby jej nigdy nie było i wszyscy szczęśliwi.

Tutaj warto też poczytać o SELECT FOR UPDATE oraz o Condition Race. Ważne przy współbieżności. 

Do poczytania: https://mst.mimuw.edu.pl/lecture.php?lecture=bad&part=Ch7

### Subskrypcje/Powiadomienia

Czasami chcemy, żeby o naszych zmianach np. dodanie rekordu do bazy danych, informować zainteresowane strony. Wyobraźmy sobie, że np. mamy notyfikacje w naszej aplikacji i informujemy uższkodników o promocji, o uptejdzie aplikacji czy coś podobnego.

Istnieją zaawansowane rozwiązania, można po prostu odpytywać API, natomiast jest to średnie rozwiązanie.

Są od tego odpowiednie protokoły i czy serwisy 3rd party, które ładnie rozwiązują ten problem.

Natomiast najprostszym jest chyba... LISTEN i NOTIFY z Postgresa. Dużo osób nie zdaje sobie sprawę, że postgres posiada wbudowaną obsługę notyfikacji. A tu jednak. Fajny kombajn z tego postgresa, wszystko ogarnia. Anyway. 

Do przejrzenia: https://www.cybertec-postgresql.com/en/listen-notify-automatic-client-notification-in-postgresql/

### Uprawnienia i bezpieczeństwo

Bazy danych czasem udostępniają coś takiego jak column/row-level security. Co to znaczy? Otóż dzięki temu możemy ustalać sobie, który użytkownik może widzieć jakie kolumny czy jakie rekordy nawet w której tabeli w której bazie/schemacie. 

Niektóre DB wymagają od nas instalacji dodatkowych pakietów by to osiągnąć, inne mają to domyślnie, jeszcze inne w ogóle nie udostępniają tak granularnej kontroli. Postgres dla przykładu jednak tak. Fajna sprawa.

### Profilowanie

Zapytania możemy profilować podobnie jak kod Pythona. Są do tego specjalne narzędzia. Jest coś takiego jak `EXPLAIN` i `ANALYZE`, są statystyki, są profilery.

EXPLAIN pozwala nam z wyprzedzeniem zbadać to, co dana baza danych planuje zrobić by wykonać query. Jest to tak zwany 'plan zapytania'. Warto zapamiętać te dwa terminy. W przypadku postgresa `EXPLAIN` generuje plan. `EXPLAIN ANALYZE` zaś dodatkowo go wykonuje, podając rzeczywiste dane i statystyki. 

Więcej do poczytania: https://www.cybertec-postgresql.com/en/3-ways-to-detect-slow-queries-in-postgresql/

### Kolejność kolumn

Nawet kolejność kolumn np. w postgresie ma znaczenie i wpływ na to, jak szybko wykona się nasze zapytanie. Ogromny wpływ nawet.

Podsumuję tutaj wnioski, jakich oczekiwałbym od juniora. Dokładnego mechanizmu bym nie wymagał, natomiast fajnie by było wiedzieć, że ilość kolumn w tabeli ma wpływ na wydajność, to, którą kolumnę przetwarzamy również ma wpływ, ogromny. Warto zatem zapamiętać, że nie jest pożądane tworzenie ogromnych tabel z setkami kolumn. Czasem trzeba je dzielić i znaleźć kompromis między wygodą a wydajnością.

Do poczytania: https://www.cybertec-postgresql.com/en/column-order-in-postgresql-does-matter/ 

### Podsumowanie

Bazy danych to niezbędny element prawie każdego systemu. Warto kapkę coś tam wiedzieć. Językiem dominującym w świecie bazodanowym jest SQL. Znajomość podstaw tegoż raczej nam nie zaszkodzi a może pomoże.

## ORM

Co to takiego ORM?  A no parę słów o tym jakże przydatnym narzedziu.

### Czym jest ORM?

ORM, czyli Object-Relational Mapping, a po naszemu **Mapowanie obiektowo-relacyjne**. Takie narzędzie, które wartości z SQLa, za pomocą odpowiednich 'klas' czy 'mapowań', "konwertuje" na obiekty w Pythonie, które są łatwiejsze do obsługi tak naprawdę. To zbiór przydatnych metod, ułatwień i abstrakcji.  

### ORM vs czysty SQL

Różnica między ORM a tradycyjnym podejściem, gdzie samodzielnie piszemy czysty SQL, jest diametralna.

#### Wincy abstrakcji

Pierwszą różnicą będzie fakt, że ORM ukrywa wiele rzeczy przed nami, dostarczając warstwę abstrakcji ponad samym SQLem. Robi to kosztem wydajności i kosztem tego, iż zakłada się, że programista wie, w jaki sposób ORM działa, gdyż ich twórcy podejmują za nas pewne decyzje. Te decyzje wpływają na to, jak ORM działa i jak tworzy zapytania. Czasami ich nieznajomość sprawia, że możemy strzelić sobie w twarz, nieświadomie. Niewiedza momentami potrafi zaboleć. Do tego ta wydajność. 

#### Mniejsza wydajność

Nie jest to niewiadomo jaki narzut, natomiast przy skomplikowanych zapytaniach prawdopodobonie będzie trzeba się odnieść do napisania czystego SQLa. Może też się okazać, że coś, co w czystym SQLu zajmie minutkę, w ORMie, przez np. nietypowość zagadnienia, może zająć godziny. I vice versa. Tak też bywa.

#### Mimo wszystko warto

Niemniej jednak dla większości, zdecydowanej większości, w którą wliczasz się Ty, bo inaczej tej książki byś nie czytał/czytała, ORM będzie znaczącym ułatwieniem. Jednakże, jak to zawsze mam w zwyczaju, muszę zaznaczyć, że warto wiedzieć i znać chociaż podstawy SQLa i wiedzieć, jak ORM działa pod spodem, chociaż tak mega mega pobieżnie.

#### Debugowanie/profilowanie ORM

ORM jest dodatkowo trudniejszy w debugowaniu i profilowaniu - query są generowane przez silnik, często potrafią być niezbyt przyjazne jeśli idzie o czytelność, dla człowieka plus nieco nieoptymalne jeśli idzie o wydajność.

Ponownie, dla 99% przypadków nie będzie miało to znaczenia, bo zapytanie zwracające listę userów będzie tak samo proste i tu i tu.

#### Serializacja z/do obiektów Pythonowych 

ORM dostarcza nam również pewną warstwę abstrakcji w postaci mapowania danych z bazy do obiektów Pythonowych. Serializacja danych i też ich walidacja. W przypadku pisania ręcznie zapytań SQL to często twoją odpowiedzialnością staje się sprawdzenie, czy dane są poprawne, ich interpretacja czy też konwersja. Jeśli o ORMa idzie to albo udostępnia on szereg narzędzi, które nam z tym pomagają albo wręcz zajmuje się tym za nas. Coś fajnego.

### Podsumowanie

ORM to po prostu forma abstrakcji i uproszczenia interakcji z bazą danych z poziomu danego języka. Ma swoje wady i zalety, trzeba je znać, by podejmować świadomy wybór. W 95% wypadków ułatwi ci życie, natomiast pozostałe 5% chyba jest poza zakresem tej książki przeznaczonej dla junior wannabes.

Kluczowe terminy: Django ORM, S
