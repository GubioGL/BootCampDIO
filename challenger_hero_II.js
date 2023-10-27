
function classification(xp_){
    let nivel = ""

    if(xp_<=10){                            nivel = "Ferro"
    }else if ((20  >= xp_) && (xp_ > 10)) { nivel = "Bronze"
    }else if ((50  >= xp_) && (xp_ > 20)) { nivel = "Prata"
    }else if ((80  >= xp_) && (xp_ > 50)) { nivel = "Ouro"
    }else if ((90  >= xp_) && (xp_ > 80)) { nivel = "Diamante"
    }else if ((100 >= xp_) && (xp_ > 90)) { nivel = "Lendário"
    }else{                                  nivel = "Imortal"
    }
    return nivel
}

function ranked(victories_, defeats_){
    let result = victories_ - defeats_
    if( result<0){result = 0 }
    return `O Herói tem de saldo de ${result} está no nível de ${classification(result)}`
}

console.log(ranked(70,2))