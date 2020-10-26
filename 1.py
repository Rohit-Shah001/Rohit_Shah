import sys
# You may change this function parameters
def findMaxProfit(numOfPredictedDay, predictedSharePrices):
    # Participants code will be here
    l = []
    for i in predictedSharePrices:
        ans = numOfPredictedDay * i
        l.append(ans)
    x = max(l)
    return x

def main():
    line = input().split()
    numOfPredictedDay = int(line[0])
    predictedSharePrices = list(map(int, line[1:]))

    answer = findMaxProfit(numOfPredictedDay, predictedSharePrices)

    # Please do not remove the below line.
    print(answer)
    # Do not print anything after this line

if __name__ == '__main__':
    main()