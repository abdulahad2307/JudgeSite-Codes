import os
import sys

#
# Complete the simpleArraySum function below.
#
def simpleArraySum(ar):
    s = 0
    
    for i in range(0,len(ar)):
        s = s + ar[i]
    return s


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ar_count = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = simpleArraySum(ar)

    fptr.write(str(result) + '\n')

    fptr.close()