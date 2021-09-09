# -*- coding: utf-8 -*-

# https://programmers.co.kr/learn/courses/30/lessons/72411
from itertools import combinations
from collections import Counter


def solution(orders, course):
	answer = []

	for c in course:
		allcomb = []
		for order in orders:
			comb = combinations(sorted(list(order)), c)
			allcomb += comb
		
		if len(allcomb) == 0:
			continue
		counter = Counter(allcomb).most_common()
		maxc = counter[0][1]
		if maxc >= 2:
			answer.append(''.join(counter[0][0]))
			for i in range(1, len(counter)):
				if counter[i][1] != maxc:
					break
				answer.append(''.join(counter[i][0]))
	
	answer.sort()
	return answer

#orders, course = ["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2,3,4]
#orders, course = ["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"], [2,3,5]
orders, course = ["XYZ", "XWY", "WXA"], [2,3,4]	

solution(orders, course)