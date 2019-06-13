"""
DAO (DataBase Access Object 数据库访问对象)
1. 可以使用原生SQL
2. 也可以使用元类设计ORM(Object Relationship Mapping  对象关系映射)
"""


DB_CONFIG = {
   'host': 'localhost',
   'port': 3306,
   'db': 'log_db',
   'user': 'root',
   'password': 'root',
   'charset': 'utf8'
}