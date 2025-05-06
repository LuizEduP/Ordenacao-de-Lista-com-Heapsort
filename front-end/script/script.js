let input = {"numeros":""}

let button = document.getElementById("button").addEventListener('click', () => {
    let adicionado = document.getElementById("numeros").value;
    input.numeros = adicionado;
    const apiUrl = "http://localhost:5000/ordenar"
    
    fetch(apiUrl, {
        method: 'POST', 
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(input)
      })
      .then(response => {
        if (!response.ok) {
          throw new Error('Erro na requisição');
        }
        return response.json();
      })
      .then(data => {
        console.log('Resposta da API:', data);
      })
      .catch(error => {
        console.error('Erro:', error);
      });

      fetch(apiUrl)
      .then(response => {
        if (!response.ok) {
          throw new Error('Erro ao buscar os dados da API');
        }
        return response.json();
      })
      .then(dados => {
        const lista = document.getElementById('lista');

        
        dados.numeros.forEach(item => {
          const li = document.createElement('li');
          li.textContent = item.numero;
          lista.appendChild(li);
        });
      })
      .catch(error => {
        console.error('Erro ao carregar a lista:', error);
      });
})

