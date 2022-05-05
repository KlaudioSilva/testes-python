# from curses import window
import PySimpleGUI as pg

# passo 1: configurar tema
pg.theme('DarkAmber')

# passo 2: criar layout
layout = [
    [pg.Text('Digite nome:')],
    [pg.InputText()],
    [pg.Button('Ok'), pg.Button('Cancelar')]
]

# passo 3: criar a janela
window = pg.Window('Janela v2.0', layout)

# passo 4: loop event
while True:
    event, values = window.read()
    if event == 'Cancelar' or event == pg.WIN_CLOSED:
        break
    print(values[0])

# passo 5: fechar a janela
window.close()