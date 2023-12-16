import os, sys
DB_HOST = os.getenv('DB_HOST', 'localhost')
DB_PORT = os.getenv('DB_PORT', '5432')
DB_NAME = os.getenv('DB_NAME')
DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')

DEBUG = os.getenv('DEBUG', False)



#  CREATE TABLE STUDENT(      
#  id serial PRIMARY KEY,     
#  name VARCHAR(60) NOT NULL, 
#  mobile VARCHAR(20),        
#  email VARCHAR(50) NOT NULL,
#  gender VARCHAR(8) NOT NULL,
#  dob DATE NOT NULL          
#  );   