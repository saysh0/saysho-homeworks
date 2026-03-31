use 121225ptm_Red_Hats_Sysytem_JCC_Weapon;
drop function hypotenuse_of_triangel;
-- task1 Расчет площади круга
/* Создайте функцию для расчета площади круга, если известен его радиус.
Используйте формулу 
Где:
S — площадь круга,
r — радиус круга,
​π≈3.14159, используйте функцию PI(), которая возвращает это число.
*/
delimiter //
create function area_of_circle(r decimal(10, 3))
returns decimal(10, 3)
deterministic
begin
	return pi() * (r * r); 
end //
delimiter ;

select area_of_circle(5) as S;

-- task2 Функция для расчета гипотенузы треугольника
/* Создайте функцию для расчета гипотенузы прямоугольного треугольника, если известны длины его катетов.
Используйте формулу 
Где:
c — длина гипотенузы прямоугольного треугольника,
a, b — длины его катетов
*/
delimiter //
create function hypotenuse_of_triangel(katet1 decimal(10, 2), katet2 decimal(10, 2))
returns decimal(10, 3)
deterministic
begin
	return sqrt(pow(katet1, 2) + pow(katet2, 2));
end //
delimiter ;

select hypotenuse_of_triangel(5, 6) as c;
