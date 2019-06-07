if __name__ == '__main__':
    n = int(raw_input())
    student_marks = {}
    for _ in range(n):
        line = raw_input().split()
        name, scores = line[0], line[1:]
        scores = map(float, scores)
        student_marks[name] = scores
    query_name = raw_input()

#for i in range(n): **This section isn't working for some reason**
 #   if query_name == line[i]:
  #      a = sum(scores)
   #     b = a/len(scores)
    #    print ("%.2f" %round(b, 2))

query_scores = student_marks[query_name]
print("{0:.2f}".format(sum(query_scores)/(len(query_scores))))
