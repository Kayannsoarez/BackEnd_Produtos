from pydantic import BaseModel

# Define uma classe Product que herda de BaseModel
class Product(BaseModel):
    """
    Modelo de dados para representar um produto.

    Atributos:
        id (int): Identificador único do produto.
        name (str): Nome do produto.
        description (str): Descrição do produto.
        price (float): Preço do produto.
    """
    # Declaração dos atributos da classe com os tipos esperados
    id: int
    name: str
    description: str
    price: float