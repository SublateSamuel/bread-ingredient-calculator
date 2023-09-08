import typer

from normal_bread.operation import calculate as normal_bread
from hamburger_bread.operation import calculate as hamburger_bread


app = typer.Typer()

@app.command()
def bread(
    flour: float = typer.Option(..., "--flour", "-f", help="The quantity of flour in grams."),
    liquid: str = typer.Option(..., "--liquid", "-l", help="The type of liquid (water or milk). Accepted values: 'water' or 'milk'."),
):
    """
    Calculate ingredient quantities for a baker's recipe.
    """
    normal_bread(flour, liquid)


@app.command()
def hamburger(
    flour: float = typer.Option(..., "--flour", "-f", help="The quantity of flour in grams."),
    liquid: str = typer.Option(..., "--liquid", "-l", help="The type of liquid (water or milk). Accepted values: 'water' or 'milk'."),
):
    """
    Calculate ingredient quantities for a baker's recipe.
    """
    hamburger_bread(flour, liquid)
    
if __name__ == "__main__":
    app()
