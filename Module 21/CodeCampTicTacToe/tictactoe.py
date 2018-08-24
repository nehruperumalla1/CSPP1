# def checking_win(sett):

def game_play(game):
	x = 'x'
	o = 'o'
	xcount = 0
	ocount = 0
	countt = 0
	for index in game:
		# print("Invalid")
		if len(index) != 3:
			# print("Invalid")
			return "invalid game"
		if x in index:
			xcount += index.count(x)
		if o in index:
			ocount += index.count(o)
		if '.' in index:
			countt += index.count('.')
	if xcount+ocount+countt != 9:
		return "invalid input"
	if abs(xcount - ocount) != 1:
		return "invalid game"
	else:
		set1 = set()
		set2 = set()
		set3 = set()
		set4 = set()
		set5 = set()
		for i in range(len(game)):
			for j in range(len(game[i])):
				if i == j:
					set1.add(game[i][j])
				if i + j == (len(game)-1):
					set2.add(game[i][j])
				sett = set(game[i])
				if len(sett) == 1:
					if 'x' in sett:
						return 'x'
					return 'o'
				if j == 0:
					set3.add(game[i][j])
				if j == 1:
					set4.add(game[i][j])
				if j == 2:
					set5.add(game[i][j])


		if len(set1) == 1:
			if 'x' in set1:
				return 'x'
			return 'o'
		if len(set2) == 1:
			if 'x' in set2:
				return 'x'
			return 'o'
		if len(set3) == 1:
			if 'x' in set3:
				return 'x'
			return 'o'
		if len(set4) == 1:
			if 'x' in set4:
				return 'x'
			return 'o'
		if len(set5) == 1:
			if 'x' in set5:
				return 'x'
			return 'o'
		return "draw"
def main():

	row = []
	for index in range(3):
		column = input()
		column = list(map(str, column.split(' ')))
		row.append(column)
	row = game_play(row)
	print(row)
if __name__ == '__main__':
	main()





