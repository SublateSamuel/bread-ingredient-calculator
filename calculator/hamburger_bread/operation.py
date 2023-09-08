import typer
from rich.console import Console
from rich.table import Table
from rich import box

from hamburger_bread.ingredient_factor import IngredientFactor


console = Console()

def validate_liquid_type(liquid):
    if not liquid.lower() in ('milk', 'water'):
        console.print("[bold red]Invalid liquid type.[/bold red] Please choose 'water' or 'milk'.")
        raise typer.Exit(1)

def calculate_ingredient_quantities(flour, liquid):
    liquid_factor = IngredientFactor.MILK.value
    liquid_quantity = flour * liquid_factor
    dry_yeast = flour * IngredientFactor.DRY_YEAST.value
    sugar = flour * IngredientFactor.SUGAR.value
    salt = flour * IngredientFactor.SALT.value
    butter = flour * IngredientFactor.BUTTER.value
    egg = IngredientFactor.EGG.value

    return {
        "Flour": flour,
        liquid.title(): liquid_quantity,
        "Yeast": dry_yeast,
        "Sugar": sugar,
        "Salt": salt,
        "Butter": butter,
        "Egg": egg,
    }

def create_ingredient_table(ingredient_quantities):
    table = Table(
        title="Ingredient Quantities",
        box=box.ROUNDED,
        show_edge=True,
    )
    table.add_column("Ingredient", style="cyan")
    table.add_column("Quantity", style="magenta")

    emoji_dict = {
        "Flour": "🌾",
        "Water": "💧",
        "Milk": "🥛",
        "Yeast": "🍞",
        "Sugar": "🍬",
        "Salt": "🧂",
        "Butter": "🧈",
        "Egg": "🥚",
    }

    for ingredient, quantity in ingredient_quantities.items():
        emoji = emoji_dict.get(ingredient, "")
        table.add_row(
            f"[bold]{emoji} {ingredient}[/bold]",
            f"{quantity:.2f} ml" if "Milk" in ingredient else f"{quantity:.2f}g",
        )

    return table

def calculate(flour, liquid):
    validate_liquid_type(liquid)
    ingredient_quantities = calculate_ingredient_quantities(flour, liquid)
    table = create_ingredient_table(ingredient_quantities)
    console.print(table)