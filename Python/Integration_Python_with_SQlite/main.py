# Import the library/Importa as bibliotecas
from sqlalchemy import inspect,create_engine, select
from sqlalchemy import Column, String, Integer, BINARY, DECIMAL, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.orm import DeclarativeBase,Session


# 1° Vamos criar a engine e base
engine = create_engine('sqlite://')

class Base(DeclarativeBase):
    pass


# 2°Mapping the class in database/Mapeando as classes que esta relacionada com os dados
# 2.1 Mapping the Cliente/Mapeando a classe Cliente
class Cliente(Base):
    __tablename__ = "Cliente"
    id      = Column(Integer  , primary_key=True)
    name    = Column(String   , nullable=False)
    cpf     = Column(String(9), nullable=False)
    address = Column(String(9))

    r_Cliente = relationship("Conta",back_populates= "r_Conta")
    def __repr__(self):
        return f"Name: {self.name}, cpf:{self.cpf}, id={self.id}, address:{self.address} \n"


# 2.2 Mapping the Account/ Mapeando a classe Conta
class Conta(Base):
    __tablename__ = "Conta"
    id      = Column(Integer, primary_key=True)
    type    = Column(String)
    agency  = Column(String)
    num     = Column(Integer)
    saldo   = Column(DECIMAL)
    id_client = Column(Integer, ForeignKey('Cliente.id'))

    r_Conta = relationship("Cliente",back_populates= "r_Cliente")

    def __repr__(self):
        return f"id:{self.id}, type:{self.type} Agency:{self.agency},num={self.num\
            }  with saldo:{self.saldo} , id_client:{self.id_client} \n"

Base.metadata.create_all(engine)


with Session(engine) as session:
    # Inserindo dados: Criando 3 clientes
    clientes = [
            Cliente(name='João', cpf='12345678901', address='Rua A'),
            Cliente(name='Maria', cpf='12345678902', address='Rua B'),
            Cliente(name='José', cpf='12345678903', address='Rua C'),]
    session.add_all(clientes)
    
    
    contas = [ 
            Conta(type='CC1',agency='0001',num=10, saldo=10,id_client=1),
            Conta(type='CC2',agency='0002',num=20, saldo=20,id_client=2),
            Conta(type='CC3',agency='0003',num=30, saldo=30,id_client=3),]
    session.add_all(contas)
    session.commit()
 
 
# Aqui podemos pegar dos dados das tabelas que estão conectados.     
data = session.query(Cliente)\
                .join(Conta,Cliente.id == Conta.id_client)\
                .with_entities(Cliente.name,Conta.agency).all()
print(data)

# Aqui podemos pegar dos dados individualmente .  
# join_str = select(Conta).join_from(Conta,Cliente)
# for result in session.scalars(join_str):
#     print(result)
    
# join_str = select(Cliente).join_from(Conta,Cliente)
# for result in session.scalars(join_str):
#     print(result)
    
    
# Fechando a seção   
session.close()