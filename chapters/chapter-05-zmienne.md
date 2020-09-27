# Zmienne, wprowadzenie

Dobrze, trochę sobie poprintowaliśmy, jest okej. Nie jest to jednak coś bardzo ekscytującego. Czy Python potrafi coś innego w ogóle? W innym wypadku to taki słaby z niego język w sumie. Oczywiście, że umie dużo więcej.

## Zapamiętywanie wartości

Następnym pojęciem, jakie chciałbym przedstawić, jest idea zmiennych.

O co tu chodzi? Już tłumaczę.

Mamy sobie ten nasz komputer. Ma on jakąś tam pamięć, czy to RAM, czy dyskową, prawda? Prawda. Jest ona dość pojemna, szybka, czasem trwała nawet. Fajnie by zatem było móc z niej korzystać w jakiś sposób podczas programowania. Nasze mózgi to myślenia to nadają się całkiem dobrze, ale do pamiętania różnych rzeczy już gorzej,, zwłaszcza trwałego.

Takim podstawowym narzędziem, z którego korzystamy, żeby coś sobie zapisać lub wyciągnąć z pamięci komputera, są właśnie zmienne/stałe.

To sposób, by do pamięci komputera wrzucić jakąś wartość i przypisać jej swego rodzaju identyfikator, by później można było z niej normalnie korzystać. Jak to wygląda w Pythonie? Prosta sprawa.

```python
nazwa_zmiennej = wartość
```

Gdzie wartość jest praktycznie dowolna.

Nazwa za to już nie jest – są pewne zasady, których musimy się trzymać podczas nazywania zmiennych jak chociażby to, że nie może się ona zaczynać od cyfry, musi od litery czy znaku _.


## Nazwy zmiennych

W nazwach zmiennych możemy stosować również polskie znaki, ale nie róbmy tego. Bo nie. 

Zmienne nazywamy po angielsku, korzystając przy tym ze snake case - to taka praktyka, gdzie poszczególne wyrazy w nazwie zmiennej dzielimy od siebie za pomocą znaku _. Trzymaj się tego, bo to ważne, bardzo ważne.

Teoretycznie rzecz ujmując, jeśli pracujesz w 100% polskim zespole, gdzie masz pewność, że w przyszłości NA PEWNO nikt, kto polskiego nie zna, nie będzie czytał tego kodu (czyli nigdy), to okej. Teoretycznie możnaby pisać kod po polsku, ale... Nie jest to ogółem dobra praktyka, proszę, nie rób tego o ile tylko możesz. Czasem mogą cię przymusić na przykład przy projektach z sektoru publicznego, realizowanych przez pewne duże korporacje, ale to nie do końca są projekty, w których chcesz się znaleźć.

Czyli sprawa ma się tak: zmienne i wszystko w naszym kodzie nazywamy opisowo, tak by od razu było wiadomo, co dany kawałek kodu robi, co znajduje się w zmiennej. Nie przesadzajmy jednak w drugą stronę – nazwą zmiennej nie powinien być cały poemat. Do tego w nazwach raczej używamy tylko liter, cyfr(rzadziej), podkreślenia. Tutaj konserwatywnie i bez szału. Zwięzłe, trafne nazwy.

Dlaczego? Poprawne nazywanie zmiennych, funkcji, klas i wszystkiego w twoim kodzie, sprawia, że jest on czytelny, że jest on zrozumiały. Po prostu. Musisz to robić. Tak, od samego początku. Wyrobi to w tobie dobry nawyk, który jest krytycznie ważny.

Pozwól, że rzucę ci przykładem.

```python
 def redirect_logged_in_user(self, request, *args, **kwargs):
        if self.redirect_authenticated_user:
            redirect_to = resolve_url(settings.REDIRECT_URL)
            if redirect_to == request.path:
                raise ValueError(
                    "Redirection loop detected. Check that your"
                    "REDIRECT_URL doesn't point to a login page."
                )
            return HttpResponseRedirect(redirect_to)
        return super().dispatch(request, *args, **kwargs)
```

Nawet nie znając zbytnio języka, a jedynie angielski, wychodzi na to, że dość szybko idzie się domyślić, co ten kod robi. Żeby nie było – to jest autentyczny kawałeczek z kodu produkcyjnego. Trochę zmieniony, ale sens zachowany.

Konkretnie chodzi o to, że to jakaś funkcja/metoda czy coś tam, co bierze jakieś żądanie, czyli pewnie jakaś web aplikacja, sprawdza, czy powinno się przekierowywać zalogowanych użytkowników i wtedy, jeśli użytkownik jest zalogowany a przekierowywanie jest włączone, to go przekierowuje gdzieś, a gdzie go ma przekierować, to zależy od jakiejś zmiennej REDIRECT_URL z settingsów, czyli ustawień, czyli pewnie jakaś konfiguracja. 

Jeśli nie znacie angielskiego, to nic, spróbujcie to przetłumaczyć na własny rachunek. Googlujcie nawet słowo po słowie, a okaże się, że naprawdę bardzo szybko można dojść do tego, co dany kod robi. Wystarczy trochę znajomości języka i niewielki kontekst informatyczny odnośnie tego, jakie zwyczaje mają programiści w nazywaniu pewnych rzeczy, konkretnych terminów i ich znaczeń.

No i przy okazji sprawdza się, czy to `gdzieś`, w które mamy przekierować użytkownika, nie jest przypadkiem miejscem, w którym się znajdujemy, bo wtedy nam się nieskończona pętla stworzy. Ciągłe przekierowania. Nieskończona pętla. 

Teraz, dla kontr przykładu, kod z **nieco** mniej opisowymi nazwami.


```python
   def rdr_lg_usr(self, r, *args, **kwargs):
        if self.rau and r.u.ath:
            to = rslv(stings.TO)
            if to == r.pt:
                raise VEr(
                    "Redirection loop detected. Check that your"
                    "REDIRECT_URL doesn't point to a login page."
                )
            return HttpRR(to)
        return super().dp(r, *args, **kwargs)
```

Nie wiem jak wam, ale mnie ten kod nic nie mówi w zasadzie. No dobra, na podstawie pewnych informacji, mogę się domyślać niektórych rzeczy, wywnioskować je z kontekstu, ale…

To nie tak powinno wyglądać. Absolutnie. Za każdym razem, kiedy widzę jakikolwiek produkcyjnie wypuszczony kod, który wygląda jakoś podobnie, dostaje raka. Potem mój rak dostaje raka. 

I tak sobie obaj siedzimy, ja i mój rak, i płaczemy, bo obaj mamy raka. I po co było czytać taki kod? Jeszcze gorzej – czasami trzeba z czymś takim pracować, bo jakiś jełop zdecydował, że jak sobie skróci `redirect` do `rr`, to te 6 literek co sobie zaoszczędził, zbawi jego świat, jego piękne palce, codebase i wszystko inne. A idźże mnie pan z tym.

Czasami, naprawdę, bardzo, ale to bardzo rzadko trafia się taka okoliczność, gdzie faktycznie można coś tam skrócić. Są to jednak zdecydowanie wyjątki od reguły. To takie miejsca, gdzie nawet jak rzucisz skrótem, to każdy będzie wiedział o co chodzi. Ewentualnie jak masz adnotacje typów, to też czasem ułatwia sprawę i umożliwia pewne ustępstwa.

Trzeba doliczyć tu też fakt, że ja oczywiście tutaj mocno przejaskrawiam przykład, ale chodzi o to, by pokazać pewien fakt.

Zatem jak widzisz – nazwy są krytycznie ważne a każdemu, co tworzy kod jak ten w drugim przykładzie, trzeba zasądzić a) rentę z racji braku mózgu b) wyrok 15 lat kodzenia w legacy code napisanym w C++, jako gratis.

Także tak.

## No po co mi to wszystko?
Znowu – Riedel zadał dobre pytanie. Już mówiłem – komputer jest lepszy w pamiętaniu rzeczy niż ty. To po pierwsze. Po drugie dochodzi tutaj inna kwestia – lenistwa. Załóżmy sobie, że mamy jakieś imię, które chcemy zapamiętać.

Wchodzi nam do pokoju Prorok i chce, żebyśmy mu wyprintowali kilka część jego przemowy:

`Dobry wieczór. Coś się... coś się popsuło i nie było mnie słychać, to powtórzę jeszcze raz(...)`

Dlaczego? Nie pytaj, zrób to. Szybko, szybko, zanim zdamy sobię sprawę, że to bez sensu.

```python
print("Dobry wieczór. Coś się... coś się popsuło...")
print("Dobry wieczór. Coś się... coś się popsuło...")
print("Dobry wieczór. Coś się... coś się popsuło...")
print("Dobry wieczór. Coś się... coś się popsuło...")
```

i done, prawda? Tylko tak. To jest albo bardzo dużo pisania, albo dużo kopiego pasty (metoda kopiego pasty polega na kopiowaniu i wklejaniu czegoś - przypominam skromnie dla tych mniej obeznanych). Oba rozwiązania nie są za dobre. 

I tu zmienne wchodzą całe na biało, jak UTF-8 w poprzednim rozdziale.

``` python
prophet_lyrics = "Dobry wieczór. Coś się... coś się popsuło..."
print(prophet_lyrics)
print(prophet_lyrics)
print(prophet_lyrics)
print(prophet_lyrics)
```

Inny przykład – załóżmy, że chcemy sobie jakieś dokładne obliczenia matematyczne porobić, do których potrzebujemy liczby PI z dużą dokładnością. I co, za każdym razem będziemy pisać `3.14159265359…` czy może po prostu zrobimy tak:

```python
PI = 3.14159265359
print(PI)
```

Krócej, prawda? Tak mi się wydaje. To oczywiście dość słaby przykład, ale obrazuje to, co chcę przedstawić. A jeszcze taka notka: normalnie to tak nie róbcie, bo Python ma już sam w sobie zdefiniowaną PI, wystarczy ją zaimportować. Co to dokładnie znaczy, omówimy później, ale jakby w następnych rozdziałach PI była wam do czegoś potrzebna, to zróbcie tak:

```python 
from math import pi
print(pi)
```

I gotowe!

## Znowu trochę teorii

Wróćmy do tego, co lubię. Czyli zgłębiania tego, dlaczego, co i jak.

Te nasze zmienne całe. Na czym one polegają? Jak komputer je rozumie? A no dość prosto, zatem już tłumaczę.

Najpierw omówimy taki ogólny model tego, jak komputer widzi zmienne.

Otóż sprawa ma się tak, że za każdym razem, kiedy tworzymy nową zmienną, nasz komputer sprytnie sobie działa i robi coś na takiej zasadzie, że asocjuje niejako daną zmienną, a raczej jej nazwę, z jakimś konkretnym adresem w pamięci.

W zasadzie to nawet nie komputer a kompilator/interpreter, ale to tam nie wnikajmy na razie.

Co to znaczy w praktyce i z czego wynika?

Jak wcześnie już ustaliliśmy, komputer rozumie tylko zera i jedynki. Nic więcej. Musi sobie zatem wszystko tłumaczyć na rzeczy zrozumiałe dla niego.

Nie inaczej jest w przypadku zmiennych. Kiedy w kodzie zapisujemy coś pokroju:

```python
new_variable = "TEXT"
```

Pod spodem interpreter Pythona robi sobie taki myk, który asocjuje w prosty sposób kawałek tekstu, czyli `new_variable` z jakimś adresem w pamięci, jakąś lokalizacją. Bo nie wiem, czy pamiętasz, ale chwilkę temu mówiłem, że zmienne są przechowywane w pamięci. No właśnie. Zatem, żeby komputer wiedział, gdzie ma konkretnie szukać jakiejś wartości, podaje mu się adres, pod którym ta wartość się znajduje.

A jak wygląda ta pamięć komputera? Nie inaczej niż taka bardzo długa linijka z ponumerowanymi komóreczkami. Wyobraź sobie niesamowicie długi rząd komórek ustawionych obok siebie. W tych komórkach mogą znajdować się dwie wartości – 0 albo 1. Tak właśnie działa pamięć komputera.

Teraz w tych komórkach zapisujemy sobie nasze zmienne, dane. Tak jak mówiłem, żeby później móc ich znowu używać, żeby komputer wiedział, skąd ma zaczytać raz zapisane już dane, potrzebujemy adresu tych danych. Adres jest niczym innym, jak tak zwanym przesunięciem. To liczba bitów/bajtów (zależy od notacji), jaką należy się przesunąć od początku pamięci, by znaleźć daną wartość. Wtedy nasz sprzęt sobie tam skoczy, pod konkretny adres. Przeczyta, co musi i zwróci nam to, żebyśmy my nie musieli pamiętać.

## Heksadecymalne liczby

Teraz małe wtrącenie – pamiętasz, jak mówiłem o tym, że system binarny jest nieco rozlazły? Otóż z racji tego, że chociażby pamięć adresowa w komputerze zazwyczaj ma bardzo dużo możliwych adresów, mamy coś takiego jak system szesnastkowy, czyli heksadecymalny.  Podobna idea co system dwójkowy, ale zamiast dwóch cyfr, czy dziesięciu jak w dziesiętnym, mamy tutaj szesnaście.

Dlaczego szesnaście? Łatwo się przelicza pomiędzy nim a dwójkowym i jest zwięzły, bo duże liczby można wyrazić za pomocą małej liczby cyfr, gdyż bazujemy tu na potęgach szesnastki, a jeśli potęgi wchodzą w grę to wzrost/spadek jest wykładniczy, nie inaczej jest jeśli o długość zapisu idzie. 

Do tego liczby w binarnym ładnie się tłumaczą na heksa.

Wszystko jest analogiczne do teorii z systemu binarnego, więc przypomnij sobie, jak to tam wyglądało np. z przeliczaniem i po prostu zrób analogicznie w systemie heksadecymalnym. Jak samodzielnie się nie uda, to pogoogluj. Jakie są tam ‘cyfry’? A no takie:


| HEX | 0  |  1 | 2  | 3  | 4  | 5  | 6  | 7  | 8  | 9  | A  | B  | C  | D  | E | F |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---| --- | --- |
| DEC |  0 |  1 |  2 |   3|   4|   5|  6 |  7 |  8 |  9 |  10 |  11 |  12 | 13  |14  | 15 |

Czyli tak w skrócie: cyfry z dziesiętnego + 6 pierwszych liter alfabetu.

W każdym razie. Pamiętaj zatem, że pamięć zazwyczaj adresujemy za pomocą systemu heksadecymalnego, a liczby w nim zapisane zazwyczaj oznaczamy przedrostkiem 0x, analogicznie jak w przypadku binarnego, gdzie było 0b.

![Przedstawienie pamięci](/home/grski/dev/private/junior-python/chapters/resources/images/adresowanie1.png)

(Tak, wiem piękne bazgroły. Nie umiem into profesjonalne ilustracje, więc są ręczne.)

Wracając do tematu. Przeciętny komputer ma obecnie jakieś minimum 4 GB RAMU. To około 4 miliardy bajtów. Czyli 32 miliardy bitów. Sporo. Dlatego też adresujemy hexem. Adresy będą krótsze w prezentacji. Zdecydowanie krótsze.

To teraz wyobraź sobie takie 32 miliardy bitów, każdy jako jedna komóreczka, te komóreczki są koło siebie w linii ciągłej. To, w dużym uproszczeniu, tak wygląda pamięć twojego komputera.

Mała uwaga. Z racji tego, że bit to taka malutka jednostka, to obecnie raczej adresujemy za pomocą bajtów. Czyli adres w pamięci – nic innego jak liczba, jest liczbą bajtów, o które trzeba się przesunąć od początku pamięci, by dorwać się do danej wartości. 

Zatem jeśli interpreter kojarzy nam, że `new_variable` to ogółem adres `0x123`, to za każdym razem, kiedy będziemy się odwoływać do `new_variable`, nasz interpreter przesunie się o `0x123` bajty od początku pamięci i stamtąd sobie weźmie wartość.

Tylko moment, chwila…

## Kiedy przestać czytać?

Bo adres początkowy ma, ale końcowego tak niezbyt. Co teraz? Już mówię. Znowu wrócimy sobie do C i innych archaicznych rzeczy.

Zacznijmy od takiego kodu:

```c
#include <stdio.h>

void main() {
    short a = 1;
    a += 1;
    short b = 4;
    char z = ##### TAJEMNICA #####;
    printf(z);
    int c = 4;
    int h = 5;
    printf(c);
}
```



Spróbuj przeanalizować ten kod samodzielnie i pomyśleć co tu się stało. Nie jest aż taki trudny. Generalnie zadeklarowaliśmy sobie kilka zmiennych - `a, b, c, h, z` i wydrukowaliśmy z oraz c.

Resztę omówimy niżej, ale spróbuj najpierw wywnioskować coś samodzielnie!

I teraz uwaga, zrobimy mały trik. Otóż spojrzymy na to, jaki kod wygeneruje z tego kompilator. W tym wypadku `x86-64 gcc 9.3`. Popatrzmy jakie instrukcja dla procesora nasz kompilator wypluł, jaki kod `Assembly` powstał.
Z racji rozmiaru kod na następnej stronie.

\pagebreak

``` assembly
main:
        push    rbp
        mov     rbp, rsp
        sub     rsp, 16
        mov     WORD PTR [rbp-2], 1
        movzx   eax, WORD PTR [rbp-2]
        add     eax, 1
        mov     WORD PTR [rbp-2], ax
        mov     WORD PTR [rbp-4], 4
        mov     BYTE PTR [rbp-5], 102
        
        movsx   rax, BYTE PTR [rbp-5]
        mov     rdi, rax
        mov     eax, 0
        call    printf
        
        mov     DWORD PTR [rbp-12], 4
        mov     DWORD PTR [rbp-16], 5
        mov     eax, DWORD PTR [rbp-12]
        cdqe
        mov     rdi, rax
        mov     eax, 0
        call    printf
        nop
        leave
        ret
```

Whoa. O co tu chodzi? Spokojnie, już omawiamy. Kawałek po kawałku.

``` assembly
main:
        push    rbp
        mov     rbp, rsp
        sub     rsp, 16
```

To pomińmy - nie interesuje nas w tym konkretnym przykładzie.

```assembly
        mov     WORD PTR [rbp-2], 1
```

To już nas interesuje. To odpowiednik naszego: `short a = 1;`  I co tu się dzieje? Magiczne ilustracje na pomoc!

![Rozpisane polecenie wyżej](/home/grski/dev/private/junior-python/chapters/resources/images/zmienne.png)

Okej, trochę to rozpisałem na ilustracji, teraz przejdźmy do głębszych wyjaśnień.

Nasza deklaracja `short a = 1;`   oznacza po prostu stworzenie zmiennej `a`, typu `short` i przypisaniu jej wartości `1`. Short to nieduża liczba całkowita, w tej implementacji ma akurat 16 bitów, czyli 2 bajty. W Pythonie podobny (na jakimś poziomie) zapis wyglądałby po prostu `a = 1`. Czyli tworzymy zmienną `a` o wartości 1. Tak to wygląda w C. Pora zejść poziom niżej. A co jest poziom niżej? Przypomnij sobie z poprzednich rozdziałów albo Googluj.

`mov` mówi procesorowi, żeby przenieść wartość drugiego argumentu w miejsce sprecyzowane w pierwszym argumencie.

Pierwszym argumentem jest całe to wyrażenie `WORD PTR [rbp-2]`. Oznacza ono ni mniej, ni więcej, że pod (PTR) adresem, konkretniej adresem [rbp-2], czyli `rbp` minus dwa bajty, mamy `WORD`, czyli słowo, a słowo w tej implementacji akurat to 2 bajty, czyli 16 bitów. Czym jest `rbp` - nie zajmujmy się tym teraz, niezbyt ważne. Wyobraź sobie, że to jakiś tam adres, odniesienie w pamięci, wskaźnik na coś, cokolwiek.

A jako drugi argument mamy wartość, którą trzeba tam wstawić, czyli `1`.

Przeanalizuj to sobie na spokojnie, nie jest to aż tak skomplikowane. Zwróć uwagę na to, że typ `short`, który ma rozmiar 2 bajtów w tej implemenacji, czyli 16 bitów, jakoś brzmi tak podobnie do rozmiaru, którego kompilator użył przy pierwszym argumencie, tam jest `WORD` - też 2 bajty i 16 bitów. Przypadek? 

Do tego wróć się trochę i popatrz na dalszą część tego kodu, zwłaszcza deklaracje następnych zmiennych, ich typy i fragmenty z X PTR [rbp-XD].

Po tym wszystkim powinna ci się lampka zaświecić. Odpowiadając na pytanie z początku rozdziału - skąd kompilator wie, kiedy przestać czytać? Otóż w procesie kompilacji znika coś takiego jak `a`. Jego wystąpienia zastępywane są czymś pokroju `WORD PTR [rbp-2]`. Mając to z kolei, program doskonale wie, kiedy przestać czytać i kiedy zacząć, bo mamy i adres, i ilość bajtów jaką odczytać.

Spędź chwilę czasu nad tym, pomyśl. Nie musi od razu zaskoczyć. Przeanalizuj najpierw cały ten kod. Spokojnie. Dopiero potem przejdź dalej.

## Wszystko fajnie, ale w Pythonie inaczej

Teraz tak - muszę zrobić tutaj bardzo ważną adnotację. Otóż cały czas w przykładach z tego rozdziału używam kodu z języka C i opisuję proces, który tam zachodzi przy kompilacji i tak dalej.

W Pythonie sprawa wygląda jednak trochę inaczej, jak już mówiłem. Wynika to z różnych natur tych dwóch języków, statycznie kompilowany C i dynamicznie interpretowany Python. Ta wiedza, którą ci tu przekazuje, jest jednak uniwersalna, bo o ile na wyższym poziomie, czyli tym, co jest płytko pod powierzchnią, Python tak nie wygląda, to na najniższym poziomie już jak najbardziej - w końcu CPython napisany jest w.... C.

W Pythonie mechanizm deklaracji zmiennych wygląda troszkę inaczej (jak, to porozmawiamy innym razem) i tak dalej, ale logika jest, powiedzmy, gdzieś tam zachowana. Prościej jednak jest mi tłumaczyć na przykładzie z C i Assembly. Dlaczego? Bo w Pythonie, podczas interpretacji, zastosowanych zostaje milion różnych trików optymalizacyjnych i różne dziwne rzeczy się tam dzieją. Dla przykładu - podczas samego startu Pythona inicjalizowanych jest około 50 tysięcy różnych obiektów, zmiennych, innych rzeczy! Nieźle, co? Dlatego na razie operujemy na "prostszym" C. Później pewnie wejdziemy trochę w te optymalizacyjne Pythonowe wątki, ale na razie nie trzeba. Także jak czasami słyszysz kompilator zamiast interpreter, wydaje ci się, że coś się pomyliło i tak dalej, to nie obawiaj się.

Do tego nie przejmuj się naprawdę, jeśli powyższe nie jest dla ciebie oczywiste, ten fragment z kodem. Na spokojnie. posiedź troszkę nad nim, to nie jest takie proste! Zastanów się, przeanalizuj samodzielnie, poguglaj nawet. To, że po sekundzie nie rozumiesz, co się tam dzieje, nie sprawia, że jesteś nierozumny czy głupi. Także do przodu!

## Typy danych

Jak już przy zmiennych, C i takich rzeczach jesteśmy, to chciałbym parę słów rzucić właśnie na temat typów zmiennych. Jak już w poprzednich rozdziałach pisałem, Python nie wymaga od nas definiowania typów dla naszych zmiennych, nie ma w nim statycznego typowania. Przypomnij sobie co to oznaczało i odpowiedz na pytanie - co oznacza brak statycznego typowania? Czym jest dynamiczne typowanie? Jakie są tego wady/zalety. Poszukaj w książce, może w odpowiedziach do poprzednich rozdziałów. Zrób to teraz.

Mimo tego dobrze wiedzieć, na jakie typy zazwyczaj dzielimy sobie różne zmienne. Dlaczego? Bo Python też ich używa, tylko sam niejako zgaduje jakiego typu użyliśmy. A więc:





\pagebreak