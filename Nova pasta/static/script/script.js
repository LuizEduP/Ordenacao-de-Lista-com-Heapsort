document.getElementById("button").addEventListener("click", async () => {
  const input = document.getElementById("numeros").value;
  const listaUl = document.getElementById("lista");

  try {
      const resposta = await fetch("/ordenar", {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({
              numeros: input.split(",").map(num => num.trim())
          })
      });

      const dados = await resposta.json();
      listaUl.innerHTML = "";

      if (resposta.ok) {
          dados.ordenado.forEach(num => {
              const li = document.createElement("li");
              li.textContent = num;
              listaUl.appendChild(li);
          });
      } else {
          alert(dados.erro || "Erro ao ordenar.");
      }
  } catch (erro) {
      console.error("Erro na requisição:", erro);
      alert("Erro ao conectar à API.");
  }
});
