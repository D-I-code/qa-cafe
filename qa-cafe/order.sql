CREATE TABLE orders (
  order_id int(100) AUTO_INCREMENT PRIMARY KEY not null,
  name varchar(50) not null,
  extras varchar(10) not null,
  price float(20) not null
);

INSERT INTO orders (name, extras, price)
VALUES ('Latte', 'whipped cream', 4.20);

