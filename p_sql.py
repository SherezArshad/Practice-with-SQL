'''
Daniyal Arshad


'''
import sqlite3
import pandas as pd
import numpy as np
from datetime import datetime, timedelta



def student_report(Filename, StudentID):


    conn = sqlite3.connect(Filename)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    query = "SELECT name FROM sqlite_master Where type = 'table';"

    transcript = ""
    for row in cursor.execute("SELECT name FROM sqlite_master Where type = 'table';").fetchall():
        query = ("SELECT last || ', ' || first AS name, grade FROM " + row[0] + " WHERE id = '" + StudentID + "';")
        result = cursor.execute(query).fetchone()
        if result:
            if not transcript:
                transcript += result['name'] + ', ' + StudentID
                transcript += '\n' + '-' * len(transcript) + '\n'
            transcript += row[0].replace('_', ' ') + ': ' + result['grade'] + '\n'
    return transcript

    curosor.close()
    connection.close()
 


def A_students(conn, table_name = "ISTA_131_f17", class_val = None, max_val=10):

    cursor = conn.cursor()
    conn.row_factory = sqlite3.Row

    lst_of_students = []


    if class_val == None:
        query = ("SELECT last, first FROM " + table_name + " WHERE grade ='A' ORDER BY last LIMIT "+ str(max_val))
        cursor.execute(query)
    else:
        query = ("SELECT last, first FROM " + table_name + " WHERE grade = 'A'  AND level LIKE" + class_val + " ORDER BY last LIMIT "+ str(max_val))

        for row in cursor:
            lst_of_students.append(row[0] , row[1])




    return lst_of_students

   


def class_performance(conn, table_n = 'ISTA_131_F17'):

    cursor = conn.cursor()
    conn.row_factory = sqlite3.Row
    query = ("SELECT * FROM " + table_n + ";")
    cursor.execute(query)



    dict = {}
    count = 0
    A_student = 0
    B_student = 0
    F_student = 0
    R_student = 0
    U_student = 0




    for row in cursor:
        count += 1
    query = ("SELECT grade FROM " + table_n + " ORDER BY grade asc;")
    cursor.execute(query)
        


    for row in cursor:
        if row[0] == 'A':
            A_student += 1

        elif row[0] == 'B':
            B_student += 1

        elif row[0] == 'F':
            F_student += 1

        elif row[0] == 'R':
            R_student += 1

        elif row[0] == 'U':
            U_student += 1

    dict['A'] = round(((A_student/count)*100) ,1)
    dict['B'] = round(((B_student/count)*100) ,1)
    dict['F'] = round(((F_student/count)*100) ,1)
    dict['R'] = round(((R_student/count)*100) ,1)
    dict['U'] = round(((U_student/count)*100), 1)

    return dict






def read_frame(csv_filename = "sunrise_sunset.csv"):
    lst = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    lst2 = []


    for month in lst:
        for val in ["_r", "_s"]:
            lst2.append(month + val)


    df = pd.read_csv("sunrise_sunset.csv", header = None, names = lst2, index_col = 0, dtype = str)
    print(df)
    return(df)





def get_series(sun_DataFrame):
    lst = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    
    rise_lst = pd.concat([sun_DataFrame [val + "_r"] for val in lst])
    set_lst = pd.concat([sun_DataFrame [val + "_s"] for val in lst])

    rise_lst = rise_lst.dropna()
    set_lst = set_lst.dropna()

    rise_lst.index = pd.date_range("010118", "123118")
    set_lst.index = pd.date_range("010118", "123118")


    return rise_lst, set_lst


def longest_day(sunrise, sunset):
    longest_day = sunset.copy().astype(int)
    longest_day = longest_day.subtract(sunrise.astype(int))
    return longest_day.idxmax(), str(longest_day[longest_day.idxmax()])


def sunrise_dif(sunrise, Timestamp):

    dt = timedelta - seconds(0)
    (dt.days, dt.minutes)

  

    






    


