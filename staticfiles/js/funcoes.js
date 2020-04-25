function tratamentoBoolean(valor){
    situacao = "" ;
    switch (valor){
        case false:
            situacao = "Não" ;
            break;
        case true:
            situacao = "Sim" ;
            break;
        default:
            situacao = "Indefinido" ;
     }

     return situacao ;
     console.log(situacao);
}