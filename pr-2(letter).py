x=input("enter the name\n")
y=input("enter the date\n")
letter="dear Name,\nYou are Selected!\nDate"
letter=letter.replace("Name",x)
letter=letter.replace("Date",y)
print(letter)
