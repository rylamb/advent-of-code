#!/usr/bin/env python3

import requests
import sys

from collections import Counter

COOKIE = sys.argv[1]
YEAR = '2024'
DAY = '1'

def get_input():
    req = requests.get(f'https://adventofcode.com/{YEAR}/day/{DAY}/input',
                       headers={'cookie':'session=' + COOKIE})
    return req.text.strip()

def get_example(offset=0):
    req = requests.get(f'https://adventofcode.com/{YEAR}/day/{DAY}',
                       headers={'cookie':'session='+ COOKIE})
    return req.text.split('<pre><code>')[offset+1].split('</code></pre>')[0].strip()


if __name__ == "__main__":
    left = []
    right = []
    if len(sys.argv) > 2 and sys.argv[2] == "example":
        for item in get_example().splitlines():
            row = item.split("   ")
            left.append(int(row[0]))
            right.append(int(row[1]))
    else:
        for item in get_input().splitlines():
            row = item.split("   ")
            left.append(int(row[0]))
            right.append(int(row[1]))

    left.sort()
    right.sort()
    
    dist_counter = 0
    idx = 0
    while idx < len(left):
        dist_counter += abs(left[idx] - right[idx])
        idx += 1
    print(f'Part 1: {dist_counter}')

    r_counted = Counter(right)
    similarity = sum([item * r_counted.get(item, 0) for item in left])
    print(f'Part 2: {similarity}')