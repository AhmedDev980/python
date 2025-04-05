# python
https://github.com/iam-veeramalla/python-for-devops

To convert the input into list we will use split()
EX:
folders = input("Enter the list of files in the folder:" ).split()
print(folders)


To get the runner up score we will use print(scores[-2]). Because it is 10, 15, 20. Then we want to find the second highest. So we will use sorted then it will arrange the numbers in ascending order then if we give [-2] we will get the second highest. 

To get the second lowest we will use sorted first so that it will arrange scores in ascending order then we will give (1) to get the second element which is second lowest
# alist.append([name, score])
# second_highest = sorted(set([score for name, score in alist]))[1]
# print('\n'.join(sorted([name for name, score in alist if score == second_highest])))


# .strip()
Used to remove extra spaces eg: "  hi " after giving .strip() output will be "hi"
#
a//b division which give round figure as reminder. EG: 9//2=4
a/b division which gives float figure as reminder. EG: 9/2=4.22
#
print(i, end='')
This prints the value of i on each iteration of the loop.

end='':

By default, print() adds a newline (\n) after printing, but with end='', you are telling Python not to add a newline. Instead, it will print everything on the same line. eg: 123

If end=' ' was used, Python would print a space after each number. eg: 1 2 3

