import pyautogui
import dados
import time
from datetime import date, timedelta

def open_desktop():
    """Vai para a área de trabalho"""
    with pyautogui.hold('win'):
        pyautogui.press('d')

def open_pagu():
    """Acessa o arquivo de nome 'pagu'"""
    pyautogui.press('p')
    pyautogui.press('a')
    pyautogui.press('g')
    pyautogui.press('Enter')

def login_pagu():
    """Faz login no sistema"""
    pyautogui.write(dados.login)
    pyautogui.press('tab')
    pyautogui.write(dados.senha)
    pyautogui.press('Enter')

def close_patient_windows():
    """Fecha a pop-up com detalhes de pacientes"""
    with pyautogui.hold('alt'):
        pyautogui.press('2')

def open_report_arsenal():
    """Abre a janela com relatórios de arsenal"""
    pyautogui.press('alt')
    pyautogui.press('e')
    pyautogui.press('e')
    pyautogui.press('enter')
    pyautogui.press('o')
    pyautogui.press('c')
    pyautogui.press('c')
    pyautogui.press('c')
    pyautogui.press('c')
    pyautogui.press('enter')

def set_printing_type():
    """Muda a emissão de relatório de impressão para arquivo"""
    with pyautogui.hold('shift'):
    # Mudar p/ gerar arquivo e não imprimir
        pyautogui.press('tab')
        pyautogui.press('tab')
        pyautogui.press('tab')
        pyautogui.press('tab')
    pyautogui.press('down')
    pyautogui.press('down')
    pyautogui.press('down')
    pyautogui.press('enter')
    # Chega na posição do botão 'Imprimir', que será nossa posição padrão para futuras
    # gerações de relatórios
    with pyautogui.hold('shift'):
        pyautogui.press('tab')
    
def go_to_first_relevant_field(first_execution):
    """Acessa primeiro campo relevante, que é o nome do arquivo
    e que servirá de referência para acessar os próximos campos"""
    # Se for a primeira execução, há um campo a mais disponível
    if first_execution:
        iterations = 18
    else:
        iterations = 17
    with pyautogui.hold('shift'):
        for i in range(iterations):
            pyautogui.press('tab')

def set_file_path(file_name, file_path):
    """Muda o diretório e nome do arquivo a ser salvo"""
    pyautogui.write(f'{file_path}{file_name}')

def go_set_almoxarifado():
    """Define o código do almoxarifado (sempre 1)"""
    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.write('1')

def go_set_setor(setor):
    """Define o código do setor"""
    pyautogui.press('tab')
    pyautogui.write(setor)

def go_set_data(date):
    """Define a data de pesquisa do relatório; queremos o relatório de um dia específico,
    portanto a data de início e de fim são as mesmas"""
    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.write(date.strftime('%d/%m/%Y'))
    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.write(date.strftime('%d/%m/%Y'))

def go_generate_report():
    """Aperta o botão de geração do relatório"""
    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.press('enter')

def daterange(start_date: date, end_date: date):
    """Gerador que retorna data por data desde uma inicial até uma final"""
    days = int((end_date - start_date).days) + 1
    for n in range(days):
        yield start_date + timedelta(n)

def generate_report(first_date, last_date, setor, file_path):
    """Gera relatório a relatório, dia por dia, de uma data inicial até
    uma data final, dado um determinado código de setor"""
    first_execution = True
    open_desktop()
    open_pagu()
    time.sleep(5)
    login_pagu()
    time.sleep(7)
    close_patient_windows()
    open_report_arsenal()
    time.sleep(3)
    set_printing_type()
    
    for single_date in daterange(first_date, last_date):
        file_name = single_date.strftime('%Y-%m-%d')
        go_to_first_relevant_field(first_execution)
        set_file_path(file_name, file_path)
        go_set_almoxarifado()
        go_set_setor(setor)
        go_set_data(single_date)
        go_generate_report()
        first_execution = False
        time.sleep(5)

first_date = date(2024, 4, 21)
last_date = date(2024, 11, 13)
file_path = r"C:/Users/med-pediatria/Desktop/relatorios_arsenal/"
generate_report(first_date, last_date, 10, file_path)