\pagebreak

# Internet

Tutaj poruszymy sobie różnorakie kwestie związane z siecią, Internetem i całą resztą. Mimo tego, że jako junior-python wannabe najbardziej przejmujemy się samym Pythonem i programowaniem, to należy pamiętać, że kod, który piszemy a potem uruchamiamy, nie działa w jakiejś próźni. 

Wszystkie nasze web appki, programy etc. uruchamiane są w jakimś konkretnym środowisku. To środowisko oddziałowuje na sposób egzekucji naszych programów, to jak one działają. Dodatkowo nierzadko musimy z nim w jakiś sposób wchodzić w interakcję, często obustronną. Co to znaczy? A no, że oprócz samego naszego Pythona wypada znać też całą otoczkę gdzie to bangla i tak dalej, gdyż inaczej można sobie czasem strzelić w stopę. Do tego wiedza o środowisku i rzeczach powiązanych, z których pośrednio lub bezpośrednio korzystamy, czesto nie mając świadomości, czyli po prostu inne komponenty `Systemu` jaki projektujemy, tworzymy czy utrzymujemy, są jego integralną częścią jak i czymś co wpływa na naszą prace i nasz kod.

Przez System rozumiem tu jakiś układ, zestaw elementów. W IT jest to zazwyczaj, dla przykładu, nasza webappka, serwery gdzie jest ona uruchamiana, klient, etc.

Pomówmy zatem o tym całym systemie i środowisku.

## Droga żądania

Większość aplikacji webowych działa w modelu klient - serwer. Klient robi zapytania (requesty) do serwera, serwer zwraca odpowiedź (response). 

Jak to się jednak dzieje, ze jesteśmy w stanie wysłać to zapytanie. Co się dzieje w chwili, kiedy wpisujesz `grski.pl` w pasku przeglądarki a następnie widzisz mojego bloga?

Otóż sprawa wygląda następująca.

Zakładając, że jesteś połączony z Internetem, twoje zapytanie zostanie przetworzone przez twojego ISP (Internet Service Provider/Dostawca Usług Internetowych), który podbije do czegoś, co nazywa się DNS. DNS to Domain Name Server, czyli taka książka telefoniczna, która zawiera mapowanie domen/adresów jak grski.pl, do lokalizacji (IP) w sieci.

Co to znaczy? Każdy serwer ma swoje mniej lub bardziej unikalne IP. Tak zwany adres IP. To coś jak adres zamieszkania. 

IP wygląda tak: **172.16.254.1**. To 32 bitowa liczba, przynajmniej w przypadku standardu IPv4. Coś takiego trudno zapamiętać, prawda? Mi tak. Natomiast `grski.pl` już tak. Stąd powstało takie oto mapowanie i domeny. Domeny ułatwiają zapamiętanie i pozwalają na to, by ułatwić życie użyszkodnikom.

Zarzucę też ciekawostkę. Jeśli IPv4 definiuje adres IP jako 32 bitową liczbę, to pytanie do Ciebie, jakie problem może się tu pojawić w dzisiejszych czasach? Otóż 32 bitowa liczba jest mała jak na dzisiejsze standardy. Pomyślcie ile urządzeń jest połączonych do Internetu, większość z nich ma unikalne adresy publiczne. Matko bosko. Generalnie zbliżamy się do punktu, gdzie nie będzie wolnych unikalnych adresów IP. Przykra sprawa.

Powstało zatem IPv6, które ten problem rozwiązuje. Przykład IPv6: **2001:0db8:85a3:0000:0000:8a2e:0370:7334**. Tutaj rozmiar to już 128 bitów. 2 do potęgi 128 daje od ciula dużo opcji, starczy nam na trochę tej przestrzeni adresowej. 

Dobrze, wróćmy jednak do zapytania.

Mamy obecnie tak: twoja przeglądarka (klient) -> ISP -> DNS -> Serwer.

Następnie na serwerze często znajdują się Load Balancery/Proxy, czyli takie kawałki softwareu, które odpowiednio nakierowują rządania/zapytania do nich trafiające na pasujące zasoby lokalne/usługi/API etc.

Z LB/Proxy żądanie trafia do docelowego serwisu. Następnie otrzymujemy odpowiedź i gotowe.

Pomiędzy może być jeszcze wiele innych usług jak cache, CDN etc, ale przedstawiłem tutaj wersję skróconą. A jak już o CDN mowa, to...

## CDN

Czym jest CDN i dlaczego jest ważny? To w zasadzie dzięki nim możemy bez problemów korzystać z mobilnej sieci, mniej płacić za Internet, to dzięki CDNom nie zacina ci się film ze śmiesznymi kotkami na wypoku, a twój operator może obsłużyć obecną liczbę klientów zamiast np. połowy. Wiem, trochę przesadzam, ale no tak troszkę tylko. Czym zatem jest?

### Wprowadzenie

Najpierw jednak garść informacji, by zyskać nieco perspektywy. Żyjemy w czasach, gdzie egzystencja bez Internetu jest praktycznie niemożliwa, a na pewno bardzo niewygodna. Większość dzisiejszych luksusów w jakiś sposób bazuje/korzysta z tego wynalazku. Często jednak nie zdajemy sobie sprawy z tego, jak ogromny ten Internet jest i jak szybko się rozwija, pozwólcie, że wyjaśnię.

W 2018 roku przekroczyliśmy kolejną barierę - to wtedy na Ziemi pękł nowy rekord użyszkodników internetu - 4 miliardy ludzi korzystających z Internetu, czyli to aż 53% populacji. Jest to wzrost niesamowity, biorąc pod uwagę fakt, że jeszcze 4 lata wcześniej użytkowników Internetu było około 2,4 miliarda.

W 2016 dziennie przez Internet przelatywało 44 miliardów GB danych na dzień. Biorąc pod uwagę fakt, że wtedy userów było znacznie mniej, to uwzględniając użytkowników w 2018, daje to nam około 51 miliardów GB dziennie. Oczywiście jest to mocno niedoszaczowany wynik, gdyż nie dość, że użytkowników przybywa, to i jeszcze pochłaniają oni coraz więcej danych, ale na potrzeby tego artykułu wystarczy, gdyż jakiś obraz to nam daje. Obecnie mamy 2022 i około 5 miliardów. 62,5% populacji.

Średni użytkownik smartfona zużywa w ciągu miesiąca 2.9 GB transferu mobilnego (dane ze stycznia 2018). To 50% więcej niż rok wcześniej.. Sieć rozwija się w zatrważającym tempie. Dlaczego w zatrważającym? Cóż, o ile chodzi o połączenie kablowe, to aż takiej tragedii nie ma, no bo można dołożyć kabel czy dwa, chociaż to też wszystko skomplikowane i kosztowane, to prawdziwy problem rodzi sieć danych komórkowych, gdyż jest ona mocno ograniczona przez fizykę, a biorąc pod uwagę ciągły rozrost... Cóż, mamy się troszkę o co martwić albo nasza sieć nieco się zapcha.

### I wtedy wchodzi CDN, cały na biało

Tak. Sytuację całą łagodzi właśnie CDN. Cóż to takiego? To takie serwery, które cachują najpopularniejsze treści w Internecie, by ogólnie odciążyć sieć, skrócić czasy ładowania i zapobiec pewnym problemom, poprawić bezpieczeństwo. Serwery te rozrzucone są po całej Ziemi w miejscach strategicznych geograficznie dla sieci.

W sieci mamy dostawców treści. Te treści są różne, tekst, obrazki, filmy, multimedia. Dostawcy treści umieszczają je na swoich stronach, serwerach i jest spoko. W momencie, kiedy chcesz sobie coś w Internecie przeczytać czy obejrzeć, to twoje urządzenie łączy się poprzez Internet z serwerem dostawcy treści i przesyła do Ciebie określoną treść. Wszystko spoko, prawda? No nie. 

Problem pojawia się, kiedy tych danych i użytkowników przybywa na całym świecie. Problem wynika z architektury Internetu. Gdy oglądasz odcinek swojego ulubionego serialu, to twój komputer nie łączy się bezpośrednio z serwerem dostawcy, nie. Zanim się to stanie musi się on przejść przez dziesiątki innych urządzeń, które skierują go we właściwe miejsce, tak samo odpowiedź od tego serwera.

Wyobraź sobie, że jesteś w urzędzie i żeby załatwić określoną sprawę potrzebujesz podpisu dziesięciu różnych urzędników a na koniec jeszcze podpis przełożonego z Ameryki, do którego jest długa kolejka. Zabiera to dużo czasu, energii i tak dalej, prawda? Tak. Skomplikowana sprawa ogółem. Rolą CDN'a jest skrócenie tej listy potrzebnych podpisów do jednego urzędnika, który jest akurat w lokalnym urzędzie.

Czyli jak z serwerami - twoje zapytanie zamiast tłuc się do serwera w Azji czy Ameryce i męczyć jeden serwer, spyta najpierw lokalnego gościa, który jest miasto obok. W 99% przypadków on wystarczy. W pozostałym 1% trzeba będzie tarabanić do Ameryki, ale na miejscu sprawe załatwimy szybko, bo dzięki pomocy z obsługą petentów lokalnie, wujek Sam ma do obsługi mniej, przez co kolejka jest znacznie mniejsza.

### Szczegóły

Z serwera Dostawcy Treści do CDNów przesyłane i cachowane są pewne dane - jakie? Te, które są najbardziej popularne - to bardzo ważne, by na CDNach utrzymywać głównie te dane, które są najbardziej popularne, gdyż dzięki temu CDNy przejmują większość ruchu, redukując obciążenie sieci osiągając wysoki hit rate.

Jest to skomplikowany proces, bo przecież w różnych regionach popularne są różne treści, a to jak się one zmienią, nie jest banalne do przewidzenia.

Algorytmy, które się tu wykorzystuje do tego, by przewidzieć co i gdzie będzie popularne, to naprawdę bardzo ciekawa sprawa i ważna - przestrzeń i zasoby CDNów są ograniczone, zatem wybór tych treści jest trudny. Niesamowity przykład takiej optymalizacji i przewidywanie tego, co będzie akurat popularne, można zaobserwować na przykładnie Netflixa i tego, jak oni to rozwiązują.

### Czym jest hit rate, lifetime?

Użyłem wcześniej wyrażenia hit rate. To termin, który określa jaki procent requestów userów może być przetworzona przez CDN i tylko CDN, a jaka potrzebuje pomocy z serwera Dostawcy Treści. Obecnie niektórzy potrafią tak zoptymalizować swoje serwery, by hitrate do cache wynosił nawet w okolicach 99%. Niesamowite wyniki.

Do tego dochodzi jeszcze określenie czasu, przez który raz wgrane treści mają być dostępne - lifetime - po jego wygaśnięciu cache jest 'usuwany' z serwera i na jego miejsce wskakują nowe (albo wciąż te same, jeśli dalej są popularne)/uaktualnione dane. Jest on zupełnie różny, zależnie od danych, regionu, samego dostawcy usługi.

### Czy CDN to jeden ogromny serwer?

Nie, to często całe klastry rozproszonych geograficznie serwerów. Setki tysiące maszyn, które mają pewną hierarchię i według niej działają. Jak? Mniej więcej taką. Serwer dostawcy treści to CP.

Następnie mamy CD & LCF - to taka centrala można by rzec.

Potem jest CCF a pod nim CDPF. CCF to lokalny urząd, a CDPF to urzędnik.

Domyślnie, kiedy robisz jakiś request danej treści, to ląduje on w CCF'ie, CCF sprawdza sobie, czy to, czego potrzebujesz, jest gdzieś w jego zasobach, czyli na serwerach CDPF, gdzie trzymane są zcachowane treści. Czyli w skrócie sprawdza, czy to, o co prosisz, jest gdzieś 'skopiowane' na lokalnym serwerze.

Jeśli na jednym nie ma, to leci do kolejnego z CDPFów pod swoją kontrolą. Co, jeśli nie znajdzie na żadnym ze swoich CDPFów? Wtedy zgłasza fakt do CD & LCF, który pyta się kolejno pozostałych CCFów.

Jeśli każdy CCF stwierdzi, że tego contentu nie ma na CDPFach pod ich kontrolą? Wtedy CD & LCF robi request do serwera twórcy treści, stamtąd sobie dane pobiera i zachowuje lokalnie. Także oryginalny serwer jest męczony w bardzo niewielkiej ilości przypadków, dzięki czemu sam serwer jak i jego okoliczna sieć jest znacznie odciążona, ruch zostaje rozrzucony po lokalnych i rozproszonych CCFach zamiast być skupiony w jednej lokalizacji.

To między innymi dzięki takim rozwiązaniom (lub podobnym) GitHub z pomocą firmy Akamai, byli w stanie sprostać niedawnemu rekordowemu atakowi DDOS skierowanymi przeciwko tej popularnej platformie, który w szczytowej fazie przybrał rozmiar 1.35 Tbps - prawie półtora Tb na sekundę. Niesamowite. To dzięki temu Wypok jako-tako działa. Dzięki temu Netflix nie zapycha całego Internetu.

### Podsumowanie

Wiele rzeczy jest, dzięki którym nasze dni są łatwiejsze, a nawet tego nie wiemy. CDNy były pewnie dla większości z was czymś właśnie takim. Oczywiście w tekście sporo jest uproszczeń, także bear with it.

## Cache

Czym jest cache? Cache to taka jakby baza danych, ale o przeznaczeniu nieco innym. W domyśle cache zachowuje dane na określoną ilość czasu, zazwyczaj dość krótką, relatywnie do bazy danych, które czasami zachowują dane permanentnie. 

Cache zatem to taka baza danych o krótkim terminie ważności, w której przychowujemy zapamiętane wyniki komputacji, tych, które są kosztowne zazwyczaj i tylko te, które dotyczą odczytu a nie zapisu do bazy danych na przykład.

Czyli jeśli mamy sobie jakiś widok/funkcję, cokolwiek, która przyjmuje argument, u nas to będzie akurat jakiś request, to dla podobnych albo takich samych, cache zwróci wynik 'z pamięci' zamiast liczyć od nowa.

Do poczytania:

1. https://www.techtarget.com/searchstorage/definition/cache
2. https://realpython.com/lru-cache-python/
3. https://realpython.com/python-memcache-efficient-caching/



## Chmura

AWS, Azure, GCP to dostawcy usług chmurowych. Co to znaczy? Czym jest chmura? Chmura to po prostu taka jakby serwerownia, ale u kogoś innego na chacie. Kto inny martwi się pewnymi rzeczami.

Za odpowiednią opłatą dostawcy chmurowi ogarniają za nas pewne rzeczy, udostępniają dodatkowe uslugi, zajmują się większością rzeczy.

To często takie ułatwienia, gdzie w zamian za pewien koszt i fakt, iż dostawcy chmurowi czasem decydują za nas w pewnych kwestiach, ciężar opieki nad niektórymi sprawami przerzucamy na zewnętrzną firmę. W dużym skrócie. 

AWS to chmura od Amazona, Azure od Microsoftu a GCP od Googla.

Która lepsza? Ta, której używa twój docelowy pracodawca. W gruncie rzeczy są one jednak do siebie podobne, zmieniają się tylko nazwy niektórych usług. Dodatkowo jednak chmura będzie posiadała lepszy toolset do określonych zadań, druga do innych.

IMO jeśli o korpo idzie to najwięcej chyba na Azure/AWS. 

Startupy to głównie AWS. 

GCP to mieszanka.

Źródło: instytut danych z dupy. 

Ja osobiście najczęściej spotykałem się z AWSem, ale to tylko ja. Polecam zapoznać się i pobawić trochę w stawianie różnych usług w chmurze samodzielnie. Każda z nich oferuje programy, gdzie za zarejestrowanie otrzymamy pewien zasób hajsu do przepalenia na nasze zabawy. Wykorzystaj, bo warto. Doda ci to samodzielności i +10 do fejmu jak nauczysz się podstawowych rzeczy z DevOpsowania. A co to to całe devopsowanie? Link numer 4. W skrócie to taki gość od infrastruktury i ogarniania serwerów, czyli miejsca, gdzie nasze aplikacje są uruchamiane.

Anyway.

Do poczytania:

1. https://azure.microsoft.com/pl-pl/resources/cloud-computing-dictionary/what-is-the-cloud/
2. https://experience.dropbox.com/pl-pl/resources/what-is-the-cloud
3. https://devopsiarz.pl/kurs-ansible/  <- mocno dodatkowo. Ansible to soft do automatyzacji pewnych zadań, żeby ręcznie nie klikać. 
4. https://devopsiarz.pl/devops/kto-to-jest-devops-engineer/ 
5. https://en.wikipedia.org/wiki/Infrastructure_as_code
6. https://12factor.net/

## Docker

Cóż takiego to ten Dokier cały? Wszędzie o nim piszą.

Otóż docker to narzędzie służące budowaniu i uruchamianiu kontenerów, konteneryzacji. Taka jakby maszyna wirtualna symulująca komputer w komputerze. Główna różnica leży jednak w tym, że kontenery są o wieeeele bardziej wydajne jeśli idzie o zasoby. 

VMki stawiają cały system i emulują wszystko od podstaw. Docker korzysta z gotowych komponentów twojego systemu przez co jest o wiele mniej zasobożerny.

Dzięki kontenerom możemy pobierać gotowe 'obrazy', które zawierają wszystko, czego aplikacja po trzebuje do uruchomienia jak i samą aplikację. 

Wyobraź sobie, że musisz ręcznie instalować wszystkie zależności, pakiety etc. 

Teraz wyobraź sobie to samo na 50 serwerach, bo akurat musicie skalować aplikację. Docker nam to ułatwia. Raz zbudowany kompletny obraz wymaga jedynie uruchomienia.

Obecnie standardem jest to, że aplikacje się konteneryzuje. 

Do poczytania: 

1. https://www.czarnaowca.it/2022/01/docker-tutorial-1-co-to-jest-docker-i-do-czego-jest-nam-potrzeby/
2. https://sii.pl/blog/docker-dla-programistow-co-to-jest/

\pagebreak