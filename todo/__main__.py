import click
from todo.commands import *

@click.group(name='todo')
@click.version_option('0.1.0', prog_name='todo')
def todo():
  pass

todo.add_command(add_todo)
todo.add_command(remove_todo)
todo.add_command(complete_todo)
todo.add_command(list_todos)

if __name__ == '__main__':
  todo()