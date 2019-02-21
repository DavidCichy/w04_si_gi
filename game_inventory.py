# This is the file where you must work.
# Write code in the functions (and create new functions) so that they work
# according to the specification.


def display_inventory(inventory):
    '''Display the inventory like this:
    rope: 1
    torch: 6

      '''
    total_items_count = 0
    for key, value in inventory.items():
      print("{}: {}".format(key, value))
      total_items_count += value
      # print("Total number of items: {}".format(total_items_count))


def add_to_inventory(inventory, added_items):
    '''Add to the inventory dictionary a list of items from added_items.'''

    for item in added_items:
      if item in inventory:
        inventory[item] += 1
      else:
        inventory[item] = 1

    return inventory


def print_dashes(number):
    print("{}".format("-" * number))


def print_item_in_line(lenght_of_1st_row, value1, lenght_of_2st_row, value2):
    spaces1 = lenght_of_1st_row - len(str(value1))
    spaces2 = lenght_of_2st_row - len(str(value2))
    print("{}{} | {}{}".format(" " * spaces1, value1, " " * spaces2, value2))


def print_table(inventory, order=None):
    '''
    Take your inventory and display it in a well-organized table with
    each column right-justified like this:

    -----------------
    item name | count
    -----------------
         rope |     1
        torch |     6
    -----------------

    The 'order' parameter (string) works as follows:
    - None (by default) means the table is unordered
    - "count,desc" means the table is ordered by count (of items in the
      inventory) in descending order
    - "count,asc" means the table is ordered by count in ascending order
    '''
    name_header = "item name"
    value_header = "count"

    longest_item_name_lenght = len(name_header)
    longest_item_value_lenght = len(value_header)

    for key, value in inventory.items():
      if len(key) > longest_item_name_lenght:
        longest_item_name_lenght = len(key)
      if len(str(value)) > longest_item_value_lenght:
        longest_item_value_lenght = len(str(value))

    total_width_of_table = longest_item_name_lenght + longest_item_value_lenght + 3

    print_dashes(total_width_of_table)
    print_item_in_line(longest_item_name_lenght, name_header, longest_item_value_lenght, value_header)
    print_dashes(total_width_of_table)

    if order == "count,asc":
      for key, value in sorted(inventory.items(), key=lambda kv: kv[1]):
       print_item_in_line(longest_item_name_lenght, key, longest_item_value_lenght, value)

    elif order == "count,desc":
      for key, value in sorted(inventory.items(), key=lambda kv: kv[1], reverse=True):
       print_item_in_line(longest_item_name_lenght, key, longest_item_value_lenght, value)

    else:
      for key, value in inventory.items():
       print_item_in_line(longest_item_name_lenght, key, longest_item_value_lenght, value)

    print_dashes(total_width_of_table)


def import_inventory(inventory, filename="import_inventory.csv"):
    '''
    Import new inventory items from a file.

    The filename comes as an argument, but by default it's
    "import_inventory.csv". The import automatically merges items by name.

    The file format is plain text with comma separated values (CSV).
    '''
    try:
      with open(filename, 'r') as import_file:
        added_items_list = []
        for line in import_file:
          added_items_line = line.split(",")
          for item in added_items_line:
            added_items_list.append(item)

      inventory = add_to_inventory(inventory, added_items_list)

    except:
      print("File 'no_such_file.csv' not found!")

    return inventory


def export_inventory(inventory, filename="export_inventory.csv"):
    '''
    Export the inventory into a .csv file.

    If the filename argument is None, it creates and overwrites a file
    called "export_inventory.csv".

    The file format is plain text with comma separated values (CSV).
    '''

    pass

inv = {'rope': 1, 'torch': 999999999, 'Dragon Blade Of Awesomeness': 3}
print_table(inv, "count,asc")
inv = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
print_table(inv, "count,asc")
dragon_loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = add_to_inventory(inv, dragon_loot)
display_inventory(inv)
import_inventory(inv, "test_inventory.csv")
print_table(inv, "count,desc")
inv = {'rope': 1, 'torch': 6}
inv = import_inventory(inv, 'test_inventory_export.csv')
print_table(inv)
