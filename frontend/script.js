function add(text, cls) {
  const d = document.createElement("div");
  d.className = "msg " + cls;
  d.innerHTML = text;
  chat.appendChild(d);
}

function send() {
  const q = msg.value;
  add(q, "user");
  msg.value = "";

  typing.style.display = "block";

  fetch("http://127.0.0.1:5000/chat", {
    method: "POST",
    headers: {"Content-Type": "application/json"},
    body: JSON.stringify({query: q})
  })
  .then(r => r.json())
  .then(d => {
    typing.style.display = "none";
    add(d.answer, "bot");
  });
}
