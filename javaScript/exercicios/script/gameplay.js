
const parameter = new URLSearchParams(window.location.search);
const dif = parameter.get('dif');
// Variáveis do HTML
const difField = document.getElementById('dif');
const result = document.getElementById('result');
const inputNumber = document.getElementById('inputNumber');
const triesField = document.getElementById('tries');
const tipsField = document.getElementById('tips');
// Variáveis do Jogo
let sortedNumber = 0;
let tries = 4;
let tips = 2;

triesField.textContent = tries;
tipsField.textContent = tips;


switch(dif){
    case 'easy':
        difField.textContent = 'Dificuldade escolhida: Fácil';
        sortedNumber = Math.floor(Math.random() * 30) + 1;
        break;
    case 'med':
        difField.textContent = 'Dificuldade escolhida: Médio';
        sortedNumber = Math.floor(Math.random() * 50) + 1;
        break;
    case 'hard':
        difField.textContent = 'Dificuldade escolhida: Difícil';
        sortedNumber = Math.floor(Math.random() * 100) + 1;
        break;
    default:
        difField.textContent = 'Não encontramos a dificuldade'
        break;
}

console.log(sortedNumber);

function exit() {
    window.location.replace('./home.html');
}


function gameplay() {
    let number = parseInt(inputNumber.value);

    if ( number == sortedNumber ) {
        result.textContent = 'Você acertou !!';
        // Informa o usuário da vitória e logo em seguida manda para a tela inicial

        return;
    
    }
    else {
        if (tries > 0){
            tries = tries -1;
            triesField.textContent = tries;

            result.textContent = 'Buuuuuhhh nao foi desta vez !!! Voce tem '+ tries +' tentativas restantes';
        }
        if (tries <= 0) {
            result.textContent = "Game Over"

            return exit();
        }
        if (number > sortedNumber){
            tipe.textContent = "Esta maior que o numero sorteado";
        }
        
        if (number < sortedNumber){
            tipe.textContent ="Esta menor que o numero sorteado";
            }

      function tips(){
        if (tips < 0) {
            alert ("voce nao tem dicas restantes.");
            return
        }
        else {
            tips = tips - 1;
            tipsField.textContent = tips;
        }
      }
   }
}    

