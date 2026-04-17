"""
this program defines a dish class to store dish details
it also defines a cookbook class to manage multiple dishes
user can add dishes and display all stored dishes
"""

class Dish:
    """
    class to represent a single dish
    """
    def __init__(self, dish_id, dish_name, ingredients, instructions):
        """
        initialize dish attributes
        """
        self.dish_id = dish_id
        self.dish_name = dish_name
        self.ingredients = ingredients
        self.instructions = instructions

    def show_dish(self):
        """
        display dish details
        """
        print("\ndish details")
        print("-" * 30)
        print(f"dish id: {self.dish_id}")
        print(f"dish name: {self.dish_name}")
        print(f"ingredients: {self.ingredients}")
        print(f"instructions: {self.instructions}")


class Cookbook:
    """
    class to manage collection of dishes
    """
    def __init__(self):
        """
        initialize empty dish list
        """
        self.dish_list = []

    def insert_dish(self, dish_data):
        """
        add a dish to cookbook
        """
        self.dish_list.append(dish_data)

    def show_all(self):
        """
        display all dishes in cookbook
        """
        if not self.dish_list:
            print("no dishes available")
            return

        print("\nall dishes in cookbook")
        print("=" * 40)

        for dish_data in self.dish_list:
            dish_data.show_dish()


# create cookbook object
cookbook_data = Cookbook()

# loop to take multiple dishes
while True:
    user_choice = input("\nadd dish or type exit: ")

    if user_choice.lower() == "exit":
        break

    # take dish input
    id_input = input("enter dish id: ")
    name_input = input("enter dish name: ")
    ingredient_input = input("enter ingredients: ")
    instruction_input = input("enter instructions: ")

    # create dish object
    dish_data = Dish(id_input, name_input, ingredient_input, instruction_input)

    # add to cookbook
    cookbook_data.insert_dish(dish_data)

# display all dishes
cookbook_data.show_all()