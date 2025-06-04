// Dados e listas
const areas = ["exatas", "saude", "humanas", "arte", "tecnologia"];
const ambientes = ["escritorio", "hospital", "criativo", "laboratorio", "campo"];
const estilos = ["dinamico", "estavel", "flexivel"];
const personalidades = ["analitico", "comunicativo", "cuidadoso", "criativo", "pratico"];
const motivacoes = ["dinheiro", "impacto", "criatividade", "pesquisa"];

const nomesBase = [
  "Faculdade Alfa", "Instituto Beta", "Centro Gamma", "Universidade Delta", "Escola Épsilon",
  "Faculdade Zeta", "Instituto Eta", "Centro Teta", "Universidade Iota", "Escola Kappa"
];

function aleatorio(arr) {
  return arr[Math.floor(Math.random() * arr.length)];
}

function geraNome(index) {
  const base = nomesBase[index % nomesBase.length];
  const area = areas[index % areas.length];
  return `${base} de ${area.charAt(0).toUpperCase() + area.slice(1)} ${index + 1}`;
}

const faculdades = [];
for(let i = 0; i < 3000; i++) {
  faculdades.push({
    nome: geraNome(i),
    area: aleatorio(areas),
    ambiente: aleatorio(ambientes),
    estilo: aleatorio(estilos),
    personalidade: aleatorio(personalidades),
    motivacao: aleatorio(motivacoes)
  });
}

// Perguntas para o questionário
const perguntas = [
  {id: "area", texto: "Qual área você prefere?", opcoes: areas},
  {id: "ambiente", texto: "Qual ambiente de trabalho você prefere?", opcoes: ambientes},
  {id: "estilo", texto: "Que estilo de trabalho você gosta?", opcoes: estilos},
  {id: "personalidade", texto: "Qual sua personalidade?", opcoes: personalidades},
  {id: "motivacao", texto: "Qual sua maior motivação?", opcoes: motivacoes}
];

// Montar o questionário no HTML
const form = document.getElementById("questionario");
perguntas.forEach(({id, texto, opcoes}) => {
  const div = document.createElement("div");
  const label = document.createElement("label");
  label.setAttribute("for", id);
  label.textContent = texto;
  const select = document.createElement("select");
  select.id = id;
  select.name = id;

  const optionDefault = document.createElement("option");
  optionDefault.value = "";
  optionDefault.textContent = "-- Selecione --";
  optionDefault.disabled = true;
  optionDefault.selected = true;
  select.appendChild(optionDefault);

  opcoes.forEach(op => {
    const option = document.createElement("option");
    option.value = op;
    option.textContent = op.charAt(0).toUpperCase() + op.slice(1);
    select.appendChild(option);
  });

  div.appendChild(label);
  div.appendChild(select);
  form.appendChild(div);
});

// Função para recomendar faculdades com base nas respostas
function recomendarFaculdades(respostas) {
  return faculdades.filter(f => {
    let score = 0;
    if(f.area === respostas.area) score++;
    if(f.ambiente === respostas.ambiente) score++;
    if(f.estilo === respostas.estilo) score++;
    if(f.personalidade === respostas.personalidade) score++;
    if(f.motivacao === respostas.motivacao) score++;
    return score >= 3;
  }).slice(0, 10);
}

// Mostrar resultado na tela
const resultadoDiv = document.getElementById("resultado");
document.getElementById("btnEnviar").addEventListener("click", () => {
  // Pegar respostas
  const respostas = {};
  let faltando = false;
  perguntas.forEach(({id}) => {
    const val = document.getElementById(id).value;
    if (!val) faltando = true;
    respostas[id] = val;
  });
  if (faltando) {
    alert("Por favor, responda todas as perguntas.");
    return;
  }

  // Recomendação
  const recomendadas = recomendarFaculdades(respostas);

  // Mostrar
  resultadoDiv.innerHTML = "";
  if(recomendadas.length === 0) {
    resultadoDiv.textContent = "Nenhuma faculdade corresponde exatamente às suas preferências. Tente variar as respostas.";
    return;
  }

  recomendadas.forEach(f => {
    const card = document.createElement("div");
    card.className = "faculdade-card";
    card.innerHTML = `
      <h3>${f.nome}</h3>
      <p><strong>Área:</strong> ${f.area.charAt(0).toUpperCase() + f.area.slice(1)}</p>
      <p><strong>Ambiente:</strong> ${f.ambiente.charAt(0).toUpperCase() + f.ambiente.slice(1)}</p>
      <p><strong>Estilo:</strong> ${f.estilo.charAt(0).toUpperCase() + f.estilo.slice(1)}</p>
      <p><strong>Personalidade:</strong> ${f.personalidade.charAt(0).toUpperCase() + f.personalidade.slice(1)}</p>
      <p><strong>Motivação:</strong> ${f.motivacao.charAt(0).toUpperCase() + f.motivacao.slice(1)}</p>
    `;
    resultadoDiv.appendChild(card);
  });
});
