const algorithms = window.CIPHER_ALGORITHMS || [];
const tabButtons = document.querySelectorAll(".tab-button");
const inputText = document.querySelector("#input-text");
const resultText = document.querySelector("#result-text");
const keyInput = document.querySelector("#cipher-key");
const keyLabel = document.querySelector("#key-label");
const statusLine = document.querySelector("#status-line");
const useResultButton = document.querySelector("#use-result");

let activeAlgorithm = algorithms[0];

function setActiveAlgorithm(algorithmId) {
    activeAlgorithm = algorithms.find((item) => item.id === algorithmId) || algorithms[0];

    tabButtons.forEach((button) => {
        button.classList.toggle("is-active", button.dataset.algorithm === activeAlgorithm.id);
    });

    keyInput.type = activeAlgorithm.keyType;
    keyInput.value = activeAlgorithm.defaultKey;
    keyLabel.textContent = activeAlgorithm.keyLabel;
    resultText.value = "";
    setStatus(`${activeAlgorithm.name} selected`);
}

async function runCipher(action) {
    if (!activeAlgorithm) {
        setStatus("No algorithm selected", true);
        return;
    }

    const payload = {
        key: keyInput.value,
        text: inputText.value,
    };
    payload[action === "encrypt" ? "plain_text" : "encrypted_text"] = inputText.value;
    setStatus("Processing...");

    try {
        const response = await fetch(`/api/${activeAlgorithm.id}/${action}`, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(payload),
        });
        const data = await response.json();

        if (!response.ok) {
            throw new Error(data.error || "Request failed");
        }

        resultText.value = data.result;
        setStatus(`${activeAlgorithm.name} ${action} complete`);
    } catch (error) {
        resultText.value = "";
        setStatus(error.message, true);
    }
}

function setStatus(message, isError = false) {
    statusLine.textContent = message;
    statusLine.classList.toggle("is-error", isError);
}

tabButtons.forEach((button) => {
    button.addEventListener("click", () => setActiveAlgorithm(button.dataset.algorithm));
});

document.querySelectorAll("[data-action]").forEach((button) => {
    button.addEventListener("click", () => runCipher(button.dataset.action));
});

useResultButton.addEventListener("click", () => {
    if (resultText.value) {
        inputText.value = resultText.value;
        resultText.value = "";
        setStatus("Result moved to input");
    }
});

document.querySelector("#cipher-form").addEventListener("reset", () => {
    window.setTimeout(() => {
        inputText.value = "";
        resultText.value = "";
        keyInput.value = activeAlgorithm.defaultKey;
        setStatus("Ready");
    });
});

setActiveAlgorithm(activeAlgorithm.id);
