'''
Created on Apr 8, 2018

@author: cececombemale
'''
from client import Client
from plan import Plan 
import sqlite3
import os 

conn = sqlite3.connect('client.db')

c = conn.cursor()
print("Welcome to your customizable workouts!")

#create table in database
c.execute("""CREATE TABLE IF NOT EXISTS clients(
        first text,
        last text,
        email text
        )""")
#create table in database     
c.execute("""CREATE TABLE IF NOT EXISTS plan(
        name text,
        monday text,
        tuesday text,
        wednesday text,
        thursday text,
        friday text,
        saturday text,
        sunday text,
        email text,
        FOREIGN KEY(email) REFERENCES clients(email)
        )""")
#functions that insert,delete,load, and edit 

#insert a client
def insert_client(cl):
    c.execute("INSERT INTO clients values(:first, :last, :email)",{'first': cl.first,'last': cl.last, 'email':cl.email})
    conn.commit()
#insert a plan
def insert_plan(pl,email):
    c.execute("INSERT INTO plan values(:name, :monday, :tuesday, :wednesday, :thursday, :friday, :saturday, :sunday, :email)",
              {'name': pl.name,'monday': pl.monday, 'tuesday':pl.tuesday, 'wednesday': pl.wednesday,'thursday': pl.thursday, 'friday': pl.friday, 'saturday': pl.saturday, 'sunday': pl.sunday, 
               'email': email})
    conn.commit()
#loads workout plan based on its name
def load(plan_name):
    c.execute("SELECT * FROM plan WHERE name=:name", {'name' : plan_name})
    print(c.fetchall())
#functions to edit each day of a workout plan
def edit_monday(monday,name):
    c.execute("UPDATE plan SET monday = :monday WHERE name = :name",
    {'monday': monday, 'name': name})
    conn.commit()
def edit_tuesday(tuesday,name):
    c.execute("UPDATE plan SET tuesday = :tuesday WHERE name = :name",
    {'tuesday': tuesday, 'name': name})
    conn.commit()
def edit_wednesday(wednesday,name):
    c.execute("UPDATE plan SET wednesday = :wednesday WHERE name = :name",
    {'wednesday': wednesday, 'name': name})
    conn.commit()
def edit_thursday(thursday,name):
    c.execute("UPDATE plan SET thursday = :thursday WHERE name = :name",
    {'thursday': thursday, 'name': name})
    conn.commit()
def edit_friday(friday,name):
    c.execute("""UPDATE plan SET friday = :friday WHERE name = :name""",
    {'friday': friday, 'name': name})
    conn.commit()
def edit_saturday(saturday,name):
    c.execute("UPDATE plan SET saturday = :saturday WHERE name = :name",
    {'saturday': saturday, 'name': name})
    conn.commit()
def edit_sunday(sunday,name):
    c.execute("UPDATE plan SET sunday = :sunday WHERE name = :name",
    {'sunday': sunday, 'name': name})
    conn.commit()
#delete a workout plan based on its name
def delete(plan_name):
    c.execute("DELETE from plan WHERE name = :name",
              {'name':name})
    conn.commit()
#delete a client based on their email
def delete_client(email):
    c.execute("DELETE from clients WHERE email = :email",
              {'email':email})
    c.execute("DELETE from plan WHERE email = :email",
              {'email':email})
    conn.commit()
#edits first name of client
def edit_first(first,email):
    c.execute("UPDATE clients SET first = :first WHERE email = :email",
    {'first': first, 'email': email})
    conn.commit()
#edits last name of a client
def edit_last(last,email):
    c.execute("UPDATE clients SET last = :last WHERE email = :email",
    {'last': last, 'email': email})
    conn.commit()
#attempts to edit an email of a client but function is slightly broken 
def edit_email(email,email2):
    c.execute("UPDATE plan SET email = :email WHERE email = :email",
    {'email': email2})
    c.execute("UPDATE clients SET email = :email WHERE email = :email",
    {'email': email2})
    conn.commit()
    
#user input
answer = input("Would you like to add new clients (add), add a new workout plan (addw) edit a workout plan or client(edit), load a workout plan (load) or delete a workout plan or client (delete)? ")
answer = answer.lower()
answer = answer.replace(' ', '')
if(answer == 'add' or answer == 'addw' or answer == 'edit' or answer == 'load' or answer == 'delete'):
    while(answer != '0'):
        if(answer == 'add'):
            first =input("What is the client's first name? ")
            last = input("What is the client's last name? ")
            email = input("What is the client's email? ")
            first = first.lower()
            last = last.lower()
            email = email.lower()
            cl = Client(first,last,email)
            insert_client(cl)
        elif(answer == 'addw'):
            name =input("What is the name of the workout plan? ")
            name.lower()
            question = input("Are there workouts on monday? *yes/y or no/n* ")
            question = question.lower()
            if(question == 'yes' or question == 'y'):
                monday = 'Monday: '
                monday += input("Please list the workouts ")
            else:
                monday = 'Monday: nothing'
            question = input("Are there workouts on tuesday? *yes/y or no/n* ")
            question = question.lower()
            if(question == 'yes' or question == 'y'):
                tuesday = 'Tuesday: '
                tuesday += input("Please list the workouts ")
            else:
                tuesday = "Tuesday: nothing"
            question = input("Are there workouts on wednesday? *yes/y or no/n* ")
            question = question.lower()
            if(question == 'yes' or question == 'y'):
                wednesday = 'Wednesday: '
                wednesday += input("Please list the workouts  ")
            else:
                wednesday = "Wednesday: nothing"
            question = input("Are there workouts on thursday? *yes/y or no/n* ")
            question = question.lower()
            if(question == 'yes' or question == 'y'):
                thursday = 'Thursday: '
                thursday += input("Please list the workouts ")
            else:
                thursday = "Thursday: nothing"
            question = input("Are there workouts on friday? *yes/y or no/n* ")
            question = question.lower()
            if(question == 'yes' or question == 'y'):
                friday = 'Friday: '
                friday += input("Please list the workouts ")
            else:
                friday = "Friday: nothing"
            question = input("Are there workouts on saturday? *yes/y or no/n* ")
            question = question.lower()
            if(question == 'yes' or question == 'y'):
                saturday = 'Saturday: '
                saturday += input("Please list the workouts ")
            else:
                saturday = "Saturday: nothing"
            question = input("Are there workouts on sunday? *yes/y or no/n* ")
            question = question.lower()
            if(question == 'yes' or question == 'y'):
                sunday = 'Sunday: '
                sunday += input("Please list the workouts ")
            else:
                sunday = "Sunday: nothing"
            email = input("Please list the email associated with the client to link the plan? ")
            pl = Plan(name,monday,tuesday,wednesday,thursday,friday,saturday,sunday)
            insert_plan(pl, email)
            q = input("Would you like to associate another client with this plan? *yes/y* *no/n*")
            while(q=='yes' or q =='y'):
                email = input("Please list the email associated with the client to link the plan? ")
                insert_plan(pl, email)
                q = input("Would you like to associate another client with this plan? *yes/y* *no/n*")
        elif(answer == 'edit'):
            what = input("Do you want to edit a client (client) or a plan (plan) ")
            what = what.lower()
            if(what == 'plan' ):
                name = input("What is the name of the plan? ")
                answer = input("Would you like to edit Monday, Tuesday, Wednesday, Thursday, Friday, Saturday or Sunday")
                answer = answer.lower()
                answer = answer.replace(' ', '')
                if(answer == "monday"):
                    monday = "Monday: "
                    monday += input("Please list the workouts for Monday: ")
                    edit_monday(monday,name)
                if(answer == "tuesday"):
                    tuesday = "Tuesday: "
                    tuesday += input("Please list the workouts for Tuesday: ")
                    edit_tuesday(tuesday,name)
                if(answer == "wednesday"):
                    wednesday = "Wednesday: "
                    wednesday += input("Please list the workouts for Wednesday: ")
                    edit_wednesday(wednesday,name)
                if(answer == "thursday"):
                    thursday = "Thursday: "
                    thursday += input("Please list the workouts for Thursday: ")
                    edit_thursday(thursday,name)
                if(answer == "friday"):
                    friday = "Friday: "
                    friday += input("Please list the workouts for Friday: ")
                    edit_friday(friday,name)
                if(answer == "saturday"):
                    saturday = "Saturday: "
                    saturday += input("Please list the workouts for Saturday: ")
                    edit_saturday(saturday,name)
                if(answer == "sunday"):
                    sunday = "Sunday: "
                    sunday += input("Please list the workouts for Sunday: ")
                    edit_sunday(sunday,name)
            if(what == 'client'):
                user = input("Would you like to edit the first name (first), the last name (last) or the email (email) of the client?")
                user = user.lower()
                if(user == 'first'):
                    email = input("What is the email of the client you want to edit? ")
                    first = input("What do you want to change the client's first name to? ")
                    edit_first(first, email)
                elif(user == 'last'):
                    email = input("What is the email of the client you want to edit? ")
                    last = input("What do you want to change the client's last name to? ")
                    edit_last(last, email)
                elif(user == 'email'):
                    email = input("What is the email of the client you want to edit? ")
                    email2 = input("What do you want to change the client's email to? ")
                    edit_email(email, email2)
                else:
                    print("Sorry that is invalid input")
        elif(answer == 'load'):
            name = input("What is the name of the plan you want to load? ")
            load(name)
        elif(answer == 'delete'):
            what = input("Do you want to delete a client (client) or a plan (plan) ")
            what = what.lower()
            if(what == 'plan'):
                name = input("What is the name of the plan? ")
                delete(name)
            elif(what == 'client'):
                email = input("What is the email of the client ")
                delete_client(email)
            else:
                print("Sorry thats not a valid option")
        else:
            print("Sorry that is not a valid option")
        answer = input("Would you like to add new clients (add), add a new workout plan (addw), edit a workout plan (edit), load a workout plan (load), delete a workout plan (delete), or enter '0' to quit the program ")
        answer = answer.lower()
        answer = answer.replace(' ', '')

conn.commit()
conn.close()

