-- task 1 Вывести названия продуктов таблица products, включая количество заказанных единиц quantity для каждого продукта таблица order_details.
-- Решить задачу с помощью cte и подзапроса
select *
from northwind.products;

select *
from northwind.order_details;

-- cte, признаюсь поспотрел как сделать у аишки ибо недопонял что надо использовать join

with t1 as (
    select 
        product_id,
        quantity
    from northwind.order_details
)
select 
    p.product_name,
    t1.quantity
from northwind.products p
join t1 
    on p.id = t1.product_id;

-- podzapros, вот тут не понял, прошу обьяснить на уроке
select product_name
from products 
where id in 
(select product_id
from order_details);

-- task 2 Найти все заказы таблица orders, сделанные после даты самого первого заказа клиента Lee таблица customers.

use northwind;

select *
from orders;

select *
from customers;

select *
from orders
where order_date > (
    select min(o.order_date)
    from orders o
    join customers c 
	on o.customer_id = c.id
    where c.last_name = 'Lee');
    
-- task 3 Найти все продукты таблицы  products c максимальным target_level
    
select *
from northwind.products
where target_level = (
    select max(target_level)
    from northwind.products);
