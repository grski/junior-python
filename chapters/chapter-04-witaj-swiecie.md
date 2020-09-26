# Witaj, Świecie!

Wreszcie zaczynamy zabawę z kodowaniem! Uf, trochę nam to zajęło, co? Tylko jakieś 50 stron. W każdym razie.

## Wypisujemy tekst na ekran

Witaj, Świecie! Te słowa, to dość popularny zwrot w programowaniu, przynajmniej ich angielska równowartość – Hello World! 

Jest to coś, co tradycyjnie uznaje się za tekst, jaki wydrukuje pierwszy program ,który początkujący programista stworzy w swej karierze – wydrukowanie napisu ‘Hello World!’ czy ‘Witaj, Świecie!’ w konsoli. 

My zrobimy podobnie, ale nieco inaczej, bo na dwa sposoby. Dlaczego? Otóż w Internecie często można spotkać się z opinią, że w Pythonie na wszystko istnieje już rozwiązanie, gotowy kod, który ktoś inny stworzył, my jedynie go importujemy, wykorzystujemy i w sumie na tym polega całe programowanie w Pythonie.

Takie sklejanie programu z gotowych klocuszków. Grunt to wiedzieć, z jakich klocuszków skleić.

Cóż, często to racja. Bardzo często. Nie inaczej jest z hello worldem.

Otóż w Pythonie, standardowy Hello World, można zastąpić:

```python
import __hello__
```

Co ukaże się naszym oczom?

```
Hello world!
```

Yup. Python nawet na hello worlda ma gotowe rozwiązanie, ale to tak bardziej w ramach ciekawostki – teraz pokażę wam, jak można wydrukować coś na ekranie za pomocą Pythona w sposób normalny.

```python
print("Witaj, Świecie!")
```

I tyle w zasadzie. W konsoli wyświetlić się: „Witaj, Świecie!”. Tylko tyle i aż tyle.

Mała notka też dla tych bardzo początkujących: jeśli nie wiesz, gdzie ten kod wpisać, to sprawa jest prosta – utwórz sobie dowolny plik, który będzie miał rozszerzenie .py, w swoim folderze roboczym, czyli CWD, zajrzyj do rozdziału o czterech jeźdźcach konsoli, jeśli już zapomniałeś, o co chodzi.

Następnie w tym pliku wpisz właśnie tę linijkę za pomocą edytora tekstu. Potem wystarczy tylko:

```bash
python nazwa_utworzonego_pliku.py
```

i gotowe. Ewentualnie zamiast python, być może będzie trzeba wpisać python3, zależy jak tam sobie poinstalowałeś wszystko.

Co tutaj się stało? Skorzystaliśmy z jednej ze wbudowanych funkcji Pythona, które umieszczone są w corze(rdzeń) języka, czyli funkcji, która każda instalacja Pythona3 posiada. Funkcja ta nazywa się print – z angielskiego, wydrukuj. 

Hmmm, co zatem może robić funkcja, która nazywa się „wydrukuj”? Dobre pytanie. Wydaje mi się, że tutaj nastąpi prawdziwy test tego, czy nadajesz się na programistę. Jeśli jesteś w stanie określić, co robi funkcja print/wydrukuj, to prawdopodobnie nadajesz się na programistę. Gratulacje.

Tejże funkcji przekazujemy argument (czyli coś, na czym funkcja ma zadziałać) w postaci tego, co ma wydrukować. Zostanie to wypisane na ekranie, razem ze znakiem nowej linii. Znak nowej linii, który automatycznie Python doklei nam do tego, co drukujemy, oznacza, że jeśli teraz użyjemy następnego printa, by znowu coś wypisać, to nasza wartość, z drugiego printa, zostanie wypisana w nowej linijce. 

Bo chodzi o to, żeby komputer wiedział, kiedy ‘entera’ nowego wyświetlić i zakończyć obecną linię. To żeby mu dać znać, kiedy ma to zrobić, mamy coś takiego jak ‘znak nowej linii’. Jak sobie enter wciskasz w Wordzie, to pod spodem tam jest wstawiany ten właśnie znak. Czyli:

```python
print("Linijka 1")
print("Linijka 2")
```

Zwróci nam, zgodnie z oczekiwaniami:

```
Linijka 1
Linijka 2
```

Znakiem końca linii jest zazwyczaj `\n`. Czyli w rzeczywistości, zamiast wyświetlić tylko `„Linijka 1”`, Python wyświetli `„Linijka 1\n”`.

Czy to wszystko proste? Anty klimatyczne? Tak. Przynajmniej pozornie. Bo pod spodem, dzieje się tu wiele bardzo, bardzo ciekawych rzeczy, o których na razie nie masz pojęcia.

To, że dziś, za pomocą jednej linijki kodu, jesteś w stanie wypisać sobie w konsoli jakiś tekst, to efekt kilkudziesięciu lat pracy i budowania fundamentów przez ojców informatyki. Wiem, że może brzmieć to śmiesznie, ale tak jest. Popatrz np. na kod Assemblera, czyli języka, w którym wszyscy kiedyś pisali.

``` nasm
segment .data
msg     db      "Hello World!", 0Ah    

segment .text
        global  _start

_start:
        mov     eax, 4
        mov     ebx, 1
        mov     ecx, msg
        mov     edx, 14
        int     80h

; wyjście z programu
        mov     eax, 1
        xor     ebx, ebx
        int     0x80
```

Wait… What? Także tak. Doceń to, co masz teraz. 

Tylko od razu zaznaczam – nie przejmuj się jeśli kompletnei nic nie rozumiesz z tego kodu. Spokojnie. Ja też nie za dużo. To nie ma znaczenia. Chodzi tylko i wyłącznie o to, by pokazać ci ciekawe, stare drogi.

A wiesz, co jest jeszcze ciekawsze? 

Fakt, że obecnie, niżej, pod spodem, Python właśnie tak wygląda. To znaczy nie sam Python – bo Python to tylko język - zbiór zasad, definicji, natomiast chodzi o CPythona – czyli implementacji interpretera Pythona, a one już mogą być dowolne, pisałem o tym wcześniej, możesz poczytać. Warto to zapamiętać, że domyślną implementacją Pythona jest CPython.

Różnica między Pythonem a CPythonem jest taka, że Python to po prostu język, czyli zbiór instrukcji i opis tego, jakie ten języka ma funkcje i jak ma się zachowywać w danych sytuacjach. 

A CPython to już konkretne implementacja tego – przetłumaczenie na zachowania komputera, konkretny program wykonujący polecenia w konkretny sposób. Także CPython != Python.

Czyli jeszcze raz powtórzmy. Python to język. Interpreter Pythona to już jakiś program, który interpretuje kod napisany w języku Python i wykonuje określone polecenia. Zazwyczaj, kiedy mówimy o interpreterze Pythona, mamy na myśli jego domyślną implementację, czyli CPythona – interpreter Pythona napisany w C, ale są inne. Pamiętaj.

Dlaczego trzeba doceniać obecne abstrakcje?

Zacznijmy od tego, że jeśli korzystasz z jakiegokolwiek w miarę współczesnego komputera, to jestem prawie pewien, że widzisz polskie znaki w wypisanym tekście, bez żadnych problemów. W ogóle widzisz ten tekst. Prawda?

Nie zawsze było to takie proste i oczywiste. 

Dlaczego?

Wynika to z tego, jak działa komputera.

## Język binarny – jedyne, co rozumie komputer

Nie wiem jak dla ciebie, ale dla mnie zawsze interesujące było to, jak działa komputer. Jak to się dzieje, że po wciśnięciu jakiegoś magicznego guziczka, energia elektryczna zaczyna ‘przepływać’ przez tę cudowną maszynę, na ekranie pojawiają się różne znaczki i wszystko jest takie piękne, fajne.

Otóż sprawa jest prosta. U samiutkich podstaw tego, jak działają komputery, leży nic innego, jak dwie proste rzeczy: Prawda i Fałsz, 0 i 1, tak i nie. Chodzi mi o system binarny, język maszynowy.

Co przez to rozumiem? Otóż komputer, to nic innego, jak taka ogromna, ogromna grupa zlepionych razem przewodników/półprzewodników, takich jakby ‘przełączników’, które mogą być ‘włączone’ lub ‘wyłączone’ - mają dwa stany. Stany te reguluje się za pomocą napięcia prądu, jaki przez przewodniki przepływa, to ono świadczy o tym, czy któryś jest włączony, czy wyłączony.

W zależności od tego, jaką mamy kombinację, które ‘przewodniki’ mamy włączone, które wyłączone, komputer będzie robił różne rzeczy. To tak jak z pralką – zależnie od tego, jakie przyciski na niej pozostawisz wciśnięte, zrobi ona coś innego.

Z racji tego, że mamy tu dwa stany, cokolwiek co ma z tym do czynienia, często okraszamy przymiotnikiem ‘binarny’. System liczb binarnych. Wybór binarny. Drzewo binarne. Ludzie binarni żyjący w świecie probabilistycznym i tak dalej.

W każdym razie. Ustalamy zatem jedno. Nasz komputer operuje tylko na dwóch wartościach – 0 i 1, czyli brak/niskie napięcie i wysokie napięcie. To wszystko. W dużym uproszczeniu to właśnie to jest kompletną podstawą całego komputera i nic więcej.

Zakładam, że moi czytelnicy to sprytni ludzie. Powinno zatem pojawić się zaraz pytanie – Ale jak to? Skoro komputer rozumie tylko 0 i 1, to jak to się dzieje, że mogę tu wpisywać różne litery, czytać je potem, mogę poruszać myszką, wpisywać inne liczby niż 0 i 1. Co? Pan coś tu ściemnia, panie Górski.

Otóż nic bardziej mylnego. Wasz komputer naprawdę rozumie tylko 0 i 1. Wszystko inne to efekt różnego rodzaju kalkulacji, przeliczeń i kodowania innych wartości do właśnie tychże 0 i 1.

Doskonałym przykładem jest tutaj ten tekst.

## Jak komputer widzi litery – system binarny

Wyobraź sobie, że wszystkie literki, które tutaj widzisz, tak naprawdę, pod spodem są niczym innym jak liczbą, zapisaną w systemie binarnym.

Dla ścisłości – czym jest liczba zapisana w systemie binarnym? To nic innego jak normalna liczba, tylko wyrażona za pomocą jedynie 0 i 1. My, jako ludzie, obraliśmy sobie jako podstawowy, system dziesiętny. Prawdopodobnie dlatego, że tyle mamy palców, ale kto tam dokładnie wie.

W każdym razie – operujemy na założeniu takim, iż mamy 10 cyfr, każda rząd wielkości może mieć 9 lub 10 możliwych stanów, lub może go nie być wcale, a rzędy wielkości opierają się na potęgach dziesiątki.

W binarnym systemie jest tak naprawdę podobnie, tyle że zamiast 10 cyfr, mamy tylko dwie i dwie wartości. Dodatkowo kolejne rzędy wielkości przeliczamy sobie nie na podstawie potęg dziesiątki a na podstawie potęg dwójki.

Weźmy, dla przykładu, liczbę 123. Jak liczymy jej wartość? Otóż.

1 – liczba setek, trzecia cyfra
2 – liczba dziesiątek, druga cyfra
3 – liczba jedności, pierwsza cyfra

$1*10^2+2*10^1+3*10^0$ = $1*100+2*10+3*1$ = $100+20+3$ = 123



Jak łatwo zauważyć, wykładnikiem potęgi jest liczba, równa numerowi cyfry, licząc od prawej strony, pomniejszona o 1. 

Brzmi to wszystko skomplikowanie, bo my tak o tym nie myślimy – robimy pewne rzeczy naturalne z racji doświadczenia, więc trochę praktyki może wymagać przestawienie się na taki sposób myślenia o tym.

Sytuacja w binarnym zapisie będzie analogiczna. Jak obliczamy wartość danej liczby w zapisie binarnym? Załóżmy, że chcemy dowiedzieć się, jaką wartość ma liczba 101101.

```
1 – 6 cyfra liczby
0 – 5 cyfra liczby
1 – 4 cyfra liczby
1 – 3 cyfra liczby
0 – 2 cyfra liczby
1 – 1 cyfra liczby
```

A zatem: \
$1*2^5+0*2^4+1*2^3+1*2^2+0*2^1+1*2^0$ \
$1*32+0*16+1*8+1*4+0*2+1*1$ \
$32+0+8+4+0+1$=45

Czyli 101101 to nic innego jak odpowiednik 45 w systemie dziesiętnym. A jak przeliczyć z systemu dziesiętnego na binarny? Bardzo prosto. 
Otóż dzielisz sobie liczbę przez dwa i za każdym razem wypisujesz resztę. \
$45/2$ = 22 reszty 1 \
$22/2$ = 11 reszty 0 \
$11/2$ = 5 reszty 1 \
$5/2$ = 2 reszty 1 \
$2/2$ = 1 reszty 0 \
$1/2$ = 0 reszty 1

Teraz, czytamy sobie reszty od DOŁU do góry: 101101. Zgadza się? Yep.

Przeanalizuj to sobie na razie dokładnie i powoli. To nic, jeśli na początku coś nie jest  jasne, to tylko sposób przeliczania z jednego systemu na drugi. 

Przydaje się tutaj znajomość wartości potęg dwójki. Gdy w pamięci masz jakąś ich część, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16386 itd., to niektóre przeliczenia staną się łatwiejsze i szybsze. 

W każdym razie. Wróćmy do tematu. Czyli… A tak. Literki to też liczby.

## Kodowanie znaków – ASCII

No właśnie. Skoro komputer rozumie tylko i wyłącznie liczby, te w systemie binarnym, czyli w zasadzie zera i jedynki, to jak mu powiedzieć, że ma przechowywać jakąś literkę?

Wyobrażacie sobie świat, w którym zamiast czytać moje słowa na ekranie za pomocą liter, czytalibyście każdą literkę zapisaną w jakiś sposób za pomocą systemu binarnego, ręcznie na kartce sobie to tłumaczyli na ludzki? Ja nie, ale mniej więcej tak to wygląda w rzeczywistości, tylko robi to za nas komputer.

Otóż kilku mądrych panów zebrało się kiedyś i stwierdzili oni, że w sumie dobrym pomysłem będzie, by niejako stworzyć tłumaczenie swego rodzaju – tłumaczenie, mapowanie liter alfabetu do… liczb. 

Każda litera alfabetu otrzymała swój unikalny kod w postaci jakiejś liczby. Dlaczego? Bo jak powiedzieć komputerowi, że ‘k’, to ‘k’? Nie da się. Komputer jest głupi, nie rozumie pojęcia litery.

Liczby w systemie dziesiętnym zaś bez problemu przekonwertujemy do liczby w systemie binarnym, czyli do czegoś, co komputer już zrozumie.

Ustalono sobie zatem coś, co nazywa się standard ASCII, czyli skrót od ang. American Standard Code for Information Interchange. To taka swego rodzaju tablica, która zawiera mapowanie znaków alfabetu angielskiego, znaków interpunkcyjnych na liczby. Taki słownik niejako, która literka, jakiej liczbie odpowiada.

Dla przykładu ‘A’ - duża A, zostało oznaczone jako 0100 0001, czyli 65. ‘a’ to zaś 97. Znak nowej linii to 0000 1010, czyli 10. Dlaczego? Bo tak i już. Tak sobie amerykańskie mędrki wymyśliły i koniec. Standard został ustalony, stosujcie się do niego. Taka kwestia umowna to w sumie jest.

Mała nota, zazwyczaj liczby zapisane w systemie binarnym piszemy z przedrostkiem `0b`, żeby było wiadomo, że mamy do czynienia akurat z binarnym. Bo jak tu odróżnić 10 w dziesiętnym od 10 w binarnym? Zapis ten sam a wartości różne.

B w kodowaniu ASCII to z kolei 0b0100 0010, czyli 66. I tak dalej. 

Każda literka, którą tutaj widzisz, jest tłumaczona w podobny sposób i zapisywana na dysku twojego komputera jako ciąg jedynek i zer. Następnie, przy odczytywaniu, komputer, po zinterpretowaniu jaką literą jest dana liczba, wyświetla określoną literkę. Kompletnie on jednak nie rozumie tego, że ta ‘k’ to jest jakaś literka, a nie kawałek kodu binarnego. Po prostu.

Co wyróżnia ASCII? ASCII jest kodowaniem, gdzie każdy element można wyrazić za pomocą 7 bitów. Co to znaczy, za pomocą 7 bitów? Bit to nic innego jak ‘cyfra’ w systemie binarnym.

 Przynajmniej pierwotnie było takie założenie. Pozwala ono zatem na translację 128 znaków, na liczby z przedziału od 0 do 127, włącznie.

Wiele osób, przynajmniej te, które miały trochę styczności z programowaniem lub informatyką, się zdziwi. Jak to – ASCII 7-bitowe? Wszystkich uczą często, że 8-bitowe przecież. Otóż nie, pierwotnie ASCII było projektowane jako 7-bitowy system, posiadając 128 znaków.

To, że dziś często myślimy o ASCII w kontekście 8-bitowym, wynika z tego, że podczas tworzenia ASCII, 8-bitów nie było jeszcze takim standardem. Wiele systemów kodowań było 7-bitowych, a 8 bit wykorzystywały sobie na jakieś tam swój różne dziwne potrzeby. 

Co to znaczy, że 8 bitów jest ‘standardem’? Otóż obecnie mamy coś takiego jak bajt. Bajt to z kolei zbiór 8 bitów. Czyli np. 1111 0000 czy 1000 0000. 

To taka bardzo mała jednostka pamięci twojego komputera, z której możesz skorzystać. Czy to RAM, czy pamięci dyskowej.

Jest to jasno określone i proste. Ale… Bajt nie zawsze był określony jako 8 bitów. Istniały systemy, gdzie 1 bajt, podstawowa jednostka, były zdefiniowane zupełnie inaczej – na 2 bity, na 7 bitów, na 6 bitów. Pick your poison. Wolna amerykanka.

W ogóle dużo rzeczy w informatyce, czy programowaniu, podobnie jak w matematyce, jest umownych. Przyzwyczaj się do tego, że czasem robimy tak coś w konkretny sposób, bo tak, a nie inaczej. Informatycy to ogółem od matematyków się wywodzą w prostej linii w zasadzie, zatem dziwni z nas ludzie.

Dlatego też obecnie, mimo tego, że ASCII oryginalnie jest 128 znakowym systemem 7-bitowym, to zapisuje się go za pomocą 8 bitów, dając mu 256 możliwych znaków, oficjalnie, 8-bitowe ASCII nazywamy rozszerzonym ASCII, ale potocznie, zazwyczaj jak mówimy ASCII, to mamy na myśli to 256-znakowe – z kilkoma dodatkowymi znakami.

Wybrany fragment tabelki znaków ASCII:

|Decymalny|Znak|Binarny|Decymalny|Znak|Binarny
|--- |--- |--- |--- | --- |--- |
65 | A | 0b1000001 | 66 | B | 0b1000010
68 | D | 0b1000100 | 69 | E | 0b1000101
69 | E | 0b1000101 | 70 | F | 0b1000110
72 | H | 0b1001000 | 73 | I | 0b1001001
73 | I | 0b1001001 | 74 | J | 0b1001010
76 | L | 0b1001100 | 77 | M | 0b1001101
77 | M | 0b1001101 | 78 | N | 0b1001110
80 | P | 0b1010000 | 81 | Q | 0b1010001
81 | Q | 0b1010001 | 82 | R | 0b1010010
84 | T | 0b1010100 | 85 | U | 0b1010101
85 | U | 0b1010101 | 86 | V | 0b1010110
88 | X | 0b1011000 | 89 | Y | 0b1011001
89 | Y | 0b1011001 | 90 | Z | 0b1011010

Po prostu wcześniej był chaos. A z chaosu wyłonił się ład. I powstała informatyka. W miejscu tym ład i chaos współistniały w harmonii.

No, w każdym razie. Bo wątek zgubiłem.

Mamy sobie to kodowanie, w tym wypadku ASCII, i jest elegancko. Chociaż nie do końca, bo pojawia się problem. ASCII teraz używamy na 8 bitach, tak? No tak. 8 bitów, to 8 zer lub jedynek, tak? Tak. Za pomocą 8 zer lub jedynek jesteśmy w stanie wyrazić 256 liczb. 

Biorąc pod uwagę, ze 1 liczba = 1 litera, to szybko wyjdzie nam, że mamy do wykorzystania maksymalnie 256 znaków. Trochę mało, jak na to, żeby pomieścić wszystkie alfabety świata, prawda? Owszem. Weźmy tu jeszcze pod uwagę, że ‘A’ i ‘a’ to dwie różne litery jak dla komputera – mały i duży znak to nie to samo. Doliczmy kropki, przecinki i inne znaki interpunkcyjne.

Szybko okazuje się, że na same literki za dużo miejsca nie zostało.

Dlatego też kodowanie ASCII zawiera tylko litery alfabetu łacińskiego. Po polsku już sobie nie napiszesz w ASCII, bo znaków brakuje. Kurła i co teraz?

A no widzicie, żeby Polacy i inne nacje, typu nie wiem, Chińczycy czy Japończycy, którzy mają tych znaczków pierdyliard, bo każdy wyraz potrafi być innym znaczkiem, czyli tak jakby u nas inną literą, nie czuli się pokrzywdzeni, zaczęły powstawać nowe kodowania. Dużo kodowań. O wiele za dużo.

## I wtedy UTF-8 wchodzi cały na biało

Obecnie jednak takim standardem jest coś zwanego UTF-8. Jest to system kodowania znaków Unicode, który do zapisu wykorzystuje od 1 do 4 bajtów. O, ważna informacja. Do 4 bajtów. 4 bajty, ile to było? 1 bajt, 8 bitów, 4 bajty, 32 bity.

32 bity, to z kolei 32 jedynki lub zera, czyli za ich pomocą można zapisać różnych liczb, zatem też i różnych znaków. No tutaj to już sporo się robi, bo to nam daje jakieś 4 294 967 296 możliwych znaków. Sporo, co? Nawet jak te wszystkie azjatyckie znaczki wrzucimy, to i tak sporo miejsca zostanie. Pięknie, idylla.  Marzenie.

Marzenie, bo w rzeczywistości, od wprowadzenia RFC 3629, UTF-8 obsługuje co najwyżej 2 097 152 znaków. To przez różne zaszłości historyczne, szczegóły implementacyjne i inne dziwne rzeczy, którymi nie musisz się martwić ani Ty, drogi czytelniku, ani ja, tylko raczej grube mózgi typu Ken Thompson i spółka, jakoś tak jednak wyszło, że niektóre bity są zarezerwowane na specjalne cele, niektóre bajty muszą mieć określony format, by wiadomo było różne przydatne rzeczy i tak dalej.

A o co chodzi z tym RFC całym? Ogółem to takie standardy, które pewne mózgi wyznaczają. Na jakiej podstawie? Na jakiej uznają. Podobnie jak z ASCII – bo tak i tak. Ogółem upraszczam i zasadniczo to podczas podejmowania różnych decyzji, osoby decyzyjne kierują się bardziej racjonalnymi argumentami.

Tyle znaków nam raczej wystarczy na co dzień. Obecnie w UTF-8 mamy wykorzystanych tak standardowo około 1 112 064 znaków. Czyli mamy nawet jeszcze trochę zapasu w razie czego, żeby dodawać potem nowe znaki. 

Czy też raczej `codepointy`, ale my sobie uprośćmy, nie wnikajmy i mówmy po prostu znaków.  Czym jest codepoint? Zazwyczaj jak się dyskutuje o różnych kodowaniach, to zamiast ‘znak’, używa się pojęcia codepoint. Drobna różnica. Z twojej perspektywy nie ma jakoś to bardzo znaczenia.

Mała nota też: skojarzcie też, że jak UTF-8, to ogółem Unicode. Te dwa terminy trzymajcie w pamięci razem. Co prawda Unicode nie jest tym samym co UTF-8.

Do tego kolejna notka. Jest też coś takiego jak UTF-16. Czym się różnią? Długością słowa. Czyli w UTF-8 jedno słowo ma 8 bitów, w UTF-16 ma 16 bitów. I tyle. Żeby nie było – bajtów mają po tyle samo, czyli maksymalnie 4, a w przypadku UTF-16, minimalnie 2 (no bo 16 bitów).Czym jest słowo? Bynajmniej nie jest to słowo jak ze słownika. Słowo, czyli słowo maszynowe, to taki trochę bajt, ale nie do końca. Sposób na pogrupowanie bitów w X sztuk po prostu. Nie musisz się tym zbytnio przejmować.

UTF-8 jest w 100% kompatybilny z ASCII – tekst w ASCII jest poprawnym UTF-8, ale UTF-8 już NIE musi być poprawnym ASCII. To bardzo ważne! Zapamiętaj!

Czyli popatrzcie, samo zaczęcie jakiejkolwiek rozmowy o tym, jak działa podstawowa funkcja w Pythonie, rzucenie chociaż trochę światła na to, co leży pod jej przykrywką, zajęło mi tutaj jakieś 6 stron.

A to dopiero początek – ledwo co stópki zamoczyliśmy w całym temacie, jakby mi przyszło opisać wszystko o tej jednej prostej funkcji, to pewnie by mi tu książki nie starczyło. 

Kiedyś tę wiedzę – o wszystkich niskopoziomowych rzeczach, faktycznie trzeba było posiadać, by cokolwiek napisać. Dziś?

Dziś mamy takie czasy, że  bazując na dekadach pracy tytanów intelektu informatyki, możemy sobie stworzyć tak abstrakcyjne języki, że nic z tego nie musimy znać. Wystarczy wpisać print("xd") i działa. To naprawdę coś niesamowitego, mimo tego, że nam wydaje się banalne. 

To jest właśnie piękno nauki, informatyki. Bazując na pracy innych, możemy tworzyć nowe rzeczy. Wyśmienicie.

W każdym razie.

## Podsumowanie
Zróbmy podsumowanie tego, co udało nam się zrobić i dowiedzieć.

Mamy ogółem w pythonie taką funkcję jak print, która, uwaga, drukuje nam tekst na ekranie. Ten tekst w rzeczywistości, to nie jest tekst dla komputera, tylko nic innego jak ciąg zer i jedynek, bo komputer nie rozumie nic innego, za sprawą tego, jak jest zbudowany – napięcie lub brak/niskie napięcie – to jedyne co on tak naprawdę rozumie.

W związku z tym powstało coś takiego jak system binarny. To taki system liczenia, troszkę inny od dziesiętnego, w którym liczby wyrażamy za pomocą dwóch cyfr i tylko tyle. Jest on nieco bardziej rozlazły w porównaniu do dziesiętnego – zapisanie tej samej liczby, co w dziesiętnym, zajmuje więcej miejsca, można by rzec, ale ogółem nie jest to jakieś skomplikowane pojęcie, da się ogarnąć.

No i teraz mając już coś, co komputer jest w stanie zrozumieć, czyli system binarny, bazujący na dwóch wartościach, możemy na tym coś budować.

My, jako sprytni ludzie, zbudowaliśmy sobie coś, co się nazywa kodowaniem znaków. Otóż wykminiliśmy sobie, że w określonych wypadkach, dana liczba w systemie binarnym, będzie znaczyła nie konkretną liczbę a np. znak właśnie.

I tak oto powstało jedne z pierwszych popularniejszych kodowań, czyli ASCII. ASCII było spoko, ale miało tę wadę, że mało znaków twórcy tam przewidzieli, powiedzmy. 

Zatem przyszło coś nowego, czego używam do dziś, co jest nieco lepsze – UTF-8. Żeby nie było problemów z kompatybilnością wsteczną, to znaczy, żeby stare teksty i programy działały na nowych komputerach, UTF-8 jest kompatybilny z ASCII, to znaczy tekst w ASCII jest też poprawnym tekstem UTF-8. W drugą stronę już niekoniecznie nie każdy UTF-8 jest poprawnym ASCII.

Pewnie cię trochę nudzę, co? Ostrzegałem na początku – będzie też trochę teorii i innych rzeczy, bo to nie będzie tylko książka o Pythonie. Chociaż przyznam szczerze, że mnie akurat te wszystkie tematy bardzo jarają, interesują. 

To dla mnie niesamowite, co stworzyliśmy jako ludzkość i jak te wszystkie procesy zachodzą. Piękna sprawa. Mam nadzieję, że chociaż po części będzie mi się udawało zaciekawić cię, czytelniczko, czytelniku, podczas tej lektury, takimi tematami – nie tylko samym Pythonem, ale informatyką, nauką ogółem.

Z drugiej strony, uważam, że takie podejście, które tu prezentuje – omawiając szerszy zakres, trochę historii i teorii, a nie same suche powiedzenie, „O tu masz printa i to drukuje tekst.” jest o wiele lepsze. Daje ci ono wgląd w fundamentalne teorie, które leżą u stóp tego, czym się będziesz posługiwać na co dzień. Poznasz narzędzie i jego budowę, zastosowanie, będziesz świadom. Moim zdaniem to konieczne do bycia dobrym programistą.

Zaraz przejdziemy do zadań/pytań. Oprócz nich, chciałbym, byś po każdym rozdziale bawił czy bawiła się sama nieco tym, o czym piszę – mówimy o print, poprintuj sobie trochę. Ja wiem, że wydaje się to nudne, ale zrób to. Proszę. Do tego, możesz poguglować trochę więcej i zgłębić tematy, o których tu mowa. To pomoże.
Rozdział 5.7. 
Zadania i pytania
Niektóre będą mega banalne, ale i tak na nie odpowiedz. No. Jak nie do końca znasz odpowiedź, to się nie przejmuj, przeczytaj jakiś kawałek jeszcze raz ewentualnie, spróbuj pomyśleć. 

Najlepiej to weź kawałek papieru i na nim spisuj swoje odpowiedzi na pytania, które nie wymagają programowania. To sprawi, że lepiej zapamiętasz. Sformułuj odpowiedź na podstawie tekstu. Później podam ci odpowiedzi.

1. Jaka funkcja w Pythonie służy do drukowania tekstu na ekran?
1. Czy ta funkcja drukuje coś poza tekstem, który został wpisany, czy nie? Podpowiedź: co się stanie, jak ponownie jej użyjesz, do wypisania czegoś nowego na ekran? Czy tekst będzie w tej samej linii?
1. Skąd komputer wie, kiedy zacząć drukować w nowej linii?
1. Czym jest system binarny?
1. Czym jest bit? A czym bajt?
1. Jakiej długości obecnie jest bajt? Czy zawsze bajty były tej długości?
1. Jakie wartości rozumie komputer tak kompletnie u podstaw? Dlaczego?
1. O co chodzi z ASCII? Co to jest?
1. Jak komputer sobie wewnętrznie reprezentuje tekst, który wpisujesz?
1. A ten cały UTF-8?
1. Ile plus minus (rząd wielkości) znaków można przedstawić za pomocą dwóch kodowań, o których mówiliśmy w tym rozdziale?
1. Przelicz następujące liczby z dziesiętnego na binarny: 5, 10, 32, 127, 256.
1. Teraz w drugą stronę, z binarnego na dziesiętny: 0000 1101, 1000 0000, 0010 0100.
1. Czy te dwa systemy kodowania, które omawialiśmy, są ze sobą kompatybilne wstecznie? Czy w obie strony? To znaczy A z B i B z A? Czy może tylko w jedną?


Odpowiedzi znajdziesz na następnej stronie.

## Odpowiedzi

1. Funkcja print.
1. Tak, drukuje ona dodatkowo znak nowej linii na końcu naszego tekstu, co sprawia, że jeśli coś nowego wyprintujemy, to będzie to w nowej linii.
1. Komputer wie, że trzeba teraz tekst od nowej linii wypisać, jeśli napotka specjalny znak, znany jako znak nowej linii. Nam go nie wyświetla, ale sam go interpretuje.
1. To system zapisu liczb za pomocą 2 cyfr – 1 i 0.
1. Bit to podstawowa i najmniejsza jednostka informacji, której używamy do zapisu wartości binarnych , czyli taka cyfra w systemie binarnym– to taka podstawowa cząsteczka, która przyjmuje jedną z dwóch wartości. Bajt zaś to nic innego jak 8 bitów.
1. Obecnie przyjmuje się raczej, że bajt to 8 bitów. Nie zawsze tak było, przed rozpowszechnieniem konwencji 8-bitowej, można było spotkać bajty zupełnie innej długości.
1. Komputer, u samych podstaw, rozumie tylko dwie wartości. 1 i 0. Nic innego. Wszystko powyżej to już ludzka abstrakcja. Wynika to z tego, jak jest zbudowany – system binarny bazuje na tym, że komputer operuje na dwóch wartościach: napięcie i brak/niskie napięcie.
1. ASCII to system kodowania znaków. Takie tłumaczenie swego rodzaju, gdzie odpowiednie liczby przypisujemy do konkretnych znaków. Coś w rodzaju szyfrów które tworzyło się w dzieciństwie. Po prostu umawiamy się, że X znaczy Y.
1. Tak samo, jak wszystko inne – za pomocą 1 i 0, czyli liczb. Te liczby potem tłumaczy na konkretne znaki.
1. UTF-8 to system kodowania UNICODE. Czyli trochę takie ASCII, ale nowsze. Pozwala przedstawić więcej znaków i tak dalej.
1. ASCII – 256, UTF-8 –  2 097 152
1. Tego mi się nie chce robić.
1. Tego też nie.
1. Tak, UTF-8 jest kompatybilne wstecznie z ASCII. ASCII nie jest kompatybilne z UTF-8, czyli każdy poprawny tekst zakodowany w ASCII będzie poprawny w UTF-8/Unicode, natomiast nie każdy teskt w UTF-8 będzie poprawnym ASCII.

\pagebreak
