number_list = [x for x in range(20) if x % 2 ==0]
print(number_list)

number_list = [y for y in range(100) if y % 2 ==0 if y % 5==0]
print(number_list)

obj= ["Even" if i%2==0 else "Odd" for i in range(10)]
print(obj)

matrix= [[1,2], [3,4], [5,6], [7,8]]
transpose= [[row [i] for row in matrix] for i in range(2)]
print(transpose)