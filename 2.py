def findMaxProfit(numOfPredictedTimes, predictedSharePrices):
    # Participants code will be here
    answ = []
    for i in predictedSharePrices:
        ans = numOfPredictedTimes * i
        answ.append(ans)
        x  = max(answ)
    return x

def main():
    line = input().split()
    numOfPredictedTimes = int(line[0])
    predictedSharePrices = list(map(int, line[1:]))

    answer = findMaxProfit(numOfPredictedTimes, predictedSharePrices)
    # Do not remove below line
    print(answer)
    # Do not print anything after this line

if __name__ == '__main__':
    main() 