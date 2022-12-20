import sqlite3 as sqlite

connection = sqlite.connect("orders.db")

cursor = connection.cursor()

table_keys = "(customer_name, drink, drink_size, extras, price)"

sql_file = open("order.sql")
sql_string = sql_file.read()
cursor.executescript(sql_string)

def run_query(query):
    data = cursor.execute(query)
    return data


def add_order(customer_name, drink, drink_size, extras, price):
    query = f"INSERT INTO orders {table_keys} VALUES('{customer_name}', '{drink}', '{drink_size}', '{extras}', {price});"
    run_query(query)
    return True


def get_order(order_id):
    query = f"SELECT * FROM orders WHERE order_id = {order_id});"
    run_query(query)
    return True


def get_all_orders():
    query = f"SELECT * FROM orders"
    result = run_query(query).fetchall()
    print(f"orders: {result}")
    return True


def del_order(order_id):
    query = f"DELETE FROM orders WHERE order_id = {order_id}"
    run_query(query)
    return True


def del_all_orders():
    query = f"DELETE FROM orders"
    run_query(query)
    return True


def update_order_by_id(order_id, price):
    query = f"UPDATE orders SET price = {price} WHERE order_id = {order_id}"
    return run_query(query).fetchall()


