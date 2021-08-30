# -*- coding: utf-8 -*-

# https://programmers.co.kr/learn/courses/30/lessons/72411
import operator

def countcomb(menulist, count):


def solution(orders, course):
	answer = []
	menuStats = {}	# 메뉴 통계

	for order in orders:
		for menu in order:
			if menuStats.get(menu):
				menuStats[menu] += 1
			else:
				menuStats[menu] = 1
	
	menuStats_sorted = sorted(menuStats.items(), key=operator.itemgetter(1), reverse=True)
	print(menuStats_sorted)

	for count in course:
		countcomb(menuStats_sorted, count)


	return answer

orders, course = ["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2,3,4]
#orders, course = ["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"], course = [2,3,5]
#orders, course = ["XYZ", "XWY", "WXA"], [2,3,4]	

solution(orders, course)