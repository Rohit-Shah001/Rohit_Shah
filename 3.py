def find_min_days(prices, profit):
    # Participants code will be here
    l = []
    for i in profit:
        for j in prices:
            pr = i/j
            l.append(pr)
    ma = max(l)        
    return ma

n, d = map(int, input().split())
prices = list(map(int, input().split()))
profit = list()
for i in range(d):
    profit.append(int(input().strip()))
answer = find_min_days(prices,profit)
# Do not remove below line
print(answer)
# Do not print anything after this line 