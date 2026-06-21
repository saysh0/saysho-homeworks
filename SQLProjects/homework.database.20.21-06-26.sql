# 1.Вывести названия фильмов с расшифровкой рейтинга для каждого. Рейтинги описаны здесь. В таблице film хранятся годы рейтингов. Нужно воспользоваться оператором case чтобы определить для каждого кода условие, по которому будет выводится его развернутое описание (1 предложение). 
select title, rating,
CASE 
	when rating = 'G' then 'All ages admitted. Nothing that would offend parents for viewing by children.'
	when rating = 'PG' then 'Some material may not be suitable for children. Parents urged to give "parental guidance". May contain some material parents might not like for their young children.'
	when rating = 'PG-13' then 'Some material may be inappropriate for children under 13. Parents are urged to be cautious. Some material may be inappropriate for pre-teenagers.'
	when rating = 'R' then 'Under 17 requires accompanying parent or adult guardian. Contains some adult material. Parents are urged to learn more about the film before taking their young children with them.'
	else 'No one 17 and under admitted. Clearly adult. Children are not admitted.'
END as 'rate_transkription'
from sakila.film;


# 2.Выведите количество фильмов в каждой категории рейтинга. Используем group by.
select rating, count(*) 
from sakila.film
group by rating;


# 3.Используя оконные функции и partition by, выведите список названий фильмов, рейтинг и количество фильмов в каждом рейтинге. Объясните, чем отличаются результаты предыдущего запроса и запроса в этой задаче. 
select title, rating, count(*) over(partition by rating) as ass
from sakila.film;


# 4.Изучите таблицы payment и customer. Выведите список всех платежей с указанием имени и фамилии каждого заказчика, датой платежа и суммой.
select c.first_name, c.last_name, p.payment_date, p.amount 
from sakila.payment p 
join sakila.customer c on p.customer_id = c.customer_id
order by 3 DESC;



# 5.Поменяйте предыдущий запрос так, чтобы дата выводилась в формате “число, название месяца, год” (без времени).
select c.first_name, c.last_name, date_format(p.payment_date, '%d-%M-%Y'), p.amount 
from sakila.payment p 
join sakila.customer c on p.customer_id = c.customer_id
order by 3 DESC;