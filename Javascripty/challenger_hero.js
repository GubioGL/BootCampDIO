let xp = 10000
let nome =  "Xiquinho"
let nivel= ""

if(xp<=1000){                  nivel = "Ferro"
}else if ((2000 >= xp) && (xp > 1000)) { nivel = "Bronze"
}else if ((3000 >= xp) && (xp > 2000)) { nivel = "Prata"
}else if ((4000 >= xp) && (xp > 3000)) { nivel = "Ouro"
}else if ((5000 >= xp) && (xp > 4000)) { nivel = "Platina"
}else if ((6000 >= xp) && (xp > 5000)) { nivel = "Ascendente"
}else if ((7000 >= xp) && (xp > 6000)) { nivel = "Imortal"
}else{                         nivel = "Radiante"}
console.log("O Herói de nome "+ nome +" está no nível de "+ nivel)