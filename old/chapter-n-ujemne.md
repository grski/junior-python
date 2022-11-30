Czy na pewno? 
Zwróć uwagę na to, że w przykładach wyżej pojawia nam się liczba ujemna, mniejsza od zera. W przypadku tekstu zapisać jest ją prosto, stawiamy minus przed i gotowe. Jako ludzie nauczeni jesteśmy, by interpretować to jako liczbę ujemną. Jak natomiast robi to komputer?

#### Przykładowy sposób reprezentacji liczb ujemnych

Przypomnijmy sobie poprzednie rozdziały i to, o czym tam mówiliśmy. Pokazywałem między innymi to, jak komputer zapisuje sobie liczby w pamięci i jak je reprezentuje, a mianowicie za pomocą systemu binarnego, bity, bajty, te sprawy. Teraz tak, jak w takim razie komputer oznacza, że dana liczba jest ujemna? Przecież `minusa` sobie nie postawi w pamięci w jakiś sposób. 

Otóż przedstawię wam, jak to wygląda, znowu, w C. Sposobów i pomysłów jak rozwiązać ten problem było wiele, dalej jest, ale my omówmy tylko jeden. Załóżmy, że operujemy sobie jakimś typem, który jest akurat wielkości 1 bajta. Znaczy to tyle, że ma 8 bitów długości. Ile w takim razie obsługuje maksymalnie wartości/liczb? Odpowiedz na to pytanie proszę, przelicz.

Dobrze, mając 8 bitów, mamy do dyspozycji 8 zer i/lub jedynek. Czyli możemy maksymalnie przedstawić 255 wartości, prawda? Od 0, do 255. A no nie do końca! 

##