-- task1 Для каждого product_id выведите inventory_id, а также предыдущий и последующей inventory_id по убыванию quantity
use northwind;
select product_id, inventory_id, quantity, lag(inventory_id) over (partition by product_id order by quantity desc) as previous_inventory_id,
	   lead(inventory_id) over (partition by product_id order by quantity desc) as next_inventory_id
from order_details;

-- task2 Выведите максимальный и минимальный unit_price для каждого order_id с помощью функции FIRST VALUE.  Вывести order_id и полученные значения
select order_id, round(unit_price, 2) as unit_price, first_value(round(unit_price, 2)) over (partition by order_id order by unit_price asc) as min_unit_price,
													 first_value(round(unit_price, 2)) over (partition by order_id order by unit_price desc) as max_unit_price
from order_details;

-- task3 Выведите order_id и столбец с разницей между  unit_price для каждого заказа и минимальным unit_price в рамках одного заказа. Задачу решить двумя способами - с помощью First VAlue и MIN
select order_id, round(unit_price, 2) as unit_price, min(round(unit_price, 2)) over (partition by order_id) as min_unit_price,
							 first_value(round(unit_price, 2)) over (partition by order_id order by unit_price asc) as first_min_unit_price
from order_details;

-- task4 Присвойте ранг каждой строке используя RANK по убыванию quantity
select *, rank() over (order by quantity desc) as rank_unit_price
from order_details;

-- task5  Из предыдущего запроса выберите только строки с рангом до 10 включительно
select *
from (select *, rank() over (order by quantity desc) as rank_unit_price
from order_details) as t1
where rank_unit_price < 11; 