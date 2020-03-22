# Przykładowe pytania

To, z jakimi pytaniami się spotkasz, zależy ściśle od tego, co umieścisz w swoim CV, dla przykładu podam ci tutaj listę pytań, z którymi ja się spotkałem na rozmowach rekrutacyjnych. Dodatkowo dorzucę kilka od siebie. Wszystkie, przynajmniej w kilku słowach, omówię.

## Django

1. Distinct w Django model
1. Django middleware - czym jest, gdzie się używa
1. Django droga requesta
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

## Python

1. 3 ulubione featury Pythona 3 względem Pythona 2\
Odp: Tutaj odpowiedzi oczywiście mocno indywidualne, więc nie podam jakiegoś wzorca, ale ja, o ile pamiętam, wymieniłem: f-stringi, unicode jako domyślne kodowanie, operator przypisania w wyrażeniach, które wejdzie dopiero w 3.8.
1. Co zmieniłbyś w Pythonie – podaj przykład nowego PEP'\
Odp: Kwestia mocno indywidualna. Ja rzuciłem coś o tym, by wywalić GIL’a. A jak już mówimy o GIL’u, to pora na klasyczne pytanie każdej rekrutacji na Python deva.
1. Co to GIL?\
Odp: Global Interpreter Lock, a to, czym jest, to już opisywałem, zatem powinieneś wiedzieć. W skrócie powoduje swego rodzaju blokadę, która sprawia, że tylko jeden wątek może się wykonywać w danej instancji interpretera naraz.
1. Wymień rodzaje comprehensions w Pythonie.\
Odp: Chodzi o np. List Comprehensions, Set Comprehensions, Dict Comprehensions
1. Podaj przykłady powyższych, po jednym na rodzaj.\
Odp: Przykładami mogą być... \
list_comprehension = [x for x in range(10)] \
dict_comprehension = {x: x**2 for x in range(10)} \
set_comprehension = {x for x in range(10)}
1. Czym są generatory i czym się różnią od list? \
Odp: Generatory to coś, co ułatwia nam operowanie na dużych ilościach danych, gdyż, są to takie swego rodzaju ‘funkcje’, które zamiast ładować jakiś cały określony data set do pamięci, przetwarza wartości po kolei i yield’uje kolejne wartości. Od listy różnią się tym, że lista ładuje wszystko do pamięci, generator już nie, upraszczając w dużym stopniu.
1. Jakie są różnice między tuplą(krotką) a listą?\
Odp: Główna różnica to fakt tego, że jedną z nich można mutować, drugą nie – listę można zmieniać po utworzeniu, tuplę, czy jak kto woli po polsku, krotkę, już nie – po zainicjowaniu już jej nie zmienisz. Poza tym jest  duża różnica w wydajności i implementacji ‘pod spodem’. Z racji tego, że tupla jest niemutowalna, to interpreter w chwili inicjalizacji ma dokładną świadomość tego, ile będzie ona zajmowała, zatem alokuje dla niej tylko tyle pamięci, ile potrzebuje i ani grama więcej. Lista natomiast podczas inicjalizacji, jest tworzona w taki sposób, że zawsze alokuje się więcej pamięci niż potrzeba na faktyczne dane z listy użytkownika, by potem operacje dodania czegoś do listy działały szybciej. Jeśli tworzysz listę np. 50 elementową, to pod spodem okazuje się, że twoje lista ma zaalokowane miejsce nie na 50 elementów, a na np. 90. Dokładnych liczb możesz dowiedzieć się sam. 
1. Czy w Pythonie można programować funkcyjnie?\
Odp:  Tak. Jest to możliwe – Python jest językiem umożliwiającym programowanie w wielu paradygmatach takich jak funkcyjny, zorientowany obiektowo, imperatywny, proceduralny. Można by się sprzeczać, czy to programowanie byłoby ‘czystym’ (raczej nie) funkcyjnie i tak dalej, ale samo w sobie jest to możliwe. Niezbyt popularna opcja i niezbyt promowana. Ogółem niektórzy krzywo patrzą na to połączenie.
1. Enkapsulacja w Pythonie - czy da się?\
Odp: I tak i nie. Z jednej strony w Pythonie brak takich modyfikatorów dostępu jak private czy public, ale mamy umowne określenia, które powodują, że np. zmienne czy funkcje zaczynające się od podkreślenia ‘_’, są raczej prywatne i nie powinno się ich używać poza daną klasą. Niemniej jest to tylko konwencja, a nie element języka, nic nie będzie ci broniło używać metody z podkreśleniem wszędzie.
1.Jak rozwiązać problem GIL'a?\
Odp: Stackless Python czy też inne implementacje lub wykorzystanie w naszym modelu współbieżności procesów zamiast wątków.
1. Co jest pod spodem dicta, jaka struktura danych teoretyczna?\
Odp: Hash map. 
1. Jak przebiega access do elementów dicta? \
Odp: Na podstawie klucza liczony jest hash za pomocą określonego algorytmu. Z tego hasha uzyskuje się z kolei offset wskaźnika do referencji.
1. Zachowanie kolejności dodania itemów do słownika w Pythonie, czym?\
Odp: W Pythonie < 3.7: OrderedDict() z collections. W >= 3.7 sam dict() domyślnie zachowuje kolejność.
1. Różnice między listą a setem.\
Odp: W liście elementy mogą się powtarzać. W secie nie. Na secie możemy wykonywać pewne operacje, których na listach już nie możemy – podobnie jak na normalnych zbiorach w matematyce – suma, część wspólna, różnica. W najprostszym przypadku można myśleć o secie jak o liście bez powtórzeń. Warto też pamiętać, że dane w secie są nieuporządkowane z założenia, więc set kompletnie nie nadaje się do porządkowania elementów.
1. Jakiego typu obiekty zwracają funkcje dict.keys(), dict.values(), dict.items()?\
Odp: Dict.items() - oczywiste. Lista tupli. Ale tak nie do końca. Bo jak się bliżej przyjrzeć to jest to klasa dict_items, która nie do końca jest listą – trochę to taka rozszerzona klasa, bo umożliwia nam wykonywanie na niej operacji takich, jak na setach. Podobnie z keys() i values(). Czyli na obiektach zwracanych przez te funkcje można wykonywać operacje sumy, różnicy czy części wspólnej ze zbiorów. Tldr – te funkcje zwracają iterable set-like object.
1. Operatory bitowe w Pythonie. Jakie znasz, do czego służą?\
	<< i >> , przesunięcie bitowe w lewo i w prawo\
	& - bitowa koniunkcja, czyli ‘i’\
	| - bitowa alternatywa, czyli lub\
	~ - bitowe negacja, czyli ~x = -x – 1\
	^ - bitowa alternatywa wykluczająca
1. Kiedy używać list comprehension, a kiedy normalną pętlą krokową?\
Odp:  Tam, gdzie możemy, powinniśmy używać list comprehensions, gdyż są one czytelniejsze i wydajniejsze, jeśli chodzi o czas wykonania, ponieważ są optymalizowane przez interpreter i lecą z prędkością gdzieś tam w jakimś stopniu zbliżoną do prędkości C, natomiast zwykłe for loopy są wykonywane normalnie przez interpreter z prędkością normalnego kodu Pythona. Jednak jeśli chcemy wykonać coś, co ma efekty uboczne lub skomplikowaną logikę, czasem warto jednak zostać przy zwykłych pętlach.
1. Jakie są różnice między pętlą for i while w Pythonie?\
Odp: Głównie składniowe oraz wydajnościowe. Pętla while będzie zawsze wykonywana przez interpreter Pythona, natomiast pętla for użyta w list comprehension, chociażby, może zostać zoptymalizowana i śmigać o wiele szybciej.
1. Czym jest iterator? Różnica iterator a iterable.

## Git
1. Czym różni się merge od rebase?\
Odp: Merge tworzy nam ‘merge commit’, natomiast ‘rebase’ niejako wkleja nam commity z mergowanego brancha. Poza tym, używając rebase, można nieźle zepsuć git loga. Co jest lepsze? Zależy kogo zapytać, są różne szkoły.
1. Różnice między Gitem a GitHubem.\
Odp: Git to narzędzie – system kontroli wersji, natomiast GitHub to serwis, na którym możemy hostować swoje repozytoria Git’a i ogółem współpracować z innymi.
1. Co robi git stash? A git stash pop?\


## Http/Rest
1. Czym jest rest?
1. Co odpowiada za to, jakiego typu treści można przesyłać na/z serwera? CONTENTY-TYPE
1. Gdzie lecą parametry w requeście?
1. 403 vs 401
1. Kody responsow http 1xx 2xx 3xx 4xx 5xx
1. Czym jest jwt?
1. Czy możliwa jest już autentykacja na poziomie load balancera tak, żeby później aplikacja nie musiała tego robić dodatkowo?
1. Sposoby autentykacji requesta: basic auth i token
1. Skąd serwer bierze username i password przy basic auth?
1. Skąd przeglądarka wie, że daną odpowiedź trzeba wyświetlić jako json a nie np. plaintext? CONTENTY-TYPE
1. Różnica miedzy PUT a PATCH
1. Dostępne metody/verby HTTP.

## Bazy danych
1. Czym jest join w sql, jak działa, przykład
1. Normalizacja bazy danych
1. Rodzaje baz danych. Relacyjne i nierelacyjne, trochę o nich.

## Elastic Search
1. Czemu elasitc search jest nierealcyjny?

## Ogólne koncepty programowania
1. Czym jest OOP
1. Czym jest SOLID - wymień chociaż jedną

## Struktury danych
1. Czym jest drzewo?
1. Zbalansowane drzewo binarne
1. Jak działa hashmapa

## DevOps
1. Bandit, iflakes8
1. Twój wymarzony pipeline

## Linux
1. Najbardziej zaawansowana 'komenda' jaką znasz w linuxie.
1. Z jakich dystrybucji korzystałeś?

\pagebreak
