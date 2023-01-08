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



## Pyenv, poetry i inne nicponie

Pyenv, poezja i inne łobuzy - nowoczesne zarządzanie zależnościami i wersjami Pythona
O współczesnych wersjach Pythona, środowiskach i zarządzaniu zależnościami.

PIP
Pip to narzędzie, które większość z Was powinna już znać. Służy do instalowania pakietów używanych w rozwoju Pythona i od kilku wersji jest domyślnie dostarczany z Pythonem. Ale co to dokładnie znaczy instalować pakiety?

W skrócie pip dostarcza narzędzi do pobierania pakietów z Python Package Index - PYPI. Jest to domyślny indeks pakietów Pythona, gdzie prawie każdy może dodać pakiety. Domyślny to dobre słowo, ponieważ pip pozwala nam używać różnych indeksów. Tak więc na przykład twoja firma może mieć swoją własną, hostowaną wersję pakietów, a następnie używać jej jako prywatnej wersji pypi. Pozwala to na przykład na lepszą weryfikację pakietów, tylko prywatne połączenia sieciowe podczas procesów CI/CD/development. Jest to dość ciekawa opcja, szczególnie biorąc pod uwagę ostatnie złośliwe ataki na popularne pakiety Pythona open source.

Indeks pakietów
Czym dokładnie jest indeks pakietów?

Właściwie to nic skomplikowanego. Jest to po prostu serwer http, powiedzmy, który dostarcza listę pakietów kodu Pythona - pakietów i pewnych metadanych o nich. Nic więcej.

Zabawne zadanie do domu, aby poeksperymentować z czymś nowym: spróbuj zaimplementować własną wersję pypi i dodać do niej pewne cechy, takie jak chroniony przez tokeny dostęp do pakietów lub nawet więcej tokenów z funkcją granularnych uprawnień.


Domyślna instalacja pakietów
Zazwyczaj jest tak, że mamy jedną, maksymalnie dwie wstecznie niekompatybilne wersje Pythona zainstalowane na naszym komputerze. W przeszłości był to Python2 & Python3, obecnie większość czasu tylko Python3 jest zainstalowany jako Python2 osiągnął EoL.

Tak czy inaczej. Oznacza to, że w Ciemnych Wiekach lub domyślnie instalowano pakiety globalnie, dla całego systemu. To jest złe z wielu powodów. Jeśli chodzi o to, co oznacza instalacja pakietu, w bardzo dużym skrócie, jest to nic innego jak pobranie pakietu kodu pythona o określonej strukturze, który zostaje pobrany i umieszczony w danym katalogu instalacji pythona, z dodatkowymi krokami możliwymi pomiędzy.

Co jeśli projekt A wymaga pakietu Z w wersji 1.0.0, ale projekt B wymaga pakietu Z w wersji 2.0.0? Czy przeinstalowałbyś ten pakiet za każdym razem, gdy przechodzisz do różnych projektów?

virtualenv
Aby zwalczyć problem opisany w poprzednim akapicie -> pakiety instalujące się globalnie, pojawił się virtualenv. W skrócie jest to coś, co pozwala nam "stworzyć" inną, "instancję" instalacji Pythona. Np. tylko dla danego projektu zamiast ogólnosystemowej.

W ten sposób możemy mieć różne wersje pakietu Pythona dla różnych projektów.

Podzbiór funkcjonalności virtualenv jest zintegrowany z domyślną instalacją CPythona od wersji 3.3 jako moduł venv.

Poezja
Co by było, gdyby pip i virtualenv miały swoje ukochane dziecko, które w dodatku uprawia sterydy? Cóż, otrzymalibyśmy Poetry.

Problemem z pipem jest zazwyczaj zarządzanie wersjami zależności.

Nawet jeśli wiemy, że nasz projekt A, wymaga pakietu Z w wersji 1.0.0, zazwyczaj na pierwszy rzut oka pip nie mówi nam o zależnościach tego pakietu Z.

Wprowadza to możliwość problemów, gdy twój projekt osiągnie punkt, w którym ma zainstalowane trochę więcej pakietów. Ponieważ te pakiety również mają zależności, a ich zależności również je mają.

Zazwyczaj nie jest to piekło zależności jak w światach JS, ale w pewnym momencie może również stać się nieco podstępne, jeśli zablokujesz zależności tylko na najwyższym poziomie.

I w pewnym momencie, gdy osiągniesz rozmiar projektu na poziomie korporacyjnym, jest to prawie gwarantowane, aby mieć z tym problemy. Również jeśli wersje tych zależności nie są domyślnie gwarantowane, co z debugowaniem?

Mam na myśli, że jeden build może mieć wersje 1.2.3 jakiejś zależności, ale inny build, wykonany 10 minut wcześniej może mieć 1.2.2, jeśli wersje nie są rozwiązywane w deterministyczny, gwarantowany sposób. Umożliwia to pojawienie się paskudnych błędów.

Jest to również zagrożenie bezpieczeństwa, ponieważ jeśli nie wiesz, jaką wersję zależności dokładnie masz, złośliwa wersja może znaleźć drogę bez naszej wyraźnej wiedzy, co jest okazją do wprowadzenia vulerability.

Mamy coś, co nazywa się dependency resolving i dependency locking*.

Zasadniczo jest to po prostu proces upewniania się, że znamy zależności naszych zależności i ich zależności.

A także mamy jasny rachunek ich wersji, zwykle podpisany hashem*.

Pozwala to na coś, co nazywa się deterministycznymi buildami, co jest jednym z kluczy nowoczesnych CI/CD i aplikacji, które trzymają się wzorca Twelve-factor app.

To jest dokładnie to, co robi Poezja i robi to dobrze.

Poza tym, skoro już przy tym jesteśmy, Poezja ułatwia również zarządzanie projektami, zajmuje się tworzeniem i zarządzaniem virtualenvs za Ciebie i umożliwia łatwiejszą, bardziej scentralizowaną konfigurację projektu poprzez wprowadzenie pyproject.toml

pyproject.toml jest zazwyczaj nowym standardowym plikiem konfiguracyjnym pakietów python.

Och również ułatwia budowanie pakietów, ponieważ może połączyć twój kod pythona i opublikować go w indeksie pakietów do wyboru.

Ogólnie rzecz biorąc, poezja jest schludna. Bardzo schludny.
Pyenv
Python to osobliwe małe zwierzę, które zrzuca skórę od czasu do czasu. Oznacza to, że sam Python, poza naszymi zależnościami, ma również swoje własne wersje. Każda wersja zawiera nowe funkcje, różne ulepszenia. Niektóre z nich są czasem nawet wstecznie niekompatybilne.

Standardowo nie jest trywialne zainstalowanie różnych wersji Pythona i ich poprawne działanie na tej samej maszynie.

Dlaczego miałbyś tego potrzebować? Cóż, tak samo jak w przypadku zależności. Jeden projekt może zależeć od Pythona 3.10, inny od 2.7, a jeszcze inny od 3.12.

Potrzebujemy czegoś takiego jak virtualenv, który zapewniłby izolację, ale zamiast poziomu projektu dla zależności od pythona, zamiast tego dla systemu na poziomie wersji pythona.

Jak to zrobić?

Za pomocą pyenv. Pyenv został wzbogacony o zgrabną wtyczkę, która pozwala nam tworzyć wirtualne biblioteki z różnych wersji/interpretacji pythona.

Pyenv + pyenv-virtualenv jest również miły pod względem integracji z poezją.

Tak czy inaczej. Tak więc mamy pyenv-virtualenv, który jest wirtualnym opakowaniem dla pyenv, który z kolei jest opakowaniem wokół zarządzania wersjami pythona, pracując nad poezją, która jest opakowaniem dla pip i pip-tools, zintegrowanym z virtualenv, który jest również rodzajem opakowania.

Mamy więc wrapper wrappera pracującego nad wrapperem wrappera. Wrapper-ception.

asciicast

Krótki sposób
Zainstaluj pyenv z oficjalnego repozytorium curl https://pyenv.run | bash
Po instalacji uruchom exec $SHELL aby zrestartować powłokę i zastosować zmiany
Zainstaluj pożądaną wersję pythona (np. 3.6.15) pyenv install 3.6.15
Przejdź do głównego katalogu projektu
Zainstaluj wtyczkę pyenv-virtualenv z repozytorium (w wersjach nigdy nie używanych jest ona zawarta w skrypcie pyenv.run, jak sądzę)
Utwórz virtualenv pyenv virtualenv 3.6.15 your-cool-virtualenv-name
Ustaw wirtualny env jako lokalny (upewnij się, że jesteś w głównym katalogu projektu) pyenv local your-cool-virtualenv-name dla automatycznej aktywacji venv
Piptools
Jeśli twój projekt jest wystarczająco prosty lub nie chcesz zawracać sobie głowy wszystkimi poprzednimi rzeczami, możesz użyć pip-tools do przypięcia swoich zależności i tego wszystkiego.

## black, isort

Olaf Górski - Lead Python Developer
2022-12-08
Podnieś poziom swojego oprzyrządowania w Pythonie - black, isort i inne narzędzia
Formatowanie i analiza statyczna kodu Pythona oraz jego oprzyrządowanie. Podejście leniwego człowieka do zapewnienia jakości kodu Pythona.

Na podstawie tego artykułu zrobiłem również prezentację - Python (anty)Patterns 002 - Black, isort, bandit

Pipeliny
Czym są i dlaczego ich potrzebujemy

Automatyzacja rzeczy? Rurociągi na ratunek

Kiedy chcemy dbać o jakość naszego kodu w Pythonie, zwykle chcemy dbać o takie rzeczy jak formatowanie, spójne wzorce importu, bezpieczeństwo i utrzymywanie naszych standarów na bieżąco. Jeśli chcemy to zrobić w naszym repo/w chmurze automatycznie, możemy użyć potoków.

Pipeliny to po prostu zestaw kroków, które składają się na nasz proces CI/CD.

Jest to mniej więcej tylko kawałek kodu, który wykonuje za nas pewne kroki. Zazwyczaj potoki są definiowane jako plik yaml, który określa jakie kroki/akcje chcemy podjąć w ramach naszego procesu CI/CD, czyli analizowanie, sprawdzanie jakości, formatowanie naszego kodu i budowanie/deponowanie go.

W tej prezentacji chciałbym skupić się na krokach związanych z automatyzacją procesu zapewniania jakości przy tworzeniu aplikacji w Pythonie.

Do najczęściej znanych narzędzi służących do tego w chmurze należą: GitHub Actions, GitLab CI/CD, Bitbucket Pipelines, CircleCI, Azure DevOps.

Zazwyczaj są to rzeczy, które odpalają się, gdy np. tworzymy merge/pull request, wpychamy jakiś kod do repo, łączymy jedną gałąź w drugą. Uruchamiają one różne kontrole, budowanie, testy i co nie.

Przepływ wygląda tak:

Trigger jest odbierany (np. Branch jest pchany do repo) -> pipeline jest odpalany -> różne kontrole są wykonywane -> na podstawie tego pipeline może się nie udać lub udać.

Poza tym, że rurociągi są tam w chmurze, uważam, że niektóre ich części są również integralną częścią lokalnego rozwoju. Głównie części związane z rzeczami o kontroli jakości.

Co sprawia, że kod jest dobry?
Obecnie trendem w Pythonie jest dbanie o pewne rzeczy, które choć nie są kluczowe, z czasem przyczyniają się do jakości, czytelności i łatwości utrzymania projektu.

Na wysokim poziomie, w mojej książce, każdy kawałek kodu Pythona może używać niektórych z:

Spójne formatowanie
Uporządkowany import, który jest podzielony na sekcje
Bezwzględny import
Używanie nowoczesnych standardów, które są zgodne z najnowszymi standardami
Brak nieużywanych importów i zmiennych
Skanowanie bezpieczeństwa/podatności
W dalszej części artykułu porozmawiamy jak sobie z tym poradzić w Pythonie.

Czarna strona
Kilka słów o formatowaniu i czerni
Częściej niż w projektach, które nie są tak zautomatyzowane i mogłyby korzystać z niektórych narzędzi dem, można znaleźć ludzi w pull requestach kłócących się o to, które formatowanie jest lepsze. Jak zmienić formatowanie? Który z nich jest lepszy? Który jest bardziej zgodny z pep8?

To może być koszmar, który jest tak kontrproduktywny, jak to tylko możliwe.

Aby pozbyć się takich problemów i mieć to załatwione za nas, używamy black w Pythonie. Black jest formatyzatorem kodu, który, cóż, po prostu formatuje kod za Ciebie. Możesz sprawić, by black automatycznie formatował Twój kod przed jego popełnieniem. W ten sposób można uniknąć wszelkiego rodzaju sporów o pep8 i preferencje formatowania kodu przez recenzentów/autorów, co sprawia, że cały projekt ma spójny wzór formatowania, co sprawia, że jest łatwiejszy do odczytania i tak dalej. Im łatwiejszy do odczytania jest kod, tym lepiej. To jest podejście leniwego człowieka. Jeśli wiesz, czego się spodziewać, nie będziesz zaskoczony. Im mniej musisz się zajmować, tym lepiej.

def is_unique(
               s
               ):
    s = list(s
                )
    s.sort()


    for i in range(len(s) - 1):
        if s[i] == s[i + 1]:
            return 0
    else:
        return 1


if __name__ == "__main__":
    print(
          is_unique(input())
         )
Gets zamienia się w to:

def is_unique(s):
    s = list(s)
    s.sort()

    for i in range(len(s) - 1):
        if s[i] == s[i + 1]:
            return 0
    else:
        return 1


if __name__ == "__main__":
    print(is_unique(input()))
Przykład z geeksforgeeks.org.

' vs "
Jedną z rzeczy wartych uwagi jest fakt, że Python jako Język pozwala na użycie zarówno ' jak i " do oznaczania ciągów znaków. Black domyślnie preferuje podwójne cytaty nad pojedynczymi. Dlaczego. Czytelność, użycie pojedynczego cudzysłowu w języku angielskim i konieczność ucieczki od niego za każdym razem, gdy używamy go wewnątrz naszych łańcuchów, trudniej pomylić się ze znakiem.

I tak dalej. Można się tutaj spierać, ja stoję po stronie podwójnego cytatu, ponieważ IMO jest to lepsze podejście. Czytelność jest królem.

Isort
Czy słyszałeś o sortowaniu importów? To ma sens

Dlaczego powinieneś odpowiednio posortować swój import
Im większy projekt, nad którym pracujemy, zwykle tym więcej rzeczy importujemy z innych części kodu.

Z biegiem czasu ten import może stać się nieporządny. Często jest tak, że. Isort to coś, co pomaga nam w tym, optymalizując nasz import, sortując go odpowiednio, alfabetycznie, grupując w sekcjach i tak dalej. Wiem, że to może wyglądać jak drobnostka, ale to właśnie te drobne rzeczy dodają ogólnej jakości kodu. Spójrz teraz na poniższe obrazki, lewy jest przed isortem, prawy po nim. Który z nich jest dla Ciebie bardziej czytelny?

from my_lib import Object

importować os

from my_lib import Object3

from my_lib import Object2

importować sys

from third_party import lib15, lib1, lib2, lib3, lib4, lib5, lib6, lib7, lib8, lib9, lib10, lib11, lib12, lib13, lib14

importować sys

from __future__ import absolute_import

from third_party import lib3

print("Hej")
print("yo")
Zostaje zamienione na:

from __future__ import absolute_import

importować os
import sys

from third_party import (lib1, lib2, lib3, lib4, lib5, lib6, lib7, lib8,
                         lib9, lib10, lib11, lib12, lib13, lib14, lib15)

from my_lib import Object, Object2, Object3

print("Hej")
print("yo")
Import absolutny
Nowym standardem jest posiadanie importów absolutnych. Dlaczego tak jest możesz przeczytać na własną rękę. Było wiele debat na ten temat, wynikiem których jest: kiedy można preferować import absolutny. Sprawiają one, że jest mniej dwuznaczności i zapewniają wyraźniejsze rozróżnienie, czego naprawdę używamy, z którego pakietu.

Mamy również narzędzie do tego celu, którym jest absolufy-imports. To narzędzie jest szczególnie przydatne w przypadku starszych projektów, gdzie możesz potrzebować poprawić importy w wielu plikach, aby dopasować je do nowej konwencji. To narzędzie robi to za ciebie.

To:

from .notifications.some_important_file import SomeClass
from .another_important_file import AnotherClass
Zostaje zamieniony na to:

from em.jobs.notifications.some_important_file import SomeClass
from em.jobs.notifications.another_important_file import AnotherClass
Bandit
Statyczna analiza naszego kodu pod kątem potencjalnych wątków bezpieczeństwa.

Dlaczego czasami potrzebujesz bandyty w swoim życiu
Kiedy piszemy nasz kod powinniśmy mieć na uwadze bezpieczeństwo. Chyba, że czasem chcesz narazić swoją firmę na potencjalną utratę milionów. Przesadzam z tym przykładem, ale jednak. Bezpieczeństwo jest ważne.

W jakiś sposób możemy popełnić błędy proste z powodu zapomnienia i zaniedbania, którym można było zapobiec w inny sposób. Aby nam o tym przypomnieć istnieją różne narzędzia, które można wykorzystać.

Wśród nich jest bandit. Bandit jest narzędziem do analizy statycznej, które skanuje Twój kod w poszukiwaniu potencjalnie niebezpiecznych fragmentów kodu i ostrzega Cię o nich. Kiedy uruchomisz bandit przeciwko swojemu kodowi, otrzymasz raport taki jak ten oraz listę miejsc w kodzie, w których znajdują się potencjalne problemy.

Skanowany kod: 

autoflake
Im mniej masz...

Zmniejszanie ilości odpadów
Czasami tak się zdarza, że w naszym kodzie możemy mieć niewykorzystane deklaracje importu lub niewykorzystane zmienne. Zdarza się to najlepszym. Aby automatycznie się tym zająć, możemy chcieć włączyć do naszych projektów autoflake.

Jest to narzędzie, które po prostu się tym zajmuje - usuwa nieużywane importy i zmienne.

Nie ma tu żadnej magii.

pyupgrade
Ten kawałek oprogramowania automatycznie aktualizuje niektóre stare wzorce składni do nowszych. To wszystko.


bumpversion
Jest taka rzecz, którą nazywamy semantycznym wersjonowaniem lub semver. Jest to konwencja, która mówi nam, aby wersjonować nasz kod według następującego wzorca: MAJOR.MINOR.PATCH

Na przykład: v0.2.12

Część majorowa jest zwiększana, gdy przechodzimy do głównych rolloutów, które zmieniają wiele.

Mniejszy kawałek jest zwiększany, gdy robimy normalne wydania, np. z większymi funkcjami.

Patch jest czymś, czego używamy dla mniejszych funkcji, łatek, poprawek itp. Ten element rośnie najszybciej.

Abyśmy nie musieli zarządzać tym ręcznie, mamy narzędzie zwane bumpversion. Aktualizuje ono wersję, tworzy commit ze zmianami, tworzy tag git i tak dalej, wszystko automatycznie. Jest to zgrabne narzędzie, które można mieć w swoim CI/CD.

Ułatwia to zarządzanie wersjami, tworzenie changelogów, filtrowanie commitów i zauważanie zmian, błędów, wersjonowanie pakietów/api itp.

Możesz zobaczyć przykładową historię commitów i użycie bumpversion tutaj, w historii commitów mojego projektu - braindead

Czy uruchamiamy to wszystko ręcznie?

Nie. Chcemy być leniwi.

Git hooks & pre-commit
Zautomatyzuj nudne zadania.

Git hooks i pre-commit
Jeśli chcesz, aby wszystko to działo się automatycznie, możesz stworzyć haki gita, które są uruchamiane np. podczas commitu lub przed commitem. Jednym ze sposobów jest po prostu stworzenie pliku .pre-commit i umieszczenie go w folderze .git i wykorzystanie np. Makefile lub użycie czegoś takiego jak narzędzie pre-commit.

Jest to miłe, poręczne narzędzie, które zajmuje się tym za ciebie. Musisz je zainstalować i stworzyć dla niego config, aby powiedzieć mu, które rzeczy ma robić przed commitem. Nie ma tu żadnej magii.

Pozwolę ci wygooglować szczegóły samemu☺

Podsumowanie
Black, isort, absolufy-imports, pyupgrade, autoflake, bandit, bumpversion to narzędzia, które nieco ułatwią Ci życie.

Może to dobry pomysł, aby włączyć je do swojego lokalnego przepływu rozwoju i rurociągów?

## Pytania i zadania

1. Napisz krótkie podsumowanie z wnioskami które narzędzie jest do czego i z przykładami użycia, a następnie podeślij wyniki swojej pracy.

\pagebreak

