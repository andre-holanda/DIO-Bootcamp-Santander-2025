''' Autor: André Holanda
    Projeto: Sistema de Controle de Acesso
    Data: 03/07/2025

    Descrição:
        Uma empresa deseja criar um sistema simples de login para permitir acesso de funcionários. O sistema precisa verificar se o usuário está cadastrado e se a senha informada está correta.
    
    Entrada:
        O programa recebe duas linhas de entrada:
            - Primeira linha: Nome do usuário cadastrado.
            - Segunda linha: Senha correspondente ao usuário.
    Saída:
        "Acesso permitido" se as credenciais estiverem corretas.
        "Usuário ou senha incorretos" caso contrário.
'''

# Dicionário com usuários cadastrados e suas senhas
usuarios = {
    "joao": "1234",
    "ana": "abcd",
    "maria": "senha123",
    "marcelo": "iou789",

}

# TODO: Verifique se o usuário existe e a senha está correta:
def validar_usuario(usuario, senha):
    """Função validar_usuario
        Função que recebe dois parâmetros e valida se os parâmetros estão cadastrados no dicionário (base).
    Parameters
    ---------------
        usuario : str
            string contendo o login do usuário
        senha : str
            string contendo a senha do usuário

    """
    login = usuario.lower()
    password = senha.lower()

    if login in usuarios:
        if password == usuarios[login]:
            print("Acesso permitido")
        else:
            print("Usuário ou senha incorretos")    
    else:
        print("Usuário ou senha incorretos")

# Entrada do usuário
usuario = input().strip()
senha = input().strip()

validar_usuario(usuario, senha)