# -*- coding: utf-8 -*-

# 2021.5.16 풀이
# https://programmers.co.kr/learn/courses/30/lessons/60058

def uvmaker(w):
	br1, br2 = 0, 0
	for i in range(len(w)):
		if w[i] == '(':
			br1 += 1
		elif w[i] == ')':
			br2 += 1
		if br1 == br2:
			return w[:i+1], w[i+1:]	# u, v

def isbalanced(w):
	stack_balance = []

	for i in range(len(w)):
		if w[i] == '(':
			stack_balance.append(w[i])
		elif w[i] == ')':
			if len(stack_balance) != 0:
				stack_balance.pop()
			else:
				return False
	if len(stack_balance) == 0:
		return True
	else:
		return False

def solution(p):
	if len(p) == 0:
		return p

	u, v = uvmaker(p)

	if isbalanced(u):
		return u + solution(v)
	else:
		tmp = '(' + solution(v) + ')'
		for i in range(1,len(u)-1):
			if u[i] == '(':
				tmp += ')'
			elif u[i] == ')':
				tmp += '('
		return tmp

print(solution("(()())()"))
print(solution(")("))
print(solution("()))((()"))
# 1. 균형잡힌 괄호 문자열: 
# 2. 올바른 괄호 문자열