from fastapi import FastAPI


app = FastAPI()

tabela = {'Número': [1, 2, 3, 4, 5],
          'Nome': ['João', 'Maria', 'Pedro', 'Ana', 'Carlos'],
          'Idade': [20, 25, 30, 35, 40],
          'Cidade': ['São Paulo', 'Rio de Janeiro', 'Belo Horizonte', 'Curitiba', 'Florianópolis'],
          'País': ['Brasil', 'Brasil', 'Brasil', 'Brasil', 'Brasil']
          }
@app.get('/')
def home():
    return f"{tabela}"
