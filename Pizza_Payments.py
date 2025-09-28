

def pizzacalculator(pizza):
    michael_amount = 0
    if pizza < 5:
        print("Michael pays for the whole pizza.")
        michael_amount = pizza
    
    else:
        kate_amount = round(pizza * 1/3,2)
        if kate_amount <= 10:
           print(f"Kate will cover {kate_amount} dollars for the pizza.")
           michael_amount = pizza - kate_amount
    
        else:
            michael_amount = pizza - 10
        

    return michael_amount  

michael_amount = pizzacalculator(15)
print(f"Michael has to pay {michael_amount} dollars for the pizza")