---
{
  "schema": "wellmanifest.docs/document/v1",
  "id": "org-metadata-sync",
  "kind": "information",
  "version": 2,
  "title": "Synchronizacja metadanych przez wspólny koordynator",
  "status": "implemented",
  "owner": "semcod/.github",
  "created": "2026-09-06",
  "updated": "2026-09-06",
  "review_after": "2026-09-13",
  "source_revision": "406fb4b692680b3d69d25ee9570e81869afbd0c5",
  "affected_repositories": [
    "semcod/.github"
  ],
  "evidence": [
    "https://github.com/semcod/.github/blob/819770c5dbac17d93fbf21204d4509947d341c70/.github/workflows/org-metadata-sync.yml",
    "https://github.com/autogrammar/imgl/actions/runs/33995006182",
    "https://docs.github.com/en/actions/reference/security/secure-use"
  ]
}
---

# Synchronizacja metadanych przez wspólny koordynator

<!-- docs:section purpose -->
## Cel

Koordynator rozpoznaje pełną tożsamość repozytorium i synchronizuje wyłącznie zadeklarowane cele. Stary odbiorca usuwał organizację z payloadu: autogrammar/imgl stawało się semcod/imgl. Triggery Autogrammar wymagały też niedostępnego w tej organizacji ORG_SYNC_PAT. Nowy wariant utrzymuje uwierzytelnianie w centralnym repozytorium.

<!-- docs:section scope -->
## Zakres

Właścicielem mechanizmu jest semcod/.github. Lista zarządzanych zewnętrznych repozytoriów znajduje się w [org-sync/managed-repositories.json](../../org-sync/managed-repositories.json). Początkowo obejmuje autogrammar/code2schema, autogrammar/imgl, autogrammar/op3 i autogrammar/toonic. Lista jest zamknięta; nie oznacza całej organizacji. Inne instalacje koordynatora zachowują zakres własnej organizacji.

<!-- docs:section evidence -->
## Dowody

Wersja źródłowa jest przypięta w metadanych. [Nieudana synchronizacja imgl](https://github.com/autogrammar/imgl/actions/runs/33995006182) zgłosiła brak tokena. [Testy koordynatora](https://github.com/semcod/.github/actions/runs/33996073150) potwierdziły 19 scenariuszy. [Podgląd](https://github.com/semcod/.github/actions/runs/33996072826) oraz [wykonanie z zapisem dla imgl](https://github.com/semcod/.github/actions/runs/33996250463) zakończyły się sukcesem. Ponowny odczyt API potwierdził temat `autogrammar` i zachowany adres WWW. Nowy resolver czyta plik zdarzenia JSON zamiast wstawiać payload do kodu powłoki; odpowiada to [zaleceniom GitHub dotyczącym niezaufanych danych](https://docs.github.com/en/actions/reference/security/secure-use). Testy w org-sync/tests sprawdzają właściciela, złośliwe dane wejściowe, prywatne repozytoria, izolację profilu, propagację błędów i zachowanie lokalnej pracy.

<!-- docs:section content -->
## Działanie i obsługa

Istniejący harmonogram `17 */6 * * *` wykonuje synchronizację Semcod oraz czterech jawnie zarządzanych projektów Autogrammar. Ich opisy i tematy aktualizuje tryb `--metadata-only --skip-profile`; adresy WWW, GitHub Pages i profil organizacji pozostają poza tym trybem. Dla Semcod zachowano dotychczasową synchronizację wraz z profilem i kontrolą widoczności repozytorium przed konfiguracją Pages.

Repozytoria zarządzane centralnie nie potrzebują lokalnego triggera ani ORG_SYNC_PAT. Sekret istniejącego koordynatora musi mieć rzeczywiste uprawnienia do modyfikacji wskazanych celów. Nie kopiujemy osobistego tokena operatora do repozytoriów członkowskich.

Podgląd bez zmian:

```bash
gh workflow run org-metadata-sync.yml --repo semcod/.github --ref main -f repository=autogrammar/imgl -f dry_run=true
```

Wykonanie dla jednego celu:

```bash
gh workflow run org-metadata-sync.yml --repo semcod/.github --ref main -f repository=autogrammar/imgl -f dry_run=false
```

Parametr bez organizacji nadal oznacza repozytorium Semcod. Pusty parametr ręcznego uruchomienia oznacza pełny zakres Semcod. Pełna tożsamość obcej organizacji musi znajdować się na liście zarządzanej. Błąd pojedynczego celu powoduje niezerowy wynik całego zadania, nawet gdy inne cele się powiodły.

Bootstrap sprawdza rzeczywisty remote Git. Nie instaluje triggera dla innej organizacji ani dla centralnie zarządzanego celu; nie zapisuje zmian w brudnym checkout. Wycofanie istniejącego triggera odbywa się w osobnym PR konsumenta dopiero po sprawdzeniu centralnego uruchomienia.

<!-- docs:section limitations -->
## Ograniczenia

Harmonogram oznacza aktualizację co sześć godzin, z możliwym opóźnieniem kolejki GitHub, a nie natychmiast po pushu. Dry-run potwierdza odczyt i proponowaną zmianę; uprawnienia do zapisu i końcowe wartości wymagają sprawdzenia wykonania oraz ponownego odczytu API. Usunięcie wadliwego triggera nie zastępuje takiej weryfikacji.

Format dokumentu przyjęto z wellmanifest/docs 0.1.1. Sam ten dokument nie deklaruje instalacji chronionego checkera w semcod/.github. Trwający raport przekrojowy zależności pozostaje własnością subactor/docs.

<!-- docs:section next_actions -->
## Utrzymanie

Dodanie projektu wymaga jawnej pozycji w katalogu, konfiguracji organizacji, testu zakresu oraz udanego podglądu, wykonania i odczytu wartości. Przy zmianie zachowania zwiększ wersję tego dokumentu. Rollback: cofnij zmianę koordynatora i przywróć poprzedni trigger dopiero po przygotowaniu jego uwierzytelniania i poprawnego odbiorcy.
