from tabulate import tabulate

def print_menu(title, list_options):
    list_options.append(list_options.pop(0))
    print(f"{title}:")
    for index in range(len(list_options)):
        print(f"({index + 1}) {list_options[index]}" if index != len(list_options) - 1
              else f"(0) {list_options[index]}")


def print_message(message):
    print('\033[92m' '\033[0m')
    print(message)


def print_general_results(result, label):
    """Prints out any type of non-tabular data.
    It should print numbers (like "@label: @value", floats with 2 digits after the decimal),
    lists/tuples (like "@label: \n  @item1; @item2"), and dictionaries
    (like "@label \n  @key1: @value1; @key2: @value2")
    """
    pass


# /--------------------------------\
# |   id   |   product  |   type   |
# |--------|------------|----------|
# |   0    |  Bazooka   | portable |
# |--------|------------|----------|
# |   1    | Sidewinder | missile  |
# \-----------------------------------/
def print_table(table):
    print('\33[32m'  '\33[32m')
    print(tabulate(table, tablefmt="grid" ))
    print('\33[32m' '\33[0m')
   
    
    


def get_input(label):
    """Gets single string input from the user.

    Args:
        label: str - the label before the user prompt
    """
    return input(f"{label}: ")


def get_inputs(labels):
    """Gets a list of string inputs from the user.

    Args:
        labels: list - the list of the labels to be displayed before each prompt
    """
    answers = []
    for label in labels:
        validate = False
        while not validate:
            answer = get_input(label)
            if label == "Customer" and len(answer) != 8:
                print_error_message("Customer ID has to be 8 chars long.")
                continue
            elif label == "Price":
                try:
                    float(answer)
                except ValueError:
                    print_error_message("Price needs to be a number. Floating number has to be separated by a dot.")
                    continue
            elif label == "Date":
                date_split = answer.split("-")
                if len(date_split) != 3 or not date_split[0].isnumeric() or int(date_split[0]) < 0 \
                        or not date_split[1].isnumeric() or not date_split[2].isnumeric() \
                        or int(date_split[1]) not in range(1, 13) \
                        or int(date_split[2]) not in range(1, 32):
                    print_error_message("Wrong date provided. Has to be in format YYYY-MM-DD")
                    continue
            answers.append(answer)
            validate = True
    return answers


def print_error_message(message):
    """Prints an error message to the terminal.

    Args:
        message: str - the error message
    """
    print(f"ERROR OCCURED:\n{message}")
