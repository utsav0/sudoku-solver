#import time
#initial_time = time.time()

sudoku =    [[0, 0, 0, 2, 6, 0, 7, 0, 1], 
            [6, 8, 0, 0, 7, 0, 0, 9, 0], 
            [1, 9, 0, 0, 0, 4, 5, 0, 0], 
            [8, 2, 0, 1, 0, 0, 0, 4, 0], 
            [0, 0, 4, 6, 0, 2, 9, 0, 0], 
            [0, 5, 0, 0, 0, 3, 0, 2, 8], 
            [0, 0, 9, 3, 0, 0, 0, 7, 4], 
            [0, 4, 0, 0, 5, 0, 0, 3, 6], 
            [7, 0, 3, 0, 1, 8, 0, 0, 0]]
print("This is the Unsolved Sudoku :",end="\n\n")
for i1 in sudoku:
		count = 1
		for j1 in i1 :
				if count == 3 or count ==6 or count ==9:
					print(str(j1),end = " | ")
				elif count == 1:
					print("|",str(j1), end = " ")
				else:
					print(str(j1),end = " ")
				count += 1
		print ("")
		if sudoku.index(i1) ==2 or sudoku.index(i1) ==5 :		print("_________________________")
def find(ind,j,count):
	lst = [1,2,3,4,5,6,7,8,9]
	lst1 = []
	lst2 = []
	lst3 = []
	emlst = []
	#condition  for first box in first line
	if count< 3:
		if ind < 3:
			#checking in the row
			for i in lst:
				if i not in sudoku[ind]:
					lst1.append(i)
				#checking the num in column
			for i in lst1:
				for j in range (9):
					if i == sudoku[j][count]:
						break
				else:
						lst2.append(i)
				#checking the num in box
			for j in range (3):
							for k in range(3):
								emlst.append(sudoku[j][k])
			for i in lst2:
									if i not in emlst:
										lst3.append(i)
			if len(lst3)==1:
				sudoku[ind][count] = lst3[0]
		#condition for first box in second line					
		elif ind < 6 and ind >2 :
			#checking in the row
			for i in lst:
				if i not in sudoku[ind]:
					lst1.append(i)
				#checking the num in column
			for i in lst1:
					for j in range (9):
						if i == sudoku[j][count]:
							break
					else:
							lst2.append(i)
				#checking the num in box
			for j in range (3,6):
							for k in range(3):
								emlst.append(sudoku[j][k])
			for i in lst2:
									if i not in emlst:
										lst3.append(i)
			if len(lst3)==1:
				sudoku[ind][count] = lst3[0]
		#condition for first box in third line
		elif ind >5:
				#checking in the row
			for i in lst:
				if i not in sudoku[ind]:
					lst1.append(i)
				#checking the num in column
			for i in lst1:
					for j in range (9):
						if i == sudoku[j][count]:
							break
					else:
							lst2.append(i)
				#checking the num in box
			for j in range (6,9):
							for k in range(3):
								emlst.append(sudoku[j][k])
			for i in lst2:
									if i not in emlst:
										lst3.append(i)
			if len(lst3)==1:
				sudoku[ind][count] = lst3[0]
	elif count < 6 and count > 2:
		#condition for second box first line
		if ind < 3:
				#checking in the row
			for i in lst:
				if i not in sudoku[ind]:
					lst1.append(i)
				#checking the num in column
			for i in lst1:
					for j in range (9):
						if i == sudoku[j][count]:
							break
					else:
							lst2.append(i)
				#checking the num in box
			for j in range (3):
							for k in range(3,6):
								emlst.append(sudoku[j][k])
			for i in lst2:
									if i not in emlst:
										lst3.append(i)
			if len(lst3)==1:
				sudoku[ind][count] = lst3[0]
		#condition for second box second line
		elif ind < 6 and ind >2 :
			for i in lst:
				if i not in sudoku[ind]:
					lst1.append(i)
				#checking the num in column
			for i in lst1:
					for j in range (9):
						if i == sudoku[j][count]:
							break
					else:
							lst2.append(i)
				#checking the num in box
			for j in range (3,6):
							for k in range(3,6):
								emlst.append(sudoku[j][k])
			for i in lst2:
									if i not in emlst:
										lst3.append(i)
			if len(lst3)==1:
				sudoku[ind][count] = lst3[0]
		#condition for second box third line
		elif ind > 5:
			for i in lst:
				if i not in sudoku[ind]:
					lst1.append(i)
				#checking the num in column
			for i in lst1:
					for j in range (9):
						if i == sudoku[j][count]:
							break
					else:
							lst2.append(i)
				#checking the num in box
			for j in range (6,9):
							for k in range(3,6):
								emlst.append(sudoku[j][k])
			for i in lst2:
									if i not in emlst:
										lst3.append(i)
			if len(lst3)==1:
				sudoku[ind][count] = lst3[0]
	elif count > 5:
		#condition for third box first line
		if ind < 3:
			for i in lst:
				if i not in sudoku[ind]:
					lst1.append(i)
				#checking the num in column
			for i in lst1:
					for j in range (9):
						if i == sudoku[j][count]:
							break
					else:
							lst2.append(i)
				#checking the num in box
			for j in range (3):
							for k in range(6,9):
								emlst.append(sudoku[j][k])
			for i in lst2:
									if i not in emlst:
										lst3.append(i)
			if len(lst3)==1:
				sudoku[ind][count] = lst3[0]
		#condition for third box second line
		elif ind < 6 and ind > 2:
			for i in lst:
				if i not in sudoku[ind]:
					lst1.append(i)
				#checking the num in column
			for i in lst1:
					for j in range (9):
						if i == sudoku[j][count]:
							break
					else:
							lst2.append(i)
				#checking the num in box
			for j in range (3,6):
							for k in range(6,9):
								emlst.append(sudoku[j][k])
			for i in lst2:
									if i not in emlst:
										lst3.append(i)
			if len(lst3)==1:
				sudoku[ind][count] = lst3[0]
		#condition for third box third line
		elif ind > 5:
			for i in lst:
				if i not in sudoku[ind]:
					lst1.append(i)
				#checking the num in column
			for i in lst1:
					for j in range (9):
						if i == sudoku[j][count]:
							break
					else:
							lst2.append(i)
				#checking the num in box
			for j in range (6,9):
							for k in range(6,9):
								emlst.append(sudoku[j][k])
			for i in lst2:
									if i not in emlst:
										lst3.append(i)
			if len(lst3)==1:
				sudoku[ind][count] = lst3[0]

def whole():
			for element in sudoku:
				count1 = 0
				for subelement in element:
					if subelement == 0:
					 ind= sudoku.index(element)
					 find(ind, subelement, count1)
					count1 +=1
		#	print("one round complete")
whole()
#making the sudoku looks real .
def show():
	print("\n\nTHe Best Solution We Can Provide Is : \n ")
	for i2 in sudoku:
		count = 1
		for j2 in i2 :
				if count == 3 or count ==6 or count ==9:
					print(str(j2),end = " | ")
				elif count == 1:
					print("|",str(j2), end = " ")
				else:
					print(str(j2),end = " ")
				count += 1
		print ("")
		if sudoku.index(i2) ==2 or sudoku.index(i2) ==5:
			print("_________________________")
def answer ():
	for i in range (81):
		for i in range(9):
			for j in range(9):
				if sudoku[i][j] == 0:
					whole()
	show()
answer()
#print ("this is total time taken :",time.time()-initial_time)