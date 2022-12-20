CREATE TABLE IF NOT EXISTS orders (
  order_id INTEGER PRIMARY KEY AUTOINCREMENT,
  customer_name varchar(50) not null,
  drink varchar(50) not null,
  drink_size varchar(50) not null,
  extras varchar(10) not null,
  price float(20) not null
);


