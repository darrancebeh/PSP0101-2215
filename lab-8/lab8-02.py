def getMean(set):
    total = 0.00;
    for n in set:
        total += n;
    return(total/len(set))

def getVariance(set, mean):
    dev = 0.00;
    for n in set:
        dev += ((n-mean)*(n-mean));
    return((1/len(set))*dev);

a = 0;
numset = [];
while (a >= 0):
    a = float(input("Enter quiz mark: "));
    if(a >= 0):
        numset.append(a);

mean = getMean(numset);
print(f"Mean: {mean}");
print(f"Variance: {getVariance(numset, mean)} ")