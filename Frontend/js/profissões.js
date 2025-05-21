// Função para capturar as informações do formulário e gerar sugestões
document.getElementById('careerForm').addEventListener('submit', function(event) {
    event.preventDefault();

    // Captura as informações inseridas no formulário
    const interest = document.getElementById('interest').value.trim();
    const skills = document.getElementById('skills').value.trim();
    const education = document.getElementById('education').value;

    const careerList = document.getElementById('careerList');
    careerList.innerHTML = ''; // Limpa a lista de sugestões

    // Exemplos de sugestões com base nas informações fornecidas
    const careers = [
        { name: 'Desenvolvedor de Software', criteria: ['Tecnologia', 'Análise', 'Superior'] },
        { name: 'Médico', criteria: ['Saúde', 'Comunicação', 'Superior'] },
        { name: 'Designer Gráfico', criteria: ['Arte', 'Criatividade', 'Superior'] },
        { name: 'Assistente Social', criteria: ['Ajuda Social', 'Comunicação', 'Superior'] },
        { name: 'Analista de Dados', criteria: ['Tecnologia', 'Análise', 'Superior'] }
    ];

    // Filtro das sugestões
    const filteredCareers = careers.filter(career => {
        return career.criteria.some(c => interest.includes(c) || skills.includes(c));
    });

    // Exibe as sugestões de carreira
    if (filteredCareers.length > 0) {
        filteredCareers.forEach(career => {
            const li = document.createElement('li');
            li.textContent = career.name;
            careerList.appendChild(li);
        });
    } else {
        careerList.innerHTML = '<li>Nenhuma sugestão encontrada. Tente alterar suas respostas.</li>';
    }
});
