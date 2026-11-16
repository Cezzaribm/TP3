from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from modelos import Base, Prateleira, Livro, Exemplar, Usuario, Emprestimo

conexao_banco = create_engine('sqlite:///biblioteca.db', echo=False)
Base.metadata.create_all(conexao_banco)

FabricaDeSessoes = sessionmaker(bind=conexao_banco)
sessao = FabricaDeSessoes()

prateleira_ti = Prateleira(codigo="P01", nome="Tecnologia")
prateleira_geral = Prateleira(codigo="P02", nome="Geral")

livro_engenharia = Livro(codigo="L01", titulo="Engenharia de Software", autor="Ian Sommerville", ano="2019")

exemplar1 = Exemplar(codigo="EX01", livro=livro_engenharia, prateleira=prateleira_ti, disponivel=False)
exemplar2 = Exemplar(codigo="EX02", livro=livro_engenharia, prateleira=prateleira_ti, disponivel=True)

usuario_carlos = Usuario(codigo="U01", nome="Carlos Eduardo")
usuario_maria = Usuario(codigo="U02", nome="Maria Clara")

emprestimo1 = Emprestimo(codigo="EMP01", usuario=usuario_carlos, exemplar=exemplar1, ativo=True)

sessao.add_all([
    prateleira_ti, 
    prateleira_geral, 
    livro_engenharia, 
    exemplar1, 
    exemplar2, 
    usuario_carlos, 
    usuario_maria, 
    emprestimo1
])

sessao.commit()
print("Banco de dados populado com sucesso!")
