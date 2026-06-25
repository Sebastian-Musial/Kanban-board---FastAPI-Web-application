# Kanban board - tablica kanban

Kanban board jest projektem aplikacji webowej, której celem jest umożliwienie zarządzania zadaniami za pomocą klasycznej tablicy kanban.
Tablica będzie składała się z kolumn, które będą zawierały karty z zadaniami tworzonymi przez użytkownika.
Aplikacja jest przeznaczona do użytku jednoosobowego.


# Funkcjonalność

Aplikacja będzie zawierała najczęściej udostępniane funkcje w tablicach kanban:
- Tworzenie tablicy kanban
- Tworzenie kolumn
- Tworzenie kart z zadaniami
- Dodawanie treści do kart: tytuł, opis i termin realizacji zadania
- Przechoyuwwanie kart w wybranych przez użytkownika kolumnach


# Jak uruchomić

1. Utwórz .env na podstawie .env.example
2. Uruchom PostgreSQL: docker compose up -d
3. Utwórz i aktywuj venv
    - python -m venv .venv
    - .venv\Scripts\activate.bat - dla windows aktywacja środowiska w CMD
    - source .venv/bin/activate - dla Linux to samo
4. Zainstaluj zależności: pip install -r requirements.txt
5. Uruchom API: python -m uvicorn app.main:app --reload


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
- termin realizacji do kiedy dane zadanie ma zostać wykonane



# Podstawowy wzór tablicy kanban

Uniwersalna tablica kanban może zawierać następujące kolumny:
- To do
- In progress
- Done