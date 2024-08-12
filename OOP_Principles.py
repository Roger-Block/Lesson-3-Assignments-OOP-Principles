                    #================================================================
                    #========= Lesson 3: Assignments: OOP Principles ===============
                    #================================================================

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ 1. Encapsulation in Personal Budget Management ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Objective:
    # The aim of this assignment is to reinforce the understanding of encapsulation in Python, focusing on the use of private attributes and getters and setters. Students will apply these concepts to create a Personal Budget Management system.

# Problem Statement: 
    # You are required to build a Personal Budget Management application. The application will manage budget categories like food, entertainment, utilities, etc., ensuring that budget details remain private and are accessed or modified through public methods.

# Task 1: 
    # Define Budget Category Class
        # Create a class BudgetCategory with private attributes for category name and allocated budget.
        # Initialize these attributes in the constructor.
        # Expected Outcome: A BudgetCategory class capable of storing category details securely.


# Task 2: 
    # Implement Getters and Setters
        # Write getter and setter methods for both the category name and the allocated budget.
        # Ensure that the setter methods include validation (e.g., budget should be a positive number).
        # Expected Outcome: Methods that allow controlled access and modification of the private attributes, with validation checks in place.

# Task 3: 
    # Add Budget Functionality
        # Implement a method to add expenses to a category and adjust the budget accordingly.
        # Validate the expense amount before making deductions from the budget.
        # Expected Outcome: Ability to track expenses per category and update the remaining budget safely.

# Task 4: Display Budget Details
    # Create a method to display the details of a budget category, including the name, allocated budget, and remaining budget after expenses.
    # Expected Outcome: Users can view a summary of each budget category, showcasing encapsulation in action.
    # Code Examples:
        # class BudgetCategory:
        #     # Constructor and private attributes
        #     # ...

        #     # Getters and setters for category name and budget
        #     # ...

        #     def add_expense(self, amount):
        #         # Method to add an expense to the category
        #         # ...

        #     def display_category_summary(self):
        #         # Method to display the budget category details
        #         # ...

    # # Example usage
    # food_category = BudgetCategory("Food", 500)
    # food_category.add_expense(100)
    # food_category.display_category_summary()

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ 2. E-commerce Product Catalog System ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Objective:
    # The goal of this assignment is to demonstrate a deep understanding of inheritance and method overriding in Python. Students will apply these concepts to develop an E-commerce Product Catalog System that handles various types of products with both common and unique attributes.

# Problem Statement:
    # An e-commerce platform requires a system to manage different types of products, such as books, electronics, and clothing. Each product type shares some common characteristics but also has unique features. The system should be able to display information about each product appropriately.

# Task 1:
    # Create Base Product Class
    # Develop a base class Product with common attributes like product ID, name, price, and a method to display product information.
        # Expected Outcome: A Product class that can hold general information about a product and display it.

# Task 2: 
    # Implement Subclasses for Specific Products
            # (ONLY BOOK SUBCLASS REQUIRED)
        # Create subclasses Book, Electronic, and Clothing that inherit from Product.
        # Each subclass should have additional attributes relevant to its category (e.g., author for books, specs for electronics, size for clothing).
        # Expected Outcome: Each subclass contains both inherited attributes from Product and new attributes specific to the product type.

# Task 3: 
    # Override Display Method in Subclasses
        # Override the method to display product information in each subclass to include specific attributes.
        # For example, the Book class should display the author, Electronic should display specs, etc.
        # Expected Outcome: Calling the display method on an instance of any subclass shows both common and specific product details.

# Task 4:
    # Test Product Catalog Functionality
        # Instantiate objects of each subclass and call their display methods to ensure correct information is shown.
        # Expected Outcome: The system should accurately display detailed information for each type of product, demonstrating inheritance and method overriding.
        # Code Examples:
                # class Product:
                #     # Constructor and common attributes
                #     # ...

                #     def display_info(self):
                #         # General method to display product info
                #         # ...

                # class Book(Product):
                #     def __init__(self, product_id, name, price, author):
                #         super().__init__(product_id, name, price)
                #         self.author = author

                #     def display_info(self):
                #         # Overridden method for books
                #         # ...

                # # Example usage
                # my_book = Book("123", "Python Essentials", 29.99, "J. Doe")
                # my_book.display_info()

#================================================================================================
#=====================================Begin Code=================================================
#================================================================================================
print("\n"*10,"="*100)
class BudgetCategory:
    def __init__(self, category_name, allocated_budget):
        self.__category_name = category_name
        self.__allocated_budget = allocated_budget
        self.__remaining_budget = allocated_budget

    def get_category_name(self):
        return self.__category_name

    def set_category_name(self, new_category_name):
        self.__category_name = new_category_name

    def get_allocated_budget(self):
        return self.__allocated_budget

    def set_allocated_budget(self, new_allocated_budget):
        if new_allocated_budget >= 0:
            self.__allocated_budget = new_allocated_budget
            self.__remaining_budget = new_allocated_budget
        else:
            print("Invalid allocated budget. Please enter a positive number.")

    def add_expense(self, amount):
        if amount >= 0:
            if self.__remaining_budget >= amount:
                self.__remaining_budget -= amount
                print("Expense added successfully.")
            else:
               print("Invalid expense amount. Please enter a positive number.")

    def display_category_summary(self):
        print("Category:", self.__category_name)
        print("Allocated Budget:", self.__allocated_budget)
        print("Remaining Budget:", self.__remaining_budget)

food_category = BudgetCategory("Food", 500)
food_category.add_expense(100)
food_category.display_category_summary()

print("="*100)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ 2. E-commerce Product Catalog System ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

class Product:
    def __init__(self, product_id, name, price):
        self.product_id = product_id
        self.name = name
        self.price = price

    def display_info(self):
        print("Product ID:", self.product_id)
        print("Name:", self.name)
        print("Price:", self.price)


class Book(Product):
    def __init__(self, product_id, name, price, author):
        super().__init__(product_id, name, price)
        self.author = author

    def display_info(self):
        super().display_info()
        print("Author:", self.author)


# Example usage
my_book = Book("123", "Python Essentials", 29.99, "J. Doe")
my_book.display_info()

print("="*100)

#================================================================================================
#=================================== End of Code=================================================
#================================================================================================


# Author: Roger Block