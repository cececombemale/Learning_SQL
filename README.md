#Playing around with SQL and Python

##The goal in making this program was to get familiar with creating a database, putting information into that database, editing the information and removing it. 

##Key: I use a user's email as the ID for each person and foreign key connecting the workout plan to the person.

##Classes:

######Client class- defines a client with a first name, last name, and email address.
######Workout plan class- defines which workouts occur on which day.
######Instances of these classes were used to insert each client and workout plan to the database.

#Functions:

######Adding a client or workout plan to the database
######Editing a workout plan
######Editing a client
######Loading a workout plan
######Deleting clients and workout plans

#Other details:
######Each workout plan can be linked to multiple clients.
######When a client is deleted, the workout plan in the second table associated with the client is also deleted.