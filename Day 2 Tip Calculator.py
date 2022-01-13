print("Tip Calculator initialized..... *bip bip* *burp*\n")

bill = input("What was the total cost for the bill in USD?\n") #<- the inptu here is read as a string

tip = input("Please type in the percentage tip you would like to give.\n")
tip = (1 + float(tip)/100 )

party_count = input("How many people are splitting the bill today?\n")

divided_cost = round((float(bill) * float(tip) /  float(party_count)),3) #I did some more research and found an command in Python named round() that lets me round decimal places, so I decided to implement it in the divded cost section of the program

print(f"Each person in the party should be paying around: ${divided_cost}") #I tried using an F-string here to automagically format any variables I was printing and it looks like it works fairly smooth