function show(anything) {
    document.querySelector('#id_bot_name').value = anything;
    document.querySelector(".span-bot").textContent=anything;

    console.log(document.querySelector('#id_bot_name').value)
}