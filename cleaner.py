import sqlite3
from datetime import datetime
import time

db_name = "QA_S08"
row = []
sql_transaction = []
start_row = 0



connection = sqlite3.connect('{}.db'.format(db_name))
c = connection.cursor()

def create_table():
    c.execute("CREATE TABLE IF NOT EXISTS question_answer_pairs(question TEXT, answer TEXT)")

def sql_insert(question, answer):
    try:
        sql = """INSERT INTO question_answer_pairs(question, answer) VALUES ("{}","{}");""".format(question, answer)
        transaction_bldr(sql)
    except Exception as e:
        print('inser_ERROR',str(e))

def transaction_bldr(sql):
    global sql_transaction
    sql_transaction.append(sql)
    if len(sql_transaction) > 100:
        c.execute('BEGIN TRANSACTION')
        for s in sql_transaction:
            try:
                c.execute(s)
            except:
                pass
        connection.commit()
        sql_transaction = []



if __name__ == '__main__':
    create_table()
    row_counter = 0  

    f = open("question_answer_pairs.txt", "r")
    for x in f:
    	row_counter += 1
    	row.append(x)
    if row_counter > start_row:
    	for i in range(len(row)):
    		column = []
    		i += 1
    		if i < len(row):
    			a = row[i].split('\t')
    			for r in a:
    				column.append(r)
    			question = column[1]
    			answer = column[2]
    			
    			sql_insert(question, answer)
    			continue

    		print("Completed")
    		break
    		


	# print(i)



