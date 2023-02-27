async function runChecks() {
    showLoading();
    console.log("run");
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
        .then((data) => parseErrorMessages(data.messages))
        .catch(function(error) {
            hideLoading();
            if (error.response == 422) {
                console.log("Oops");
            } else {
                console.log("something else");
            }
        });
}

async function parseErrorMessages(errorMessages) {
    hideLoading();
    clearErrorMessages();

    if (errorMessages.length == 0) {
        createErrorWindowMessage(
            "No Errors Found!",
            "Your code looks good."
        )
    } else {
        for (const i in errorMessages) {
            let specs = errorMessages[i].split(":", 4);
            let line = specs[1];
            let column = specs[2];

            let error = specs[3].trim().split("[");
            let errorType = error[error.length - 1];
            errorType = errorType.substring(0, errorType.length - 1);
            let message = error.slice(0, error.length - 1);

            createErrorWindowMessage(
                errorType + " Error at " + line + ":" + column,
                message    
            );
        }
    }
}

async function createErrorWindowMessage(label, body) {
    const errorWindowMessage = document.createElement("section");
    errorWindowMessage.classList.add("error");

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

async function showLoading() {
    document.getElementById("load").classList.remove("hidden");
    document.getElementById("load").classList.remove("fade-in");
}

async function hideLoading() {
    document.getElementById("load").classList.add("hidden");
    document.getElementById("load").classList.add("fade-in");
}
