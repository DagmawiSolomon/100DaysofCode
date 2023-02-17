bids = [

]

is_true = True
while is_true:
    name = input("What's is your name: ")
    bid = input("What's your bid: $ ")
    continue_prompt = input("Are there any other bidders? Type 'yes' or 'no'. ").lower()

    def bid_logic(bidder, bid_ammout,list):
        list.append(
            {
                "name": bidder,
                "bid": int(bid_ammout),
            }
        )
    if continue_prompt == "no":
        is_true = False

    bid_logic(name, bid, bids)

num = 0
index = 0
for i in range(0, len(bids)):
    if num < bids[i]["bid"]:
       num = bids[i]["bid"]
       index = i

name = bids[index]["name"]
print(f"Winner is {name}" )
