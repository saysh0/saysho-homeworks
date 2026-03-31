use northwind;

-- 1 Посчитайте основные статистики - среднее, сумму, минимум, максимум столбца unit_cost.

select round(avg(unit_cost), 2) as avg, round(sum(unit_cost), 2) as sum, round(min(unit_cost), 2) as min, round(max(unit_cost), 2) as max
from purchase_order_details;

-- 2 Посчитайте количество уникальных заказов purchase_order_id

select count(purchase_order_id) as unical_purchase_order_id
from purchase_order_details; 

-- 3 Посчитайте количество продуктов product_id в каждом заказе purchase_order_id Отсортируйте полученные данные по убыванию количества

select purchase_order_id, count(product_id)
from purchase_order_details
group by purchase_order_id
order by 2 desc;

-- 4 Посчитайте заказы по дате доставки date_received Считаем только те продукты, количество quantity которых больше 30

select count(purchase_order_id), quantity, date_received
from purchase_order_details
group by date_received
having quantity > 30;

-- 5 Посчитайте суммарную стоимость заказов в каждую из дат Стоимость заказа - произведение quantity на unit_cost

select round(sum(quantity * unit_cost), 2) as sum_orders_cost, date_received
from purchase_order_details
group by date_received;

-- 6 Сгруппируйте товары по unit_cost и вычислите среднее и максимальное значение quantity только для товаров где purchase_order_id не больше 100

select purchase_order_id, round(avg(quantity), 2) as avg, round(max(quantity), 2) as max
from purchase_order_details
where purchase_order_id <= 100
group by unit_cost;

-- 7 Выберите только строки где есть значения в столбце inventory_id Создайте столбец category - если unit_cost > 20 то 'Expensive' в остальных случаях 'others' Посчитайте количество продуктов в каждой категории

select IF(unit_cost > 20, 'Expensive', 'others') AS category, count(*) AS product_count
from purchase_order_details
where inventory_id is not null
GROUP BY category;

select * 
from purchase_order_details;
