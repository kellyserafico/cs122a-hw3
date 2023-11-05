from relational_algebra import *
import sqlite3
class Expressions():

    # The following query is the solution to: Retrieve the name of all Trainers who have the credentials CNS
    sample_query = Projection(NaturalJoin(Selection(Relation("Trainer"),Equals("credentials","CNS")),Relation("person")),["name"])

    expression1 = Projection("person", ['name', 'gender'])

    expression2 = Projection(NaturalJoin(Relation("university_affiliate"), NaturalJoin(Selection(Relation("non_student"), Equals("member_type", "Faculty")), Relation("person"))), ["name", "department"])

    # expression3 = Projection(NaturalJoin(Selection(Relation("space"), Equals("space_description", "weight room")), Selection(Relation("space"), Equals("space_description", "cardio room"))), "space_id")


    # names of people who were at a location at 2023-04-01
    #names of people who were at weight or cardio room at 2023-04-01
    
    #space ids of weight room and cardio room
    poop = (Union(Selection(Relation("space"), Equals("space_description", "cardio room")), (Selection(Relation("space"), Equals("space_description", "weight room")))))
    # expression3 = Projection(Selection(Relation('location_reading'), Equals("space_id", poop)), "person_id")
    expression3 = Projection(NaturalJoin(Selection(NaturalJoin(poop, Relation("location_reading")), Equals("timestamp", "2023-04-01 00:00:00")), Relation("person")), "name")

    #expression4 = 

    #expression5 =

    #expression6 = 

    #expression7 = 

    #expression8 = 

    #expression9 = 

    #expression10 = 
    
    
    sql_con = sqlite3.connect("sample122A.db")

    result = expression3.evaluate(sql_con=sql_con) #CHANGE SAMPLE QUERY TO THE EXPRESSION YOU WANT TO TRY
    print(result.rows)