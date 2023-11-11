from backend.geral.config import *
from backend.modelo.jogador import *
from backend.modelo.jogador import Jogador

# inserindo a aplicação em um contexto :-/
with app.app_context():

    if os.path.exists(arquivobd):
        os.remove(arquivobd)

    # criar tabelas
    db.create_all()

    j1 = Jogador(pontos = 0)
    db.session.add(j1)
    db.session.commit()
    print(j1)
    print(j1.json())

    print("Banco de dados e tabelas criadas")