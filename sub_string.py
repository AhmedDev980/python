def count_substring(string, sub_string):
  total = 0
  for i in range(len(string)):
    if string[i:len(string)].startswith(sub_string):
      total += 1
    return total

if __name__ = '__main__':
  string = input().strip()
  sub_string = input().strip()
  count = count_substring(string, sub_string)
  print(count)

# INPUT
# ABCDCDC
#CDC
#OUTPUT
#2
#CDC is substring which came 2 time from left side of  string CDCCDC came 2 times
  
