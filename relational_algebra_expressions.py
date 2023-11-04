from relational_algebra import *
import sqlite3
class Expressions():

    # The following query is the solution to: Retrieve the name of all Trainers who have the credentials CNS
    sample_query = Projection(NaturalJoin(Selection(Relation("Trainer"),Equals("credentials","CNS")),Relation("person")),["name"])

    expression1 = Projection("person", ['name', 'gender'])

    expression2 = Projection(NaturalJoin(Relation("university_affiliate"), NaturalJoin(Selection(Relation("non_student"), Equals("member_type", "Faculty")), Relation("person"))), ["name", "department"])

    expression3 = Projection(NaturalJoin(Selection(Relation("space"), Equals("space_description", "weight room")), Selection(Relation("space"), Equals("space_description", "cardio room"))), "space_id")

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