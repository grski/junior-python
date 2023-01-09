\pagebreak

# Python, o co chodzi?

## Python – o co chodzi?

Zanim weźmiemy się za naukę Pythona, nieco opowiem o historii samego języka, skąd się on wywodzi, jakie ma cele, założenia, jak ewoluował, zmieniał się na przestrzeni lat, a jak wygląda obecnie, gdzie jest wykorzystywany i dlaczego.

## Jak korzystać z tej książki

Chwila, stop. Chciałbym nieco powiedzieć Ci, jak moim zdaniem należy z tej książki korzystać. Po pierwsze, starałem się, by była ona napisana tak, żeby z jednego tematu naturalnie przechodzić do następnego – od tematów prostych, do tych nieco bardziej skomplikowanych. Dzięki liniowej budowie powinna być ona łatwa do zrozumienia.

Jednak jeśli jesteś już nieco bardziej doświadczonym programistą, czy też po prostu chcesz sobie przypomnieć pewne rzeczy, to skacz po niej śmiało – większość rozdziałów jest w miarę zamkniętymi komponentami.

Kolejną rzeczą, o której chcę wspomnieć, a raczej powtórzyć, to fakt, że w tej książce nie znajdziesz informacji wyłącznie o Pythonie. Poza informacjami, o samym języku, postaram się wprowadzić Cię też w pewne pojęcia z ogólnie pojętej informatyki, tak, byś wiedział nieco więcej, byś miał pojęcie, jak coś działa, dlaczego tak, a nie inaczej. 

Uważam, że to niezbędna wiedza, by zostać dobrym programistą, który się rozwija i daleko zajdzie. Takie rozdziały będą nieco bardziej teoretyczne w swej naturze, ale nie znaczy to, że nudne, wręcz przeciwnie moim zdaniem.

Jeśli chcesz dobrze przyswoić informacje tu zawarte i naprawdę się nauczyć czegoś nowego, to dobrze radzę: po pierwsze, rób notatki, krótkie, treściwe i proste. 

Po drugie – kod przepisuj. Nie korzystaj z metody Copiego Pasty. Przepisuj samodzielnie i koniec.

Na koniec trzy – samodzielnie wykonuj zadania, które będę umieszczał na końcu rozdziałów, ale to nie wszystko – eksperymentuj z kodem. Zmieniaj go, zobacz, jakie będą efekty tych zmian. Przekonaj się o tym w praktyce, przeanalizuj swoje modyfikacje, przemyśl je i ich rezultaty, to jak wypływają na działanie programu. To jest najlepsza metoda nauki. To podstawowe założenie, które przyświecało mi przy pisaniu, że będziesz samodzielnie wykonywał/wykonywała ćwiczenia, czytał/czytała dodatkowo inne artykuły, książki, prowadzić eksperymenty z kodem.

Więcej o tym, jak powinno się uczyć i jakie metody się sprawdzają, możecie przeczytać we wpisie na blogu Gynvael’a Coldwind’a – Poradnik początkującego programisty. Grski poleca. W ogóle cały blog wam polecam. Mało jest miejsc w Internecie, gdzie znaleźć można tak dobre i ciekawe treści. Googlnijcie, bo warto.

Dodatkowo pragnę zaznaczyć, że nie będę w tej książce pisał o wszystkich najdrobniejszych rzeczach. To nie jest encyklopedia Pythona, założenie jest tutaj takie, że po szczegóły różnych rzeczy sięgniecie sami. Ja chcę zwrócić uwagę na często pomijane rzeczy. **Zalecam zatem, by obok tej książki poczytać sobie materiały z dokumentacji Django, Pythona, wyśmienitą książkę Learning Python, 5th edition oraz kurs CS50**. Ja bardziej chce uświadomić wam istnienie pewnych rzeczy i niektóre koncepty objaśnić, dodatkowo zająć się tą często pomijaną wiedzą praktyczną, szczerym spisem swoich doświadczeń. 

## Część interaktywna

Na moim githubie znajdziesz repozytorium `junior-python-exercises - https://github.com/grski/junior-python-exercises. Jeśli życzysz sobie, by twoje rozwiązania zadań i odpowiedzi były sprawdzane, sforkuj to repo (potem dowiesz się co to znaczy) następnie w folderze odpowiednim dla rozdziału dodaj folder ze swoim nickiem z githuba a w środku odpowiedzi. Ja zrobię code review/przejrzę te odpowiedzi i dam jakiś feedback :) 

## Python 2 – Python 3?

Python obecnie jest głównie w dwóch wersjach – Python 2 i Python 3. Są to dwa ‘główne’ wydania tego samego języka, jednakże wersja 3 jest nowsza, wprowadza pewne nowe rzeczy, które nie są wstecznie kompatybilne z wersją nr 2, stąd ten przeskok numeru.

Wprowadzenie Pythona 3 nastąpiło wiele lat temu, obecnie mamy czasy, kiedy Python 2 nie jest już rozwijamy. Umarł i koniec. Jedyne projekty, jakie w nich są, to jakieś grubsze legacy. Poza tym, gdzieś tam słychać powoli jakieś głoski o Pythonie 4.

Co to znaczy z twojej perspektywy, jako początkującego? Nic. Po prostu wiedz, że obecnie uczysz się Pythona 3 i tyle. To wciąż ten sam język, jednak występują między nim, a Pythonem 2 pewne różnice, które w razie czego, możesz bez problemu poznać w kilka chwil. Ja wybieram wersję najnowszą, by przedstawić ci najświeższe informacje to raz, a dwa, tak szczerze, Python 2 staje się już powoli reliktem przeszłości, a kto tworzy w nim obecnie nowy software, robi błąd, chociaż nie wydaje mi się, by takie przypadki można było jeszcze gdzieś znaleźć, poza paroma korpo wyjątkami. 

Jak już, to Pythona 2 wykorzystuje się teraz tylko do utrzymania starych aplikacji w nim napisanych, a uwierz mi na słowo, częściej niż rzadziej, nie chcesz pracować przy utrzymaniu starych molosów. Chyba że płacą Ci dużo pieniędzy. Dużo, dużo pieniędzy. Jeszcze więcej niż dużo. Poważnie. Chociaż i tak nie warto. Co po pieniądzach, gdy dosłownie zmieniasz zawód z programisty na szambo-nurka, nurkując w ekskrementach programistycznych jakichś ludzi, którzy bardziej niż zwykle nienawidzili swego życia, więc stworzyli potwora?

Python 2 przechodzi do przeszłości i dobrze, niemniej jednak czasem napomnę o różnicach, tak w ramach ciekawostki w zasadzie.

## Krótki opis długiej historii Pythona


Python jest językiem dość starym, że się tak wyrażę. Starszym ode mnie, chociaż to żadne osiągnięcie akurat.

Obecnie pełno na rynku języków dość nowych, dzieci jak Scala, Dart, Elm, Elixir, Kotlin czy wiele, wiele innych. W porównaniu z nimi Python jest staruszkiem, pojawił się on bowiem na początku roku 1991 na CWI – Centrum Matematyki i Informatyki w Amsterdamie. Nie jest to co prawda dziadunio taki jak np. C z roku 1972, ale taki pełnoprawny język w średnim wieku, to już jak najbardziej.

Jego głównym twórcą był Guido van Rossum, który do dziś ma przydomek „Benevolent Dictator for Life” (a w zasadzie miał, o czym za chwilę) i w zasadzie uznawany jest za najwyższy autorytet w świecie Pythona.

Jeśli o takie nietypowe fakty chodzi, to można dodać, że jeśli uda ci się znaleźć adres e-mail Guido gdzieś w sieci (nie jest to trudne) i wyślesz mu ciekawy mail z pytaniem, czy czymkolwiek, to istnieje spora szansa, że odpowie. Tak przynajmniej wynika z doświadczeń sporej ilości innych użytkowników Pythona.

Sama nazwa języka nie pochodzi, jak by się mogło wydawać, od gatunku węża, a od serialu emitowanego w latach siedemdziesiątych przez BBC - „Latający Cyrk Monty Pythona”, którego to Guido był fanem i uznał, że nazwanie swojego języka programowania ‘Python’, to będzie coś. No i w sumie jest. Samo to powinno wystarczyć, by zachęcić Cię do używania tego języka.

Python rozpoczął swój żywot publiczny w wersji 0.9.0, ale za długo w niej nie pożył, szybko wychodziły kolejne wersje. Wiązały się z nimi różne perturbacje, gdyż sam van Rossum, jak i najważniejsi członkowie zespołu, wiele razy zmieniali swój ‘dom’, przechodząc z jednej organizacji do drugiej. Kod kodem, ale za coś żyć trzeba.

Wszystko się jednak ustatkowało wraz z nastaniem wersji 2.1, która została wydana już pod szyldem Python Software Foundation – fundacji non-profit, która działa do dziś i wzorowana jest na Apache Software Foundation. 

W założeniu Python miał być następcą języka ABC – innego prehistorycznego tworu, o którym nie będziemy się zbytnio rozwodzić, mimo tego, że wpływ jego jest ewidentny w Pythonie.

Oprócz ABC, w Pythonie wyraźne są pewne wpływy lub elementy zapożyczone z takich języków jak: C, C++, Haskell, Java, Perl czy Lisp. Czy powinno ci coś to mówić? Zdecydowanie nie, jeśli jesteś początkujący albo początkująca. Wiedz po prostu, że Python ma pewne elementy wspólne z innymi językami i nie jest jakimś tam wielkim dziwolągiem.


## Abdykacja Guido
W okolicach czasu pisania tej książki, w sumie na samym początku (cóż mogę powiedzieć, robiłem długie przerwy...), stała się rzecz niesłychana, otóż Guido van Rossum, autor Pythona, postanowił oddalić się od łańcucha decyzyjnego w świecie Pythona i zrzucić swój tytuł BDFL, powoli w ogóle przechodząc na emeryturę niejako. Całość spowodowana była PEP 572, który zaproponował między innymi sam Guido, a który wywołał dość nieprzychylne reakcje społeczności. O co się rozchodziło? 

O operator := i przypisanie w wyrażeniach. Spora część osób bardzo głośno i donośnie zaczęła krytykować ten pomysł, często bez jakichkolwiek podstaw, gdyż, przynajmniej mnie, sam PEP wydaje się raczej przemyślany i fajny, ta funkcjonalność na pewno się gdzieś przyda w Pythonie. O samym tym PEP-ie porozmawiamy później jeszcze, więc na razie bez szczegółów.

Poniżej zamieszczam, przetłumaczono przeze mnie tekst e-maila, który opublikował Guido.

„Teraz kiedy sprawa PEP 572 została wreszcie zamknięta, nie chcę już nigdy musieć włożyć w coś tyle wysiłku i walki, tylko po to, by przekonać się, że ogrom osób potępia moje decyzje.

Chciałbym kompletnie odizolować się od procesu decyzyjnego w kwestiach związanych z Pythonem. Przez chwilę wciąż zamierzam pozostać aktywnym jako zwykły Core Developer, dalej będę mentorował ludzi — teraz w sumie nawet może więcej. Niemniej jednak oficjalnie daję swojej osobie takie permanentne wakacje od tytułu BDFL, musicie radzić sobie sami.

No bo tak w zasadzie to cóż, jest to coś, co prędzej czy później i tak by was czekało — za każdym rogiem wciąż czai się gdzieś jakiś tir, który chce mnie rozjechać, to raz a dwa, że lat mi nie ubywa z biegiem czasu... Oszczędzę wam listy moich problemów zdrowotnych.

Nie zamierzam wyznaczać swego następcy.

Co zrobicie? Jakaś demokracja? Anarchia? Dyktatura? Federacja?

Nie przejmuje się tymi trywialnymi, pomniejszymi decyzjami podejmowanymi codziennie w Issue Trackerze, czy też na GitHubie. Rzadko ktoś mnie tam o opinie prosi, a jak już to raczej w sprawach niezbyt ważnych. Tutaj zatem nic się nie zmieni. I o to jestem spokojny.

Nad czym trzeba będzie jednak pomyśleć to: 
- to, w jaki sposób będą zatwierdzane lub odrzucane nowe PEP-y;
- to, w jaki sposób wybierać nowych Core Devów;

Myślę, że może nam się udać, zdefiniować to, jak te procesy mają wyglądać, w formie nowych PEP-ów, które to będą swoistą nową konstytucją dla tej społeczności. Cały haczyk w tym wszystkim polega jednak na tym, że ja wam tutaj nic nie podpowiem — wy, comitterzy, będziecie musieli sami wszystko wymyślić, ustalić.

Pamiętajcie jednak o tym, że wciąż istnieje tu coś takiego jak CoC (Code of Conduct, czyli taki jakby regulamin), jeśli się wam to nie podoba, to nie pozostaje wam nic innego niż opuścić tę grupę. Może to też trzeba przemyśleć, kiedy kogoś stąd wyrzucić (czyli zbanować z grupy python-dev albo python-ideas).

Na sam koniec przypomnę tylko, że archiwa z tej grupy mejlowej są dostępne publicznie.

Nie odchodzę, wciąż tu jestem, ale chcę, byście zaczęli być samodzielni. Jestem zmęczony i potrzebna mi długa, długa przerwa”. —Guido van Rossum

Cóż można tu więcej wspomnieć.

To był smutny moment w historii Pythona, tym bardziej że tak naprawdę Guido to Python a Python to Guido.

To tyle. Szokujące wiadomości.

Cóż, niechaj się wiedzie panu, panie Guido.

Co prawda nie do końca darzę go pełnią sympatii, przez różne mocno poprawnie polityczne zachowania, wręcz bym powiedział, że paranoiczne, ale wciąż. Zrobił kawał dobrej roboty i za to szacunek mu się należy.

Pytanie jednak jak będzie wyglądał świat Pythona bez tego człowieka? Jaki kierunek wybierze? To okazja do wzrostu, ale zarazem zagrożenie, że zgubimy kierunek, który obecnie jest dość fajny.

W każdym razie... Nowy wiatr zadmie w żagle, dokąd nas zaprowadzi? Czas pokaże. Za rok, dwa pięć. Zdecydujemy o tym my, społeczność, która tworzy Pythona, czyli w zasadzie za niedługo i ty, drogi czytelniku.

Notka: tak z perspektywy czasu, to dalej jest git. Zwinięcie Guido nie zmieniło jakoś Pythona na gorsze.

## Wężowe cele

Z tym Pythonem, to tak sprawa wygląda, że naprawdę warto go używać. Osobiście uważam, że jest on jednym z najlepszych języków do nauki podstaw programowania, czyli taki, jak miał być w zamyśle. Pozwala on szybko przejść do zrozumienia pewnych pojęć programistycznych, gdyż uczeń nie musi skupiać się zbytnio na opanowywaniu skomplikowanej składni czy zawiłych wyrażeń, jak to czasami ma miejsce w innych językach. 

Python jest zwięzły i prosty – większość kodu może być bardzo łatwo zrozumiana przez kogokolwiek, kto choć trochę mówi po angielsku, lub ma słownik pod ręką, a sam kod jest zazwyczaj krótki i elegancki.

Wyjaśnienia tak naprawdę wymaga tylko kilka symboli, używanych, by skrócić zapis. Poza tym Pythona czyta się tak naprawdę podobnie, jak zdania w języku angielskim. To jest też właśnie pierwszy wężowy cel – prostota przedkładana nad złożoność.

Python z założenia miał być prosty, przyjemny i elegancki. Uważam, że taki jak najbardziej jest.

Kolejnym celem jest przenośność. Pythona można uruchomić chyba na większości obecnie popularnych platform – Windows, prawie dowolny Linux, macOS. Do wersji 3.7, wydanej 27.06.2018, oficjalnie wspierane było nawet coś tak dziwnego, jak FreeBSD w wersji <= 9.

Dzięki temu Pythona można odpalić prawie wszędzie, jeśli tylko pozwalają na to zasoby sprzętowe.

Następnym celem, który miał przed sobą Python, jest otwartość. Niektóre języki są dość ‘hermetyczne’ - można ich używać tylko po opłaceniu licencji albo tylko w określonych warunkach, celach. 

Z Pythonem tego problemu nie ma – jest on kompletnie darmowy w użytkowaniu, modyfikacji, dystrybucji i czymkolwiek tam jeszcze sobie użytkownik życzy. 

Dodatkowo Python jest otwarto-źródłowy a za jego rozwojem stoi społeczność. Co to znaczy w praktyce? Każdy ma wgląd do źródeł języka to raz, dwa, że jeżeli coś ci się w Pythonie nie podoba, uważasz, że coś mogłoby zostać zrobione lepiej, to… 

Nie ma problemu. Weź daną funkcję i po prostu ją dopisz, zmień. Jeśli społeczność uzna, że twoje zmiany są zasadne i przydatne, to wylądują one w samym języku. Każdy może mieć zatem realny wpływ na to, jak wygląda Python, jak on działa. Świetna sprawa.

To tylko kilka z idei, które przyświecają Pythonowi, wszystkich ich tutaj nie opiszę, ale uważam, że te najważniejsze udało mi się zawrzeć. 
## Wąż co jakiś czas zrzuca skórę

O cóż mi chodzi? O fakt, że Python i jego zastosowania cały czas się zmieniają. Podobnie jak wąż, zrzuca on swoją starą skórę i zyskuje nową.

Pierwotnie był to język, który wykorzystywano raczej jako język skryptowy. Automatyzacja pewnych procesów na serwerach, jakieś operacje na plikach, tekście i tak dalej. Nudne rzeczy ogółem. Python nie zdobył rynku szturmem, troszkę mu to zajęło. Na samym początku był raczej niszowy. Z czasem i ewolucją samego języka, powszechnie zaczęto dostrzegać jego zalety i piękno.

Dlatego też na przestrzeni lat Python stawał się coraz to popularniejszy, jeśli chodzi o rozwój backendowych części aplikacji webowych, a jak sami wiemy, te od początku ostatniego tysiąclecia tak naprawdę, przeżywają nieustanny rozkwit. Sprawę ułatwiało pojawienie się na rynku kolejnych frameworków pythonowych, przeznaczonych właśnie do tworzenia aplikacji internetowych, takich jak Flask, Pyramid, Pylons, Web2py czy wreszcie Django, które było prawdziwym game-changerem. Taka ciekawostka. Jak sobie instagramika przeglądasz, to wiesz na czym stoi? A no na Django właśnie.

Dzięki temu Python stał się całkiem popularny jako język wykorzystywany do pisania aplikacji internetowych, ale to nie wszystko. W obecnych latach możemy zauważyć nieustający wzrost zapotrzebowania na różnych specjalistów związanych z Data Science, Artifical Inteligence, Machine Learning czy Neural Networks.

Wszystkie te i pokrewne branże rozwijają się niesamowicie a językiem, który w zasadzie praktycznie tam króluje, jest Python. Ma tam swojego konkurenta w postaci R, czy szybko rosnącej zawodniczce w postaci Julii, ale wciąż, trzyma się mocno ten nasz wąż.

Dlaczego? Spójrzcie na idee, jakie przyświecają Pythonowi – samo się wyjaśni. Analityk nie ma być dobrym koderem, on ma za zadanie przetworzyć dane, zatem potrzebny jest mu język, który szybko pozwoli mu, bez zbędnego zagłębiania się w składnie czy to, jak działa sam język, przelać swoje myśli w kod.

Python idealnie się do tego nadaje z racji swej prostoty i wszechstronności. Już sobie to wyobrażam jak siedzi taki analityk jeden z drugim i patrzą, czy na pewno zwolnili całą zaalokowaną wcześniej pamięć w ich super pięknym kodzie napisanym w C albo C++. Nie ma takiej opcji po prostu. I dobrze.

Co prawda powstaje tutaj pewien problem w postaci wydajności, ale o tym później, bo jest to coś, co można przeskoczyć i rozwiązać o wiele łatwiej, niż gdyby próbować nauczyć każdego C/C++.

Oczywiście Pythona wciąż używa się w różnego rodzaju skryptach, automatyzacji i tak dalej, niemniej jednak uważam, że nie jest to już jego główne zastosowanie, jak to było lata, lata temu.

Tak więc, jak widzicie, Python się rozwija i pojawia w coraz większej ilości projektów, dziedzin i stref związanych z ogólnie pojętą informatyką. Osobiście uważam, że ten trend raczej się utrzyma, podobnie zresztą, jak do tej pory, i Python z roku na rok będzie zyskiwał co raz to większą popularność, wejdźmy jednak w szczegóły – dlaczego?


## Zalety Pythona


### Ekspresywność


Python jest bardzo ekspresywny. Co to znaczy? Otóż w Pythonie za pomocą relatywnie niewielkiej ilości kodu, można osiągnąć to, co w innych językach zajęłoby czasami kilka razy tyle. Żeby nie być gołosłownym, popatrzmy na przykład klasycznego programu, którym zaczyna się naukę programowania – Hello World, czy po polsku, Witaj Świecie. Co w ogóle jest ironią, bo jak zaczynasz programować, to się raczej ze światem powinno żegnać, bo więcej go już za bardzo nie będziesz oglądał/a ze swojej piwnicy.
W Pythonie wygląda on tak:

``` python
print(‘Hello World’)
```

Dość proste i zrozumiałe, prawda? Jedna linijka i gotowe.
Przyjrzymy się natomiast innym językom.
Zacznijmy od Javy:
``` java
public class HelloWorld{
    public static void main(void) {
        System.out.println(”Hello World”);
    }
}
```

Tu dalej w miarę jasno, mimo kilku pozornie tajemniczych komend, wciąż można łatwo odczytać, co dany program robi, ale weźmy, załóżmy, na celownik C++:

``` cpp
#include <iostream> 
using namespace std;
int main() {
    cout << "Hello World!";
    return 0;
}
```

Tutaj już troszkę mniej oczywistym jest, co dany program robi, prawda? W dodatku popatrzcie na ilość linii użytych do wykonania zadania. Nie ma porównania.

Zaznaczam jednak, że w obu tych językach można by wydrukować hello world’a za pomocą krótszego kodu, nie znam tychże sposobów, bo żaden ze mnie Javowiec czy gość od C/C++, jednocześnie zbyt leniwa buła, by ich poszukać, niemniej jednak chodzi mi tutaj o samo pokazanie idei.

Innym przykładem tego, jak krótki może być kod w Pythonie względem porównywalnego kodu w C++/Javie czy innych języków, jest niżej, to kod nieco bardziej skomplikowany, ale być może coś z niego zrozumiesz. Dostarczył mi go w komentarzu @jacekw na Steemit i to jego autorstwa jest tenże kod. Dzięki : )

A więc cóż będzie nasz zadany kod robił? Jego zadanie jest proste:

1. stwórz listę liczb w kolejności malejącej 19 do 0.
1. Pomiń liczby parzyste.
1. Podnieś każdą liczbę do kwadratu.
1. Posortuj rosnąco.
1. Wypisz wynik.

Swoją drogą, jest to forma algorytmu, przedstawiona w postaci krokowej, coś, do czego jeszcze wrócimy w przyszłości. Obecnie zapamiętaj sobie jedno – algorytm to po prostu jednoznaczny zbiór instrukcji służących wykonaniu jakiegoś celu.

W każdym razie.

Zacznijmy tym razem od *C++* może.

``` cpp
#include <iostream> 
#include <vector> 
#include <algorithm> 
#include <functional> 
using namespace std; 

int main() { 
    vector<int> s, a; 
    for (int i = 20; i > 0; i--) s.push_back(i);
    copy_if (s.begin(), s.end(), back_inserter(a), [](int x { 
        return x % 2 == 1 ;} );
    transform(a.begin(), a.end(), a.begin(), [](int x){
        return x*x;});
    sort(a.begin(), a.end()); 
    for (auto&& i : a) cout << i << " "; return 0; 
} 
```

Nie wiem jak wy, ale dla mnie to dość zawiły fragment kodu. Jako początkujący programista miałbym problem z jego zrozumieniem. Sporo dziwnych symboli, znaczków. O co tu tak dokładnie chodzi?

Trudno powiedzieć na pierwszy rzut oka.

Następny uczestnik tego porównania to...

*Java*

``` java
import java.util.Arrays;
import java.util.stream.IntStream;

public class Main {
    public static void main(String[] args) {
        int[] a = IntStream.range(0, 20)
                .map(i -> 20 - i - 1)
                .filter(x -> x % 2 == 1)
                .map(x -> x * x)
                .sorted()
                .toArray();
        System.out.println(Arrays.toString(a));
    }
}
```

*Python*:

``` python
a = filter(lambda x: x % 2 == 1, reversed(range(20)))
a = list(map(lambda x: x*x, a))
print(list(sorted(a)))
```

Alternatywnie moja wersja w Pythonie wyglądałaby tak:

``` python
print(sorted([i*i for i in reversed(range(20)) if i % 2]))
```

Pozostawię bez komentarza. Na koniec dodam jednak jeszcze, jako ciekawostkę, przykład z innego języka – Haskella.

``` haskell
sort $ map (^2) $ filter odd [20, 19..1]
```

Też ciekawy, prawda?

Czy to znaczy, że te języki są gorsze, a Python jest królem? Absolutnie nie, nigdy tak nie myśl.

Każdy język jest jak narzędzie – ma swoje zastosowania, w których jest dobry, wyśmienity, ale ma też takie, do których kompletnie się nie nadaje. Tak jest i tutaj. Tak jest wszędzie. Owszem, czasem zdarzają się fanatycy danych technologii czy rozwiązań, którym językowo-technologiczne zapalenie opon mózgowych przyćmiewa obiektywny osąd, ale to nic. My nie chcemy tacy być. Bądźmy mądrzy i rozsądni, ułatwiajmy sobie życie, używając odpowiednich narzędzi do odpowiednich zadań.

Niemniej jednak Python pozwala nam pisać więcej w mniejszej ilości kodu. To oczywiście przychodzi w zamian za pewną cenę, którą trzeba zapłacić, i która sprawia, że Python dobry jest w pewnych sytuacjach a w innych już nie. 

### Prostota

Wróćmy do poprzedniego punktu – jak popatrzymy na kod Pythona, to można by rzec, że to w zasadzie po prostu zapisane polecenie po angielsku. Cóż bowiem znaczy słowo print? Nic innego jak drukuj/wydrukuj. 

Od razu można się domyślić, że programiście chodzi o to, by komputer coś wypisał na ekran. Podobnie sprawa się ma z innymi elementami języka, naprawdę, wystarczy znać angielski i już prawie możemy zrozumieć sporą część Pythona. W dużej liczbie języków jest podobnie, ale nie są one aż tak bardzo podobne do angielskiego, jak Python. 

Naprawdę, drugiego tak prostego języka jeszcze nie spotkałem, a trochę ich, przynajmniej pobieżnie, zdarzyło mi się używać – czy to JavaScript, Java, C, C++, Dart, Scala.

Jedynym językiem, który może konkurować z Pythonem prostotą, jest chyba C – ale to z racji tego, że core tego języka jest po prostu malutkie. Gdy przyjdzie nam do zarządzania pamięcią, wskaźników i innych, równie fajnych rzeczy z C, to zaczyna się tęsknić za Pythonem.

### Python językiem dynamicznie typowanym

Co to znaczy? Cóż, jeśli jesteś nowicjuszem w programowaniu, to możesz kompletnie nie mieć pojęcia, o co chodzi, ale to nic. 

W skrócie sprawa tyczy się faktu takiego, że w statycznie typowanych językach, podczas deklaracji zmiennych, należy podać, jakiego typu dane będzie ta zmienna przechowywała. Za przykład niech posłuży nam tutaj Java:

``` java
int someNumber = 123;
```

Zapis powyżej mówi ‘programowi’, który będzie wykonywał nasz kod, że chcemy utworzyć zmienną o nazwie someNumber, która będzie zawierała dane typu int – integer, czyli nic innego jak liczby całkowite.  A co to w ogóle znaczy, że ma utworzyć zmienną? 

Spróbuję wytłumaczyć to dość prosto, ale może mi się nie udać i jeśli nie do końca zrozumiesz zasadę działania tego mechanizmu, lub trudno będzie Ci, wyobrazić sobie jak to funkcjonuje, to nie przejmuj się, wrócimy do tematu później.

To polecenie spowoduje ‘powiedzenie’ naszemu komputerowi czegoś takiego:

Słuchaj komputer, tu masz jakieś dane, (w tym wypadku ‘123’), zapamiętaj sobie tę wartość, zapisz ją gdzieś, bo będę chciał w przyszłości tego do czegoś użyć, i od teraz, za każdym razem, gdy napiszę w programie `someNumber`, to wiedz, że chodzi mi właśnie o wartość zapisaną w tamtym miejscu.

Próba zapisania innych danych do tej zmiennej, załóżmy, tablicy czy liczby rzeczywistej, nie skończy się zbyt dobrze lub po naszej myśli.

W Pythonie takich obostrzeń i wymogów nie ma. Po pierwsze, podczas inicjalizacji zmiennej, nie musimy podawać jej typu, a po drugie później, możemy bez problemu zmieniać rodzaj danych, jaki przechowujemy w danej zmiennej, zatem ekwiwalentem zapisu wyżej w Pythonie, byłby kod:

``` python
some_number = 123
```

Później bez problemu zaś, możemy wpisać sobie:

``` python
some_number = ‘Hi there’
```

Z czego to wynika, dowiesz się już nieco dalej w książce, ale głównie chodzi o to, że w Pythonie zmienne to tak naprawdę referencje do obiektu, a nie sam obiekt per se. Jak powiedziałem, wrócimy do tego, na razie nie musisz zaprzątać sobie tym głowy. Zapamiętaj tylko to, że Python ci życie ułatwia i nie narzuca za dużo, robi robotę za ciebie, poczciwy wąż.

### Społeczność

Python ma jedną, naprawdę dużą zaletę. Jest to jego społeczność, która raz, że jest naprawdę pomocna, dwa, że jej rozmiar jest imponujący. Dzięki temu ilość dostępnych materiałów, poradników, bibliotek, frameworków i skryptów potrafi po prostu pozytywnie zaskoczyć.

Dzięki otwarto-źródłowej kulturze Pythona wiele niesamowitych narzędzi codziennie jest oddawanych w nasze ręce do użytku, zupełnie za darmo, tak po prostu. 

Powoduje to, że często nie musimy wymyślać koła na nowo – wystarczy import jakiejś biblioteki, którą ktoś już kiedyś napisał. Oszczędza to często czasu i zmartwień, pozwalając się skupić na tym, co w naszej implementacji ważne.

Poza tym, co zrobić, kiedy utkniemy w którymś miejscu pisania programu i nie wiemy co dalej, gdy napotkamy jakiś błąd, którego nie potrafimy rozwiązać? Cóż, z racji wieku samego Pythona oraz rozmiaru jego społeczności, można w większości przypadków założyć, że ktoś przed nami napotkał już podobny problem i zapytał o to w Internecie, lub opisał rozwiązanie danego problemu.

Ludzie chętnie dzielą się wiedzą wbrew pozorom. Dzięki temu nie musimy sami szukać rozwiązania godzinami, grzebiąc w dokumentacji, źródłach czy po prostu eksperymentując. Możemy najzwyczajniej w świecie kogoś zapytać, bo dużo osób zna Pythona, albo znaleźć odpowiedź innych, którzy rozwiązali ten problem przed nami. Nie każdy język ma tak rozbudowaną bazę wiedzy i społeczność.

Jako kontr przykład, podam język Dart. Dość nowy język, niezbyt popularny, ogółem mała społeczność. Niemniej jednak czasem tworzyłem w tym języku i zdarza się nierzadko, iż napotykam jakiś problem, o którym informacji nie znajdę nigdzie, bo po prostu akurat nikomu innemu się nie przydarzył jeszcze, lub też nikt inny go nie opisał, więc muszę sam szukać rozwiązania, przeczesując dokumentacje, źródła i po prostu eksperymentując. 

To zaś jest często droga przez mękę.

Do tego czasami dochodzi niedogodność w postaci tego, że niektóre rzeczy, które np. w Pythonie czy Javie zostały już napisane przez kogoś innego, ładnie zapakowane w paczkę i rozpowszechnione do użycia, w Darcie niekoniecznie są i trzeba je napisać samodzielnie.

Podobnie, jeśli chodzi o samą naukę języka – materiałów jest znacznie mniej, często są one przestarzałe z racji tego, że Dart jest językiem ciągle się rozwijającym i to mocno, co tydzień wychodzą nowe wersje, a przynajmniej kiedyś tak było, czy jest tak dalej, to nie wiem, samego języka, a z racji niskiej popularności mało osób o nim pisze, jeszcze mniej tworzy o nim książki czy poradniki. 

To nie ułatwia nauki, zwłaszcza początkującym programistom. Dobrze, że chociaż dokumentacja jest całkiem dobra, co prawda nie tak dobra, jak dokumentacja np. Django, ale i tak – nie jest źle.

Dlatego też twierdzę, że społeczność Pythona jest jego największą zaletą i to ona, dosłownie, tworzy ten wspaniały język, czyniąc go tym, czym jest.

### Mnogość zastosowań

Python jest językiem ogólnego przeznaczenia. Można w nim stworzyć praktycznie wszystko, poza pewnym, raczej wąskim gronem zastosowań, do których kompletnie się nie nadaje i do których nie był projektowany.

Znając Pythona, możemy tworzyć aplikacje desktopowe, gry, aplikacje webowe, skrypty, emulatory, interpretery, kompilatory, aplikacje do obliczeń naukowych, aplikacje do wizualizacji danych i ich scrapowania z sieci, uczenie maszynowe i tak dalej. Lista jest naprawdę długa.

Oczywiście, do jednych zadań Python jest lepszy, do innych gorszy, bo na przykład rzadko zdarza się, że aplikacje desktopowe czy gry tworzy się w Pythonie, gdyż są do tego lepsze języki, ale w każdym razie, jest to możliwe i niezbyt trudne tak szczerze.

W tym, że Pythona można wykorzystywać do wielu rzeczy, pomaga to, o czym pisałem wyżej – czyli duża społeczność tworząca ogromne ilości bibliotek, frameworków i gotowych skryptów.

Pozwala to na wygodne użycie Pythona w różnych dziedzinach i to dzięki temu oraz samej prostocie języka, zdobywa on szturmem inne pola, poza webdevem i devopsami, jak Data Science, Artificial Intelligence, Neural Networks czy na ogół obliczenia naukowe.

Po prostu czasem utworzenie programu w Pythonie sprowadza się tak naprawdę do zaimportowania jakiegoś modułu i dodaniu kilku drobnych komend mówiących mu, co ma dla nas zrobić. Prościej się nie da.

### Czytelność

Python projektowany był z czytelnością w zamyśle. W Pythonie przynależność kodu do danego bloku oznaczamy za pomocą wcięć, czyli nieco inaczej, niż w większości języków, gdzie zazwyczaj używa się do tego celu klamer lub nawiasów, ewentualnie słów kluczowych jak BEGIN czy END.

W Pythonie zaś liczą się wcięcia, których niepoprawne użycie powoduje błędy uruchomienia. Daje to efekt w postaci tego, że praktycznie każdy poprawny kod Pythona jest w miarę elegancki i łatwo czytelny. Oczywiście, istnieją odstępstwa od tej normy, ale mówię o ogóle kodu, gdzie stosuje się dobre praktyki czy standardy, takie jak PEP8, chociażby, o którym to pomówimy jeszcze później.

Gdy dodamy do tego prostotę i ekspresywność samego języka, to szybko wyjdzie nam na to, że kod w Pythonie jest często po prostu ładny, łatwy do odczytania, zmodyfikowania i przyjazny nowicjuszom.

Owszem, osobom przechodzącym z innych języków może się to wydać, przynajmniej na początku, dziwne, że w Pythonie używamy wcięć zamiast nawiasów czy klamer, ale jest to ładne rozwiązanie moim zdaniem. 

Dodatkowo brak w Pythonie jeszcze jednej rzeczy – średniki na końcu wyrażeń nie są konieczne. Mniej pisania o cały jeden znak na linię i czystszy kod.

Oczywiście, czasem stosujemy średniki w Pythonie, niemniej jednak są to sytuacje rzadkie i z góry określone, naprawdę nieliczne.

To chyba też kolejna rzecz, która może dziwić programistów innych języków, chociaż w obecnych czasach nie jest to aż taka rzadka praktyka, by w języku nie były konieczne średniki.

Dlaczego w ogóle jednak czytelność jest ważna? Czas programisty jest drogi, nasze mózgi mają mocno ograniczone zdolności. Dobrze jest, gdy pewne rzeczy od razu widać, gdy nie musimy się nad czymś zastanawiać, bo jest to oczywiste. 

Jeśli program jest bardzo czytelnie napisany, to szybciej uda nam się go zrozumieć, a to jest krytyczne w tym, by wykonać zadanie – wbrew pozorom, praca programisty nie polega na ciągłym klepaniu kodu, wręcz przeciwnie. 

Osobiście, to większość czasu w pracy spędzam na czytaniu kodu innych ludzi – czy to współpracowników, czy też autorów bibliotek, frameworków a czasem nawet swój własny. Czytelny wygląd dużo ułatwia, a to ważne, bo czytanie i rozumienie kodu jest o wiele trudniejsze niż jego pisanie.

### Automatyczne zarządzanie pamięcią

W Pythonie zarządzanie pamięcią odbywa się automatycznie – programista nie ma w tym udziału, robi to za nas sam język za pomocą takiego mechanizmu jak Garbage Collector, dba on o odpowiednie uwalnianie zasobów i pamięci po obiektach, których już nie używamy.

Także nie musimy przejmować się takimi rzeczami jak alokacja i de-alokacja pamięci, jak to ma miejsce np. w C czy C++. 

Dlaczego to zaleta? Z racji tego, że niepoprawne zarządzanie pamięcią może doprowadzić do bardzo poważnych błędów, które narażają na szwank cały system, a to, by takowe nie wystąpiły, jest na głowie programisty i często nie jest to rzecz prosta, ba! Czasami banalne konstrukcje związane z alokacją i de-alokacją pamięci, rzeczy, które wydają się oczywiste, mają skomplikowane podłoża, które doprowadzają do poważnych błędów, jeśli źle zrozumiane.

W przypadku Pythona tak nie ma – programista na ogół nie ma nawet dostępu do bezpośrednich operacji na pamięci. Jest to bardzo mądre ograniczenie, przydatne w tego typu języku. Podobnie jest, chociażby, w Javie.

### Wspieranie różnych paradygmatów programowania

Są języki, które wspierają mocno w zasadzie tylko jeden paradygmat programowania – jak np. Java, czy Smalltalk, które zaprojektowane są, by ściśle spełniać założenia paradygmatu obiektowego, czy Haskell, który jest językiem funkcyjnym i tylko funkcyjnym, ale są też takie jak Python, które wspierają wiele paradygmatów. O co z tym chodzi, tak po ludzku?

W Javie czy Haskellu masz nieco z góry narzucone to, jak masz ‘myśleć’ i w jakim kluczu powinieneś realizować rozwiązania pewnych problemów za pomocą kodu. Co to znaczy tak dokładnie, omówimy innym razem.

W Pythonie natomiast masz wolność wyboru. To ty sam decydujesz o tym, które podejście Ci się podoba i którego chciałbyś użyć. Uważam to za zaletę, gdyż ponownie — w jednych sytuacjach lepiej sprawdzają się jedne rozwiązania, w innych drugie. Mając wybór, możesz użyć tego właściwego i już.

### Wiele wspieranych platform

Jak już wspomniałem gdzieś wcześniej, Python obsługuje praktycznie dowolną używaną dziś platformę. Windows, Linux, AIX, IBM, macOS, OS/390, z/OS, Solaris, VMS, HP-UX. Co sobie kto zażyczy, prawie na pewno jest. Okej, niby teraz używamy tylko Windowsa, Linuxa i macOS, tak praktycznie mówiąc, ale nawet te systemy są przez niektóre języki niewspierane.

### Dojrzałość

Python jest językiem, który powstaje od roku 1991 – obecnie ma prawie 30 lat. Przez ten czas jego ekosystem, narzędzia i biblioteki zdążyły dojrzeć, przejść przez problemy wieku dziecięcego, które niektóre języki mają jeszcze przed sobą.

Znaczy to mniej więcej tyle, że Pythonowi zazwyczaj można ufać. O ile sam programista czemuś nie zawini, to język raczej nas nie zawiedzie, z racji tego, że przetrwał próbę czasu, a większość błędów i rażących bugów, została już dawno wyłapana, załatana.

Czy to znaczy, że to język idealny czy bez błędów? W żadnym razie. Niemniej jednak, z racji tego, że wykorzystywany był/jest on w setkach tysięcy ważnych aplikacji biznesowych, można śmiało stwierdzić, że pewną dozą zaufania warto naszego węża obdarzyć.

### Prostota w integracji z innymi językami

Pythona dość łatwo można integrować z innymi językami na różnych platformach. Programy napisane w Pythonie zazwyczaj dość łatwo współpracują z innymi programami, napisanymi, chociażby w odmiennych językach.

Nie każdy język ma tę cechę, gdyż niektóre języki tworzą dość hermetyczną, specyficzną i zamkniętą kulturę, gdzie połączenie czy integracja ich z innymi środowiskami jest nad wyraz lub niepotrzebnie trudna.

Dodatkowym atutem Pythona jest to, że można pisać do niego ‘rozszerzenia’ w języku C czy C++, które będą działały o wiele szybciej, niż sam Python. Dzięki temu możemy mieć większość aplikacji napisaną w Pythonie – kod prosty, krótki i przyjemny tam, gdzie może być, a akurat jakieś wąskie jej gardło, które musi wykonywać się naprawdę szybko, w C czy C++. Raczej się tego nie stosuje, ale czasem pojawiają się różne, dziwne powody, dla których warto.

### Szybkość tworzenia kodu

Z racji prostoty i mnogości bibliotek w Pythonie, aplikacje, jak i sam kod, można w nim tworzyć wręcz błyskawicznie. To niewątpliwa zaleta, zwłaszcza w czasach, kiedy większość klientów chce, by ich produkt był zrobiony na wczoraj, a terminy zawsze gonią.

Mało tego, zazwyczaj ten zrobiony na szybko kod jest też dość przyzwoitej jakości.

No i faktem jest też, że nawet jeśli nie chcemy wykorzystać Pythona produkcyjnie, to wciąż możemy go użyć, by stworzyć malutkie MVP. Co to MVP? Minimal viable product – czyli taką appkę, która będzie miała minimum funkcjonalności, ale gdzieś tam ktoś już za to będzie chciał zapłacić, bo do czegoś mu się przyda, co ucieszy inwestorów i w ogóle ludzi, bo jest super, mamy MVP, VC sypną, znowu, groszem, kolejna runda finansowania, hajs i hype się zgadza, nasz statek zwany startupem płynie dalej.

Zapamiętaj ten skrót – MVP to gorący buzzword w zwariowanym świecie STARTAPUFF!

Kończąc dygresję, nawet jeśli nie używamy Pythona produkcyjnie a tylko do MVP, czy tworząc jakiś prototyp po prostu, w Pythonie możemy zrobić to błyskawicznie, sprawdzić, czy dane rozwiązanie działa, jeśli tak, to cóż, zawsze można wersję produkcyjną zaimplementować w innym języku. Jakimś szybszym.


## Wady Pythona

To teraz o tych gorszych stronach.

### Python językiem dynamicznie typowanym

Chwila, moment, przed sekundą jeszcze, pisałem, że jest to zaleta. Co jest? Masz gościu rozdwojenie jaźni, czy jak? Co? Kto to powiedział? Halo. A tak serio, to...

Dynamiczne typowanie Pythona to zaleta, która umożliwia nam tworzenie pewnych świetnych mechanizmów, ale i również, w rękach niedoświadczonego programisty, wada. 

Pozwala ona bowiem na stworzenie kodu, który spowoduje kompletnie nieoczekiwane, trudne w debugowaniu błędy, którym można by zapobiec w języku statycznie typowanym, w którym to taki kod w ogóle by nie został skompilowany.

W Pythonie, czy innych dynamicznie typowanych językach, takiego mechanizmu nie ma, więc trzeba tutaj nieco uważać, by nie stworzyć błędu, który będzie później trudny do zdiagnozowania i zdebugowania. 

Oczywiście obecnie mamy narzędzia, które nam ułatwiają to zadanie, czy nawet upodobniają w pewnym stopniu Pythona do języków statycznie typowanych, gdyż istnieją, chociażby, adnotacje typów, pozwalające nam podawać to, jaki typ powinna mieć zmienna/funkcja. 

Niemniej jednak nie jest to obowiązkowy czy konieczny element języka i nie spowoduje on błędu podczas próby uruchomienia aplikacji, a jedynie co najwyżej ostrzeżenie IDE albo analizatora kodu, które można zwyczajnie zignorować.

Zatem dynamiczne typowanie jest nieco jak nóż, z jednej strony możesz użyć go do zrobienia czegoś fajnego, dobrego posiłku na przykład, a z drugiej strony, musisz żyć, ze świadomością, że należy zwracać szczególną uwagę, gdy się z nim obchodzisz, bo możesz się skaleczyć.

Jednakże czy z tego faktu należy rezygnować z korzyści i zastosowań, jakie on ma? Rzucę klasykiem – Nic bardziej mylnego! 

Nie wiem jak wam, ale ja to zdanie czytam ze specjalnym akcentem i pewnym głosem w głowie.

### Wydajność

Jedno jest jasne – jeśli chodzi o kwestie ściśle wydajnościowe, Pythonowi daleko do miana króla. Ogółem fajny ten Python, taki nie za szybki można powiedzieć.

Oczywiście, obecnie się to zmienia, ale sama natura Pythona jako języka interpretowanego sprawia, że nigdy nie będzie on tak szybki, jak kompilowany do natywnego kodu, C, czy inne języki tego typu. Trzeba się z tym pogodzić i już.

Oczywiście nie twierdzę tutaj, że Python jest bardzo powolny, czy ociężały. Nie. Python nie jest wolny, wręcz przeciwnie – dzięki różnym optymalizacjom poczynionym na przestrzeni lat, Python naprawdę zyskał na szybkości i dziś śmiało stwierdzam, że jest to język wystarczająco szybki, ale mocno należy zaznaczyć, że nie jest to język najszybszy. I tyle.

A jak już o wydajności mówimy to i o rozmiarach wspomnę – wymagania sprzętowe Pythona sprawiają, że na niektórych platformach go po prostu nie uruchomimy. Są pewne obszary świata embedded, gdzie króluje C czy Assembly, Python tam nie istnieje i nie ma co z tym dyskutować.

Oczywiście są też projekty jak RaspberryPi, gdzie faktycznie, Python również rządzi wszystkim.

Czyli jeśli chcesz pisać wysoce wydajne gry z piękną grafiką, czy też może wielowątkowe aplikacje, które w rzeczywistym czasie obsługują ogromne ilości obliczeń, albo może malutkie mikro-kontrolery, to cóż, Python nie jest raczej zbyt dobrym wyborem w takim razie.

W innych przypadkach Python sobie poradzi i nie trzeba przejmować się szybkością wykonania/zasobami. Dlaczego? Otóż żyjemy w takich czasach, że czas serwera jest znacznie tańszy niż czas dewelopera. To znaczy lepiej, żeby język był może i kapkę wolniejszy, ale za to, jeśli pisze się w nim znacznie szybciej, to go wybieramy. Tak jest po prostu taniej, lepiej, zdrowiej.

Nie oznacza to, że mamy tu przyzwolenie na to, by pisać byle jaki kod, który działa siermiężnie i wolno, ale działa. Absolutnie! Trzeba szanować czas użytkownika, zasoby sprzętowe, które mamy i kilka innych rzeczy. Oszczędzaj RAM gdziekolwiek jesteś. Jak we wszystkim – należy znać umiar i granice. Chodzi mi tutaj bardziej o sytuacje, teoretyczną, gdzie mamy jakiś kod obsługujący zapytanie do serwera. 

Przejście zapytania przez sieć zajmuje, załóżmy, sekundę. Wykonanie i zwrócenie odpowiedzi przez Pythona zajmie około 0,1 sekundy. Potem znowu powrót do użytkownika, czyli kolejna sekunda. Łącznie 2,1 sekundy. 
Możemy przepisać ten kod w innym języku, załóżmy, Javie – kod będzie kilka razy dłuższy, pisanie zajmie go więcej czasu, ale za to wykona się, powiedzmy, 10 razy szybciej. Czyli użytkownik, zamiast poczekać 2,1 sekundy, poczeka 2,01 sekundy, gdyż zazwyczaj to nie sam serwer i kod naszej aplikacji, jest wąskim gardłem, a np. baza danych, połączenie sieciowe czy dysk.

Czy ma to sens w większości przypadków? Przeskok z 2,1 do 2,01s? Sami sobie odpowiedzcie. O takie sytuacje mi chodzi – wtedy nie ma sensu zazwyczaj bawić się w optymalizacje i Python jest po prostu wystarczająco szybki.

Tak to przynajmniej się ma w znacznej większości projektów, gdyż tych, które nie mogą sobie pozwolić na to minimalne zwolnienie, jest niezbyt dużo. Zresztą ty – jako początkujący programista, raczej nawet na oczy takich projektów na starcie kariery nie ujrzysz, bo nie pora na to. 

### GIL

W Pythonie mamy coś takiego jak GIL – Global Interpreter Lock. Nie będę się tutaj rozwodził nad szczegółami tego mechanizmu, wystarczy, że będziesz wiedział, iż to przez niego Python nie do końca jest idealnym wyborem, kiedy przyjdzie nam rozmawiać o wielowątkowych aplikacjach, gdyż tylko jeden wątek w danym momencie może mieć dostęp do interpretera w procesie, bo GIL blokuje resztę.

A o co chodzi z tą wielowątkowością i tak dalej? W skrócie i dużym uproszczeniu to chodzi tu o wykonywanie wielu rzeczy jednocześnie, najczęściej za pomocą wielu rdzeni procesora, by przyśpieszyć działanie jakiejś aplikacji. 

Bo nie wiem, czy kojarzysz, ale masz w komputerze coś takiego jak CPU – tak zwany procesor. Ten procesor odpowiada za większość obliczeń, kalkulacji i wykonywanie twoich poleceń, tak w dużym skrócie. 

Podczas rozwoju technologii, doszliśmy w pewnym etapie do momentu, kiedy trudno było już sprawić, żeby jeden rdzeń był szybszy. Zatem, żeby to wszystko działało jeszcze szybciej, a ty mógł/mogła odtwarzać pięć aplikacji w tle, obecnie procesory mają po kilka rdzeni. 

Rdzenie to takie jakby małe procesory wewnątrz procesorów. Wyobraź sobie pracownika. 1 rdzeń = 1 pracownik. I wracając do tego wcześniej – pracownik jak to pracownik, ma ograniczoną wydolność, bo ogranicza go np. fizyka. No jeden człowiek, nieważne jak silny, nie jest w stanie przenieść więcej worków betonu niż X na godzinę. My, po pewnym czasie doszliśmy właśnie do tego momentu, że technologicznie stworzyliśmy pracownika, czyli procesor, co to do tego X się zbliżył, powiedzmy.

Pojawił się zatem problem, bo mamy wydajność pracownika X. Mamy jednego pracownika na budowie, chcemy szybciej skończyć pracę, jak możemy to zrobić, skoro wyciągnięcie więcej niż X worków na godzinę, z tego jednego pracownika, będzie trudne lub niemożliwe na chwilę obecną? Możemy spróbować sprawić, by był jeszcze bardziej wydajny i np. zafundować mu dobrą kurację sterydami, co by silniejszy się zrobił, albo kokainą/amfą go odżywiać, sprawiając, że wydajność wzrosłaby o te 5%, ale koszt tego przedsięwzięcia byłby zupełnie niewspółmierny do uzyskanych rezultatów. Co zatem zrobić? Zatrudnić więcej pracowników. Wtedy, kiedy do pracy zaprzęgniemy kilku robotników, mogą być oni nawet słabsi od tego jednego, ale będzie ich kilku. Łączna moc przerobowa wzrośnie.

Plus minus tak wygląda sytuacja z procesorami i tym, że są one obecnie wielordzeniowe.

Tu wchodzi Python, który jest takim trochę upośledzonym brygadzistą. Dobrze sobie radzi z zarządzaniem 1 pracownikiem, ale jeśli przyjdzie mu ogarniać np. 4, to ma już pewne ograniczenia, których trzeba być świadomym.

Co prawda da się to teraz w miarę łatwo obejść, ale wciąż coś takiego pozostaje i trzeba nauczyć się z tym radzić, bo można wpaść w pułapkę.

### Wysoka ekspresywność

Ponownie, coś, co jest zaletą, jest również troszkę wadą. Dlaczego? Python ukrywa pewne rzeczy przed tobą, programistą, co powoduje, że nie zawsze wiesz, jak jest to zrobione ‘od podszewki’. Nie jest to do końca dobre, bo czasami przydaje się wiedzieć, jak pewne rzeczy zostały zaimplementowane i dlaczego akurat tak. 

Sporo to wyjaśnia. Prostym tego przykładem jest częste pytanie – dlaczego indeksujemy listy czy tablice od 0? Jeżeli jesteś programistą C/C++, najprawdopodobniej znasz odpowiedź.

Programiście języków wysokopoziomowych zaś nie zawsze ją znają. Ba! Wręcz powiedziałbym, że rzadko. Nie bój się, jeśli nie wiesz, ten temat poruszymy w książce, ale nieco później.

Jest to jednak mała cena, jaką trzeba za płacić w porównaniu z tym, co ta ekspresywność i wysoka abstrakcja oferuje. 

Po prostu to problem łatwy do naprawienia – wystarczy trochę chęci, by poczytać kapkę więcej. A czas, który poświęcimy na zgłębienie tych różnych tematów, jest o wiele krótszy niż czas, który poświęcilibyśmy, pisząc swój program w języku o niższym stopniu abstrakcji/ekspresywności.

### Python nie istnieje w świecie mobile

Aplikacje mobilne i Python to raczej dwa odmienne światy. Tak po prostu i już. Na pewno istnieją projekty próbujące coś w tym zakresie wskórać, ale nie ma co się łudzić na to, że znając tylko Pythona, stworzymy fajną appkę na Androida.

Jak ktoś ci mówi inaczej, to lepiej olej typa, bo Python mu wszedł za mocno i bredzi.

### Zbytnia wygoda

Często może być tak, że po tym, jak zaczniesz pisać w Pythonie, przesiadka na inne języki, gdzie pewne rzeczy musisz zrobić zupełnie inaczej, jest troszkę bolesna. To również potencjalna wada Pythona.

Piszesz sobie szczęśliwie swoje programy w Pythonie, sporo rzeczy robisz jedną linijką kodu, jest fajnie pięknie, ale nagle przychodzi ci napisać coś w Javie i następuje brutalne zderzenie z rzeczywistością, które powoduje, iż lądujesz w otchłaniach ciemności, rozpaczy i depresji, twoje życie traci sens a żona musi rano zrzucać cię z łóżka, co byś wstał. Nie no, żartuje, pisanie w Javie nie jest takie złe, nie mam nic do języka. Po prostu mało który język jest tak fajny, jak Python.

### Tyle

Pisząc o wadach i zaletach Pythona, starałem się być w miarę obiektywny. Oczywiście jest to niezbyt możliwe z racji tego, że to książka jest o Pythonie, a ja sam jestem jego entuzjastą. Niemniej jednak uważam, że udało mi się przestawić Ci mocne i słabe strony Pythona, dzięki czemu możesz zdecydować czy warto się go uczyć. Moim zdaniem jak najbardziej tak!

Poza tym, kurka, jak już masz tę książkę, to korzystaj i się ucz!

## Kto używa Pythona?

W tym wypadku lepiej byłoby zapytać o to, kto Pythona nie używa.

Dla przykładu jednak podam kilka mniej lub bardziej znanych firm, które z Pythona korzystają, są to: ILM, Google, Facebook, Instagram, Spotify, Quora, Netflix, Dropbox, Reddit, NASA, NSA, Red Hat, Nokia, IBM, Nasdaq, Sephora, Citi, Toyota, Gartner, Atlassian, Evernote, Lego, WebMD, Telefonica.

Cały YouTube w zasadzie stoi (stał) na Pythonie. W Google mówi się: ‘Tam, gdzie możemy – Python, tam, gdzie musimy – C++’ (podobno).

Całkiem sporo, prawda? No cóż, nic dziwnego, z racji tego, że Python, według indeksu TIOBE jest obecnie 3. najpopularniejszym językiem programowania na świecie. Nad nim są już tylko Java, C, C++. Dodatkowo Python co roku zdobywa coraz większą popularność i rośnie w siłę. Jak to ktoś kiedyś powiedział, niekoniecznie mądry, `tej siły już nie powstrzymacie`.

Poniżej widzicie tabelke z indeksem TIOBE, który to, powiedzmy, jest standardem w świecie programowania, jeśli chodzi o mierzenie popularności pewnych technologii, trendów i tak dalej.


|Sep 2019|Sep 2018|Change|Programming Language|Ratings|Change|
|--- |--- |--- |--- |--- |--- |
|1|1||Java|16.661%|-0.78%|
|2|2||C|15.205%|-0.24%|
|3|3||Python|9.874%|+2.22%|
|4|4||C++|5.635%|-1.76%|
|5|6||C#|3.399%|+0.10%|
|6|5||Visual Basic .NET|3.291%|-2.02%|
|7|8||JavaScript|2.128%|-0.00%|
|8|9||SQL|1.944%|-0.12%|
|9|7||PHP|1.863%|-0.91%|
|10|10||Objective-C|1.840%|+0.33%|
|11|34||Groovy|1.502%|+1.20%|
|12|14||Assembly language|1.378%|+0.15%|
|13|11||Delphi/Object Pascal|1.335%|+0.04%|
|14|16||Go|1.220%|+0.14%|


Jak widać, Python spokojnie pokonuje takie języki, jak C#, PHP, JavaScript, SQL, R, czy Ruby. Tego ostatniego w zasadzie 8-krotnie.

Przyszłościowy ten wąż.

Naprawdę uważam, że obecnie znajdujemy się w punkcie, lub dość blisko takiego punktu, gdzie w Pythonie zostało napisane zbyt dużo kodu, by w przyszłości został on wyparty. Zerknijmy na to, jak Python zyskuje popularność na przestrzeni lat.


|Programming Language|2019|2014|2009|2004|1999|1994|1989|
|--- |--- |--- |--- |--- |--- |--- |--- |
|Java|1|2|1|1|9|-|-|
|C|2|1|2|2|1|1|1|
|Python|3|7|5|6|23|21|-|
|C++|4|4|3|3|2|2|2|


Imponujące, prawda? 20 lat temu Python nie znajdował się nawet w czołowej 20. W 2004 już 6. A teraz? Na podium.

Popatrzcie też na starego potwora - COBOLa– mimo tego, że nie był to jakoś bardzo przemyślany czy piękny język, to do dziś jest on rozwijany i używany z racji tego, ze swego czasu sporo softu się w nim pisało, zwłaszcza dla banków i najzwyczajniej w świecie pozbycie się wszystkich systemów działających na podstawie tego języka i przepisaniu ich na coś nowszego, byłoby zbyt kosztowne.

Czyli mimo tego, że COBOL jest językiem dość specjalistycznym, o wąskim zastosowaniu, to wciąż jest używany, a przecież pierwsze wzmianki o COBOLU pochodzą z roku 1959, czyli na upartego, jeśli ktoś chce, może dziś programować w technologi sprzed w zasadzie 60 lat i znajdzie w tym pracę.

Do przyjemnych to raczej nie należy, ale cóż. Można? Można.

Jak już wcześniej wspomniałem o Pythonie – tej siły już nie powstrzymacie. Python przyszedł, rozgościł się i na razie nigdzie się nie wybiera, a prawdopodobnie zostanie na dobre. 

Tego ostatniego pewien nie jestem, oczywiście jako programista Pythona będę się starał, by tak było – dokładając swoją cegiełkę i tworząc jak najwięcej kodu w Pythonie, niemniej jednak (jeszcze) gwarancji dać nie mogę na to, że zostanie on z nami na zawsze. 

Mogę ją dać na co innego – że w przeciągu następnych 15 lat Python nie zostanie wyparty z ogólnie pojętego programowania popularnego i nie będzie problemem, by znaleźć pracę, znając ten język, także, jeśli o to się boisz, to masz moje słowo, że tak nie będzie.

Zatem idąc w Pythona, robisz dość mądry ruch, jeśli chodzi o twoją karierę. To zrób to, posłuchaj Górskiego, i do dzieła.


## Python w porównianiu z...

### Javą/C#

Wrzucę te dwa języki do jednego worka, ku oburzeniu niektórych. Zaraz mi się tu zlecą fanboje z hejtem, ale co tam.

Niemniej jednak zacznijmy od tego, że oba te języki wspierane są/kierują nimi wielkie korporacje. Python nie. Dla jednych to wada, dla innych zaleta. Python jest też zdecydowanie prostszy w nauce od tych dwóch języków, bez dwóch zdań.

Jest też o wiele bardziej ekspresywny – kod jest zazwyczaj krótszy, o wiele krótszy.

Niestety, często też wolniejszy od jednego, jak i drugiego.

Python jest również mniej popularny od Javy, która jest obecnie na samym szczycie i to bez dwóch zdań, ale za to też wyraźnie popularniejszy niż C#.

Do tego Java/C# jest częściej wykorzystywana przez duże korporacje aniżeli Python. Ogromne projekty to często domena Javy czy C#. Dla mnie kolejna wada.

### Perlem

Cóż, mało kto obecnie używa Perla, ale z racji tego, że niegdyś często porównywano te dwa języki, to wspomnę i o nim. Osobiście nigdy nie pisałem w Perlu, lecz zdarzało mi się widzieć kod w nim napisany.

Ewidentnie bywa on czasami niezbyt czytelny, a ilość stosowanych w Perlu nawiasów potrafi człowieka przytłoczyć. Python jest też obecnie znacznie popularniejszy niż Perl. Przytłaczająco popularniejszy. Nie będę się zatem dalej nad tym porównaniem rozwodził, bo to sensu nie ma.

### C

C jest językiem ‘drobnym’ - jego core jest niewielkie, ale dające niesamowite możliwości, niemniej jednak wciąż jest to język opatrzony pewnymi ograniczeniami.

C króluje w miejscach, gdzie Python nie ma racji bytu – sterowniki, embedded, aplikacje, gdzie naprawdę krytyczna jest szybkość lub też wydajność. W C programista jest w stanie co do bajtu zarządzać pamięcią wykorzystywaną przez jego program. W Pythonie? Zapomnij o czymś takim.

Python jest zatem od C o wiele wolniejszy, zajmuje więcej pamięci. W zamian za to zyskujemy o wiele większą ekspresywność, szybkość pisania kodu i bezpieczeństwo – Python jest po prostu prostszym językiem w porównaniu do C, lecz raczej nigdy się ich nie porównuje.  Dlaczego? 

Gdyż domyślna implementacja Pythona napisana jest właśnie w… C to raz, a dwa, służą one zupełnie innym zadaniom. Są to języki, powiedziałbym, komplementarne, a nie przeciwne, gdyż dobrze uzupełniają się w swoich wadach.

Dużo bibliotek, które dla szybkości, pisze się w C, ma swoje wrappery, napisane w Pythonie właśnie. Co to te wrappery? Pomyśl sobie o swoim samochodzie. W środku ma on prawdopodobnie dość skomplikowany komputer. Ty, jako użytkownik, jesteś w stanie z nim prosto obcować za pomocą różnych guziczków, przycisków, menu i tak dalej – łatwa rzecz. Samodzielnie jednak nie jesteś w stanie modyfikować tego, jak ten system konkretnie działa, co robi w jakiej sytuacji itd., ale nie przeszkadza to jakoś bardzo, bo w 99% nie ma takiej potrzeby, a dla tego 1% brak sensu, by porzucać samochód i zacząć chodzić na piechotę. A jak już potrzebujesz zmienić coś w tym, jak ten komputer działa… Takie rzeczy może zrobić mechanik za pomocą konkretnych narzędzi i modyfikacji softu.

Python i jego programista jest tutaj tobą, a C to komputer pokładowy samochodu. 

Tam, gdzie potrzebna jest niesamowita wydajność, którą pokonać może chyba tylko Assembly, można użyć C, tam, gdzie ważniejsza jest czytelność i szybkość produkcji kodu, można użyć Pythona. Super kombo. Swoją drogą to spora część programistów Pythona zna również C. To chyba naturalna kolej rzeczy.

Koniec tych porównań, bo można by tak bez końca. W tej chwili sam powinieneś dobrze znać silne strony Pythona, jak i te słabe.

## Alternatywne implementacje

Jak wspomniałem gdzieś po drodze, Python to język, który posiada swój interpreter służący do uruchamiania programów napisanych w tymże języku. Czyli to taki program do odpalania programów. Incepcja. We need to go deeper.

Standardowo ten interpreter napisany jest w języku C – czyli CPython. Istnieją jednak inne implementacje tego interpretera, które czasem mają inne priorytety niż CPython, rozszerzają jego funkcjonalność czy po prostu są napisane w innym języku, bo tak i już, bo można. Kto bogatemu zabroni.

Oczywiście, nie wszystkie z nich spełniają w pełni założenie pełnej kompatybilności z całym standardem Pythona, niektóre nieco od tego odbiegają, nie są czymś praktycznym, a raczej takim proof-of-concept – po prostu czymś zrobionym tylko dlatego, że można. 

### Stackless Python

Zacznę może od implementacji zwaną Stackless Python, która bazuje na CPythonie, z tym że skupia się ona na współbieżności, wielowątkowości, czyli po prostu rozszerza CPythona, poprawiając pewne rzeczy, w których on akurat nie jest może zbyt dobry domyślnie. Takie tam różne tematy związane z GILem i spółką.

### Cython

Cython to nic innego jak, w zasadzie, kompilator Pythona do… C. Piszesz kod w Pythonie, a w efekcie otrzymujesz program działający z prędkością programu napisanego w C. Nieźle. Nie jest to co prawda kompletna implementacja tego języka a, jak wspomniałem, ‘tłumacz’ do C, ale o takich narzędziach też napiszę.

### PyPy

Python napisany w… Pythonie. Incepcja. We need to go deeper. Z drugiej strony nic dziwnego, w końcu, z tego, co kojarzę, to od pewnej wersji, kompilator Go też jest napisany w Go. Podobnie z innymi nowoczesnymi językami.

Jest to jedna z trzech implementacji, które są raczej praktycznie w 100% kompatybilne ze standardową implementacją Pythona. Cóż takiego ciekawego jest w tej implementacji? 

Otóż fakt, że posiada ona JIT – kompilator Just In Time, znany, chociażby z Javy. Co to takiego?

Kompilator JIT to taki kompilator, który działa dopiero po uruchomieniu danego programu i kompiluje nasz akurat używany fragment kodu w locie, często do formy natywnej dla danego CPU to raz, a dwa, że kompilator JIT ma zazwyczaj informację o środowisku uruchomieniowym, co pozwala mu poczynić lepsze optymalizacje względem statycznego kompilatora, który tych informacji nie posiada. O co tu chodzi?

CPython ‘kompiluje’ nasz kod Pythonowy, do bajtkodu zrozumiałego dla maszyny wirtualnej Pythona, która to następnie wykonuje zadany bajtkod, który skompilowany został przed uruchomieniem skryptu. PyPy robi to ‘w locie’, mając możliwość czynienia lepszych optymalizacji niż statyczny kompilator.

Dlaczego zatem PyPy nie jest domyślną implementacją, skoro jest szybszy, niby lepszy? Otóż by kod został wykonany szybciej, musi być spełnione kilka warunków.

Przede wszystkim PyPy i jego JIT potrzebują chwili, by się ‘rozgrzać’ - czyli nasz skrypt musi wykonywać się przynajmniej kilka sekund, by mieć możliwość zyskania przyśpieszenia w związku z użyciem PyPy.

Drugim wymogiem jest to, że wąskim gardłem naszego programu muszą być Pythonowe instrukcje, a nie np. instrukcje zawarte w jakiś modułach wewnętrznych napisanych w C.

Jeśli te wymogi są spełnione, to bardzo prawdopodobne jest, że użycie PyPy przyśpieszy wykonanie naszego programu i być może nawet zmniejszy zużycie pamięci. W innych przypadkach… Cóż… Prawdopodobnie nie zyskamy zbyt dużo na użyciu PyPy. O PyPy wypowiada się nawet sam twórca Pythona – Guido van Rossum.

> “Jeśli chcesz przyśpieszyć swój kod, to prawdopodobnie powinieneś użyć PyPy.” Guido Van Rossum – twórca Pythona

Dodatkowo PyPy domyślnie implementuje np. cechy z Stackless Python, czy Sandboxing, który obecnie jest jeszcze raczej prototypem niż produkcyjną implementacją, ale wciąż.

### IronPython

Python i C#. Co go wyróżnia? Przede wszystkim to, że nie ma GIL’a, to, że można korzystać z biblioteki .NETowej, łatwo można go osadzać w aplikacjach .NET. Druga z głównych alternatywnych implementacji, która raczej spełnia standard Pythona.

### Jython

Python na wirtualnej maszynie Javy. Zalety? Łatwa integracja z programami Javowymi, możliwa kompilacja programów Pythonowych do klas Javowych. Programy uruchamianie na wirtualnej maszynie Jythona mają pełen dostęp do klas i API Javy. Można go też kompilować statycznie i tworzyć servlety, applety, beany. Jython również jest wielowątkowy w prawdziwym tego słowa znaczeniu, czyli nie musimy się tutaj martwić GIL’em. Trzecia, ostatnia, praktycznie w 100% kompatybilna implementacja.

### Brython

Brython to wynalazek, który sprawia, że twój kod, napisany w Pythonie, zadziała w… przeglądarce, po stronie klienta poprzez tłumaczenie Pythona do JavaScriptu. Aktywnie utrzymywany i w miarę aktualny. Ciekawy projekt.

Z innych implementacji wspierających kompilację do JS, istnieją: RapydScrypt, Transcrypt.

### MicroPython

Mówiłem, że Python na mikro-kontrolerach to niezbyt, prawda? Cóż, ten projekt ma na celu to zmienić. Podobnie jak PyMite.

### CLPython

Python zaimplementowany w język Common Lisp. Podobnie jak Jython czy IronPython, CLPython może mieszać kod Pythonowy z kodem języka, w którym został napisany, ma dostęp do jego bibliotek.

### TinyPy

Python w 64Kb kodu. Bo tak.


Oprócz tego istnieją implementacje Pythona w Haskelu, PHP, JavaScripcie, Rubiniusie i innych różnorakich wynalazkach jak połączenie LOLCODU z Pythonem czy Like, Python.

## Podsumowanie

Starczy już tej całej teorii i gadania, streśćmy zatem to, o czym do tej pory powiedziałem.

Python jest ogólnego przeznaczenia dynamicznie typowanym językiem interpretowanym, którego zaletami są ekspresywność, społeczność, ilość gotowych rozwiązań, szybkość tworzenia aplikacji oraz czytelność kodu w nim tworzonego, łatwość w nauce.

Dobrze sprawdza się w webdevie, skryptach, zastosowaniach naukowych, związanych z Data Science czy podobnymi dziedzinami.  Nieco gorzej radzi sobie w aplikacjach wielowątkowych, tych, które wymagają bardzo wysokiej wydajności czy też w środowisku z mocno ograniczonymi zasobami. Dodatkowo Python nie istnieje w świecie tworzenia appek mobilnych, gier czy desktopowych.

Niemniej istnieją rozwiązania na różne bolączki Pythona związane z tymi problemami, jedne lepsze, inne gorsze, ale są. Nie zmienia to faktu, że jest on lepiej przystosowany do pewnych zadań, niż do innych i warto o tym pomyśleć, przy wyborze technologii do danej aplikacji.

## Pytania
1. Na jakiej wersji Pythona będziemy się skupiać i dlaczego?
1. Podaj przykłady, przynajmniej 3, obecnie popularnych zastosowań Pythona.
1. W jakich zastosowaniach Python nie jest zbyt dobry?
1. Podaj kilka zalet Pythona, jak i jego wad. Kto z niego korzysta? Do czego można go użyć?
1. Podaj przykłady alternatywnych implementacji Pythona – poza Cpythonem.
1. Jakie są główne założenia Pythona?
1. Jak Python wypada w porównaniu do Javy? Główne różnice/cele.
1. Czy Python działa na wielu platformach? Jeśli tak, to na jakich? Wymień 3+.
1. Jakim językiem jest Python, statycznie czy dynamicznie typowanym? Co to znaczy?
1. W jaki sposób ogranicza nas GIL – tak w skrócie?

\pagebreak
