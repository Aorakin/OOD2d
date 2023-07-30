allBid = input("Enter All Bid : ").split(' ')
allBid = list(map(int,allBid))
maxBid = max(allBid)
if allBid.count(maxBid)>1:
    print("error : have more than one highest bid")
elif len(allBid)<=1:
    print("not enough bidder")
else :
    allBid.remove(maxBid)
    print(f'winner bid is {maxBid} need to pay {max(allBid)}')

