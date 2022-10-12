import PySimpleGUI as sg

layout = [[sg.T("Total de registros existentes:")],
          [sg.T("1- Socios:"), sg.T("0", key='-SOCIOS-')],
          [sg.T("2- Planos:"), sg.T("0", key='-PLANOS-')],
          [sg.T("3- Mensalidades:"), sg.T("0", key='-MENSALIDADES-')]]
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