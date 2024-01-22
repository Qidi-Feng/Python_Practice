if __name__ == '__main__':
	results = []
	score_total = []
	for _ in range(int(raw_input())):
		name = raw_input()
		score = float(raw_input())
		results.append([name,score])       ##use nested list
		score_total.append(score)

	ans = sorted(set(score_total))[1]		##use sorted(set()) to get sorted unique list
	for a,c in sorted(results):			##loop a nested list
		if c==ans:
			print(a)
