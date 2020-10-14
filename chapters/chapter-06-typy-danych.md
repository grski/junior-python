# Typy danych

W poprzednim rozdziale mówiliśmy sobie o zmiennych. Będąc przy tym, siłą rzeczy warto wspomnieć o typach danych jakie nasze zmienne mogą przechowywać w Pythonie. Porozmawiamy sobie o tym konkretnym języku, ale podobny podział występuje w większości języków.

Jak już w poprzednich rozdziałach pisałem, Python nie wymaga od nas definiowania typów dla naszych zmiennych, nie ma w nim statycznego typowania. Przypomnij sobie co to oznaczało i odpowiedz na pytanie - co oznacza brak statycznego typowania? Czym jest dynamiczne typowanie? Jakie są tego wady/zalety. Poszukaj w książce, może w odpowiedziach do poprzednich rozdziałów. Zrób to teraz.

Mimo tego dobrze wiedzieć, na jakie typy zazwyczaj dzielimy sobie różne zmienne. Dlaczego? Bo Python też ich używa, tylko sam niejako zgaduje jakiego typu użyliśmy. A więc w Pythonie wyróżniamy następujące podstawowe typy danych:

1. Liczby
2. Napisy
3. Typ logiczny
4. Bajty

Zaraz je sobie wszystkie po kolei omówimy. Zacznijmy od liczb, bo będzie najdłużej prawdopodobnie.

## Liczby

No to tak moi drodzy, w Pythonie wyróżniamy sobie trzy główne typy liczb: liczby całkowite, liczby zmiennoprzecinkowe i liczby złożone, czyli po kolei tak jakby inty, floaty, complex.

Co to znaczy? 

### Liczby całkowite

Tu sprawa jest chyba prosta, prawda? `1, -1, 5, 0, 938, -24861` to przykłady liczb całkowitych, czyli po prostu `zwykłe` liczby bez żadnych przecinków, udziwnień i wynalazków. Więcej na ich temat rozpisywał się jakoś zbytnio nie będę bo i nie ma po co. 

### Liczby zmiennoprzecinkowe

Z czym do czynienia mamy tutaj? Nic innego aniżeli liczby z `częścią po przecinku` mówiąc prostym językiem. I w zasadzie tyle.

Tutaj udziwnienia są i to duże, ale pod spodem. Porozmawiamy o tym w innym rozdziale, bo to dłuższy temat, ale generalnie sprowadza się to do tak zwanej niedokładności reprezentacji liczb zmiennoprzecinkowych w systemie binarnym. Tak tak. Jasne, prawda? Powiem tylko tajemniczo, żebyście pamiętali zawsze i wszędzie, że używanie zwykłych floatów/doublów do dokładnych obliczeń czy przechowywania informacji o pieniądzach, to niezbyt dobry pomysł, gdyż czasami `0.1+0.2 != 0.3`. 

### Liczby złożone

Bardzo rzadko spotykane, ale czasem jak ktoś robi obliczenia naukowe jakieś albo inne dziwne rzeczy, to może mu się ta wiedza przydać - otóż są to liczby składające się z części rzeczywistej i urojonej. Matematyczne tematy. Jak nie wiesz o co chodzi, to nie przejmuj się.

Definiujemy je tak: `21 +3j` albo `complex(32, 3)`. 

I tyle. Na razie tyle potrzeba ci wiedzieć jeśli idzie o rzeczy, którymi kwalifikujemy jako liczby w Pythonie. Są jeszcze np. decimale czy rationalsy, ale o nich innych razem!

## Napisy

Napisy, czyli tak zwane stringi. 

## Pytania i zadania

1. Czy w Pythonie jest dynamiczne typowanie? A może statyczne?
2. Co to oznacza? Jakie są tego wady, jakie zalety. 
3. 