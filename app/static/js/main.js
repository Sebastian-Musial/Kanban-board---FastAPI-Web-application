const PLACEHOLDERS = ["board_id", "column_id", "card_id"];

 /* Zwraca oryginalny action formularza ponieważ nie chce stracić pierwotnego wzoru URL*/
function getOriginalAction(form) {
    if (!form.dataset.originalAction) {
        form.dataset.originalAction = form.getAttribute("action");
    }

    return form.dataset.originalAction;
}

function buildDynamicAction(form) {
    let action = getOriginalAction(form);

    PLACEHOLDERS.forEach((placeholder) => {
        const input = form.querySelector(`[name="${placeholder}"]`);    /*Odszukanie odpowiedniego inputa poprzez porównanie nazwy placeholdera z tablicy*/

        if (!input) {
            return;
        }

        const value = input.value.trim();   /*input.value.trim - Pobiera wartość podaną przez użytkownika z inputa w HTMLm w przpadku odnalezienia placeholdera oraz kasuje spacje*/

        action = action.replace(
            `{${placeholder}}`,
            encodeURIComponent(value)   /*encodeURIComponent - zabezpieczenie przed spacjami i nietypowymi znakami, zamienia format na formę URL*/
        );
    });

    return action;
}


/*Walidacja formularza czy posiada wszystkie wartości*/
function validateDynamicAction(form) {
    const action = getOriginalAction(form);

    for (const placeholder of PLACEHOLDERS) {
        if (!action.includes(`{${placeholder}}`)) {
            continue;
        }

        const input = form.querySelector(`[name="${placeholder}"]`);    /*Odszukanie odpowiedniego inputa poprzez porównanie nazwy placeholdera z tablicy*/

        if (!input || input.value.trim() === "") {  /*Walidacja czy input istnieje oraz czy nie jest pusty/nie zawiera samych spacji*/
            alert(`Uzupełnij pole: ${placeholder}`);
            return false;
        }
    }

    return true;
}


/*Obsługuje formularze POST - zamiana placeholderów na wpisane wartości przez użytkownika*/
function handlePostForms() {
    const forms = document.querySelectorAll('form[method="post"]'); /*Pobranie wszystkich formularzy z metodą POST z pliku HTML*/

    forms.forEach((form) => {
        form.addEventListener("submit", (event) => {    /*Interakcje na użycie potwierdzenia formularza HTML*/
            if (!validateDynamicAction(form)) {
                event.preventDefault();     //Zatrzymanie formularza
                return;
            }

            const action = buildDynamicAction(form);
            form.setAttribute("action", action);    //Podmiana action z formularza o action z wypełnionymi danymi przez klienta
        });
    });
}


/*Obsługuje formularze DELETE - Wymagane w celu obsługi metody DELETE*/
function handleDeleteForms() {
    const forms = document.querySelectorAll('form[method="delete"]');   /*Pobranie wszystkich formularzy z metodą DELETE z pliku HTML*/

    forms.forEach((form) => {
        form.addEventListener("submit", async (event) => {  //Interakcje na użycie potwierdzenia formularza HTML + async w celu oczekiwania na odpowiedź serwera
            event.preventDefault();     //Zatrzymanie formularza

            if (!validateDynamicAction(form)) {
                return;
            }

            const url = buildDynamicAction(form);

            const confirmed = confirm("Czy na pewno chcesz usunąć ten element?");   //Powójne potwierdzenie usunięcia przez użytkownika 

            if (!confirmed) {
                return;
            }

            try {
                const response = await fetch(url, { //Przekazanie do routers z metodą DELETE żądania usunięcia i oczekiwanie na odpowiedź serwera
                    method: "DELETE"
                });

                if (response.ok) {
                    window.location.href = "/";
                    return;
                }

                alert("Nie udało się usunąć elementu.");
            } catch (error) {
                console.error("Błąd podczas usuwania:", error);
                alert("Wystąpił błąd podczas usuwania elementu.");
            }
        });
    });
}

function handleActionButtons() {
    const buttons = document.querySelectorAll("[data-target]");
    const forms = document.querySelectorAll(".action-form");

    buttons.forEach((button) => {
        button.addEventListener("click", () => {
            const targetId = button.dataset.target;
            const targetForm = document.getElementById(targetId);

            forms.forEach((form) => {
                form.classList.add("hidden");
            });

            if (targetForm) {
                targetForm.classList.remove("hidden");
            }
        });
    });
}

function handleInlineForms() {
    const buttons = document.querySelectorAll("[data-toggle-form]");

    buttons.forEach((button) => {
        button.addEventListener("click", () => {
            const formId = button.dataset.toggleForm;
            const form = document.getElementById(formId);

            if (!form) {
                return;
            }

            form.classList.toggle("hidden");
        });
    });
}

document.addEventListener("DOMContentLoaded", () => { //Uruchomienie skryptów po załadowaniu HTML.
    handlePostForms();
    handleDeleteForms();
    handleActionButtons();
    handleInlineForms();
});