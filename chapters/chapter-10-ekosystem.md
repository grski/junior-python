\pagebreak

# Ekosystem narzędzi Pythonowych

Trochę o fajnych narzędziach, które wypada znać. Zakładam, że każde z tych narzędzi sobie zainstalujesz, pobawisz się nim.

## Plik README - co powinien zawierać i jak wyglądać

Jest jedna rzecz, którą każdy porządny projekt powinien zawierać. Plik README. Dobrze napisany, czytelny i obszerny plik README jest podstawową formą dokumentacji dla każdego projektu, zawierającą elementarne informacje o samym projekcie, ale moim zdaniem nie tylko. Dobrze napisany plik README powinien zawierać nieco więcej. Co dokładnie? Już opisuję.

### Technologia

Zazwyczaj gdy pracujemy z plikami README, to mają one rozszerzenie `.md`, czyli według konwencji piszemy je w Markdownie. Markdown to coś, co pozwala nam niejako formatować tekst. Używanie go w README nie jest wymogiem, ale dość powszechnie przyjętym standardem, który ułatwia nam nieco życie i daje większe możliwości aniżeli zwykły plik tekstowy.

### Jakie sekcje powinien zawierać dobry plik README?

 Poniżej przedyskutujemy to, jakie sekcje, co opisujące, powinien zawierać dobry plik README.

### Tytuł

README zaczynamy oczywiście od tytułu. By to zrobić, należy po prostu wpisać w linii tytuł a przed nim dodać `#`, co oznaczy daną linię jako nagłówek Markdown.

### Opis projektu

Tutaj umieszczamy elementarne informacje o projekcie. 

1. Jaki to komponent systemu? Np. API, Worker, frontend, biblioteka. 
2. Za jakie funkcjonalności odpowiada? Np. Jest to API systemu generującego faktury. 
3. Jaki jest kontekst? Trochę dodatkowego kontekstu, tego nigdy za wiele. Np. Faktury te są potem wysyłane do klientów, (...). Używamy tutaj standardowego szablonu z książki wzornictwa firmy.
4. Kim są stakeholderzy - kto jest odbiorą tego projektu?
5. Jaki problem biznesowy rozwiązuje ten projekt?
6. Kim są jego użytkownicy końcowi?

Podsumowanie powinno być napisane w języku domeny danego problemu. Co to znaczy? Otóż jego opis, opis funkcjonalności projektu powinien zawierać słownictwo z danej dziedziny w której działamy. Jeśli robimy projekt o traktorach, to posługujmy się terminami traktorzystów. Będąc między wronami, kracz jak one. Jest to preferowane podejście w porównaniu do posługiwania się czystym, suchym technicznym żargonem.

### Stos technologiczny

W tej sekcji opisujemy najważniejsze technologie użyte, przy tworzeniu projektu. Zależności, używane aplikacje zewnętrzne, serwisy etc.

To pozwoli czytającemu na szybkie zapoznanie się z wyborami technologicznymi dokonanymi w projekcie, użytymi do rozwiązania danego problemu.

Technologie powinny być króciutko opisane, odpowiednie materiały zalinkowane, dla wygody czytającego.

### Instrukcja tworzenia środowiska lokalnego

Tutaj umieszczamy kroki wykonać, aby lokalnie postawić środowisko. Dodatkowo to w tej sekcji umiejscawiamy instrukcje jak wykonać często używane operacje, jakich komend najczęściej się używa jak np. czyszczenie bazy danych, albo jej tworzenie, migracje etc. To tutaj ląduje też wiedza, która jest mocno specyficzna dla danego projektu np. jak rozwiązano problem lokalizacji, internacjonalizacji używając np. PhraseApp czy OneSky.

Zalecam by akurat tę sekcję opisać szczególnie dobrze, mając na wzgląd użytkoników mniej technicznych, który być może będą potrzebowali postawić środowisko lokalnie w celach testowych. Czasami są to nietechniczne osoby, testerzy, stakeholderzy, produkt ownerzy etc. Im też należy się możliwość posiadania środowiska lokalnego. Dodatkowo cały proces stawiania środowiska powinien być jak najbardziej zautomatyzowany.

### Deployment

W kilku zdaniach, zwięźle i krótko, należy opisać jak aplikacja jest zdeployowana, w jakim środowisko żyje, gdzie należy szukać bardziej szczegółowego opisu architektury i tak dalej. Do tego kilka słów o CI/CD

### Autorzy

Lista głównych osób w projekcie. Przydatne, gdy przeskakujemy na nowy projekt i szybko chcielibyśmy ustalić, kto trzyma kontekst i kogo najlepiej pytać o rzeczy, bo ma największą wiedzę co do projektu. 

### Podsumowanie

Plik README to ważna i integralna część systemu. Teraz wiesz, jak powinien wyglądać.

## PIP

Instalator pakietów/paczek Pythonowych. Coś jak `choco` albo `apt`, ale w wersji dla pythona.

## Virtualenv

Środowisko wirtualne. Co to znaczy? Gdy instalujesz pakiety Pythona, niektóre projekty wymagają wersji X, inne Y. Jeśli instalowałbyś to wszystko globalnie, to powstałby problem. Mianowicie, co? Za każdym razem odinstalowywać i instalować inną wersje, kiedy zmieniamy projekt? Nope. Mamy zatem coś takiego jak virtualenv, czyli narzędzie, które na podstawie systemowego, globalnego (albo po prostu jakiegokolwiek) interptera pythona, tworza wersję lokalną np. per projekt.. 

## Poetry

Poetry to trochę taki virtualenv razem z pipem opakowany sterydami. Otóż to menadżer zależności i packagingu. Poetry pozwala nam na tworzenie stabilnych, powtarzalnych i jednoznacznych plików zależności dla naszych projektów. Co to znaczy? W skrócie chodzi o to, by wersje paczek, które pobieramy zawsze były te same albo chociaż przewidywalnie resolvovane. Zwiększa to stabilność i pozwala uniknąć przykrych  błędów.

Poetry to też narzędzie, które ułatwia publikowanie swoich paczek do PyPI. 

Do poczytania:: https://python-poetry.org/docs/

## Pyenv

Pyenv to taki virtualenv, ale dla virtualenva, albo interpretera pythona. To narzędzie, które pozwala nam mieć zainstalowane równocześnie różne wersje Pythona i ustawiać, że np. w tym folderze ma być 3.8, w tamtym 3.10 etc.

Do poczytania: https://amaral.northwestern.edu/resources/guides/pyenv-tutorial

## Pyenv-virtualenv

Integracja pyenva z virtualenvem. Opisane w artykule wyżej.

## Black, isort, bandit, flake8, bumpversion, Makefile

To narzędzia do kontroli/poprawy jakości kodu, formatowania, statycznej analizy, skanowania poddatności etc. Zazwyczaj używane w pajplajnach, CI/CD jak i lokalnie. Bardzo spoko rzeczy.

Do poczytania: https://grski.pl/data-inspector2.html

## pdoc3

Automatyczna generacja najważniejszej rzeczy na świecie, czyli dokumentacji. To narzędzie plus obszerne i sensowne docstringi == szczęśliwy developer.

Do poczytania: https://pdoc3.github.io/pdoc/

## Pycharm/Visual Studio Code

Najlepsze IDE/edytor do Pythona. Ja akurat jestem #teamPyCharm albo Visual Studio Code też daje rade.

## Robienie notatek

Jest milion narzędzi do tego. Ja polecam od siebie np. Notion. Inne opcje? 

Do poczytania: https://bootcamp.uxdesign.cc/i-tried-40-project-note-taking-apps-what-i-chose-and-my-top-10-list-1d39d41852e4

## Pytania i zadania

1. Napisz krótkie podsumowanie z wnioskami które narzędzie jest do czego i z przykładami użycia, a następnie podeślij wyniki swojej pracy.

\pagebreak

