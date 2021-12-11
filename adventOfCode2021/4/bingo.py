
def parseBoard(lines):
	rows = []
	cols = [set(), set(), set(), set(), set()]

	for line in lines:
		l = list(map(int, line.split()))
		rows.append(set(l)) # the easy way
		for i in range(5):
			cols[i].add(l[i])
	return (rows, cols)

def determineScore(board, drawn):
	myNumbers = set()
	for rc in board:
		myNumbers.update(rc)
	unmarkedNumbers = myNumbers.difference(set(drawn))
	score = sum(list(unmarkedNumbers))
	score *= drawn[-1]
	return score
		


f = open("adventOfCode2021/4/input.txt", 'r')

line = f.readline().rstrip()
drawNumbers = list(map(int, line.split(sep=',')))

# parse all boards into row and col sets
boards = []
lines = []
for line in f:
	line = line.rstrip()
	if len(line) != 0:
		lines.append(line)

	if len(lines) == 5:
		boards.append(parseBoard(lines))
		lines.clear()

f.close()

# find a winner
numDrawn = 5
lastWinIdx = 0
winners = []
win = False
while numDrawn < len(drawNumbers):
	drawn = set(drawNumbers[0:numDrawn])

	for board in boards:
		rows, cols = board

		for row in rows:
			if row.issubset(drawn):
				print(determineScore(rows, drawNumbers[0:numDrawn]))
				#exit()
				winners.append(board)
				lastWinIdx = numDrawn
				win = True
				break

		if win:
			continue


		for col in cols:
			if col.issubset(drawn):
				print(determineScore(cols, drawNumbers[0:numDrawn]))
				#print('winner is cols: ')
				#print(cols)
				#exit()
				winners.append(board)
				lastWinIdx = numDrawn
				win = True
				break

	if win:
		i = boards.index(winners[-1])
		boards.pop(i)
		win = False

	numDrawn += 1
			
	
print(determineScore(winners[-1][0], drawNumbers[0:lastWinIdx]))
