Q: Create a user defined function  to perfom following

def bill(consumers):
    Dict=dict()
    for i in consumers:
        if(1<consumers[i]<=200):
            Dict[i]=100+consumers[i]*3
        elif(201<consumers[i]<=300):
            Dict[i]=100+consumers[i]*4
        elif(301<consumers[i]<=400):
            Dict[i]=100+consumers[i]*5
        elif(401<consumers[i]<=500):
            Dict[i]=100+consumers[i]*6
        else:
            Dict[i]=100+consumers[i]*7
    print("Units= ",consumers)
    print("Bill= ",Dict)
bill({"Alice":140,"bob":230,"charly":490,"david":375,"ethan":765})
