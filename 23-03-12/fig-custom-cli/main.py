import click
from click_complete_fig import fig


@click.group()
def main():
    click.echo('Hello World!')
    
fig.add_completion_spec_command(main)
    