from datetime import date
from sqlalchemy import Column, Date, ForeignKey, Integer, String, Boolean
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()


class Prateleira(Base):
    __tablename__ = 'prateleira'

    id = Column(Integer, primary_key=True)
    codigo = Column(String, unique=True, nullable=False)
    nome = Column(String, nullable=False)

    exemplares = relationship('Exemplar', back_populates='prateleira')


class Livro(Base):
    __tablename__ = 'livro'

    id = Column(Integer, primary_key=True)
    codigo = Column(String, unique=True, nullable=False)
    titulo = Column(String, nullable=False)
    autor = Column(String, nullable=False)
    ano = Column(String, nullable=False)

    exemplares = relationship('Exemplar', back_populates='livro')


class Exemplar(Base):
    __tablename__ = 'exemplar'

    id = Column(Integer, primary_key=True)
    codigo = Column(String, unique=True, nullable=False)
    disponivel = Column(Boolean, default=True)

    livro_id = Column(Integer, ForeignKey('livro.id'), nullable=False)
    prateleira_id = Column(Integer, ForeignKey('prateleira.id'), nullable=True)

    livro = relationship('Livro', back_populates='exemplares')
    prateleira = relationship('Prateleira', back_populates='exemplares')
    emprestimos = relationship('Emprestimo', back_populates='exemplar')


class Usuario(Base):
    __tablename__ = 'usuario'

    id = Column(Integer, primary_key=True)
    codigo = Column(String, unique=True, nullable=False)
    nome = Column(String, nullable=False)

    emprestimos = relationship('Emprestimo', back_populates='usuario')


class Emprestimo(Base):
    __tablename__ = 'emprestimo'

    id = Column(Integer, primary_key=True)
    codigo = Column(String, unique=True, nullable=False)
    data_emprestimo = Column(Date, default=date.today)
    data_devolucao = Column(Date, nullable=True)
    ativo = Column(Boolean, default=True)

    usuario_id = Column(Integer, ForeignKey('usuario.id'), nullable=False)
    exemplar_id = Column(Integer, ForeignKey('exemplar.id'), nullable=False)

    usuario = relationship('Usuario', back_populates='emprestimos')
    exemplar = relationship('Exemplar', back_populates='emprestimos')
