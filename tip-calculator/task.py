print("welcome to the tip calculator")

bill = float(input("What was the total bill?"))
tip = int(input("How much tip would you like to give? 10,12, or 15?"))
split = int(input("How many people to split the bill?"))

bill_with_tip = tip / 100 * bill + bill
bill_after_split = bill_with_tip / split
final_bill = round(bill_after_split, 2)
print(f"Each person has to pay ${final_bill}")
