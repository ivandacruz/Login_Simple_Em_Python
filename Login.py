from PySimpleGUI import PySimpleGUI as sg 

# Layout
sg.theme('Reddit')
layout  = [
    [sg.Text('Usuário'),sg.Imput(key='usuario', size=(20, 1))],
    [sg.Text('Senha'),sg.Imput(key='senha',password_char='*', size=(20, 1))],
    [sg.Checkbox('Salvar o login?')],
    [sg.Button('Login')]
]
# Janela
janela = sg.window('Tela de Login', layout)
# Ler os eventos
while True:
    eventos, valores = janela.read()
    if eventos == sg.WINDOW_CLOSED:
        break
    if eventos == 'Entrar':
        if valores['usuario'] == 'ivan' and valores['senha'] == '123456':
            print('Seja bem-vindo!')