# Nazwa projektu

Beata Kadej projekt na zaliczenie WSB Wrocław 
Programista Python Developer

## Dostępność na stronie

http://beakad.pythonanywhere.com/

## Wymagania

python = "^3.10"
pendulum = "^2.1.2"
django = "^4.2.2"
css = "^0.1"


[build-system]
requires = ["poetry-core"]
build-backend = "poetry.core.masonry.api"


## Instalacja

1. Sklonuj repozytorium https://github.com/BeaKad/WSB.git na swój komputer .
2. Utwórz wirtualne środowisko Pythona.
3. Zainstaluj wymagane biblioteki z pliku poetry.lock.
4. Uruchom serwer lokalny poleceniem python manage.py runserver.

## Opis działania

Niniejszy projekt przedstawia stronę bloga.

Logując się do strony jako admin można dodawać posty, dodawać użytkowników,
dodawać komentarze, usuwać komentarze dodane przez użytkowników i nie tylko.

Wchodząc na stronę bloga użytkownik widzi wszystkie dostępne posty
i komentarze.

Aby dodać nowy post, lub komentarz pod isteniejącym już postem należy się zalogować.
W przypadku braku konta należy się zarejestrować.


## Autorzy

Beata Kadej

