# -*- coding: utf-8 -*-

# https://programmers.co.kr/learn/courses/30/lessons/72411
from itertools import combinations
import operator


def solution(orders, course):
	answer = []
	menu = []
	
	for order in orders:
		for m in order:
			if m in menu:
				pass
			else:
				menu.append(m)
	
	menu.sort()
	
	for c in course:
		comb_stats = {}
		combs = list(combinations(menu, c)) # 코스 메뉴 수만큼의 조합
		for comb in combs:
			comb_stats[comb] = 0
			for order in orders:
				ex_flag = False
				for i in comb:
					if i in order:
						ex_flag = True
					else:
						ex_flag = False
						break
				if ex_flag == True:
					comb_stats[comb] += 1

		comb_stats = sorted(comb_stats.items(), key=operator.itemgetter(1), reverse=True)
		comb_max = comb_stats[0][1]
		if comb_max >= 2:
			for comb in comb_stats:
				if comb[1] != comb_max:
					break
				answer.append(''.join(comb[0]))
	
	answer.sort()
	return answer

#orders, course = ["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2,3,4]
orders, course = ["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"], [2,3,5]
#orders, course = ["XYZ", "XWY", "WXA"], [2,3,4]	

solution(orders, course)