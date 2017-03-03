# @Ninj0r

array = [1,2,3,4,5,5,5,6,7,7,7,9,9];
modeInts = [];
trackedInt = array[0];
trackedCount = 1;
maxCount = 0;
for i in range(1,len(array)):
    currInt = array[i];
    if currInt == trackedInt:
        trackedCount += 1;
    else:
        if trackedCount > maxCount:
            maxCount = trackedCount;
            modeInts.clear();
            modeInts.append(trackedInt);
        elif trackedCount == maxCount:
            modeInts.append(trackedInt);
        
        trackedCount = 1;
        trackedInt = currInt;

for a in modeInts:
    print(a);

