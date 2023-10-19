#!/bin/python3

import math
import os
import random
import re
import sys
import requests


#
# Complete the 'getWinnerTotalGoals' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING competition
#  2. INTEGER year
#

def getWinnerTotalGoals(competition, year):
    # Write your code here
    winner_total_goals = 0
    winner = \
    requests.get(f"https://jsonmock.hackerrank.com/api/football_competitions?name={competition}&year={year}").json()[
        'data'][0]['winner']
    res = requests.get(
        f"https://jsonmock.hackerrank.com/api/football_matches?competition={competition}&year={year}&team1={winner}").json()
    total_page = res['total_pages']
    for page in range(1, total_page + 1):
        winner_as_team1 = requests.get(
            f"https://jsonmock.hackerrank.com/api/football_matches?competition={competition}&year={year}&team1={winner}&page={page}").json()[
            'data']
        for i in range(len(winner_as_team1)):
            winner_total_goals += int(winner_as_team1[i]['team1goals'])
        winner_as_team2 = requests.get(
            f"https://jsonmock.hackerrank.com/api/football_matches?competition={competition}&year={year}&team2={winner}&page={page}").json()[
            'data']
        for i in range(len(winner_as_team2)):
            winner_total_goals += int(winner_as_team2[i]['team2goals'])
    return winner_total_goals


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    competition = input()

    year = int(input().strip())

    result = getWinnerTotalGoals(competition, year)

    fptr.write(str(result) + '\n')

    fptr.close()
