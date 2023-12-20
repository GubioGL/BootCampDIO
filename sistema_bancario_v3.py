""" 
    Sistema_bancario v3
    Nessa versão sera utilizado o conhecimento de Classes
"""

from abc import ABC, abstractmethod

class Cliente():
    def __init__(self,endereco= None,conta=None):
        self.endereco = endereco
        self.conta = conta
    def realizar_transacao(self,conta,transacao):
        pass
        # transacao.registrar(conta)
    def adiconar_conta(self,conta):
        pass
        # self.conta.append(conta)

class PessoaFisica(Cliente):
    def __init__(self,nome=None,cpf=None,data_nascimento=None,endereco= None,conta=None):
        super().__init__(endereco=endereco,conta=conta)
        self.nome = nome
        self.cpf  = cpf
        self.data_nascimento = data_nascimento 

class Conta:
    
    def __init__(self,numero=None,cliente=None,historico=None):
        """
        Inicializa uma nova conta com os seguintes parâmetros:
        
        saldo: valor inicial da conta (padrão: 0)
        numero: número da conta (padrão: None)
        agencia: número da agência (padrão: None)
        cliente: nome do cliente (padrão: None)
        historico: lista vazia para armazenar o histórico da conta (padrão: None)
        """
        self.saldo   = 0
        self.numero  = numero
        self.agencia = "0001"
        self.cliente = cliente
        self.historico = historico or []
    @property
    def saldo(self):
        return self.saldo
    @property
    def numero(self):
        return self.numero
    @property
    def cliente(self):
        return self.cliente
    @property
    def agencia(self):
        return self.agencia
    @property
    def historico(self):
        return self.historico
    
    
    def sacar(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            print(f"Saque de R")
            return True
        else:
            return False
    def nova_conta(self,cliente,numero):
        return Conta()
                   
    def depositar(self, valor):
        if self.valor >= 0:
            self.saldo += valor
            print(f"Deposito de R${valor}")
            return True
        else:
            return False
            
            
class ContaCorrent(Conta):
    
    def __init__(self,cliente,numero,limite =500, limite_saque=3):
        super().__init__(cliente=cliente,numero=numero)
        self.limite = limite
        self.limite_saque = limite_saque
        
    def sacar(self, valor):
        if self.limite <= valor and self.limite_saque >= 1:
            if self.saldo - valor >= 0:
                self.saldo -= valor
                self.limite_saque -= 1
                print(f"Saque de R")
                return True
            else:
                return False
        else:
            return False
        
    def __str__(self):
        return f""" \
                    Agencia: \t{self.agencia}
                    C/C: \t\t{self.numero}
                    Titular:\t{self.cliente.nome}
                    """


class historico:
    def __init__(self):
        self.transacoes = []
    
    @property
    def transacoes(self):
        return self.transacoes
    
    def add_transacoes(self, transacao):
        self.transacao.append(
            {
                "tipo": transacao.__class__.__name__,
                "valor": transacao.valor,
            }
        )
        
class Transacao(ABC):
    @property
    @abstractmethod
    def valor(self):
        pass
    
    @abstractmethod
    def registrar(self, conta):
        pass
    
def Saque(Transacao):
    def __init__(self, valor):
        self._valor = valor
    @property
    def valor(self):
        return self._valor
    def registrar(self, conta):
        suc_transacao =  conta.sacar(self._valor)
        if suc_transacao:
            conta.historico.add_transacao(self)