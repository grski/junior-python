\pagebreak

# Bazy danych

Trochę o tym, o czym warto poczytać i o co chodzi z bazami danych.

Co to w ogóle są bazy danych? To po prostu miejsce, gdzie w sposób w miarę trwały chcemy przechowywać jakieś dane. 

Bazy danych są różnorakie i rozmaite, dzielą się na różne kategorie. My pomówimy sobie o tych Relacyjnych oraz na języku, do robienia zapytań, który króluje od dziesięcioleci w systemach bazodanowych - SQLu. Są bazy, które z niego nie korzystają, ale to nie w scopie tej książki.

Od razu zaznaczę, że przez to, iż istnieją różne rodzaje baz danych, to czasami powstają gównoburze. Która lepsza etc. Coś jak Linux vs Windows, które distro Linuxa najlepsze, Jabłka czy Śliwki, etc.

Prawda jest taka, że kretynizmem jest wychwalać w każdej sytuacji tylko jedno rozwiązanie. Każda baza ma własne zastosowanie i pewne nisze, do których nadaje się najlepiej. No, może poza OracleDB, która powinna już dawno umrzeć i przestać ludzi katować swoim istnieniem. Anyway.

## SQL

SQL to po prostu język baz danych pozwalający robić zapytania na danych. Tyle musisz wiedzieć. Do tego poczytaj o prostych zapytaniach: SELECT, UPDATE, INSERT, klauzula WHERE i inne.

Przykłady do analizy jeśli nie chce ci się samodzielnie googlować:

```sql
SELECT column1, column2, ... FROM table_name;
SELECT * FROM table_name;
SELECT DISTINCT column1, column2, ... FROM table_name;
DELETE FROM table_name WHERE condition;
DELETE FROM table_name WHERE condition;
SELECT column1, column2, ... FROM table_name WHERE condition;
SELECT column1, column2, ... FROM table_name 
ORDER BY column1, column2, ... ASC|DESC;
INSERT INTO table_name (column1, column2, column3, ...) 
VALUES (value1, value2, value3, ...);
```

## Relacyjne bazy danych

To generalnie bazy danych, gdzie posiadamy jakąś strukturę formalną, powiedzmy, poprzez zdefiniowane tabele (najczęściej) oraz gdzie między tabelami możemy definiować relacje. Dla ułatwienia roboty dodam małe generalne podsumowanie:

SQL (Structured Query Language) to język zaprojektowany do komunikacji z bazami danych relacyjnych. Pozwala on na wykonywanie operacji takich jak tworzenie, modyfikowanie i zapytania dotyczące danych zapisanych w bazie danych.

Zaletami języka SQL są:

1. Prostota i łatwość użycia - język SQL jest prosty i intuicyjny, a jego składnia jest łatwa do zrozumienia.
2. Wszechstronność - język SQL może być używany do wielu różnych rodzajów baz danych, takich jak MySQL, Oracle, Microsoft SQL Server i wiele innych.
3. Wydajność - SQL jest zoptymalizowany do wykonywania szybkich zapytań na dużych zbiorach danych.
4. Standaryzacja - język SQL jest dość standaryzowany, co oznacza, że różne bazy danych będą miały podobną składnię i zestaw funkcji.

SQL jest często używany w aplikacjach internetowych do zarządzania danymi zapisanymi w bazie danych, takich jak rejestracja użytkowników, przechowywanie produktów w sklepie internetowym i tworzenie raportów. 

### Tabele

Tabele to po prostu coś, gdzie przechowujemy dane. Tabele mają kolumny i rekordy/wiersze.

Tabela to struktura danych w bazie danych, która przechowuje dane w postaci wierszy i kolumn. Każdy wiersz tabeli reprezentuje pojedynczy rekord danych, a kolumny tabeli określają różne pola, które składają się na ten rekord.

Na przykład, jeśli tworzymy bazę danych pracowników, moglibyśmy utworzyć tabelę zawierającą informacje o pracownikach, takie jak ich imię, nazwisko, stanowisko, wynagrodzenie i datę zatrudnienia. Tabela mogłaby wyglądać mniej więcej tak:

| Imię  | Nazwisko    | Stanowisko | Wynagrodzenie | Data zatrudnienia |
| ----- | ----------- | ---------- | ------------- | ----------------- |
| Jan   | Kowalski    | Dyrektor   | 10000         | 2020-01-01        |
| Anna  | Nowak       | Manager    | 8000          | 2020-03-01        |
| Marek | Wiśniewski  | Inżynier   | 6000          | 2020-05-01        |
| Agata | Kwiatkowska | Asystentka | 4000          | 2020-07-01        |

Tabela może zawierać dowolną ilość rekordów i pol, a dane w niej zapisane mogą być różnych typów, takich jak liczby, tekst, daty itp. Czyli nieco inaczej niż w Pythonie, w SQL definiujemy typy danych i jest to obowiązkowe. 

Tabela jest podstawową strukturą danych w bazie danych i jest używana do przechowywania i udostępniania danych w aplikacjach.

Do poczytania:

1. https://www.plukasiewicz.net/SQL/Introduction (trochę formalnie wszystko opisane, ale może być)

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

Normalizacja danych to proces optymalizacji struktury bazy danych poprzez rozdzielenie danych na mniejsze, bardziej specjalizowane tabele, z których każda zawiera jedynie niezbędne dane. Celem normalizacji jest zapewnienie, że dane są przechowywane w możliwie najlepszy sposób, tzn. tak, aby uniknąć redundancji i zapewnić integralność danych.

Normalizacja danych jest przeprowadzana w kilku krokach, zwanych stopniami normalizacji. 1NF, 2NF, 3NF.

 Normalizacja danych ma kilka korzyści, takich jak:

1. Ułatwienie zarządzania danymi - dzięki mniejszej liczbie tabel i brakowi redundancji dane są łatwiejsze do zarządzania, mniejszy bałagan.
2. Poprawa wydajności - mniejsze tabele są łatwiejsze do przeszukiwania i zapytań, co prowadzi do lepszej wydajności.

Ale o szczegółach później. 

### Transakcje i współbieżność

Z transakcjami chodzi o to, że czasami chcemy pewne operacje grupować i wykonywać je razem. Np. wyobraź sobie przykład z linku niżej - przelew bankowy.

Co jeśli podczas wykonywania operacji, którą można podzielić na następujące kroki:

1. Pobierz środki z konta A i zaktualizuj stan konta A.
2. Dodaj pobrane środki do konta B i zaktualizuj stan konta B.

...nastąpi odcięcie prądu, błąd dysku, whatever? A no właśnie, klient B nie dostałby hajsu a klient A by go stracił. Niefajnie. Tu wchodzą transakcje całe na biało, pozwalając nam na to, by w sposób trwały, przed zakończeniem danej grupy operacji, zapisać je. Wszystko albo nic. 

Jeśli po drodze coś się nie uda to transakcja jest cofana jakby jej nigdy nie było i wszyscy szczęśliwi.

Tutaj warto też poczytać o SELECT FOR UPDATE oraz o Race Condition. Ważne przy współbieżności. 

Do poczytania: https://mst.mimuw.edu.pl/lecture.php?lecture=bad&part=Ch7

### Subskrypcje/Powiadomienia

Czasami chcemy, żeby o naszych zmianach np. dodanie rekordu do bazy danych, informować zainteresowane strony. Wyobraźmy sobie, że np. mamy notyfikacje w naszej aplikacji i informujemy użytkowników o promocji, o updejcie aplikacji czy coś podobnego.

Istnieją zaawansowane rozwiązania, można po prostu odpytywać API, natomiast jest to średnie rozwiązanie.

Są od tego odpowiednie protokoły i serwisy 3rd party, które ładnie rozwiązują ten problem.

Natomiast najprostszym jest chyba... LISTEN i NOTIFY z Postgresa. Dużo osób nie zdaje sobie sprawę, że postgres posiada wbudowaną obsługę notyfikacji. A tu jednak. Fajny kombajn z tego postgresa, wszystko ogarnia. Anyway. 

Do przejrzenia: https://www.cybertec-postgresql.com/en/listen-notify-automatic-client-notification-in-postgresql/

### Uprawnienia i bezpieczeństwo

Bazy danych czasem udostępniają coś takiego jak column/row-level security. Co to znaczy? Otóż dzięki temu możemy ustalać sobie, który użytkownik może widzieć jakie kolumny czy jakie rekordy nawet w której tabeli w której bazie/schemacie. 

Niektóre DB wymagają od nas instalacji dodatkowych pakietów by to osiągnąć, inne mają to domyślnie, jeszcze inne w ogóle nie udostępniają tak granularnej kontroli. Postgres dla przykładu jednak tak. Fajna sprawa. 

Aby skonfigurować np. row-level security, należy dodać reguły dostępu do tabeli, które określają, które wiersze są widoczne dla poszczególnych użytkowników lub grup użytkowników. Na przykład, można utworzyć regułę, która pozwala użytkownikowi o nazwie "john" widzieć tylko te wiersze, w których pole "department" ma wartość "marketing".

Row-level security jest użytecznym narzędziem do ograniczania dostępu do danych w bazie danych i może być używane w połączeniu z innymi mechanizmami bezpieczeństwa, takimi jak uprawnienia użytkowników i role.

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

## Tenanty i co to takiego

Trochę o tenant pattern w Django realizowanego za pomocą django-tenants i postgresa.

(Notka: ten kawałek został napisany kilka lat temu przeze mnie i Dominika Szadego, który był wtedy moim juniorkiem <3) 

### Perspektywa młodego
Witam! Mam na imię Dominik, jestem junior developerem w thirty3.

Środowisko, które będzie wymagające, ale jest chyba najlepsze dla takiego początkującego jak ja. Miejsce, gdzie jest mentor, który pomoże mi w trudnych chwilach, odpowie na wszystkie moje pytania i wskaże drogę, powie o błędach, które popełniam.

Czy dzięki temu nauka programowania jest łatwiejsza niż wcześniej? Jak najbardziej! Czy czyni ją łatwą? Nie! 

Dzisiaj chciałbym napisać kilka słów o moim dotychczasowym doświadczeniu, nowych zadaniach, mentoringu i tak dalej, we wspólnym artykule z moim mentorem - Olafem, i co najważniejsze - o tenancy pattern w architekturze oprogramowania.

Powiedziałbym, że proces uczenia się można podzielić na dwie części:

zrozumienie nowego zagadnienia (technologii, narzędzia itp.), które kończy się tym, że ma się ogólne pojęcie o tym, jak rzeczy są robione, co pozwala budować rzeczy na podstawie przykładu, robić niewielkie modyfikacje istniejących rzeczy i tak dalej;

niekończący się proces doskonalenia, który prowadzi do tego, że jest się w stanie tworzyć złożone rzeczy od podstaw;

Dla mnie bycie młodszym programistą oznacza, że często będę stawał przed problemami, które będą wymagały od mnie wykonania pierwszej części - nauczenia się czegoś nowego, aby je rozwiązać. To jest dokładnie to, jak mógłbym opisać mój pierwszy miesiąc w thirty3 - bycie poza moją strefą komfortu programowania i robienie rzeczy, których nigdy wcześniej nie robiłem. Co jest W PYTE.

#### Pierwsze dni

Pierwsze dni w nowej pracy zawsze są trudne i przysięgam, że kiedy konfigurowałem swoje środowisko pracy w poprzednich firmach, zawsze coś szło nie tak - brakowało mi jakichś narzędzi, pakietów, dostawałem dziwne błędy. Na szczęście uruchomienie projektu w thirty3 po raz pierwszy było zupełnie odwrotne.

W tym przypadku difference-makerem było połączenie Dockera i Makefile. Wszystko, co musiałem zrobić, to pobrać dockera (i docker-compose) na mój komputer i postępować zgodnie z cholernym README.md, aby mieć wszystko gotowe i działające. Aplikacja działa. Dokumentacja, praktyki są zdefiniowane, kod jest jasny i łatwy do zrozumienia, testy są. To była bryza.

Przynajmniej do pewnego momentu. Nie minęło wiele czasu, gdy zostałem uderzony przez architekturę multi-tenant. Co to jest. Wyobraź sobie, że masz aplikację używaną przez wiele firm (tenantów). Chciałbyś mieć pewność, że nie dojdzie do przypadkowego wycieku danych między firmami, a jednocześnie, że architektura będzie skalowalna i wydajna.

#### Tenanty na ratunek

W thirty3 używaliśmy django-tenants do rozwiązania tego problemu, przynajmniej w kilku przypadkach. Istnieje jedna instancja bazy danych do przechowywania danych dla aplikacji, ale wiele schem - jedna dla każdego tenanta (firmy). Tworzy to logiczną separację między danymi. Zanim przeskoczę do przykładów, jak próbowałem zrozumieć tę koncepcję i początki, więc, miejmy nadzieję, natychmiast zauważysz moje błędy i zrozumiesz, jak to działa. Załóżmy, że mamy bardzo prosty projekt Django, który pozwala firmom tworzyć projekty, nad którymi będą pracować. 

Potrzebujemy dwóch django appek:

```
companies
projects
```
Oraz modele zadeklarowane w odpowiednich plikach models.py:

```python
# `companies/models.py`
class Company(TenantMixin):
    name = models.CharField(max_length=255)
```

```python
# `projects/models.py`
class Project:
    name = models.CharField(max_length=255)
    is_paid = models.BooleanField()
```
Zachowanie, które chcielibyśmy mieć polega na tym, że każda Firma ma swoje Projekty, które nie są dostępne dla innych firm.

Jak wspomniałem wcześniej każdy najemca ma swój schemat w bazie danych - jakby baza w bazie. Powstaje on wraz z utworzeniem modelu, który dziedziczy po TenantMixin (Company). Rzeczą, która pozwala nam odróżnić lokatorów jest unikalny atrybut schema_name (atrybut TenantMixin), którą musimy podać przy tworzeniu każdego obiektu Company. (Uwaga Olafa: to nie musi być nazwa schematu - może to być ID lub prawie wszystko naprawdę, tak długo jak jest unikalne. Ogólnie schema_name jest tylko metadaną, która pozwala nam wiedzieć gdzie szukać w db).

Poza tym musimy stworzyć specyficzny schemat o nazwie "public", którego celem (O: Właściwie jest on tam w postgresie domyślnie, po prostu tworzymy model w naszej tabeli z tenantami i setupujemy publica jako wspolną schemę) jest przechowywanie globalnych danych nie specyficznych dla danego tenanta/firmy oraz wszystkich schema_name tenantów.

#### Tenanty w Django
Pytanie, które powinniśmy sobie teraz zadać brzmi: skąd Django wie, które dane powinny być przechowywane w schemacie "publicznym", a które w schematach dla konkretnych najemców? Ogarnia się to w pliku settings poprzez ustawienie zmiennych SHARED_APPS i TENANT_APPS. Są to listy aplikacji Django (podobnie jak INSTALLED_APPS). Umieszczenie aplikacji w np. TENANT_APPS będzie oznaczało, że tabele dla Modeli z tej aplikacji będą tworzone w każdym schemacie tenanta. Z drugiej strony, jeśli dodamy naszą aplikację do listy SHARED_APPS, to tak jak w przypadku innych aplikacji gdzie nie występują tenanty, tabele zostaną utworzone w schemacie "publicznym".

``` 
SHARED_APPS = ["companies", …]
TENANT_APPS = ["projects", …]
```
Innym pytaniem jest, w jaki sposób Django wie, na którym schemacie lokatorów należy wykonać akcje? Najemcy są identyfikowani przez URL, np. żądanie URL "tenant.something.com" spowoduje, że nazwa hosta zostanie wyszukana w odpowiedniej tabeli w schemacie "public". Jeśli zostanie znalezione dopasowanie, kontekst schematu jest aktualizowany, co oznacza, że zapytania będą wykonywane w dopasowanym schemacie tenanta. Django-tenants dostarcza kilka narzędzi do ustawiania schematów z perspektywy kodu.

```python
with schema_context(schema_name):
    # queries will be performed against the schema "schema_name"
```
lub

```python
with tenant_context(tenant_object):
    # queries will pe performed against the schema of tenant_object.
```
Wiedząc to wszystko przyjrzyjmy się poniższym fragmentom kodu, aby zidentyfikować pewne błędy, które popełniłem podczas procesu myślowego. 

```python
class TenantsTestCase(BaseTenantTestCase):
    def test_tenants_example(self):
        companies = Company.objects.all()
        ...
```

Oczekiwane zachowaniem dla mnie byłoby uzyskać wszystkie firmy, a jednak wynikiem był pusty QuerySet. Ok, może muszę stworzyć jakiegoś tenanta zanim wyświetle, logiczne, spróbujmy.

```python
class TenantsTestCase(BaseTenantTestCase):
    def setUp(self):
        Company.objects.create(name=”Test company”, schema_name=”test_schema”)
    def test_tenants_example(self):
        companies = Company.objects.all()
```

Tym razem otrzymałem błąd

`Nie można otrzymać listy tenantów będąc w kontekście tenanta, wejdź w schemat publiczny.`

Zadałem sobie pytanie "Co się dzieje?", Ale udało mi się znaleźć gdzieś użycie schema_context. Więc spróbowałem:

```python
class TenantsTestCase(BaseTenantTestCase):
    def setUp(self):
        Company.objects.create(name=”Test company”, schema_name=”test_schema”)
    def test_tenants_example(self):
        with schema_context(“public”):
            companies = Company.objects.all()
```

Świetnie, tym razem nie ma błędu. Tak czy inaczej, zmienna companies to wciąż pusty QuerySet. Ostatnia próba:

```python
class TenantsTestCase(BaseTenantTestCase):
    def setUp(self):
        with schema_context(“public”):
            Company.objects.create(name=”Test company”, schema_name=”test_schema”)
    def test_tenants_example(self):
        with schema_context(“public”):
            companies = Company.objects.all()
```

Wreszcie, tym razem otrzymałem QuerySet z dwoma obiektami Company. Ale czekaj, przecież stworzyłem jeden. Czas połączyć to wszystko w całość.

Okazuje się, że kiedy uruchamiamy testy z Django-tenants, tworzony jest nowy tenant, z schema_name "test" i wszystkie zapytania wykonywane są przeciwko temu schematowi, chyba że go przełączymy. (O: Przynajmniej w naszym przypadku, ponieważ używamy przypadku FastTenant -> w przeciwnym razie tenanty są tworzone np. per TestCase, co trwa bo migracje są aplikowane per tenant etc.)

```python
class TenantsTestCase(BaseTenantTestCase):
    def setUp(self):
        # schema_context = "test"
        with schema_context("public"):
            # schema_context = "public"
            Company.objects.create(name=”Test company”, schema_name=”test_schema”)
    def test_tenants_example(self):
        # schema_context = "test"
        with schema_context("public"):
            # schema_context = "public"
            companies = Company.objects.all()
        # schema_context = "test"
```

Teraz pamiętajmy, że Company, który jest naszym obiektem tenanta jest przechowywany w schemacie "public" więc puste QuerySety, które otrzymaliśmy wcześniej były poprawne, ponieważ próbowaliśmy szukać obiektu Company w schematach, które ich nie zawierają. Idąc dalej, tworzenie obiektu Project musi odbywać się w kontekście konkretnego schematu tenanta, ponieważ to właśnie tam przechowywane są jego tabele.

```python
class TenantsTestCase(BaseTenantTestCase):
    def test_tenants_example(self):
       # Here we can create project, as we are in context of “test” 
       # tenant
       Project.objects.create(name=”Test project”, is_paid=True)
       with schema_context("public"):
            # Here we can not create Project, we are in “public” 
            # context,no tables for Project here
            companies = Company.objects.all()
```

Dla mnie praca z tenantami rozwiązuje się wokół śledzenia, jak zmienia się kontekst, aby zawsze wiedzieć, jakie zapytania mogę wykonać i jakich efektów się spodziewać.

### Perspektywa dziada
Ok. Wystarczy z perspektywy Dominika. Teraz czas na mnie. Dam Ci trochę oglądu z szerszej perspektywy. To, co przeczytałeś do tej pory, to zrozumienie przez Dominika koncepcji tenantów i tego, jak używaliśmy jej w thirty3. Jest mniej więcej poprawne, niektóre rzeczy są zbyt uproszczone, ale ogólna idea jest gdzieś tam taka jak trzeba. Jestem z niego trochę dumny, mi zajęło znacznie więcej czasu, aby zrozumieć pewne rzeczy. Starczy klepania po plecach. Teraz postaram się przekazać wam więcej informacji dotyczących procesu decyzyjnego, który mieliśmy, gdy zaczęliśmy używać tenantów, dlaczego ich używamy i dlaczego wy też możecie chcieć to zrobić.

Zacznijmy.

#### Czym są tenanty?
Pierwsza rzecz - tenanty. Czo to jest? To taka koncepcja, używana najczęściej w np. produktach SaaS, że upraszczając nieco, to są to tak jakby Twoi klienci. Ja przynajmniej lubię myśleć w ten sposób. Coś jak wtedy, kiedy zamiast tworzyć rozwiązanie na miarę dla danej Firmy, z którego korzysta tylko ta firma, to tworzysz generalne rozwiązanie, gdzie firma jest po prostu jakby userem.

Niektóre rzeczy są zdefiniowane globalnie w DB i współdzielone między userami/firmami, inne rzeczy są zdefiniowane i powinny być dostępne tylko dla tej konkretnej Firmy i tak dalej. W normalnym przypadku, gdy tylko ta firma będzie korzystać z aplikacji, nie musisz myśleć o tym dużo. Problem pojawia się, gdy chcesz zglobalizować tę aplikację i mieć wiele firm. Wszystkie z nich mają jakieś prywatne dane, jakieś publiczne. Te dane powinny być oddzielone i niedostępne dla innych firm korzystających z danego SaaSa. Potrzebujesz kolejnej warstwy abstrakcji, która logicznie wiąże lub enkapsuluje te dane firmowe. Aw shiet, here go tenants. Jakie są inne korzyści?

#### Skalowanie SaaSa
W miarę upływu czasu i rozwoju naszych aplikacji, gdy zaczynasz zdobywać klientów, którzy nie są twoją najbliższą rodziną ani inwestorami, sprawy zaczynają się komplikować. Prywatność staje się nagle ważna. Naruszenie danych/wycieki są kosztowne. Następnie produkt zaczyna zdobywać trakcję, twoja baza użytkowników rośnie, optymalizacja staje się problemem. Zdarza się to w prawie każdym udanym produkcie.

Dobrze jest pomyśleć o tych problemach i przygotować się na nie, ale tylko tyle ile trzeba, żeby nie przesadzić z inżynierią. W naszym przypadku, w większości przypadków, decydowaliśmy się użyć wzorca Tenant w tym celu, używając schematów DB do realizacji planu. Dzięki temu trudniej jest by dane wszystkich klientów wyciekły czy żeby jeden klient uzyskał wjazdy do wrażliwych danych drugiego klienta, łatwiej skalować nasze aplikację, nie obciążając przy tym zbytnio naszego czasu pracy.

#### Metody skalowania bazy danych
Co jest czynnikiem, który najczęściej nas ogranicza, przynajmniej w większości aplikacji? DB. Jakie są sposoby skalowania DB? Poziomy i pionowy. Pionowy oznacza, że masz jedną DB, na którą po prostu rzucasz więcej zasobów - lepszy sprzęt. Takie skalowanie ma swoje granice. Gdy je trafisz, nieważne ile masz pieniędzy - to już koniec. Czy możesz coś z tym zrobić?

Tu z pomocą przychodzi skalowanie poziome, czyli używanie większej ilości maszyn/DB zamiast jednej. Jest to jednak dość podstępne - samo postawienie drugiej bazy obok nic nie da. W grę wchodzą nagle takie rzeczy jak wzorce master-slave, spójność danych, sieć węzłów i tak dalej. Dość złożony temat moim zdaniem.

Oczywiście ten sposób ma również ograniczenia, ale często są one znacznie większe niż ograniczenia pionowo skalowanego systemu. A więc tak - zarządzanie tenantami w produkcie podobnym do SaaS można zrobić na wiele różnych sposobów. Pierwszym z nich jest DB per klient. Tutaj prawdopodobnie mielibyśmy jeden większy DB z rzeczami współdzielonymi globalnie w aplikacji, a następnie mniejsze (lub większe) DB z danymi unikalnymi dla klienta.

Drugim jest Schema per client, czyli jedna baza danych z takimi jakby 'mini bazkami' w środku. 

Trzeci to niestandardowe uprawnienia i relacje w tabelach, na przykład z danymi wszystkich klientów umieszczonymi w jednym schemacie, jednym db.

Pierwszy jest kosztowny i kłopotliwy w zarządzaniu na mniejszą skalę.

Trzeci często kończy się niechlujnymi tabelami DB, obawami o prywatność i koszmarem permissionów.

Drugi natomiast... Cóż, prawie nie nakłada kosztów na sytuację, w której miałbyś zwykłą architekturę pojedynczego schematu/DB - nie jest to architektura SaaS, ale ułatwia skalowanie i rozdzielanie danych klienta poprzez abstrakcję DB - zamiast mieć wiele DB, które są kłopotliwe w zarządzaniu, używa jednego DB tak, jakby było ich "wiele", przynajmniej w pewnym sensie.

Dlatego zdecydowaliśmy się na to rozwiązanie. I szczerze mówiąc, jesteśmy całkiem zadowoleni z wyników.

Dużym atutem tenantów jest również fakt, że kwerendy dalej pozostają proste. Zapytanie o faktury tylko z danej firmy? Wystarczy ustawić odpowiedni kontekst tenanta i to wszystko.

#### Różne metody zarządzania tenantami
Tak zwana ścieżka wyszukiwania, którą ustawiamy dla zapytań Postgresa za pomocą naszego db routera, może być ustawiona na wiele sposobów. Tradycyjny wzorzec tenanta wykorzystuje subdomeny jako sposób identyfikacji tenanta- np. x.myproduct.com będzie wyszukiwał tenanta x. To jeden ze sposobów. Należy pamiętać, aby zabronić użytkownikom rejestrowania tenantów z nazwami często używanych subdomen np.` ftp, mail, static` i tak dalej, w przeciwnym razie może czekać nas niemiła niespodzianka. Pamiętaj również, aby mieć certyfikaty, które mają symbol wieloznaczny dla subdomen - w przeciwnym razie zostaniesz bez SSL dla subdomen swoich najemców, co jest całkiem do bani.

Innym rozwiązaniem jest na przykład umieszczenie go jako części adresu url, ale nie subdomeny. Na przykład:`api.example.com/v1/tenant/someendpoint`. My używaliśmy tego drugiego.

#### Co tenanty nam dały
Osiągnęliśmy:

1. zero dodatkowych kosztów zarządzania dodatkową infrą
2. zero dodatkowej infry
3. łatwość skalowania -> zmiana sposobu ustawiania ścieżki wyszukiwania dla db routera i gotowe, skalowanie poziome w trzy minuty
4. dane klientów są od siebie logicznie odseparowane
5. zapytania dalej pozostają proste, tak samo jak permissiony i tabele

W każdym razie. Plus minut tak wyglądają i działają tenanty. 

PS: minusy posiadania mnie jako mentora - prawdopodobnie zaczniesz pisać.

## ORM

Co to takiego ORM?  A no parę słów o tym jakże przydatnym narzędziu.

### Czym jest ORM?

ORM, czyli Object-Relational Mapping, a po naszemu **Mapowanie obiektowo-relacyjne**. Takie narzędzie, które wartości z SQLa, za pomocą odpowiednich 'klas' czy 'mapowań', "konwertuje" na obiekty w Pythonie, które są łatwiejsze do obsługi tak naprawdę. To zbiór przydatnych metod, ułatwień i abstrakcji.  

### ORM vs czysty SQL

Różnica między ORM a tradycyjnym podejściem, gdzie samodzielnie piszemy czysty SQL, jest diametralna.

#### Wincyj abstrakcji

Pierwszą różnicą będzie fakt, że ORM ukrywa wiele rzeczy przed nami, dostarczając warstwę abstrakcji ponad samym SQLem. Robi to kosztem wydajności i kosztem tego, iż zakłada się, że programista wie, w jaki sposób ORM działa, gdyż ich twórcy podejmują za nas pewne decyzje. Te decyzje wpływają na to, jak ORM działa i jak tworzy zapytania. Czasami ich nieznajomość sprawia, że możemy strzelić sobie w twarz, nieświadomie. Niewiedza momentami potrafi zaboleć. Do tego ta wydajność. 

#### Mniejsza wydajność

Nie jest to niewiadomo jaki narzut, natomiast przy skomplikowanych zapytaniach prawdopodobnie będzie trzeba się odnieść do napisania czystego SQLa. Może też się okazać, że coś, co w czystym SQLu zajmie minutkę, w ORMie, przez np. nietypowość zagadnienia, może zająć godziny. I vice versa. Tak też bywa.

#### Mimo wszystko warto

Niemniej jednak dla większości, zdecydowanej większości, w którą wliczasz się Ty, bo inaczej tej książki byś nie czytał/czytała, ORM będzie znaczącym ułatwieniem. Jednakże, jak to zawsze mam w zwyczaju, muszę zaznaczyć, że warto wiedzieć i znać chociaż podstawy SQLa i wiedzieć, jak ORM działa pod spodem, chociaż tak mega mega pobieżnie.

#### Debugowanie/profilowanie ORM

ORM jest dodatkowo trudniejszy w debugowaniu i profilowaniu - query są generowane przez silnik, często potrafią być niezbyt przyjazne jeśli idzie o czytelność, dla człowieka plus nieco nieoptymalne jeśli idzie o wydajność. Ponownie, dla 99% przypadków nie będzie miało to znaczenia, bo zapytanie zwracające listę userów będzie tak samo proste i tu i tu.

#### Serializacja z/do obiektów Pythonowych 

ORM dostarcza nam również pewną warstwę abstrakcji w postaci mapowania danych z bazy do obiektów Pythonowych. Serializacja danych i też ich walidacja. W przypadku pisania ręcznie zapytań SQL to często twoją odpowiedzialnością staje się sprawdzenie, czy dane są poprawne, ich interpretacja czy też konwersja. Jeśli o ORMa idzie to albo udostępnia on szereg narzędzi, które nam z tym pomagają albo wręcz zajmuje się tym za nas. Coś fajnego.

### Podsumowanie

ORM to po prostu forma abstrakcji i uproszczenia interakcji z bazą danych z poziomu danego języka. Ma swoje wady i zalety, trzeba je znać, by podejmować świadomy wybór. W 95% wypadków ułatwi ci życie, natomiast pozostałe 5% chyba jest poza zakresem tej książki przeznaczonej dla junior wannabes.

\pagebreak

