''' Autor: André Holanda
    Descrição: Uma empresa quer validar se os e-mails cadastrados pelos usuários estão no formato correto. Crie uma função que receba um e-mail e verifique se ele é válido, seguindo as regras:
    Regras para um e-mail válido:
        Deve conter o caractere "@" e um domínio, como gmail.com ou outlook.com.
        Não pode começar ou terminar com "@".
        Não pode conter espaços.
'''

dominios = ['gmail.com', 'outlook.com']

# TODO: Verifique as regras do e-mail:
while True:
    # Entrada do usuário
    email = input().strip()
    
    if "@" in email:
        dominio = email.split('@')[1]
        if email[0] == "@" or email[-1] == "@":
            print("E-mail inválido")
        elif dominio not in dominios:
            print("E-mail inválido")
        else:
            print("E-mail válido")
    else:
        print("E-mail inválido")
    
    nova_consulta = input("Deseja informar um novo email? (S/N): ").strip().upper()
    if nova_consulta == "N":
        break


##################### Solução do desafio p/ passar no interpretador #####################
dominios = ['gmail.com', 'outlook.com']

# Entrada do usuário
email = input().strip()

dominio = email.split('@')[1]

# TODO: Verifique as regras do e-mail:
if "@" in email:
    dominio = email.split('@')[1]
    if email[0] == "@" or email[-1] == "@":
        print("E-mail inválido")
    elif dominio not in dominios:
        print("E-mail inválido")
    else:
        print("E-mail válido")
else:
    print("E-mail inválido")
