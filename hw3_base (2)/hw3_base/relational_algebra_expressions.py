from relational_algebra import *
import sqlite3
class Expressions():

    # The following query is the solution to: Retrieve the name of all Trainers who have the credentials CNS
    sample_query = Projection(NaturalJoin(Selection(Relation("Trainer"),Equals("credentials","CNS")),Relation("person")),["name"])
    
    #expression1 =

    #expression2 = 

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

    result = sample_query.evaluate(sql_con=sql_con)
    print(result.rows)