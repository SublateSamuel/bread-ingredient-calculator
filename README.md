# Bread Ingredient Calculator

The **Bread Ingredient Calculator** is a command-line tool that helps you calculate ingredient quantities for various types of bread recipes. Whether you're baking classic bread, hamburger buns, or any other bread variation, this tool simplifies the process by providing accurate measurements for each ingredient.

## Getting Started

These instructions will guide you through setting up the **Bread Ingredient Calculator** project on your local machine.

### Prerequisites

Before you begin, ensure you have the following prerequisites installed on your system:

- [Python](https://www.python.org/downloads/)
- [Poetry](https://python-poetry.org/docs/#installation)
- [Typer](https://typer.tiangolo.com/tutorial/first-steps/)
- [Rich](https://rich.readthedocs.io/en/stable/introduction.html)

### Installation

1. Clone this repository to your local machine using your preferred method (HTTPS or SSH).

   ```shell
   git clone https://github.com/SublateSamuel/bread-ingredient-calculator.git
   ```

2. Navigate to the project directory.

   ```shell
   cd bread-ingredient-calculator
   ```

3. Install the required dependencies using Poetry.

   ```shell
   poetry install
   ```

Now, the project is set up and ready to use.

## Usage

The **Bread Ingredient Calculator** provides a user-friendly command-line interface (CLI) to calculate ingredient quantities for your bread recipes. Follow the usage instructions below.

### Calculate Ingredient Quantities

To calculate ingredient quantities for a specific bread recipe, use the `calculate` command with the following options:

- `recipe_type` (required): The type of recipe you want to calculate ingredients for. Available options include:

  - `bread`: Classic bread recipe.
  - `hamburger`: Hamburger buns recipe (add your own).

- `flour` (required): The quantity of flour in grams.
- `liquid` (required): The type of liquid (water or milk).

#### Examples

Calculate ingredient quantities for classic bread:

```shell
poetry run python calculator/main.py calculate bread --flour 300 --liquid water
```

Calculate ingredient quantities for hamburger buns:

```shell
poetry run python calculator/main.py calculate hamburger --flour 300 --liquid milk
```

### Available Recipes

Here is a list of available recipes you can use with the `recipe_type` option:

- `bread`: Classic bread recipe.
- `hamburger`: Hamburger buns recipe (add your own).

## Contributing

Contributions to the project are welcome! If you have ideas for improvements or new features, feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

We want to express our gratitude to [Typer](https://typer.tiangolo.com/) for providing an excellent library for creating command-line interfaces in Python.

Happy baking! 🍞🥖
