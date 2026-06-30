# Kanban board - tablica kanban

Kanban board jest projektem aplikacji webowej, której celem jest umożliwienie zarządzania zadaniami za pomocą klasycznej tablicy kanban.
Tablica składa się z kolumn, które zawierają karty z zadaniami tworzonymi przez użytkownika.
Aplikacja jest przeznaczona do użytku jednoosobowego.


## Technologie

- Docker
- PostgreSQL
- HTML + CSS + JavaScript
- FastAPI
- SQLModel
- Jinja2


## Funkcjonalność

Aplikacja zawiera najczęściej udostępniane funkcje w tablicach kanban:
- Tworzenie, edycje, usuwanie tablicy kanban
- Tworzenie, edycje, usuwanie kolumn
- Tworzenie, edycje, usuwanie kart z zadaniami
- Dodawanie, modyfikowanie treści do kart: tytuł, opis i termin realizacji zadania
- Przechowywanie kart w wybranych przez użytkownika kolumnach


## Jak uruchomić

1. Utwórz .env na podstawie .env.example
2. Uruchom PostgreSQL: docker compose up -d
3. Utwórz i aktywuj venv
    - python -m venv .venv
    - .venv\Scripts\activate.bat - dla windows aktywacja środowiska w CMD
    - source .venv/bin/activate - dla Linux to samo
4. Zainstaluj zależności: pip install -r requirements.txt
5. Uruchom API: python -m uvicorn app.main:app --reload
6. Dostęp do aplikacji: http://127.0.0.1:8000


## Endpoints

- Aplikacja: 
  http://127.0.0.1:8000

- Dokumentacja API:
  http://127.0.0.1:8000/docs

- Health check:
  http://127.0.0.1:8000/health


## Przydatne komendy podczas pracy z projektem oraz adres dokumentacji 

- Utworzenie venv

  python -m venv .venv

- Aktywacja venv
  .venv\Scripts\activate.bat - dla windows aktywacja środowiska w CMD
  source .venv/bin/activate - dla Linux to samo

- Uruchomienie Dockera / Zatrzymanie Dockera wraz z wykasowanie danych
  docker compose up -d
  docker compose down -v

- Uruchomienie aplikacji
  uvicorn app.main:app --reload

- Adres dokumentacji
  http://127.0.0.1:8000/docs
  http://127.0.0.1:8000/health

- Wejście do bazy danych
  docker ps

  docker exec -it NAZWA_KONTENERA psql -U example_user -d example_db


# Model danych

## Tablica kanban

Tablica kanban posiada:
- id
- nazwę
- kolumny


## Kolumny w tablicy kanban

Kolumny w tablicy kanban posiadają:
- id
- nazwę
- kolejność
- karty z zadaniami


## Karty w tablicy kanban

Karty w tablicy kanban posiadają:
- id
- tytuł
- opis
- termin realizacji zadania



## Podstawowy wzór tablicy kanban

Uniwersalna tablica kanban może zawierać następujące kolumny:
- To do
- In progress
- Done