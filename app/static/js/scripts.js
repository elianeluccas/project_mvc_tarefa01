document.getElementById('calcForm').addEventListener('submit', function(event) {
    event.preventDefault(); // Evita o envio do formulário

    const var1 = document.getElementById('var1').value;
    const var2 = document.getElementById('var2').value;

    if (var1 && var2) {
        const resultado = parseInt(var1) + parseInt(var2);

        // Adicionar o resultado ao elemento HTML
        document.getElementById('resultado').innerText = resultado;

        // Remover classe 'hidden' se estiver oculta
        document.getElementById('resultado-container').classList.remove('hidden');
    }
});

document.getElementById('problemaForm').addEventListener('submit', function(event) {
    event.preventDefault(); // Impede o envio do formulário

    // Pegando os valores dos campos
    const var1 = document.getElementById('var1').value;
    const var2 = document.getElementById('var2').value;

    if (var1 && var2) {
        // Realizando o cálculo
        const resultado = parseInt(var1) + parseInt(var2);

        // Exibindo o resultado
        document.getElementById('resultado').innerText = resultado;

        // Tornando visível o container do resultado
        document.getElementById('resultado-container').classList.remove('hidden');
    }
});
