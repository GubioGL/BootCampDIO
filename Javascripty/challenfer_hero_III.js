class hero {
    constructor(name,age,tipo) {
      this.name = name;
      this.age  = age;
      this.tipo = tipo;
    }
    attack(){
        if( this.tipo === "ninja"  ){
            console.log(`O ${this.tipo} atacou usando shuriken!`)
        } else if ( this.tipo === "mago"   ){
            console.log(`O ${this.tipo} atacou usando magia!`)
        } else if ( this.tipo == "monge"   ){
            console.log(`O ${this.tipo} atacou usando marciais!`)
        } else if ( this.tipo == "guerreio"){
            console.log(`O ${this.tipo} atacou usando espada!`)
        }else{
            console.log("Erro!\nVerifique se vc digitou corretamente \nEscreva tudo em letra minuscula!")
        } 
    }
}

// Exemplo de uso:
const Hero = new hero("Ninja Hero", 25, "ninja");
Hero.attack();

const Hero2 = new hero("Kirito", 30, "mago");
Hero2.attack();