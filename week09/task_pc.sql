SELECT AVG(speed) FROM pc;

SELECT AVG(screen) FROM laptop JOIN product ON laptop.model = product.model GROUP BY maker;

SELECT AVG(speed) FROM (SELECT * FROM laptop WHERE price > 1000); 

SELECT AVG(price) FROM pc GROUP BY hd;

SELECT AVG(price) FROM (SELECT * FROM pc WHERE speed > 500);

SELECT AVG(price) FROM pc JOIN product ON pc.model = product.model WHERE product.maker = 'A'; 

SELECT AVG(price) FROM pc JOIN product ON pc.model = product.model WHERE product.maker = 'B' UNION SELECT AVG(price) FROM laptop JOIN product ON laptop.model = product.maker WHERE product.maker = 'B'; 

SELECT * FROM (SELECT COUNT(code) FROM pc JOIN product ON pc.model = product.model GROUP BY product.maker); 

SELECT product.maker, MAX(pc.price) FROM pc JOIN product ON pc.model = product.model;

SELECT maker, AVG(hd) FROM product JOIN pc ON pc.model = product.model GROUP BY maker HAVING maker IN (SELECT maker FROM product WHERE type='Printer') AND maker IN (SELECT maker FROM product WHERE type='PC'); 
