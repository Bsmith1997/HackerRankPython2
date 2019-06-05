students = []
N = int(raw_input())

for _ in range(N):
    name = raw_input()
    score = float(raw_input())
    students.append([name, score]) 

students.sort(key=lambda student: (student[1], student[0])) 

scores = set([students[x][1] for x in range(N)]) #Creates a set of just the scores from the students list 
scores = list(scores) #converts into a list
scores.sort() #Sorts it so the second smallest is easily accesible 

students = [x[0] for x in students if x[1] == scores[1]] #Now if the student's score is equal to the second smallest score, their name is added to the students list
students.sort() #Sort them so they print alphabetically 

for s in students: # print the result 
    print s
