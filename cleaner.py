import sqlite3

db_name = "QA_S08"
row = []
sql_transaction = []
start_row = 0
status = ""
total = 0
failed = 0
success = 0
duplicate = 0



connection = sqlite3.connect('{}.db'.format(db_name))
c = connection.cursor()

def create_table():
    c.execute("CREATE TABLE IF NOT EXISTS question_answer_pairs(question TEXT, answer TEXT)")

def sql_insert(question, answer):
    
    if answer == "" or answer == "NULL":
        global failed
        failed += 1
        return False
    else:

        try:
            sql = """INSERT INTO question_answer_pairs(question, answer) VALUES ("{}","{}");""".format(question, answer)
            transaction_bldr(sql)
        except Exception as e:
            print('inser_ERROR',str(e))

def find_existing_question(question):
    try:
        sql = "SELECT question FROM question_answer_pairs WHERE question = '{}' LIMIT 1".format(question)
        c.execute(sql)
        result = c.fetchone()
        if result != None:
            return result[0]
        else: return False
    except Exception as e:
        #print(str(e))
        return False
def sql_insert_replace_question(question, answer):
    global duplicate
    duplicate += 1
    try:
        sql = """UPDATE question_answer_pairs SET question = ?, answer = ? WHERE question =?;""".format(question, answer, question)
        transaction_bldr(sql)
    except Exception as e:
        print('s0 insertion',str(e))


def transaction_bldr(sql):
    global sql_transaction
    global success
    success += 1
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
    # print(f)
    for x in f:
        # print(x)
        row_counter += 1
        # print(row_counter)
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
                
                total += 1
                find_existing = find_existing_question(question)
                if find_existing:
                    sql_insert_replace_question(question, answer)
                else:               
                    sql_insert(question, answer)
                continue
            status = "Completed!"
    print('{}, Total: {}, Success: {}, False: {}, Duplicate: {}'.format(status, total, success, failed, duplicate))
    

