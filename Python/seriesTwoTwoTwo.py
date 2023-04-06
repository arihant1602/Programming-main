def series(n):
    problem = ""
    for i in range(1,n+1):
        problem += ("2"*i) + "+" 
    problem = problem[:-1]
    arr = problem.split("+")
    summ = 0
    for i in arr:
        summ += int(i)
    print(problem, "=", summ)
    

series(4)