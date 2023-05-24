import psycopg2

'''
PART 1

In this exercise we will use PostgreSQL and Python.

    1. Create a new database and a new table in pgAdmin (or in psql). The table is named Menu_Items and contains the columns
            item_id : SERIAL PRIMARY KEY
            item_name : VARCHAR(30) NOT NULL
            item_price : SMALLINT DEFAULT 0

    2. In the file menu_item.py, create a new class called MenuItem, the attributes should be the name and price of each item.

    3. Create several methods (save, delete, update) these methods will allow a user to save, delete and update items from the Menu_Items table. The update method can update the name as well as the price of an item.

    4. In the file menu_manager.py, create a new class called MenuManager
            Create a Class Method called get_by_name that will return a single item from the Menu_Items table depending on it’s name, if an object is not found (there is no item matching the name in the get_by_name method) return None.
    
            Create a Class Method called all_items which will return a list of all the items from the Menu_Items table.
'''


def create_connection():
    return psycopg2.connect(
        database='exercises', user='ally', password='yourpassword', host='localhost', port="5432"
        # needs to put personal password
    )


class MenuItem:
    @classmethod
    def execute_query(cls, query, values=None):
        with create_connection() as connection:
            with connection.cursor() as cursor:
                cursor.execute(query, values)
                connection.commit()

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def save(self):
        query = "INSERT INTO Menu_Items (item_name, item_price) VALUES (%s, %s)"
        values = (self.name, self.price)
        self.execute_query(query, values)

    def delete(self):
        query = "DELETE FROM Menu_Items WHERE item_name = %s"
        value = (self.name,)
        self.execute_query(query, value)

    def update(self, new_name, new_price):
        query = "UPDATE Menu_Items SET item_name = %s, item_price = %s WHERE item_name = %s"
        values = (new_name, new_price, self.name)
        self.execute_query(query, values)

    def __str__(self):
        return f"{self.name} - ${self.price}"


class MenuManager:
    @classmethod
    def execute_query(cls, query, values=None):
        with create_connection() as connection:
            with connection.cursor() as cursor:
                cursor.execute(query, values)
                return cursor.fetchall()

    @classmethod
    def get_by_name(cls, name):
        query = "SELECT * FROM Menu_Items WHERE item_name = %s"
        value = (name,)
        result = cls.execute_query(query, value)

        if result:
            item = result[0]
            return MenuItem(item[1], item[2])
        else:
            return None

    @classmethod
    def all_items(cls):
        query = "SELECT * FROM Menu_Items"
        results = cls.execute_query(query)

        menu_items = []
        for item in results:
            menu_items.append(f"{item[1]} - ${item[2]}")

        return menu_items


if __name__ == "__main__":
    item = MenuItem('Burger', 35)
    # item.save()
    # # item.delete()
    # item.update('Veggie Burger', 37)
    item2 = MenuManager.get_by_name('Burger')
    print(item2)
    items = MenuManager.all_items()
    print(items)
