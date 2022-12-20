CREATE TABLE orders (
  order_id int(100) AUTO_INCREMENT PRIMARY KEY not null,
  customer_name varchar(50) not null,
  drink varchar(50) not null,
  drink_size varchar(50) not null,
  extras varchar(10) not null,
  price float(20) not null
);

INSERT INTO orders (customer_name, drink, drink_size, extras, price)
VALUES ('Jeff', 'Latte', 'large', 'whipped cream', 4.20);

