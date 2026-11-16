from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from modelos import Emprestimo, Usuario, Exemplar, Prateleira

conexao_banco = create_engine('sqlite:///biblioteca.db', echo=False)
FabricaDeSessoes = sessionmaker(bind=conexao_banco)
sessao = FabricaDeSessoes()

print("=== CONSULTA 1: Empréstimos ativos do usuário Carlos Eduardo ===")
emprestimos_usuario = sessao.query(Emprestimo).join(Usuario).filter(
    Usuario.nome == "Carlos Eduardo",
    Emprestimo.ativo == True
).all()

for emprestimo in emprestimos_usuario:
    print(f"Empréstimo: {emprestimo.codigo} | Livro: {emprestimo.exemplar.livro.titulo} | Exemplar: {emprestimo.exemplar.codigo}")


print("\n=== CONSULTA 2: Exemplares na Prateleira de Tecnologia (P01) ===")
exemplares_na_prateleira = sessao.query(Exemplar).join(Prateleira).filter(
    Prateleira.codigo == "P01"
).all()

for exemplar in exemplares_na_prateleira:
    status = "Disponível" if exemplar.disponivel else "Emprestado"
    print(f"Exemplar: {exemplar.codigo} | Livro: {exemplar.livro.titulo} | Status: {status}")


print("\n=== CONSULTA 3: Exemplares atualmente emprestados ===")
exemplares_emprestados = sessao.query(Exemplar).filter(
    Exemplar.disponivel == False
).all()

for exemplar in exemplares_emprestados:
    print(f"Exemplar emprestado: {exemplar.codigo} | Título: {exemplar.livro.titulo}")
