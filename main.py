banco_usuario = []
banco_senha = []

cadastrando_usuario = str(input('Cadastre seu nome de usuario : \n')).lower()
banco_usuario.append(cadastrando_usuario)

cadastrando_senha = int(input('Cadastre uma senha numérica : \n'))
banco_senha.append(cadastrando_senha)


login = False

while not login:
    usuario = str(input('Insira seu usuario para logar:\n')).lower()
    senha = int(input('Insira sua senha para logar :\n'))

    if (usuario in banco_usuario) and (senha in banco_senha):
        print('Logado')
        login = True
    else:
        print('Usuario não cadastrado')

