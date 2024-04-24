import click
from todo.api import Api

PRIORITIES = {
  'o': 'Optional',
  'l': 'Low',
  'm': 'Medium',
  'h': 'High',
  'c': 'Critical'
}

@click.command(name='add', help='Add a todo')
@click.option('-t', '--title', required=True, prompt='To-do title', help='The title of the to-do')
@click.option('-d', '--description', required=True, prompt='Description', help='The description of the task')
@click.option('-p', '--priority', required=True, prompt='Priority', type=click.Choice(PRIORITIES.keys()), default='m')
def add_todo(title, description, priority):
  todo = [title, description, priority]
  api = Api()
  res = api.save_todo(todo)

  if res['status'] != 200:
    return click.secho('Task could not be saved!', fg='red')

  click.secho(f'| {res["data"][1]} | task was saved successfuly', fg='green')

@click.command(name='rm', help='Delete a todo based on its ID')
@click.option('-i', '--id', required=True, prompt='To-do id', help='The id of the to-do')
def remove_todo(id):
  api = Api()
  res = api.del_todo(id)

  if res['status'] != 200:
    return click.secho('Task could not be deleted!', fg='red')

  click.secho(f'| {res["data"][1]} | task was saved successfuly', fg='green')

@click.command(name='complete', help='Mark a todo complete based on its ID')
@click.option('-i', '--id', required=True, prompt='To-do id', help='The id of the to-do')
def complete_todo(id):
  api = Api()
  res = api.mark_complete(id)

  if res['status'] != 200:
    return click.secho('Task could not be completed!', fg='red')

  click.secho(f'| {res["data"][1]} | task was marked completed', fg='green')

@click.command(name='list', help='Show all todos without filter. Completed todos will be highlighted green.')
@click.option('--all', is_flag=True, help='show all todos')
@click.option('-p', '--priority', default='m', help='priority to filter by')
def list_todos(all, priority):
  api = Api()
  res = {}
  if all:
    res = api.get_todos('')
  else:
    res = api.get_todos(priority)


  if res['status'] != 200:
    return click.secho('Todos could not be listed!', fg='red')
  
  if len(res["data"]) < 1:
    return click.secho(f'There are no Todos with {PRIORITIES[priority]} priority!', fg='red')

  for item in res["data"]:
    color = 'red'

    if item[4] == '1':
      color = 'green'

    click.secho(item, fg=color)