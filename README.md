# auto_arsenal
Automação com pyautogui para lidar com obtenção de relatórios em sistema legado

# Automatização de Pedidos de Dietas
Script para automação de data scraping, leitura dos dados com pandas e interpretação dos mesmos a partir de sistema legado.
Obs.: Atualmente, somente a obtenção de relatórios está totalmente automatizada.

# Introdução
A obtenção dos dados neste sistema exigem o trabalho manual. A automação com pyautogui é uma forma simples de executar tarefas repetitivas num dado sistema, contanto que ele não sofra atualizações.

# Bibliotecas necessárias
Pyautogui

# Desafio
Este sistema é próprio ao hospital em que trabalhei e não permite uma interação muito eficaz através do Python, isto é, a linguagem não consegue interagir diretamente com o sistema. Para obtenção de relatórios de pedidos de arsenal, é necessário fazer uma configuração dia por dia e a emissão de um arquivo de cada vez. Isso dificulta não só o acesso à informação como qualquer possibilidade eficiente de resumir a informação e pensar em um controle de estoque eficaz, a partir de uma análise dos dados.

# Solução
O pyautogui permite simular a interação do usuário com o sistema a partir de comandos padronizados. O sistema está dotado de vários atalhos, facilitando a interação para não depender da posição de elementos a serem clicados pelo mouse. Se esse fosse o caso, seria necessário uma responsividade do pyautogui que não seria simples. Como os comandos são pelo teclado, é simples interagir com o sistema e chegar até a tela de interesse. O único complicador restante, nesse caso, é a velocidade de processamento do computador, que pode demorar a emitir relatórios e o pyautogui poderia solicitar comandos antes da hora adequada. A solução é o uso da biblioteca time para forçar o python a esperar antes de continuar a execução do script.

# Conclusão
Este sistema simples permite o acesso a ampla quantidade de informações para consulta e, melhor do que isso, para análise dos dados. Isso permite planejar melhor o futuro dos pedidos de arsenal, otimizando gastos de acordo com a necessidade real.
