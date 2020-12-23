from application.model.entity.produto import Produto
import json

class ProdutoDAO:
    def __init__(self):
        self._todos_produtos = []

        with open('C:\\Users\\Pedro Vasconcelos\\Documents\\Repositórios Git\\ProvaLinxImpulse\\application\\view\\static\\json\\products.json') as product_file:
            product_list = json.load(product_file)
        
        for i in product_list:
            self._todos_produtos.append(Produto(i['id'], i['image'], i['name'], i['description'], i['oldPrice'], i['price'], i['installments']['count'], i['installments']['value']))

    def get_exibir_produtos(self):
        return self._todos_produtos