from application import app
from flask import render_template, request
import json
from application.model.entity.produto import Produto
from application.model.dao.produto_DAO import ProdutoDAO


@app.route("/")
def home():
    todos_produtos = ProdutoDAO().get_exibir_produtos()
    return render_template("index.html", todos_produtos = todos_produtos)