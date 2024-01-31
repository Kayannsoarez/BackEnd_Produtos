from fastapi import FastAPI
from models.products import Product

# Cria uma instância da classe FastAPI
app = FastAPI()

# Rota principal acessada através do método GET
@app.get('/')
def say():
    # Retorna um dicionário JSON {'Fast':'API'}
    return {'Fast':'API'}

# Rota acessada através do método GET com um parâmetro 'name' na URL
@app.get('/{name}')
def say_hi(name: str):
    # Verifica se o parâmetro 'name' não está vazio
    if not name:
        pass
    # Retorna um dicionário JSON {'Hello': name}
    return {'Hello': name}

# Dados de exemplo da lista de produtos
data = [
    Product(id=1, name='Tenis Nike Air', description='Calçados', price=799.99),
    Product(id=2, name='Iphone', description='Tecnologia', price=3998.99),
    Product(id=3, name='Notebook', description='Tecnologia', price=4980.99),
]

# Rota acessada através do método GET para obter a lista de produtos
@app.get('/api/products')
def get_products():
    # Retorna a lista de produtos
    return data
