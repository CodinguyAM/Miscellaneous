try:
    import sqlite3

    def rdb(cursor):
        for i in cursor.fetchall():
            print(i)


    connection = sqlite3.connect('C:/Users/advay/OneDrive/Desktop/Programs & Code/SQL/Databases/'+input("Where would you like to save your DB?: ")+'.db')
    crsr = connection.cursor()
    while input("Would you like to continue using the SQL Interpreter(yes/no)") != "no":
        pr = bool(input("If you would like to print your database after your next command is executed, enter anything and then press enter. If not, simply press enter."))
        comm = input("Enter your SQL command: ")
        print("The SQL query you entered is:", comm)
        iscor = input("Is that query accurate? yes/no")
        if iscor == "no":
            comm = input("Enter your SQL command: ")
        try:
            crsr.execute(comm)
            connection.commit()
        except:
             print("The query is invalid.")
        if pr:
            rdb(crsr)
except:
    print("An error was encountered")

connection.close()
