#Say "Hello, World! With Python"
if __name__ == '__main__':
    print("Hello, World!")

#Python If-Else
import math
import os
import random
import re
import sys

if __name__ == '__main__':
    n = int(input().strip())
    assert n >= 1 and n <= 100
    if n % 2 == 0:
        if (n >= 2 and n <= 5) or (n > 20):
            print("Not ", end = "")
    print("Weird")

#Arithmetic Operators
if __name__ == '__main__':
    a = int(input())
    b = int(input())
    
    s = a + b
    dif = a - b
    prod = a * b
    
    print(s)
    print(dif)
    print(prod)

#Python: Division
if __name__ == '__main__':
    a = int(input())
    b = int(input())
    
    int_div = a // b
    float_div = a / b
    
    print(int_div)
    print(float_div)

#Loops
if __name__ == '__main__':
    n = int(input())
    
    for i in range(n):
        print(i**2)

#Write a function
def is_leap(year):
    leap = False
    
    # Write your logic here
    div4 = year % 4 == 0
    div100 = year % 100 == 0
    div400 = year % 400 == 0
    
    if div4:
        leap = True
        if div100:
            if div400:
                leap = True
            else:
                leap = False
        else:
            leap = True
    
    return leap

year = int(input())
print(is_leap(year))

#Print Function
if __name__ == '__main__':
    n = int(input())
    for i in range(1, n + 1):
        print(i, end = "")

#List Comprehensions
if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    
    perm = [[i, j, k] for i in range(x + 1) for j in range(y+1) for k in range(z + 1)
    if i + j + k != n]
    
    print(perm)

#Find the Runner-Up Score!
if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    scores = list(set(arr))
    scores.sort()
    sz = len(scores)
    print(scores[sz - 2])

#Nested Lists
if __name__ == '__main__':
    records = []
    scores = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        records.append([name, score])
        scores.append(score)
    scores = list(set(scores))
    scores = sorted(scores)
    sz = len(scores)
    sec_low_grade = scores[1]
    
    names = []
    for r in records:
        if r[1] == sec_low_grade:
            names.append(r[0])
    
    names = sorted(names)
    
    for name in names:
        print(name)

#Finding the percentage
if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    
    marks = student_marks[query_name]
    
    print(format(sum(marks) / len(marks), ".2f"))

#Lists
if __name__ == '__main__':
    N = int(input())
    l = []
    for i in range(N):
        command = input().split()
        if command[0] == "insert":
            i = command[1]
            e = command[2]
            l.insert(int(i), int(e))
        elif command[0] == "print":
            print(l)
        elif command[0] == "remove":
            e = command[1]
            l.remove(int(e))
        elif command[0] == "append":
            e = command[1]
            l.append(int(e))
        elif command[0] == "sort":
            l = sorted(l)
        elif command[0] == "pop":
            l.pop()
        elif command[0] == "reverse":
            l.reverse()

#Tuples
if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    integer_list = list(integer_list)
    
    print(hash(tuple(integer_list)))

#sWAP cASE
def swap_case(s):
    new_str = ""
    for l in s:
        if l.isupper():
            new_str += l.lower()
        else:
            new_str += l.upper()
    return new_str

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)

#String Split and Join
def split_and_join(line):
    # write your code here
    line = line.split()
    line = "-".join(line)
    return line

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)

#What's Your Name?
#
# Complete the 'print_full_name' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING first
#  2. STRING last
#

def print_full_name(first, last):
    # Write your code here
    a = "Hello "
    b = "! You just delved into python."
    
    print(a + first + " " + last + b)

if __name__ == '__main__':
    first_name = input()
    last_name = input()
    print_full_name(first_name, last_name)

#Mutations
def mutate_string(string, position, character):
    return string[0 : position] + character + string[position + 1 : ]

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)

#Find a string
def count_substring(string, sub_string):
    sz = len(string)
    n = len(sub_string)
    s = 0
    i = 0
    while(i < sz - n + 1):
        if string[i : i + n] == sub_string:
            s += 1
        i += 1
    return s

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)

#String Validators
if __name__ == '__main__':
    s = input()
    
    v = [False, False, False, False, False]
    
    alnum_found = False
    alpha_found = False
    digit_found = False
    lower_found = False
    upper_found = False
    
    for l in s:
        if not alnum_found and l.isalnum():
            v[0] = True
            alnum_found = True
        if not alpha_found and l.isalpha():
            v[1] = True
            alpha_found = True
        if not digit_found and l.isdigit():
            v[2] = True
            digit_found = True
        if not lower_found and l.islower():
            v[3] = True
            lower_found = True
        if not upper_found and l.isupper():
            v[4] = True
            upper_found = True
    
    for elem in v:
        print(elem)

#Text Alignment
# Enter your code here. Read input from STDIN. Print output to STDOUT

n = int(input())
s = 'H'

spaces_top = 2*n - 1
j = 1
for i in range(n):
    print((s*j).center(spaces_top))
    j = j + 2

for i in range(n + 1):
    print((s*n).center(n*2)+(s*n).center(n*6))
    
for i in range((n + 1) // 2):
    print((n*5*s).center(n*6))
    
for i in range(n + 1):
    print((s*n).center(n*2)+(s*n).center(n*6))

j = 2*n - 1
for i in range(n, 0, -1):
    print(4*n*" " + (s*j).center(spaces_top))
    j = j - 2

#Text Wrap
import textwrap

def wrap(string, max_width):
    text_wrap = textwrap.TextWrapper(width=max_width) 
    string = text_wrap.fill(text=string) 
    return string

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)

#Designer Door Mat
# Enter your code here. Read input from STDIN. Print output to STDOUT

n, m = input().split()
n, m = int(n), int(m)

welcome = "WELCOME".center(m, '-')
base = ".|."

for i in range(1, n, 2):
    print((i*base).center(m, '-'))

print(welcome)

for j in range(i, 0, -2):
    print((j*base).center(m, '-'))

#String Formatting
def print_formatted(number):
    # your code goes here
    
    size = len(bin(number)[2:])
    
    for i in range(1, number + 1):
        print(str(i).rjust(size), oct(i)[2:].rjust(size), hex(i)[2:].rjust(size).upper(), bin(i)[2:].rjust(size))
    

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)

#Alphabet Rangoli
import string
def print_rangoli(size):
    # your code goes here
    rows = []
    
    alph = list(string.ascii_lowercase)[0:size]
    
    for i in range(size):
        let = alph[- (i + 1): ]
        row = let[ : : -1] + let[1 : ]
        disp = "-".join(row).center(n*4-3, "-")
        rows.append(disp)
        print("-".join(row).center(n*4-3, "-"))
    
    for i in range(size - 2, -1, -1):
        print(rows[i])
    
if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)

#Capitalize
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    s = list(s.split(" "))
    w=""
    for elem in s:
        w = w + str(elem.capitalize()) + " "
    return w
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()

#The Minion Game
def minion_game(string):
    
    v, c = 0, 0
     
    for i in range(len(string)):
        if string[i] in 'AEIOU':
           v += (len(string) - i)
        else:
           c += (len(string) - i)
                
    winner = max(v, c)
    
    if winner == v and winner == c:
        print("Draw")
    elif winner == c:
        print("Stuart", str(c))
    elif winner == v:
        print("Kevin", str(v))

if __name__ == '__main__':
    s = input()
    minion_game(s)

#Merge the Tools!
def merge_the_tools(string, k):
    # your code goes here
    i = 0
    for _ in range(int(len(string)/k)):
        w = string[i:i + k]
        i = i + k
        s = ""
        for c in w:
            if not c in s:
                s = s + c
        print(s)

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)

#Introduction to Sets
def average(array):
    # your code goes here
    return format(sum(set(array)) / len(set(array)), ".3f")
    
    
if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)

#No Idea!
# Enter your code here. Read input from STDIN. Print output to STDOUT

nm = input().split()
n = int(nm[0])
m = int(nm[1])

arr = input().split()
arr = [int(elem) for elem in arr]

A = input().split()
A = [int(elem) for elem in A]
A = set(A)
B = input().split()
B = [int(elem) for elem in B]
B = set(B)

s = 0

for elem in arr:
    if elem in A:
        s += 1
    if elem in B:
        s -= 1
print(s)

#Symmetric Difference
# Enter your code here. Read input from STDIN. Print output to STDOUT

n = int(input())
N = input().split()
N = [int(elem) for elem in N]
N = set(N)

m = int(input())
M = input().split()
M = [int(elem) for elem in M]
M = set(M)

set1 = N - M
set2 = M - N
union = set1.union(set2)
union = list(union)
union.sort()

for elem in union:
    print(elem)

#Set.add()
# Enter your code here. Read input from STDIN. Print output to STDOUT

n = int(input())
s = set()

for _ in range(n):
    s.add(str(input()))
print(len(s))

#Set .discard(), .remove() & .pop()
n = int(input())
s = input().split()
s = [int(elem) for elem in s]
s = set(s)
N = int(input())

for _ in range(N):
    c = input().split()
    
    if c[0] == "pop":
        s.pop()
    elif c[0] == "remove":
        s.remove(int(c[1]))
    elif c[0] == "discard":
        s.discard(int(c[1]))
print(sum(s))

#Set .union() Operation
# Enter your code here. Read input from STDIN. Print output to STDOUT

n_eng = int(input())
eng = list(input().split())
eng = [int(elem) for elem in eng]
eng = set(eng)

n_fr = int(input())
fr = list(input().split())
fr = [int(elem) for elem in fr]
fr = set(fr)

print(len(fr.union(eng)))

#Set .intersection() Operation
# Enter your code here. Read input from STDIN. Print output to STDOUT

n_eng = int(input())
eng = list(input().split())
eng = [int(elem) for elem in eng]
eng = set(eng)

n_fr = int(input())
fr = list(input().split())
fr = [int(elem) for elem in fr]
fr = set(fr)

print(len(fr.intersection(eng)))

#Set .difference() Operation
# Enter your code here. Read input from STDIN. Print output to STDOUT

n_eng = int(input())
eng = list(input().split())
eng = [int(elem) for elem in eng]
eng = set(eng)

n_fr = int(input())
fr = list(input().split())
fr = [int(elem) for elem in fr]
fr = set(fr)

print(len(eng - fr))

#Set .symmetric_difference() Operation
# Enter your code here. Read input from STDIN. Print output to STDOUT

n_eng = int(input())
eng = list(input().split())
eng = [int(elem) for elem in eng]
eng = set(eng)

n_fr = int(input())
fr = list(input().split())
fr = [int(elem) for elem in fr]
fr = set(fr)

print(len(eng ^ fr))

#Set Mutations
# Enter your code here. Read input from STDIN. Print output to STDOUT

n_set = int(input())
A = list(input().split())
A = [int(elem) for elem in A]
A = set(A)

N = int(input())

for _ in range(N):
    com = input().split()
    
    if com[0] == "intersection_update":
        n = com[1]
        B = list(input().split())
        B = [int(elem) for elem in B]
        B = set(B)
        A.intersection_update(B)
    elif com[0] == "update":
        n = com[1]
        B = list(input().split())
        B = [int(elem) for elem in B]
        B = set(B)
        A.update(B)
    elif com[0] == "symmetric_difference_update":
        n = com[1]
        B = list(input().split())
        B = [int(elem) for elem in B]
        B = set(B)
        A.symmetric_difference_update(B)
    elif com[0] == "difference_update":
        n = com[1]
        B = list(input().split())
        B = [int(elem) for elem in B]
        B = set(B)
        A.difference_update(B)
print(sum(A))

#The Captain's Room
# Enter your code here. Read input from STDIN. Print output to STDOUT

K = int(input())

rooms = list(input().split())
rooms = [int(elem) for elem in rooms]

rooms_distinct = set(rooms)

s_distinct = sum(rooms_distinct)*K
s_total = sum(rooms)

print(int((s_distinct - s_total)/(K - 1)))

#Check Subset
# Enter your code here. Read input from STDIN. Print output to STDOUT

def read_set():
    A = list(input().split())
    A = [int(elem) for elem in A]
    A = set(A)
    return A

T = int(input())

for _ in range(T):
    nA = int(input())
    A = read_set()
    nB = int(input())
    B = read_set()
    print(A.issubset(B))

#Check Strict Superset
# Enter your code here. Read input from STDIN. Print output to STDOUT

def read_set():
    A = list(input().split())
    A = [int(elem) for elem in A]
    A = set(A)
    return A

A = read_set()
N = int(input())
all_supersets = True

for _ in range(N):
    B = read_set()
    if not A.issuperset(B):
        all_supersets = False

print(all_supersets)

#collections.Counter()
# Enter your code here. Read input from STDIN. Print output to STDOUT

from collections import Counter

def read_list():
    A = list(input().split())
    A = [int(elem) for elem in A]
    return A

X = int(input())
shoes = read_list()
customers = int(input())

count = Counter(shoes)
total = 0

for _ in range(customers):
    shoe, price = input().split()
    shoe = int(shoe)
    price = int(price)
    
    if count[shoe] != 0:
        total = total + price
        count[shoe] = count[shoe] - 1
        
print(total)

#DefaultDict Tutorial
# Enter your code here. Read input from STDIN. Print output to STDOUT

from collections import defaultdict

n, m = input().split()
n, m = int(n), int(m)

d = defaultdict(list)

for i in range(1, n + 1):
    value = input()
    d[value].append(i)
    
for i in range(m):
    value = input()
    
    if value in d:
        print(*d[value])
    else:
        print(-1)

#Collections.namedtuple()
# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import namedtuple
N = int(input())

cols = input().split()
col_names = cols[0] + "," + cols[1] + "," + cols[2] + "," + cols[3]
Mark = namedtuple("Mark", col_names)

s = 0.0

for _ in range(N):
    inp = input().split()
    
    student = Mark(inp[0], inp[1], inp[2], inp[3])
    s += float(student.MARKS)
    
print(format(s/N, ".2f"))

#Collections.OrderedDict()
from collections import OrderedDict

N = int(input())
ordered_dict = OrderedDict()
for _ in range(N):
    inp = input().split()
    name = inp[:-1]
    price = int(inp[-1])
    word = ' '.join(name)
    if word in ordered_dict.keys():
        ordered_dict[word] += price
    else:
        ordered_dict[word] = price
for key, value in ordered_dict.items():
    print(key, value)

#Word Order
# Enter your code here. Read input from STDIN. Print output to STDOUT

from collections import OrderedDict

N = int(input())
ordered_dict = OrderedDict()
for _ in range(N):
    word = input()
    if word in ordered_dict.keys():
        ordered_dict[word] += 1
    else:
        ordered_dict[word] = 1
print(len(ordered_dict))
for key, value in ordered_dict.items():
    print(value, end = " ")

#Collections.deque()
# Enter your code here. Read input from STDIN. Print output to STDOUT

from collections import deque

d = deque()

N = int(input())

for _ in range(N):
    inp = input().split()
    if inp[0] == "append":
        d.append(int(inp[1]))
    elif inp[0] == "pop":
        d.pop()
    elif inp[0] == "popleft":
        d.popleft()
    elif inp[0] == "appendleft":
        d.appendleft(int(inp[1]))
for elem in d:
    print(elem, end = " ")

#Company Logo
#!/bin/python3
from collections import Counter
import math
import os
import random
import re
import sys



if __name__ == '__main__':

    S = input()
    S = sorted(S)
    
    freq = Counter(list(S))
    
    for k, v in freq.most_common(3):
        print(k, v)

#Pilling Up!
# Enter your code here. Read input from STDIN. Print output to STDOUT

from collections import deque
n = int(input())

for _ in range(n):
    s = int(input())
    l = input().split()
    l = [int(elem) for elem in l]
    d = deque(l)
    answer = "Yes"
    length = 2**31
    for i in range(s):
        if d[0] >= d[-1] and d[0] <= length:
            length = d[0]
            d.popleft()
        elif d[0] < d[-1] and d[-1] <= length:
            length = d[-1]
            d.pop()
        else:
            answer = "No"
            break
    print(answer)
    
#Calendar Module
# Enter your code here. Read input from STDIN. Print output to STDOUT

import calendar

day = list(input().split())

weekday = calendar.weekday(int(day[2]), int(day[0]), int(day[1]))

days = ["MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY", "SATURDAY", "SUNDAY"]

print(days[weekday])

#Time Delta
#!/bin/python3

import math
import os
import random
import re
import sys
from datetime import datetime

# Complete the time_delta function below.
def time_delta(t1, t2):
    a = datetime.strptime(t1,"%a %d %b %Y %H:%M:%S %z")
    b = datetime.strptime(t2,"%a %d %b %Y %H:%M:%S %z")  
    return str(int(abs((a - b).total_seconds())))

    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        t1 = input()

        t2 = input()

        delta = time_delta(t1, t2)

        fptr.write(delta + '\n')

    fptr.close()

#Exceptions
# Enter your code here. Read input from STDIN. Print output to STDOUT

n = int(input())

for _ in range(n):
    a, b = input().split()
    try:
        print(int(int(a) / int(b)))
    except ZeroDivisionError as e:
        print("Error Code: integer division or modulo by zero")
    except ValueError as e:
        print("Error Code: {}".format(e))

#Zipped!
# Enter your code here. Read input from STDIN. Print output to STDOUT

students, subjects = input().split()

students, subjects = int(students), int(subjects)

subjects_list = []

for _ in range(subjects):
    l = list(input().split())
    l = [float(elem) for elem in l]
    subjects_list.append(l)

for sc in zip(*subjects_list):
    print(format(sum(sc) / len(sc), ".1f"))

#Athlete Sort
#!/bin/python3

import math
import os
import random
import re
import sys

def print_athletes(ath, n, m):
    for i in range(n):
        for j in range(m):
            print(ath[i][j], end = " ")
        print()

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    k = int(input().strip())

    ath = sorted(arr, key = lambda l : l[k])
    
    print_athletes(ath, n, m)

#ginortS
# Enter your code here. Read input from STDIN. Print output to STDOUT

s = input()

upper = sorted([x for x in s if x.isupper()])
lower = sorted([x for x in s if x.islower()])
digits = sorted([x for x in s if x.isdigit()])
odd_digits = [x for x in digits if int(x) % 2 == 1]
even_digits = [x for x in digits if int(x) % 2 == 0]

s = lower + upper + odd_digits + even_digits

for char in s:
    print(char, end = "")

#Map and Lambda Function
cube = lambda x : x**3 # complete the lambda function 

def fibonacci(n):
    # return a list of fibonacci numbers
    if n == 0:
        return []
    l = []
    l.append(0)
    
    for i in range(1, n):
        if i == 1:
            l.append(1)
        else:
            l.append(l[i - 1] + l[i - 2])
    return l

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))

#Detect Floating Point Number
# Enter your code here. Read input from STDIN. Print output to STDOUT-1.00
import re

n = int(input())

for _ in range(n):
    inp = str(input())
    print(bool(re.search(r"^[+-]?[0-9]*\.[0-9]+$", inp)))

#Re.split()
regex_pattern = r"[,.]"	# Do not delete 'r'.

import re
print("\n".join(re.split(regex_pattern, input())))

#Group(), Groups() & Groupdict()
# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

S = input()

m = re.search(r"([a-z0-9A-Z])\1", S)

if m:
    print(m.group(1))
else:
    print(-1)

#Re.findall() & Re.finditer()
# Enter your code here. Read input from STDIN. Print output to STDOUT

import re

S = input()

m = re.findall(r"(?<=[qwrtypsdfghjklzxcvbnm])([aeiou]{2,})(?=[qwrtypsdfghjklzxcvbnm])", S, re.IGNORECASE)

if len(m) == 0:
    print(-1)
else:
    for elem in m:
        print(elem)

#Re.start() & Re.end()
# Enter your code here. Read input from STDIN. Print output to STDOUT

import re

S = input()
k = input()

m = re.finditer(r'(?={})'.format(k), S)

i = 0

for elem in m:
    print((elem.start(), elem.start() + len(k) - 1))
    i += 1

if i == 0:
    print((-1, -1))

#Regex Substitution
# Enter your code here. Read input from STDIN. Print output to STDOUT

import re

inp = int(input())

for i in range(0,inp):
   txt = input()
   txt = re.sub(r"\ \&\&\ "," and ",txt)
   txt = re.sub(r"\ \|\|\ "," or ",txt)
   txt = re.sub(r"\ \&\&\ "," and ",txt)
   txt = re.sub(r"\ \|\|\ "," or ",txt)
   print(txt)

#Validate Roman Numerals
regex_pattern = r"M{0,3}(C[MD]|D?C{0,3})(X[CL]|L?X{0,3})(I[VX]|V?I{0,3})$" # Do not delete 'r'.

import re
print(str(bool(re.match(regex_pattern, input()))))

#Validare phone numbers
# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
n = int(input())

for i in range(n):
    phone = input()
    if re.match(r'[789]\d{9}$',phone):
        print("YES")
    else:
        print("NO")

#Validating and Parsing Email Adresses
# Enter your code here. Read input from STDIN. Print output to STDOUT
import email.utils
import re
N = int(input())

for i in range(0, N):
    s = input()
    parsed_addr = email.utils.parseaddr(s)
    if re.search(r'^[a-z][\w\-\.]+@[a-z]+\.[a-z]{1,3}$', parsed_addr[1]):
        print(email.utils.formataddr(parsed_addr))
    

#Hex Color Code
# Enter your code here. Read input from STDIN. Print output to STDOUT

import re
N=int(input())

for i in range(0,N):
    c=input()

    x=c.split()

    if len(x) > 1 and '{' not in x:
        x=re.findall(r'#[a-fA-F0-9]{3,6}',c)
        for elem in x:
            print(elem)

#Validating UID
# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
n = int(input())

for i in range(n):
    s = "".join(sorted(input()))
    c1 = len(s) == 10
    c2 = not re.search(r'[^a-zA-Z0-9]', s)
    c3 = not re.search(r'(.)\1', s)
    c4 = re.search(r'\d\d\d', s)
    c5 = re.search(r'[A-Z]{2}', s)
    
    if c1 and c2 and c3 and c4 and c5:
        print("Valid")
    else:
        print("Invalid")
        
#Validating Credit Card Numbers
# Enter your code here. Read input from STDIN. Print output to STDOUT

import re

com = re.compile(
    r"^"
    r"(?!.*(\d)(-?\1){3})"
    r"[456]"
    r"\d{3}"
    r"(?:-?\d{4}){3}"
    r"$")
    
n = int(input())
    
for _ in range(n):
    s = input()
    if com.search(s):
        print("Valid")
    else:
        print("Invalid")

#Validating Postal Codes
regex_integer_in_range = r"^[1-9][\d]{5}$"	# Do not delete 'r'.
regex_alternating_repetitive_digit_pair = r"(\d)(?=\d\1)"	# Do not delete 'r'.


import re
P = input()

print (bool(re.match(regex_integer_in_range, P)) 
and len(re.findall(regex_alternating_repetitive_digit_pair, P)) < 2)

#Matrix Script
#!/bin/python3

import math
import os
import random
import re
import sys

first_multiple_input = input().rstrip().split()

n = int(first_multiple_input[0])

m = int(first_multiple_input[1])

matrix = []

for _ in range(n):
    matrix_item = input()
    matrix.append(matrix_item)

matrix = list(zip(*matrix))

s = ""

for ss in matrix:
    for l in ss:
        s += l

print(re.sub(r'(?<=\w)([^\w\d]+)(?=\w)', ' ', s))

#XML 1 - Find the Score
import sys
import xml.etree.ElementTree as etree

def get_attr_number(node):
    # your code goes here
    s = len(node.attrib) + sum(get_attr_number(child) for child in node)
    return s
    
if __name__ == '__main__':
    sys.stdin.readline()
    xml = sys.stdin.read()
    tree = etree.ElementTree(etree.fromstring(xml))
    root = tree.getroot()
    print(get_attr_number(root))

#XML2 - Find the Maximum Depth
import xml.etree.ElementTree as etree

maxdepth = 0
def depth(elem, level):
    global maxdepth
    # your code goes here
    if (level == maxdepth):
        maxdepth += 1
        
    for child in elem:
        depth(child, level + 1)

if __name__ == '__main__':
    n = int(input())
    xml = ""
    for i in range(n):
        xml =  xml + input() + "\n"
    tree = etree.ElementTree(etree.fromstring(xml))
    depth(tree.getroot(), -1)
    print(maxdepth)

#Standarize Mobile Number using Decorators
def wrapper(f):
    def fun(l):
        # complete the function
        f(["+91 " + a[-10:-5] + " " + a[-5:] for a in l])
    return fun

@wrapper
def sort_phone(l):
    print(*sorted(l), sep='\n')

if __name__ == '__main__':
    l = [input() for _ in range(int(input()))]
    sort_phone(l) 

#Decorators 2 - Name Directory
import operator

def person_lister(f):
    def inner(people):
        # complete the function
        return map(f, sorted(people, key=lambda x: int(x[2])))
    return inner

@person_lister
def name_format(person):
    return ("Mr. " if person[3] == "M" else "Ms. ") + person[0] + " " + person[1]

if __name__ == '__main__':
    people = [input().split() for i in range(int(input()))]
    print(*name_format(people), sep='\n')

#Arrays
import numpy

def arrays(arr):
    # complete this function
    # use numpy.array
    l = numpy.array(arr, float)
    l = numpy.flip(l)
    return l

arr = input().strip().split(' ')
result = arrays(arr)
print(result)

#Shape and Reshape
import numpy as np
# Enter your code here. Read input from STDIN. Print output to STDOUT

input_list = list(input().split())
input_list = [int(elem) for elem in input_list]

print(np.reshape(np.array(input_list), (3, 3)))

#Transpose and Flatten
# Enter your code here. Read input from STDIN. Print output to STDOUT

import numpy as np

N, M = input().split()
N, M = int(N), int(M)

matrix = []

for _ in range(N):
    r = list(input().split())
    r = [int(elem) for elem in r]
    matrix.append(r)
    
array = np.array(matrix)

print(np.transpose(array))
print(array.flatten())    

#Concatenate
# Enter your code here. Read input from STDIN. Print output to STDOUT

import numpy as np

N, M, P = input().split()
N, M, P = int(N), int(M), int(P)

N_MATRIX= []
M_MATRIX= []

for _ in range(N):
    l = list(input().split())
    l = [int(elem) for elem in l]
    N_MATRIX.append(l)
    
for _ in range(M):
    l = list(input().split())
    l = [int(elem) for elem in l]
    M_MATRIX.append(l)
    
N_MATRIX = np.array(N_MATRIX)
M_MATRIX = np.array(M_MATRIX)

print(np.concatenate((N_MATRIX, M_MATRIX), axis = 0))

#Zeros and Ones
# Enter your code here. Read input from STDIN. Print output to STDOUT

import numpy as np

l = input().split()
l = [int(elem) for elem in l]

print(np.zeros((tuple(l)), dtype = np.int))
print(np.ones((tuple(l)), dtype = np.int))

#Eye and Identity
# Enter your code here. Read input from STDIN. Print output to STDOUT

import numpy as np
np.set_printoptions(legacy = '1.13')

N, M = input().split()
N, M = int(N), int(M)
print(np.eye(N, M))

#Array Mathematics
# Enter your code here. Read input from STDIN. Print output to STDOUT
import numpy as np
N, M = input().split()
N, M = int(N), int(M)

a = []
b = []

for _ in range(N):
    r = list(input().split())
    r = [int(elem) for elem in r]
    a.append(r)
    
for _ in range(N):
    r = list(input().split())
    r = [int(elem) for elem in r]
    b.append(r)
    
a = np.array(a)
b = np.array(b)

print(a + b)
print(a - b)
print(a * b)
print(a // b)
print(a % b)
print(a ** b)

#Floor, Ceil and Rint
# Enter your code here. Read input from STDIN. Print output to STDOUT
import numpy as np
np.set_printoptions(legacy = '1.13')

inp = list(input().split())
inp = [float(elem) for elem in inp]
inp = np.array(inp)
print(np.floor(inp))
print(np.ceil(inp))
print(np.rint(inp))

#Sum and Prod
# Enter your code here. Read input from STDIN. Print output to STDOUT
import numpy as np
N, M = input().split()
N, M = int(N), int(M)

mat = []

for _ in range(N):
    inp = list(input().split())
    inp = [int(elem) for elem in inp]
    mat.append(inp)
    
mat = np.array(mat)

print(np.prod(np.sum(mat, axis = 0)))

#Min and Max
# Enter your code here. Read input from STDIN. Print output to STDOUT
import numpy as np
N, M = list(input().split())
N, M = int(N), int(M)
mat = []
for _ in range(N):
    inp = list(input().split())
    inp = [int(elem) for elem in inp]
    mat.append(inp)
    
mat = np.array(mat)

print(np.max(np.min(mat, axis = 1)))

#Mean, Var, and Std
# Enter your code here. Read input from STDIN. Print output to STDOUT
import numpy as np
N, M = list(input().split())
N, M = int(N), int(M)
mat = []
for _ in range(N):
    inp = list(input().split())
    inp = [int(elem) for elem in inp]
    mat.append(inp)
    
mat = np.array(mat)

print(np.mean(mat, axis = 1))
print(np.var(mat, axis = 0))
print(round(np.std(mat, axis = None), 11))

#Dot and Cross
# Enter your code here. Read input from STDIN. Print output to STDOUT
import numpy as np
N = int(input())

A = []
B = []

for _ in range(N):
    inp = list(input().split())
    inp = [int(elem) for elem in inp]
    A.append(inp)
    
for _ in range(N):
    inp = list(input().split())
    inp = [int(elem) for elem in inp]
    B.append(inp)
    
A = np.array(A)
B = np.array(B)
    
print(np.dot(A, B))

#Inner and Outer
# Enter your code here. Read input from STDIN. Print output to STDOUT
import numpy as np
A = []
B = []

A = list(input().split())
A = [int(elem) for elem in A]
A = np.array(A)

B = list(input().split())
B = [int(elem) for elem in B]
B = np.array(B)

print(np.inner(A, B))
print(np.outer(A, B))

#Polynomials
# Enter your code here. Read input from STDIN. Print output to STDOUT

import numpy as np

inp = list(input().split())
inp = [float(elem) for elem in inp]
inp = np.array(inp)

value = float(input())

print(np.polyval(inp, value))

#Linear Algebra
# Enter your code here. Read input from STDIN. Print output to STDOUT

import numpy as np
N = int(input())
mat = []
for _ in range(N):
    inp = list(input().split())
    inp = [float(elem) for elem in inp]
    mat.append(inp)
    
mat = np.array(mat)

print(round(np.linalg.det(mat), 2))
