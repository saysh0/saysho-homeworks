-- Таблица purchase_order_details
use northwind;
select *
from purchase_order_details;

-- 1. Для каждого заказа order_id выведите минимальный, максмальный и средний unit_cost

select purchase_order_id, round(unit_cost) as unit_cost, round(min(unit_cost) over (partition by purchase_order_id)) as min_unit_cost,
round(max(unit_cost) over (partition by purchase_order_id)) as max_unit_cost,
round(avg(unit_cost) over (partition by purchase_order_id)) as avg_init_cost
from purchase_order_details;

-- 2.  Оставьте только уникальные строки из предыдущего запроса

select distinct  purchase_order_id, round(unit_cost) as unit_cost, round(min(unit_cost) over (partition by purchase_order_id)) as min_unit_cost,
round(max(unit_cost) over (partition by purchase_order_id)) as max_unit_cost,
round(avg(unit_cost) over (partition by purchase_order_id)) as avg_init_cost,
round(avg(unit_cost) over (partition by purchase_order_id)) as avg_init_cost
from purchase_order_details;

-- 3. Посчитайте стоимость продукта в заказе как quantity*unit_cost. Выведите суммарную стоимость продуктов с помощью оконной функции. Сделайте то же самое с помощью GROUP BY

-- оконная функция
select product_id, round(quantity), round(unit_cost), round(quantity * unit_cost) as product_cost,
round(sum(quantity * unit_cost) over (partition by product_id)) as sum_product_cost
from purchase_order_details;

-- group by
select product_id, round(quantity), round(unit_cost), round(quantity * unit_cost) as product_cost, round(sum(quantity * unit_cost))
from purchase_order_details
group by 1;

-- 4. Посчитайте количество заказов по дате получения и posted_to_inventory. Если оно превышает 1 то выведите '>1' в противном случае '=1'.
-- Выведите purchase_order_id, date_received и вычисленный столбец

select purchase_order_id, date_received, if(count(purchase_order_id) over (partition by date_received, posted_to_inventory) > 1, '>1', '=1') as order_amount
from purchase_order_details;
-- я думаю сюда можно добавить dictinct но не решил вставлять ибо не уверен