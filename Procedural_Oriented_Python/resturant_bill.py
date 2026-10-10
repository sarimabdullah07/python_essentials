'''
Q: Create a billing system of a resturant if the dictionary of the recipies
    are passed to function like {"chicken":170,"rice":110,"pizza":340}, the 
    function should display the bill in detail like .. 
    1: chicken 170/-
    2: rice    90/-
    3: pizza   340/-
    Total Bill Amount: 600/-
    GST 0.06:           36/-
    Bill with GST:     636/-
'''

def bill(items):
    index=1
    for i in items:
        total_bill_amount=sum(items.values())
        gst=0.06
        bill_with_gst=(total_bill_amount*gst)+total_bill_amount
        print(index,":",i,"\t",items[i],"/-",sep="")
        index+=1
    print("Total Bill Amount: ",total_bill_amount)
    print("GST rate: ",gst)
    print("Bill with GST: ",bill_with_gst)

bill({"Pizza":450,"Omelette":40,"Custard":230,"Momos":210,"Rissole":30,"Golgappas":49})
