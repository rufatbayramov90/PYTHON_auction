'''students ={
    "Hanry": 81,
    "Alvera" : 75,
    "Cohn" : 99,
    "Jony" : 52
}
student_grades = {}

for stud in students:
    score = students[stud]
    if score > 80:
        student_grades[stud] = "You Passed the Exam Successfully"
    elif score > 70:
        student_grades[stud] = "You passed the exam with a few points"
    elif score > 60:
        student_grades[stud] = "Try yourself in the next exam"
    else:
        student_grades[stud] = "You failed the exam"
print(student_grades)
'''

from replit import clear
from art import logo
print(logo)

bids ={}
bidding_finish = False

def find_high_bidder(bidding_record):
    high_bid = 0
    winner = ""
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > high_bid:
            high_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${high_bid}")



while not bidding_finish:
    name = input("What is your name?")
    price = int(input("What is your bid?  $"))
    bids[name] = price
    should_continue = input("Are there any other bidders? yes or no")
    if should_continue == "no":
        bidding_finish = True
        find_high_bidder(bids)
    elif should_continue == "yes":
        clear()

    


