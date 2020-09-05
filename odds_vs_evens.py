def odds_vs_evens(num):
    odds = []
    evens = []

    for digit in list(str(num)):
        if int(digit) % 2 == 0:
            evens.append(int(digit))
        else:
            odds.append(int(digit))
            
    if sum(odds) > sum(evens):
        return "odd"
    elif sum(odds) < sum(evens):
        return "even"
    else:
        return "equal"

print(odds_vs_evens(412420))
