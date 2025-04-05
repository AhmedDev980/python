if __name__ == '__main__':
  n = int(input())  # provide the total number of students
  student_marks = {} # dictonary to create names and marks of students
  for i in range(n):
    name, *line = input().split() # split the whole input like name as one and other line as one 
    scores = list(map(float, line)) # Here we gave the remaining line from above so that it will convert string scores to floating point numbers
    student_marks[name] = scores # student_marks is updated with the student's name as the key and their scores as the value.
  student_name = input() # we will give input as name of student
  l1 = list(student_marks[student_name])
  addition = sum(l1)
  result = addition/len(l1)
  print("%.2f" % result) # % is used for string formatting
  
