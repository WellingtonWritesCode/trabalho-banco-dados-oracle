import PySimpleGUI as sg

layout_l = [[sg.T("1- Socios:")],
            [sg.T("2- Planos:")],
            [sg.T("3- Mensalidades:")]]

layout_r = [[sg.T("0", key='-SOCIOS-')],
            [sg.T("0", key='-PLANOS-')],
            [sg.T("0", key='-MENSALIDADES-')]]

nomes = [[sg.T("Cleverton dos Santos Liltk")],
         [sg.T("Gustavo de Oliveira Christ")],
         [sg.T("Jhony Rodrigues de Souza")],
         [sg.T("Lucio Ewald do Nascimento")],
         [sg.T("Wellington da Silva Barbosa Junior")]]

layout = [[sg.T("Total de registros existentes:")],
          [sg.Col(layout_l, pad=(0, 0)), sg.Col(layout_r, element_justification='right', pad=(0, 0), expand_x=True)],
          [sg.T()],
          [sg.Col([[sg.T("Criado por: ")]], vertical_alignment='top', pad=(0,0)), sg.Col(nomes, vertical_alignment='top', pad=(0,0))],
          [sg.T()],
          [sg.Col([[sg.T("Disciplina: ")]], vertical_alignment='top', pad=(0,0)), sg.Col([[sg.T("Banco de Dados")],
                                                                                           [sg.T("2022/2")]], vertical_alignment='top', pad=(0,0))],
          [sg.T("Professor: Howard Roatti")]]
window = sg.Window("Temp-Name", layout, finalize=True)

popup_layout = [[sg.T("Temp-Name")],
                [sg.T("Cleverton dos Santos Liltk")],
                [sg.T("Gustavo de Oliveira Christ")],
                [sg.T("Jhony Rodrigues de Souza")],
                [sg.T("Lucio Ewald do Nascimento")],
                [sg.T("Wellington da Silva Barbosa Junior")],
                [sg.B("Ok")]]

event, values = sg.Window("", popup_layout, element_justification='c').read(close=True)

while 1:
    event, values = window.read()
    
    if event == sg.WINDOW_CLOSED:
        break

window.close()