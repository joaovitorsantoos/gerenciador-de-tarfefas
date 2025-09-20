# Importa a biblioteca 'Time' para melhor visualização das respostas.
import time

# Função para adicionar tarefas dentro da lista.
def add_task():
    add = input('\nWrite your task to add to the list:  ')
    tasks.append(add)
    time.sleep(3)

# Função para remover tarfefas ja existentes dentro da lista.
def remove_task():
    show_tasks()

    num_task = int(input('What task do you want to remove: \n'))
    
    if num_task.isdigit():
        num_int = int(num_task)
        if 1 <= num_int <= len(tasks):
            remove = tasks.pop(num_int - 1)
            time.sleep(3)
        else:
            print('Invalid number, try again...')
        time.sleep(3)

# Função para mostrar tarefas ja inseridas na lista.
def show_tasks():
    if tasks == []:
        print('''\nYou don't have tasks in yout list...''')
        time.sleep(3)
    else:
        for i, task in enumerate(tasks):
            print(f'\n{i+1}. {task}')
    time.sleep(3)
    
# Inicia o programa com a lista vazia.
tasks = []

# Loop para manter o pragrama ativo.
while True:
    print(f"""
|   ----- Welcome to Task Manager! -----
|
|   1 - Add Task.
|   2 - Show Tasks.
|   3 - Remove Task.
|   4 - Leave.
""")
    # Seleção da ferramenta que o usuario deseja utilizar.
    n = input('Select what you gonna do (1-4): ')

    # Verifica se o Input do usuario é um número.
    if n.isdigit():
        n_int = int(n)

        if n_int == 1:
            add_task()
        elif n_int == 2:
            show_tasks()
        elif n_int == 3:
            remove_task()
        elif n_int == 4:
            print('\nClosing...')
            break
        else:
            print('Invalid input...')
    else:
        print('Invalid input, try again...')