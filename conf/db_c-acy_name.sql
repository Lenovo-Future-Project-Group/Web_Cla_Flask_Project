-- 创建命名为cpvs2的临时数据库
create database if not exists cpvs2 default character set 'utf8';

-- 指定数据库
use cpvs2;

create table if not exists cpvs2(
    id int(11) not null auto_increment,
    name varchar(255) not null,
    primary key(id)

-- 创建表
