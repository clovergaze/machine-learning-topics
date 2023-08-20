const ACTION_ADD = "add";
const ACTION_REMOVE = "remove";

function modifyGold(characterId, action) {
    if (action !== ACTION_ADD && action !== ACTION_REMOVE) {
        throw new Error(`Invalid action (action=${action}).`);
    }

    const promptMessage = action === ACTION_ADD
        ? "Add how much gold?"
        : "Remove how much gold?";

    const amount = prompt(promptMessage);

    if (amount === null) {
        return;
    }

    const url = `/characters/${characterId}/gold`;

    fetch(url, {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify({ action, amount })
    })
    .then(response => response.json().then(data => {
        if (!response.ok) {
            alert(data.message);
        } else {
            return data;
        }
    }))
    .then(data => {
        document.getElementById('gold-amount').textContent = data.updated_gold;
    });
}
