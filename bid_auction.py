print('''
                  _   _             
                 | | (_)            
  __ _ _   _  ___| |_ _  ___  _ __  
 / _` | | | |/ __| __| |/ _ \| '_ \ 
| (_| | |_| | (__| |_| | (_) | | | |
 \__,_|\__,_|\___|\__|_|\___/|_| |_|
 
 ''')

print("Welcome to secret auctionn program.")
auction_dict ={}
no_of_bidders=True
while no_of_bidders==True:
    name=input("What is your name?: ")
    bid=int(input("What's your bid?: $"))
    auction_dict[name]=bid
    bidder=input("Are ther any other bidders? Type 'yes' or 'no'. ")
    if (bidder=="no"):
        no_of_bidders=False
    
        
bidder_list=list(auction_dict.keys())
bid_list=list(auction_dict.values())
max_bid=max(bid_list)
position=bid_list.index(max_bid)
print(f"The winner is {bidder_list[position]} ith a bid of ${max_bid}.")

    

