#!/bin/python3

import math
import os
import random
import re
import sys
import requests


#
# Complete the 'getNumDraws' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER year as parameter.
#

def getNumDraws(year):
    # Write your code here
    num_draws = 0
    for score in range(0, 11):
        res = requests.get(
            f"https://jsonmock.hackerrank.com/api/football_matches?year={year}&team1goals={score}&team2goals={score}").json()
        num_draws += res['total']
    return num_draws


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    year = int(input().strip())

    result = getNumDraws(year)

    fptr.write(str(result) + '\n')

    fptr.close()
