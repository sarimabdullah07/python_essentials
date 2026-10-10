'''
Q: Create a student result, if marks of a student is passed in the form of
    list of dictionaries [{"A":87,"B":92}] the function should calculate total
    marks and percentage of each student and append it into respective dictionaries like 
    [{"name":"A","marks":[97,95,93],"total":285,"percentage":95.0}].finally
    retrun the average of percentages to the calling scope.
'''
def student_data(result):
    total_percent=0
    for i in result:
        total=sum(i["marks"])
        percent=total/len(i["marks"])
        i["total"]=total
        i["percent"]=percent
        print(i)
        total_percent+=i["percent"]
    return (round(total_percent/len(result),2))
    
list=[{"name":"Alice","marks":[98,56,78,49,86]},
    {"name":"Bob","marks":[93,58,73,46,88]},
    {"name":"Charly","marks":[90,57,74,47,65]},
    {"name":"David","marks":[96,66,88,49,95]},
    {"name":"Ethan","marks":[97,76,68,44,55]}]
s=student_data(list)
print("Averga percentage of all the student: ",s)
