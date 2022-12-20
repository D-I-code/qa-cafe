import sqlite3 as sqlite

connection = sqlite.connect("order.sql")

cursor = connection.cursor()

table_keys = "(customer_name, drink, drink_size, extras, price)"


def runQuery(query):
    data = cursor.execute(query)
    return data


def addOrder(customer_name, drink, drink_size, extras, price):
    query = f"INSERT INTO orders {table_keys} VALUES ({customer_name}, {drink}, {drink_size}, {extras}, {price});"
    runQuery(query)
    return True


def getOrder(order_id):
    query = f"SELECT * FROM orders WHERE order_id = {order_id});"
    runQuery(query)
    return True


def getAllOrders():
    query = f"SELECT * FROM orders"
    runQuery(query)
    return True


def delOrder(order_id):
    query = f"DELETE FROM orders WHERE order_id = {order_id}"
    runQuery(query)
    return True


def delAllOrders():
    query = f"DELETE FROM orders"
    runQuery(query)
    return True


def updateOrderById(order_id, price):
    query = f"UPDATE orders SET price = {price} WHERE order_id = {order_id}"
    return runQuery(query).fetchall()







