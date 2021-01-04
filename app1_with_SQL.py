import mysql.connector

import difflib
from difflib import get_close_matches

con = mysql.connector.connect(
    user = "ardit700_student",
    password = "ardit700_student",
    host = "108.167.140.122",
    database = "ardit700_pm1database"
)

cursor = con.cursor()
inputWord = input("Enter the word: ")


query = cursor.execute(" SELECT * FROM Dictionary WHERE Expression='%s' " % inputWord)

results = cursor.fetchall()

if results:
    for result in results:
        print(result[1])
else:
    query1 = cursor.execute("SELECT Expression FROM Dictionary ")
    results1 = cursor.fetchall()

    listResults1 = [ result[0] for result in results1 ]

    ## TO CHECK IF RESULT1 IS CONVERTED TO LIST
    # if listResults1:
    #     print(listResults1)
    # else:
    #     print("Empty")

    ## TO PRINT 3 CLOSEST WORDS
    #print( get_close_matches(inputWord,listResults1) )


    nearestWord = get_close_matches(inputWord,listResults1)[0]

    yn = input("Did you mean '%s' If Yes enter Y else N:  " % nearestWord)
    yn = yn.upper()

    if yn=='Y':
        query2 = cursor.execute("select * from Dictionary WHERE Expression = '%s' " % nearestWord )
        results2 = cursor.fetchall()

        if(results2):
            for result in results2:
                print(result[1])
        else:
            print("Word not found!!")
    elif yn=='N':
        print("Word not found....Please check the spellig")
    else:
        print("Did not understand your input")