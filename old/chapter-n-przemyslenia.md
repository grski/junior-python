# Luźne przemyślenia

Ten rozdział to zbiór moich różnych przemyśleń, apeli, cokolwiek. 

## Backend to nie produkt

Chciałem kilka słów napisać nie o programowaniu per se, ale o programowaniu jako pracy. Otóż jestem dość młodym developerem, mam plus minus, w tej chwili, około dwóch lat doświadczenia komercyjnego, a jeśli o sensowną pracę w zespole chodzi, to jeszcze mniej.

To malutko. Lat na karku też za dużo nie mam, bo przecież nawet 20. mi jeszcze nie wybiła. Dlatego też ciągle uczę się wielu rzeczy i jednocześnie widzę, że inni ludzie, z większym stażem, starsi ludzie, mają podobnie — również się uczą, stąd też wrażenie, że warto poruszyć temat, o którym dziś piszę, bo wydaje mi się, że niezależnie od wieku i stażu, dużo osób tego nie rozumie.

### Małe oświecenie 

Otóż niedawno zaświeciła mi się w głowie lampka — zadaniem zespołu jest stworzenie rozwiązania, produktu, czegoś, co zadowoli klienta, spełni jakiś cel, rozwiąże dany problem. No właśnie. 

Co w związku z tym? Piszę to z perspektywy backend developera, otóż: backend nie jest produktem sam w sobie. 

Frontend też nie. O co mi chodzi dokładnie? Do pewnego czasu miałem podejście w stylu — nic mnie nie obchodzi, że funkcjonalność X nie została dowieziona na czas/nie działa/są problemy z implementacją — ja swoje zrobiłem, backend działa i jest piękny, to frontend/devops/qa/ktokolwiek nie dopiął i produkt nie działa. 

To kompletnie błędne podejście, zrozumiałem to. Po części pomogło zrozumieć mi to, jak wyglądał proces dowożenia aplikacji w naszym zespole w jednej z poprzednich firm, oraz jakie problemy napotykaliśmy po drodze, które wynikały głównie właśnie przez takie myślenie, a z drugiej strony, zostałem lekko skierowany, by spojrzeć na ten problem w moim myśleniu, przez mojego de facto mentora. 

Tu też fajna sprawa — zamiast od razu o czymś mówić, pozwolono mi spróbować czegoś na własną rękę, przemyśleć sprawę, a potem dojść do poprawnego rozwiązania samodzielnie — szacunek za to.

### Jak powinno być

Kończąc dygresję — gdy piszemy backend/frontend, cokolwiek, nie możemy myśleć tylko o tym, jaki on będzie fajny, piękny i niesamowity z perspektywy czysto backendowej/frontendowej. 

Musimy pomyśleć, jak innym będzie się współpracowało z kodem, serwisem, który tworzymy.

Czy rozwiązanie, które akurat tworzymy, będzie wygodne dla frontu? Czy wszystko jasno opisałem tak, by osoba pisząca integrację z API nie miała już żadnych pytań, bo wszystko zostało klarownie opisane w dokumentacji, dodatkowych notatkach? Może mogę im pomóc w inny sposób, rozmawiając z nimi, przed w trakcie i po implementacji? 

Dobre pytania, które, uważam, warto przemyśleć. Wydaje mi się, że trzeba uważać na to, by nie wpaść w taki swego rodzaju egoizm, gdzie wydaje nam się, że nasza praca jest najważniejsza, my ją wykonaliśmy dobrze, to ktoś inny jest kompletnie winien i koniec, my mamy czyste ręce. To tak nie działa. 

Oczywiście, są odstępstwa od reguły — ktoś celowo sabotuje prace, cokolwiek, ale to tak rzadkie sytuacje, że nie warto o nich wspominać. Programowanie to zazwyczaj praca zespołowa, a kluczowym elementem pracy zespołowej jest... no właśnie praca zespołowa. 

Zespół jest bardzo ważny, tak samo, jak ważne jest to, by poszczególne 'elementy' zespołu, dobrze współgrały. Dzięki temu cały mechanizm będzie świetnie działał. A o to chodzi. 

Nie zrozumcie mnie źle — nie mówię tu o tym, że cały czas trzeba robić jakiś 'team building', 'integracje', 'meetingi', 'spotkania' czy inne cholerstwa wciskane często na siłę. Nie. Nie jestem adwokatem scruma czy innych podobnych albo mniej podobnych, metodologii różnorakich. Nie. 

### Apel

Zasadniczym celem tego tekstu jest jedynie zaszczepienie takiej myśli, swoista prośba bym wręcz powiedział. 

Brzmi ona następująco: podczas tworzenia swojej części kodu, serwisu, czegokolwiek, pomyśl o osobie, która będzie twój kod czytała, która będzie korzystała z twojego API, może się skonsultuj z nią, opisz wszystko, udokumentuj.

Postaw się na miejscu tego fronta, backenda, opsa. 

Być może jesteś w stanie zrobić coś inaczej, co wciąż będzie technologicznie dobrym rozwiązaniem, a pozwoli drugiej stronie zrobić coś szybciej, przy czym nie spowolni to twojej pracy? Kto wie. 

Takie tylko pytanie. Warto je sobie chyba zadać. Oczywiście nie ma co przesadzać w drugą stronę — tworzenie bubla programistycznego, bo front poprosił czy cokolwiek — nie, to zły kierunek. 

Jak zwykle — trzeba znaleźć jakiś środek, bo przesadzanie w którąkolwiek ze stron jest złe. 

Konkludując już: nie bądźmy takimi egoistami. Backend nie jest produktem, frontend też nie. Możesz mieć state-of-the-art backend/front/stronę devopsową, ale jak ten inny komponent nie będzie działał, to produkt będzie ssał.

Takie podejście, gdzie z własnej woli zrobisz więcej dla innych, zwyczajnie sprawi, że twój projekt będzie lepiej działał. Im więcej pomożesz innym, tym więcej będą oni mogli pomóc tobie. Po prostu. 

Absolutnie nie znaczy to, że masz wykonywać pracę z kogoś, myślę, że rozumiesz.

To bardzo ważne, zwłaszcza teraz. Wydaje mi się, że obecnie zaczynamy przykładać co raz, to większą wagę do tego, jak się z kimś współpracuje, bo inaczej zespół będzie leżał. 

Także to bardzo ważne, co już niejednokrotnie podkreślałem i jeszcze niejednokrotnie pewnie powtórzę, zwłaszcza tobie, juniorze. Bo często to twój charakter i nastawienie decydują o tym, czy warto w ciebie zainwestować i przyjąć cię do pracy.

Zatem naprawdę weź sobie do serca tę radę.

I co? Chyba tyle.

A jak już przy apelach jesteśmy, to…

## Chciej, pisz dobry kod

Trochę absurdalny nagłówek, prawda?

Owszem, ale nie do końca. Otóż jest jedna bardzo ważna rzecz, o której chciałbym Ci powiedzieć, najlepiej kilka razy, byś ją zapamiętał czy zapamiętała. 

Otóż sprawa ma się tak, że…

Niektórzy, po pewnym czasie, dają sobie spokój. Przestają mieć ochotę, przestają się starać. Po prostu mają dość. Nie dążą już do tego, by być lepszym, by kod, który piszą, był lepszy z dnia na dzień. By każda zmiana powodowała, że repo jest w lepszym stanie niż poprzednio.

Wypaleni pracownicy.

Nigdy nie bądź taki. Proszę, to mój osobisty apel.

Staraj się być osobą, która codziennie się rozwija, której się CHCE.

I tylko tyle.

## Obrzydliwe kuriozum w świecie IT

Ostatnio obserwuję obrzydliwy proceder. Proceder upolityczniania świata IT i wytwarzania oprogramowania jako całości. Co mam na myśli? 

Regularny proces niszczenia naszej społeczności polityczną poprawnością. 

Od dłuższego czasu przyglądam się temu procesowi, ostatnio jednak gdy zobaczyłem, iż do oficjalnego repozytorium Pythona zmergowane zostały branche pull requestów, których to jedynym zadaniem było… 

Zmienienie terminologii master/slave w kontekście procesów i tak dalej. Jakby tego było mało, to dość niedawno w grupie tworzącej jądro Linuxa pojawił się obowiązkowy CoC – Code of Conduct, który brzmi… Cóż, dość specyficznie. 

Sam Linus, który znany jest ze swojego ‘charakterystycznego’ zachowania, oraz tego, że każdemu potrafi powiedzieć co myśli, a często myśli dość ostro, ogłosił, że na razie robi sobie przerwę, by ‘popracować nad swoim charakterem w świetle pewnych zmian’. No ludzie kochani. 

Te dwa wydarzenia sprawiły, że postanowiłem napisać swoje dwa słowa o tym temacie. Otóż wielce mi się to nie podoba. Uważam za kompletnie obrzydliwe, wstrętne i nieakceptowalne, by robić z procesu wytwarzania IT oraz naszego społeczeństwa, jakąś politycznie poprawną abominację, która w niczym nie przypomina piękna swej oryginalnej formy. Z czym konkretnie mam problem? 

Oto lista kilku rzeczy. 

Zacznijmy może od omawianego przykładu zmiany terminologii Pythona. To nie jest odosobniony przypadek. Podobna sytuacja miała już miejsce kilka lat temu, tyle że w kontekście kodu frameworku Django. Jak widać, zaczyna być to trendem. 

Mocno niepokojącym i głupim tak szczerze. Otóż jak pewnie wszyscy wiemy, mamy w świecie IT pewien swoisty słowniczek pojęć, które mają bliżej określone, znane wszystkim, znaczenie. Widząc niektóre słowa, niezależnie od języka, w jakim występują, możemy w dość znacznym stopniu domyślić się, co robi dana funkcja, dana zmienna czy ogółem, dany kod. 

Te terminy istniały przez wiele lat, cała nomenklatura na nich bazuje i ich używa, często dość trafnie opisują to, jaką abstrakcję przedstawiają. I teraz pojawia się problem. 

Bo przychodzi ktoś, kto w imię politycznej poprawności zaczyna zmieniać te terminy, bo być może kogoś one urażą, mimo tego, że nie mają prawa, gdyż używane są w innych kontekstach, innych znaczeniach, których używa się też w słownikach i tak szczerze to nikt się tym nie przejmuje, poza kilkoma głośnymi krzykaczami, którzy dali się pewnym kwestiom zwariować. Niestety z tego, co widzę, w świecie IT raczej więcej jest osób nieco pasywnych, niezbyt dominujących. Typ introwertyka, intelektualisty, który chce mieć spokój. 

O ile ktoś nie wejdzie aż tak bardzo w jego strefę komfortu i jej nie zaburzy, to taka osoba nie będzie się zbytnio czemuś sprzeciwiać raczej. W tym problem. Bo pewne kręgi to widzą i wykorzystują ten fakt na swoją korzyść, by pchać wszędzie swą agendę. 

To smutne. Jak dla mnie jest to kompletna głupota, która wprowadza tylko niepotrzebne zamieszanie. Co, jeśli we wszystkich językach zaczną się takie rozterki?

Co, jeśli nagle zacznie funkcjonować kilka różnych nazw zastępczych na ‘niewygodne’ terminy, bo jedne będę lepsze niż inne? Mniej/bardziej poprawne politycznie? Przecież to jest receptura na katastrofę. To tak jakbyście w kodzie opisywali jeden obiekt kilkoma różnymi nazwami. Nie jest to dobra praktyka, prowadzi do złego kodu i problemów z utrzymaniem, debugowaniem i wszystkim w zasadzie. Ja właśnie tak widzę skutki tych zmian. 

Na pewno nie pomoże tutaj fakt, że Guido przecież zaczyna się wycofywać ze świata Pythona, oddał stery, a ostatnio ma w dodatku niezłe jazdy – chodzi mi tu chociażby o  jego niedawną deklarację, kiedy to stwierdził, że, nie będzie uczył, udzielając konsultacji, białych mężczyzn, bo oni tacy okropni. Zamiast tego zamierza pomagać tylko uciśnionym mniejszością.

No ludzie kochani, proszę was… 

Następna do omówienia jest utworzenie regulaminu dla społeczności tworzącej jądro Linuxa. Nowo powstały regulamin brzmi jak paplanina wyjęta prosto z mokrego snu wojującej aktywistki LGBT.

Żebym był jasny – jestem za wolnością. Zupełnie mnie nie obchodzi, kim jesteś, co robisz, kogo kochasz i kto ci się podoba. Żyj i daj żyć. Proste. 

Z założenia te nowo powstałe zasady brzmią okej, problem jednak w tym, jak zostaną one wdrożone, bo historia pokazała już, jak to się zazwyczaj dzieje. Coś, co ma być narzędziem wolności dla wszystkich, staje się aparatem ucisku. 

Chodzi zwyczajnie o to, że SJW (Social Justice Warriors) zyskują tutaj potężne narzędzie, które umożliwi im kompletne pozbywanie się osób, które im nie przypadną go gustu. A im do gustu nie przypada raczej większość niż mniejszość. W zasadzie to panuje tam zasada ‘kto nie z nami, tam przeciw nam’. Widzicie tę rozbieżność? Ten dysonans? 

W teorii mają oni walczyć o sprawiedliwość społeczną, a praktyce są oni często tyranami, którzy niszczą ludzi. Często dobrych ludzi, kompetentnych ludzi. Jeśli nawet na Linusa udało się wpłynąć, który to jest raczej uparty i kontrowersyjny w swoich poglądach, to co będzie z innymi osobami? Co, gdy jakiś naprawdę porządny deweloper ‘urazi’ kogoś albo podpadnie kaście SJW?

Czy naprawdę potrzebujemy gdziekolwiek komisji ludzi, którzy będą mówić nam jak się zachowywać, co by przypadkiem kogoś nie urazić? Poważnie? 

Idźcie mi z tym cholerstwem stąd, idźcie z naszego świata IT. Wracajcie do swoich wysypisk na uniwersytetach i innych miejsc, gdzie siejecie tę zarazę. Tam sobie bytujcie ze swoją polityczną poprawnością, nie u nas, w świecie IT. Paszoł won! 

Nie psujcie czegoś pięknego, bo świat IT taki jest. Piękny, inkluzywny i otwarty, sam w sobie. Popatrzcie, jak on wyglądał od początku stworzenia – losowi ludzie z Internetu, bez względu na cokolwiek, wiek, pochodzenie, kolor skóry, religię, pracowali razem nad różnymi projektami, tworzyli oprogramowanie, które rozwiązywało kolejne problemy tego świata, te mniejsze i te większe. 

Po co robić w tym bałagan, mieszać się i narzucać jakieś ramy? Idźmy dalej.

Pomówmy o tak zwanej ‘dyskryminacji pozytywnej’, czy jak to tam teraz te dzbany nazywają. O co chodzi? A no o to, że jak jesteś białym, heteroseksualnym mężczyzną, jeszcze nie daj Boże, chrześcijaninem, to trzeba ci jakoś życie utrudnić, bo jesteś uprzywilejowany, ‘check your privldż!’. Rozumiecie tę hipokryzję? 

Kolejny punkt – parytety w IT. Co raz, to więcej firm zaczyna rekrutować na stanowiska tylko i wyłącznie kobiety/czarnych/gejów/łatever, by spełnić normy ‘diversity’, ‘różnorodności’. 

Wydawać się wam może, że to przecież Polski nie dotyczy, że to jakieś amerykańskie problemy. Nic bardziej mylnego. Wyobraźcie sobie, że na naszym podwórku również mają miejsce takie rzeczy. 

Inne, jeszcze bardziej przerażające, też – jak np. sponsor wycofujący się z finansowania danego wydarzenia, bo normy ‘diversity’ nie zostały zachowane, czyli na darmowe wydarzenie, na które każdy przychodzi z własnej woli, zapisało się zbyt mało kobiet. Czemu ich nie zmusiliście do przyjścia, co to ma być?! Psychoza. I to jest autentyczny przykład z Polski.

Ile opowieści słyszałem o tym, że na dane stanowisko przyjęto kobietę, mimo że była mniej kompetentna od innych kandydatów? Nie mówię tu, że kobiety są mniej kompetentne. Absolutnie. Po prostu porównując dwóch kandydatów, jeden ma lepsze umiejętności, będzie lepszym pracownikiem, drugi nie. Logiczne jest zatrudnianie lepszej osoby. 

W momencie, kiedy robimy z tej logiki prostytutkę i zatrudniamy kogoś słabszego tylko dlatego, że np. jest kobietą, albo jest czarny/żółty/zielony, to coś jest nie tak. Św. Tomasz płacze gdzieś po cichu. 

Takie rzeczy właśnie, takie ruchy w open source, w firmach, w społeczności, doprowadzą ostatecznie do pogorszenia jakości kodu, odejścia filarów i oryginalnych propagatorów ruchów open source. Nie widzę przyszłości wesoło, jeśli się nie sprzeciwimy tej zarazie. Patrzmy tylko na jedno. Na wiedzę, na to, co ktoś mówi i jak prawdziwe to jest. Na nic więcej. Tylko to niechaj się liczy i koniec.

I jestem świadom, że puszczając te słowa w eter, publicznie to mówiąc, mogę sobie zaszkodzić, stając się celem dla niektórych.

Wiecie co? Mam to w głębokim poważaniu. Nie zamierzam siedzieć cicho i przytakiwać tylko. Od zawsze miałem niewyparzoną gębę i mówiłem to, co uważałem. Nie zamierzam tego zmieniać.

Jak właśnie czytasz ten tekst i jesteś oburzony czy oburzona, to wiesz co… Trudno. Na tym polega wolność słowa, że każdy może mówić co uważa, nawet jeśli ci się nie podoba to, co mówi. Deal with it.

\pagebreak
