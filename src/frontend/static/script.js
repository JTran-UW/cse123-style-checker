async function runChecks() {
    showLoading();
    fetch("http://127.0.01:8000", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
            text: document.getElementById("text").value
        })
    })
        .then((response) => response.json())
        .then((data) => {
            if (data.detail) {
                hideLoading();
                raiseInvalidInput();
            } else {
                parseErrorMessages(data.errors);
            }
        });
}

async function parseErrorMessages(errorMessages) {
    hideLoading();
    clearErrorMessages();
    console.log(errorMessages);

    if (errorMessages.length == 0) {
        createErrorWindowMessage(
            "No Errors Found!",
            "Your code looks good."
        )
    } else {
        for (const i in errorMessages) {
            let error = errorMessages[i];
            createErrorWindowMessage(
                error.type + " Error at " + error.line + ":" + error.col,
                error.message    
            );
        }
    }
}

async function createErrorWindowMessage(label, body, color="black") {
    const errorWindowMessage = document.createElement("section");
    errorWindowMessage.classList.add("error");
    errorWindowMessage.style.color = color;

    const errorLabel = document.createElement("h3");
    errorLabel.innerHTML = label;
    errorWindowMessage.append(errorLabel);
    
    const errorBody = document.createElement("p");
    errorBody.innerHTML = body;
    errorWindowMessage.append(errorBody);

    document.getElementById("error-window").append(errorWindowMessage);
}

async function clearErrorMessages() {
    const errors = document.getElementsByClassName("error");
    
    for (let i = errors.length-1; i >= 0; i--) {
        errors[i].remove();
    }
}

async function raiseInvalidInput() {
    clearErrorMessages();

    createErrorWindowMessage(
        "Invalid input!",
        "Your code could not be parsed",
        color="red"
    );
}

async function showLoading() {
    document.getElementById("load").classList.remove("hidden");
}

async function hideLoading() {
    document.getElementById("load").classList.add("hidden");
}
