from replit import clear
#HINT: You can call clear() to clear the output in the console.

print("Welcome to the secret auction program.")
addBidder = True
bid = {}

def find_highestBidder(bidding_record):
    # This is actually all I need
    highestBid = 0
    for bidder in bidding_record:
        if bidding_record[bidder] > highestBid:
            highestBid = bidding_record[bidder]
            highestBidder = bidder
    print(f"The winner is {highestBidder} with a bid of ${highestBid}.")

while addBidder is True:
    bidderName = input("\nWhat's your name?: ")
    bidderBid = int(input("What's your bid?: $"))
    bid[bidderName] = bidderBid

    more_bidderValid = False
    while more_bidderValid is False:
        moreBidder = input("Are there any other bidders? Type 'yes' or 'no'.\n")
        if moreBidder == "no":
            more_bidderValid = True
            addBidder = False
            clear()            
            find_highestBidder(bid)
        elif moreBidder == "yes":
            more_bidderValid = True
            clear()
        else:
            print("\nPlease enter a valid input.")


# What in the ADHD hot mess is this... (go to line...)
'''highestFound = False
highestBid = 0
while not highestFound:
    
    for bidder in bid:
        
        for otherBidder in bid:
            print(f"This is {bidder} vs {otherBidder}")
            
            if bid[bidder] > bid[otherBidder] and bid[bidder] > highestBid:
                highestBid = bid[bidder]
                highestBidder = bidder
                print(f"Current highest bidder is {highestBidder} with ${highestBid}.")
                
            else:
                None
                
    highestFound = True'''
