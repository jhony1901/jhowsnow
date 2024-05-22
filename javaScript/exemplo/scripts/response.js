
var botao = document.getElementById("btnEnviar");
var inputName = document.getElementById("inputName");
var inputQuestion = document.getElementById("inputQuest1");
var inputYear = document.getElementById("inputYear");


function saudacoes() {
    let name = inputName.value;
    let food = inputQuestion.value;
    let year = inputYear.value;

    let response = document.getElementById("response");
    let idade = 0;
    let comidas = ['macarrão', 'pizza', 'lasanha', 'macarrao', 'strogonoff', 'sardinha', 'sanduiche'];
    let checkFood = false;

    idade = 2024 - year;

    if ( idade < 0 ) {
        alert('Ano de nascimento invalido.');
        return;
    }
    //              && (and)      || (or)
    if ( name.length < 3 || name.length > 15 ) {
        alert('O nome deve ter de 3 a 15 letras.');
        return;
    }

    // For EACH
    //comidas.forEach(comida => {

    //});


    // For Normal
    for (let i=0; i<comidas.length; i++) {
        if ( food.toLowerCase() == comidas[i].toLowerCase() ) {
            checkFood = true;
            break;
        }
    }

    if ( checkFood == false ) {
        alert('A comida selecionada não estão disponivel.');
        return;
    }

    if ( idade < 60 ) {
        response.textContent = "Olá, tudo bem " + name + ", hoje eu trouxe " + food + " para você";
    }
    else {
        response.textContent = "Olá, tudo bem Sr. " + name + ", hoje eu trouxe " + food + " para você";
    }
}


botao.onclick = saudacoes;