create database linkedin;
use linkedin;

create table  technology (ID int,techno varchar(10));
show tables;

insert into technology (id,techno) values(1,"ds");
insert into technology (id,techno) values(1,"tablue");
insert into technology (id,techno) values(1,"sql");
insert into technology (id,techno) values(1,"R");
insert into technology (id,techno) values(2,"powerbi");
insert into technology (id,techno) values(2,"python");
insert into technology (id,techno) values(1,"statics");
select * from technology;


## requres id of skills ds,tablue,python,sql


select id from technology where techno in ("ds","tablue","python","sql");

##with id and technology

SELECT ID, techno FROM technology where techno in ("ds","tablue","python","sql");

###second question 

create database facebook;

use facebook;

create table product_info(product_id int,product_name varchar(50));
create table product_info_like(user_id int, product_id int, liked_date varchar(50));
insert into product_info(product_id,product_name) values(1001,"blog");
insert into product_info(product_id,product_name) values(1002,"youtube");
insert into product_info(product_id,product_name) values(1003,"education");

select * from product_info;
insert into product_info_like(user_id, product_id, liked_date) values(1,1001,"19/12/2020");
insert into product_info_like(user_id, product_id, liked_date) values(2,1003,"10/11/2021");
select * from product_info_like;

SELECT p.product_id, p.product_name
FROM product_info p
LEFT JOIN (
    SELECT product_id, COUNT(*) AS like_count
    FROM product_info_like
    GROUP BY product_id
) pl ON p.product_id = pl.product_id
WHERE pl.like_count IS NULL OR pl.like_count = 0;

##thank you

