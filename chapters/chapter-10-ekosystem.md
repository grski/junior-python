\pagebreak

# Ekosystem narzędzi Pythonowych

Trochę o fajnych narzędziach, które wypada znać. Zakładam, że każde z tych narzędzi sobie zainstalujesz, pobawisz się nim.

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

