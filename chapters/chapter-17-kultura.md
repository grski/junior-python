\pagebreak

# Kultura

O kulturze pracy programisty słów kilka. O nastawieniu i takich tam. Mimo, że pozornie rzeczy drugorzędne, tak naprawdę niektóre z nich odgrywają bardzo ważną rolę w procesie wytwarzania oprogramowania.

## Trochę o menadżerach/liderach

Dobry menago/lider zespołu jest osobą, która może albo zespół doprowadzić do ruinacji albo dodać mu skrzydeł. Zespoły to podstawowy blok budulcowy firm. Jeśli menago może zniszczyć lub uskrzydlić zespół, to podobnie może z całą firmą. To podkreśla jak ważny jest ktoś normalny w roli lidera. W jaki sposób uskrzydla się lub niszczy? Operując na tym, z czego zespół się składa. Na ludziach. Człowiek to podstawowa i najważniejsza jednostka w firmie, której chęć, a głównie wygenerowana niechęc, do pracy, jest mocno zależna od wpływów liderów. Opiszę trochę przemyśleń moich z tym związanych a raczej obserwacji na temat drogi, jaką co niektórzy przechodzą i jak ich to zmienia w efekcie.

Na mej programistycznej drodze spotkałem już wielu menadżerów w wielu różnych firmach. Niektórzy byli wspaniali, wpłynęli pozytywnie na moje życie, inni byli kompletnymi kretynami, jeszcze inni zaś są dla mnie teraz prawie jak rodzina. Po pewnym czasie zacząłem przyuważać pewne wzorce, które występowały prawie zawsze, i które pozwoliły mi wyizolować trzy graniczne poziomy bycia menadżerem.

### Poziom pierszy: mistrz Excela

Mistrzowie Excela to często świeżo upieczeni menadżerowie, liderzy, którzy nie mają jeszcze za dużo doświadczenia, ale za to pełno ego, dumy i buńczuczności. Świat stoi przed nimi otworem i jest do zdobycia! Uwielbiają swoje arkusze, wszystko w nich zapisują, optymalizują, czasami uprawiają mikromagament. To ludzie będący w początkowym okresie kariery menadżerskiej, gdzie człowiek może się nieco upoić początkowo swoją włądzą.

Ten typ człowieka widzi często tylko jedną rzecz: piniondz. Oj często takich spotykałem do pewnego czasu, za często. Pazeroty. I to oni są właśnie najbardziej niebezpiecznym typem menadżera, jaki się firmie może przytafić, spośród trzech wymienionych przeze mnie. Dlaczego? Bo mylne pozory dają.

Pozornie rzecz ujmując mistrzowie Excela wyglądają całkiem spoko. Cyferki się zgadzają, plany, prezentacje, no bajeczka. ALe nie do końca. W rzeczywistości wszystko się rozje

### Poziom drugi: empatyczny akolita excela 

### Poziom trzeci: człowiek

## Kultra projektowania

Ważnym i istotnym elementem każdego kawałka kodu czy systemu, który tworzysz, jest jego design. Co to konkretnie znaczy? 

Otóż chodzi o to, by kod, jaki napiszesz był **przemyślany**. Tutaj wchodzi coś, co nazywamy `incremental design`. Znaczy to tyle, że generalnie nie da się od razu, dla projektów mniej trywialnych aniżeli Hello World, stworzyc rozwiązania idealnego. Zamiast tego trzeba myśleć o dostarczaniu rozwiązania jak o procesie, przez który przechodzimy krok po kroku.

Najpierw powinniśmy zrozumieć dany problem, dobrze go pojąć i wrzucić w nasz mózg, by przemielić go na analogie i koncepcje dla nas zrozumiałe. 

Błędy i bycie w błędzie to część tego procesu. Oswój się z tym. Prawie nigdy twój pierwszy pomysł na rozwiązanie problemu, nie będzie kompletny czy poprawny. Zamiast tego problem warto rozbijać na malutkie cząstki, które swą trywialnością będą zbliżały się do wspomnianego wcześniej Hello Worlda. Oczywiście trzeba mieć tu smak i wyczucie, gdyż za bardzo rozdrabniać się też nie można.

Gdzie leży granica? Wyczucie, moim zdaniem, przyjdzie z czasem i praktyką.

Coś, co od siebie polecam, to następujące kroki:

1. Zrozumienie problemu i zadawanie pytań. To tu jest miejsce na przemyślenia, analogie i próbę oswojenia się z danym problemem. Pytaj, nawet o pozornie głupie rzeczy, zrozum o co tutaj chodzi i jaki jest problem. Zrozum **domenę** problem i **zamodeluj** go sobie w jakiś sposób w swojej głowie. Co to znaczy? Abstrakcyjny koncept przedstaw i wyobraź sobie w nieco mniej abstrakcyjny, zrozumiały dla siebie sposób.
2. Rozrysuj koncepcję z punktu wyżej lub podsumuj swoje przemyślenia w formie pisemnej. To tutaj warto by skonfrontować twoje wyobrażenia z rzeczywistością, zapytać odpowiednich osób, czy to właśnie o to chodziło. Diagramy są tutaj nieziemsko przydatne. Zaznaczam jednak, że nie chodzi o szczegółowy plan implementacji czy coś w tym stylu. Nie. Generalny rozrys tego, o co się rozchodzi w problemie.
3. Dopiero teraz pora na pierwsze implementacje najmniejszych kawałków. Zadanie podzielone na małe części, to zadanie łatwe do ogarnięcia. Mały kawałek łatwiej ogarnąć jednorazowo, aniżeli ogromny problem. Może zastosuj teraz TDD? Napisz jakiś kawałek kodu, który odwzoruje model i jakiś kawałek rozwiązania problemu, stestuj i skonfronuj z rzeczywistością. Warto tu zaznaczyć, że kod należy pisać tak, by jak najłatwiej było go potem zmienić, zastąpić, zrefactorować. Im bardziej skomplikowany i powiązany z innymi fragmentami kod, tym trudniejszy w edycji i refactoringu. Nie jest to jednak zachęta do tego, by tworzyć ogromnego molosa, który będzie zawierał tony boilerplate kodu i robił wszystko, jednocześnie nic. Nic bardziej mylnego.
4. Mając w ręku coś, co sensownie faktycznie rozwiązuje problem i odwzorowuje dobrze model problemu, teraz można nieco zrefaktorować, poprawić, podciągnąć, uczynić kod łatwiejszym i lepiej napisanym.
5. Krok 3 i 4 powtarzamy ile trzeba. Być może też krok 2.

Nie zachęcam tutaj do tego, by od razu z góry tworzyć **waterfallowy** model, gdzie z góry planujemy wszystko w szczególe. 

Iteracja po iteracji poprawiamy swój design i kod, idąc do przodu. To o to się rozchodzi. Dzięki temu możemy testować malutkie kawałki, walidować swoje pomysły na biężąco (np. z klientem poprzez dostarczanie malutkich fragmentów, ale często) i żyć ze znośnym kodem.

Programowanie paradoksalnie, jeśli dobrze zrobione, często nie opiera się na programowaniu.

Otóż najwięcej czasu powinno zająć analizowanie problemu i myślenie, planowanie. Zmiana koncepcji jest łatwa, to tylko myśl lub diagram. Jest to relatywnie tania operacja. Zmiana w kodzie zaś często bywa kosztowna. Twoim zadaniem jest, by zawsze **myśleć** i mieć na uwadze różne względy.

![Tom Scott - meme. Pozwoliłem sobie użyć wizerunku, mam nadzieję, że nie kole to w oczy.](./chapters/resources/images/future_me.jpg)

Sytuacja jak na memie wyżej bywa przykra. Pamiętaj, że w przyszłości to ty pewnie będziesz utrzymywał swój własny kod, przynajmniej przez chwilę. Zrób sobie z przyszłości zatem przysługę i przemyśl dwa razy kod, który piszesz, przyłóż się. Nie warto być niechlujem i leniem czasami. Znaczy paradoksalnie to właśnie lenie najwięcej pomyślą, bo łatwiej jest myśleć aniżeli stukać kod. Zatem podążajmy drogą prawdziwego, a nie pozornego, lenia i dbajmy o design. Dobrze zaprojektowana aplikacja potrafi być wdzięczna przy pracy zarówno dla programisty jak i dla użyszkodnika końcowego.

Czasem starczy poświęcić godzinę myślenia, by zaoszczędzić sobię 4-8h klepania kodu.

Przy okazji nie bój się tego, że ktoś rozliczy cię z koncepcyjnej pracy na zasadzie liczenia linijek kodu jakie wyprodukowałeś/wyprodukowałaś. To nie o to chodzi w pracy kreatywnej. Żaden sensowny pracodawca nie będzie rozliczał cię z tego, że napisałeś 20 linijek zamiast 40. Liczba linii wyplutego kodu nie jest żadną miarą.  Oczywiście nie mówię o skrajnościach, kiedy jesteś juniorem i przez cały miesiąc dodałeś jeden commit zmieniając jedną linijkę, co prawdopodobnie oznacza, iż robisz kogoś w jajo.    

Do obejrzenia: https://www.youtube.com/watch?v=flxmpq7_tdM

## O wartościach

Podobno o wartościach i zasadach najwięcej mówią ci, co ich nie mają, bo reszta po prostu nimi żyje. Mimo tej mądrości ludowej, trochę się o nich rozpiszę, ale tylko delikatnie. Chciałbym wspomnieć mimo wszystko o pewnych wartościach, jakie mi w pracy przyświecają i jakie ja osobiście lubię widzieć u siebie oraz innych. Te cechy, to coś, co uważam, że stanowi podstawę dobrego programisty, kodera, pracownika.

1. Szczerość i otwarty umysł
   To dla mnie podstawa u każdego. Ludzie mają problemy z rozmawianiem ze sobą szczerze i z komunikacją. To na szczerości winna się opierać każda relacja, zwłaszcza zawodowa. To zaś wymaga otwartego umysłu i schowania ego do kieszeni. 
2. Szacunek (ludzi ulicy, znaczy ten no, klawiatury)
   Miej szacunek dla drugiego człowieka, klienta, współpracowników. Szanuj ich czas, wiedzę i pieniądze. W ten sposób można budować relacje na lata. Szanuj też przede wszystkim siebie, bo jeśli sam się nie szanujesz, to trudno by inni to robili.
3. Empatia i bycie ludzkim
   Na koniec dnia jesteśmy tylko ludźmi. Postaw się czasami w butach drugiej osoby zanim coś powiesz. Dobra atmosfera i zaufanie budowane na empatii i sympatii do drugiego człowieka pozwala osiągnąć w zespole synergię, która niesamowicie usprawni, ale i uprzyjemni pracę. Bądź człowiekiem. Nie bądź dzbanem.
4. Poczuwanie się do odpowiedzialności i bycie dumnym ze swojej pracy
   Jak coś tworzysz, bierz za to odpowiedzialność, bądź z tego dumny. Ta zasada ma daleko idące implikacje jak dbanie o swój kod, dostarczanie holistycznych rozwiązań, które zostały przetestowane, czasem `going the extra mile`, jeśli trzeba, posiadanie i wykazywanie inicjatywy zamiast ślepego podążania za taskami. 
5. Merytokracja
   Moim zdaniem ego chowamy do kieszeni. Krytykę, merytokratyczną znaczy się, twojego rozwiązania, kodu czy nawet swojej osoby, nie traktuj osobiście i jako atak. Nie. To raczej cenne lekcje, z których można się uczyć, ino trzeba odsunąć ego na dalszy plan a skupić się na tym, co ważne, czyli dobro projektu, klienta, dostarczanie wartości. Nie znaczy to, że masz się ciąglę poświęcać, nie. Szanuj siebie przede wszystkim, ale powtarzam. Ego chowamy do kieszeni a rzeczy w pracy staramy się bazować na logice, argumentom i dyskusjom prowadzonym w dorosły sposób. Dodatkowo chciałbym też nadmienić, że nie masz się też co bać proponować swoich rozwiązań, nawet jeśli idą niejako w sprzeczności z rozwiązaniami np. lidera, starszego programisty czy klienta. Jeśli pracujesz z odpowiednimi ludźmi, to docenią to a rozwiązanie wybierzecie na podstawie faktów a nie innych czynników.
6. Współpraca
   Bądź niezależny w swojej pracy lokalnie, natomiast zorientowany na współpracę globalnie. Co to znaczy? Myśl i miej gdzieś z tyłu głowy szerszą perspektywę i staraj się koordynować swoje indywidualne starania tak, by wpasowywały się w jakiś szerszy plan. Przykład tutaj to: "Zacznę implementowąć najpierw tego taska, bo dzięki temu odblokuję frontend."
7. Zakładaj dobre intencje
   When in doubt, ask. Tak w skrócie. Jeśli pracujesz z kimś, to znaczy, że prawdopodobnie ta osoba przeszła podobną weryfikację co i ty. Znaczy to, że jest jakoś kompetentna, takie założenie mam. Do tego zakładam, chyba, że fakty dowiodły inaczej, że wszyscy w zespole mamy dobre intencje. Zatem zanim coś zrobię, jeśli posiadam chociaż cień wątpliwości, co do natury sytuacji, wolę dopytać, co ktoś miał na myśli. Może zły dzień, może źle coś odebrałem, może komuś żona z rana dała popalić. Kto wie.

Uważam, że kierowanie się tymi punktami wyżej Ci nie zaszkodzi. Warto mieć je z tyłu głowy. Bo w IT często nie chodzi o IT a o ludzi i ich problemy. Jak o tym pomyślisz, to za to właśnie ci płacą - za rozwiązywanie problemów biznesowych, problemów określonych ludzi, ułatwianie ich życia. To za to płaci się grube hajsy. Dostarczanie wartości. A to wymaga tego, by mieć odpowiednie cechy i zrozumienie, być określonym człowiekiem. Myślę, że atrybuty wyżej są takimi, które pozwolą ci błyszczeć w zespole jak i firmie. To podstawy bycia normalnym człowiekiem, aczkolwiek czasem rzadko spotykane. Wyróżniaj się nie tylko twardymi umiejętnościami z informatyki, ale również byciem dobrą osobą.

Cholllera, ale poetycko i buńczucznie. 

## Kaizen

Parę słów chciałbym rzec o filozofii Kaizen. Co to znaczy? To taka japońska myśl, której motywem przewodnim jest ciągła, ustawiczna praca nad sobą i dokonywanie małych usprawnień, które razem składają się na coś większego.

Generalnie sprawdza się to bardzo w naszym zawodzie jak i w sumie wszędzie.

Codziennie powinniśmy czynić kod odrobinkę lepszym dodając nowe funkcjonalności lub poprawiając istniejące. Codziennie powinniśmy chociaż odrobinkę poczytać, pouczyć się czegoś nowego. Po pewnym czasie zaczyna działać tutaj procent składany i okazuje się, że z tego codziennego, niewielkiego wysiłku, rośnie coś ogromnego. 1% dziennie daje 3700% rocznie po uwzględnieniu procenta składanego. Ale czaszka.

Zatem Kaizen czy The Slight Edge to coś, co powinno być obecne w kulturze twojej pracy.

## Zarządzanie portfelem inwestycyjnym

Tajemniczy nagłówek. O cóż chodzi? Mianowicie o to, że każdy z nas w życiu inwestuje, nawet jeśli nie gra na giełdzie. Jak to? Tak. Ty sam jesteś swoją największą inwestycją. Twoja wiedza, kariera, życie.

Wiedza jest bardzo cenna. To coś w co należy ciągle inwestować, gdyż daje ogromne zwroty zazwyczaj. 

\pagebreak