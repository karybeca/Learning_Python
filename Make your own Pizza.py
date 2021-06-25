print ("create your own Pizza!")

my_pizza = ["Basic", 7, "Tomatos", "Cheese"]
my_pizza[0] = input ("How do you want your pizza to be named:")
print ("This is your basic Pizza: Pizza", my_pizza[0], "for", my_pizza[1],"Euros with 2 ingredients", my_pizza [2], ",", my_pizza[3]
)

my_pizza.append (input ("Please add an ingredient "))
my_pizza.append (input ("Please add an ingredient "))
my_pizza.append (input ("Please add an ingredient "))
my_pizza.append (input ("Please add an ingredient "))

print ("Your pizza now contains", len(my_pizza)-2, "ingredients, they are", my_pizza[2:])
print ("This is one ingredient too much. Only", len(my_pizza)-3, "ingredients are possible")
my_pizza.remove(input ('Which ingredient do you want to delete?'))                                                
print ("Your pizza now contains", len(my_pizza)-2, "ingredients, they are", my_pizza[2:])
price_pizza = float (input ("how much are you willing to pay for the Pizza"))
my_pizza[1] = price_pizza*1.2
print ("You created Pizza", my_pizza[0], "for", my_pizza[1], "Euro, with the ingredients", my_pizza[2:], "BON APPETIT!")




