# Podstawy Pythona – notatki

Na początku każdego kursu programowania powinno się poznać, jak komputer rozumie napisany kod — czym są bity, zmienne, typy danych itd. Po rozmowie z prowadzącym ćwiczenia doszedłem jednak do wniosku, że w tym przypadku nie ma to większego sensu, a cały kurs jest raczej „zapchajdziurą” na tym kierunku.

Jeżeli ktoś chciałby bardziej zrozumieć, co tu się dzieje i dlaczego języki programowania działają, to polecam zajrzeć do dokumentacji danego języka (wystarczy w przeglądarce wpisać: `<nazwa języka> documentation`) oraz przerobić na początek najbardziej podstawowe kursy (np. W3Schools).

Dlatego tutaj skupimy się tylko na omówieniu najbardziej podstawowej składni Pythona.

---

## 1. Whitespace (wcięcia)

Python jest bardzo wrażliwy na tzw. *whitespace* w kodzie (czyli spacje i tabulatory).

Nie ma znaczenia czy używasz spacji czy tabów — ważne, żeby były one **stosowane konsekwentnie**.

Każdy blok kodu (np. w funkcji, ifie itd.) musi mieć odpowiednie wcięcie. Najczęściej stosuje się:
- 4 spacje (standard w Pythonie)
- albo 1 tabulator

Najważniejsze zasady:
- wszystkie linie w jednym bloku muszą mieć takie samo wcięcie
- mieszanie tabów i spacji prowadzi do błędów

---

## 2. Czytanie błędów

Bardzo ważną umiejętnością jest czytanie błędów w kodzie.

Wymaga to podstawowej znajomości języka angielskiego, ponieważ komunikaty błędów są w tym języku.

Przykład błędu:
`File "D:\MyProject\ft_basics_of_programming\sln\error_test.py", line 3
print('jeszcze lepszy błąd')
^
IndentationError: unindent does not match any outer indentation level`


Interpretacja:
- błąd wystąpił w linii 3
- Python wskazuje miejsce (strzałka `^`)
- typ błędu: `IndentationError`
- oznacza to, że problem wynika z nieprawidłowych wcięć (patrz punkt 1)

---

## 3. Zmienne i typy danych

Na tym etapie nie będziemy wchodzić głęboko w teorię typów danych.

W kursie skupiamy się głównie na typach liczbowych:
- `int` – liczby całkowite
- `float` – liczby zmiennoprzecinkowe (najczęściej używane)

Przykłady:

```python
x = 1      # int
x = 1.0    # float
x = "1"    # string (tekst)
```

## 4. Funkcje

Funkcje w programowaniu działają podobnie jak w matematyce:
- przyjmują argumenty (dane wejściowe)
- zwracają wynik (dane wyjściowe)

Na tym etapie przyjmujemy, że funkcja powinna zwracać wartość przez `return`.

### Składnia funkcji:

```python
def nazwa_funkcji(arg1, arg2):
    return wynik
```
### Ważne informacje:
- def oznacza definicję funkcji
- nazwa_funkcji to dowolna nazwa (najlepiej opisowa)
- argumenty są opcjonalne (funkcja może ich nie mieć)
- return zwraca wynik funkcji
- Co jeśli nie ma return?

Jeśli funkcja nie ma return, to domyślnie zwraca:
`None`
Czyli „brak wartości”, co często może prowadzić do błędów, jeśli tego nie przewidzimy.

## 5. Instrukcje warunkowe

Instrukcje warunkowe pozwalają sprawdzać, czy coś jest prawdziwe lub fałszywe.

W Pythonie używamy do tego:
- `if`
    ```python
    if warunek:
        # kod wykona się, jeśli warunek jest prawdziwy
    ```
    - zawsze sprawdza warunek
    - jeśli jest True, wykonuje blok kodu
- `elif`
    ```python
    elif inny_warunek:
        # kod wykona się, jeśli poprzedni if/elif był False
    ```
    - oznacza „else if”
    - może występować wiele razy
    - sprawdzany tylko jeśli wcześniejsze warunki nie zostały spełnione
    else
- `else`
    ```python
    else inny_warunek:
        # kod wykona się, jeśli żaden warunek nie był spełniony    
    ```
    - nie przyjmuje warunku
    - działa jako „domyślna opcja”

### Ważne zasady:
- każdy blok (if, elif, else) musi mieć wcięcie (indentację)
- wszystkie linie w danym bloku muszą mieć takie samo wcięcie
- po warunku zawsze stawiamy :

## 6. Operatory matematyczne

W Pythonie mamy podstawowe operatory matematyczne:

- `+` – dodawanie
- `-` – odejmowanie
- `*` – mnożenie
- `**` – potęgowanie
- `%` – reszta z dzielenia (modulo)
- `/` – dzielenie (wynik zawsze typu float)
- `//` – dzielenie całkowite (bez części po przecinku)
