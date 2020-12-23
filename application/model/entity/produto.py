class Produto:
    def __init__(self, id, imagem, nome, descricao, precoAntigo, precoAtual, qntParcela, valorParcela):
        self._id = id
        self._imagem = imagem
        self._nome = nome
        self._descricao = descricao
        self._precoAntigo = precoAntigo
        self._precoAtual = precoAtual
        self._qntParcela = qntParcela
        self._valorParcela = valorParcela

    def get_id(self):
        return self._id

    def get_imagem(self):
        return self._imagem

    def get_nome(self):
        return self._nome

    def get_descricao(self):
        return self._descricao

    def get_precoAntigo(self):
        return self._precoAntigo

    def get_precoAtual(self):
        return self._precoAtual

    def get_qntParcela(self):
        return self._qntParcela

    def get_valorParcela(self):
        return self._valorParcela