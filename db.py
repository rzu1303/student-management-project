import psycopg2
from PyQt5 import QtCore
from datetime import datetime 
# import datetime 
from pprint import pprint

from config import (
    DB_HOST,
    DB_PORT,
    DB_NAME,
    DB_USER,
    DB_PASSWORD
)

db = psycopg2.connect(
database=DB_NAME,
user=DB_USER,
password=DB_PASSWORD,
host=DB_HOST,
port= DB_PORT
)

all_student = {}

def db_init():
    query = """
        CREATE TABLE IF NOT EXISTS public.student
            (
                id serial PRIMARY KEY,
                name VARCHAR(60) NOT NULL,
                mobile VARCHAR(20),
                email VARCHAR(50) NOT NULL,
                gender VARCHAR(20) NOT NULL,
                dob DATE NOT NULL
            );    
    
    """
    
    with db.cursor() as session:
        session.execute(query)
        db.commit()

#testing 
# def student_create():
#     with db.cursor() as session:
#         query = """INSERT INTO student (name, mobile, email, gender, dob)
#             VALUES ('{}', '{}', '{}', '{}', '{}');
#             """.format("ass", "011", "hshs", "female", "12-22-31")
#         # print(query)
#         session.execute(query)
#         db.commit()



def student_create(name = None, mobile = None, email=None, gender= None, dob = None):
    with db.cursor() as session:
        query = """INSERT INTO student (name, mobile, email, gender, dob)
            VALUES ('{}', '{}', '{}', '{}', '{}');
            """.format(name, mobile, email, gender, dob)
        session.execute(query)
        db.commit()
    return True  

def student_read():
    with db.cursor() as session:
        session.execute('SELECT * FROM public.student;')
        results = session.fetchall()
    # pprint(results)
    return results       

def student_update(row_id = None, name = None, mobile = None, email=None, gender= None, dob = None):
    with db.cursor() as session:
        session.execute("""UPDATE public.student SET name='{}', mobile='{}', email='{}', 
                    gender='{}', dob='{}' WHERE id = {};""".format(name, mobile, email, gender, dob, row_id))
        db.commit()
        # print(row_id)
        # print(name)

    return True

def student_delete(row_id):
    with db.cursor() as session:
        session.execute("DELETE FROM public.student WHERE id = {} ;".format(row_id))        
        db.commit() 

    return True      


if __name__=="__main__":
    db_init()
    from datetime import datetime
    from pprint import pprint
    # student_create()
    # student_read()
    # event_update()
    # event_delete()

    with db.cursor() as session:
        #####################
        query = """INSERT INTO student (name, mobile, email, gender, dob)
            VALUES ('{}', '{}', '{}', '{}', '{}');
            """.format("x3", "test 1", "Test 3", "female", "12-22-3100")
        # print(query)
        session.execute(query)
        db.commit()

        # session.execute('SELECT * FROM public.student;')
        # results = session.fetchall()
        # # pprint(results)

        # session.execute("UPDATE public.student SET name ='hi hi hi hi' WHERE id = 3 ;")
        # db.commit()

        # session.execute('SELECT * FROM public.student;')
        # results = session.fetchall()
        # pprint(results)

        # session.execute("DELETE FROM public.student WHERE id = 3 ;")
        # db.commit()

        # session.execute('SELECT * FROM public.student;')
        # results = session.fetchall()
        # pprint(results)


        #####################
        session.execute('SELECT * FROM public.student;')
        results = session.fetchall()

        all_student = {}

        for row in results:
            if str(row[0]) not in all_student:
                all_student[str(row[0])] = []

            all_student[str(row[0])].append(
                            {
                                'name': str(row[1]), 
                                'mobile': str(row[2]),
                                'email': str(row[3]),
                                'gender': str(row[4]),
                                'dob': row[5]
                            })

        # pprint(all_student)


        for item in all_student:
            # pprint(item)
            for item1 in all_student[item]:
                    # print(item1['name'])
                    pass