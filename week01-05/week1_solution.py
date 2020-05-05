
def sum_of_digits(n):
  if n < 0
    n = -1 * n

  s=0
  while n>0:
      s+=n%10
      n//=10
  return s


#print(sum_of_digits(123))


def to_digits(n):
  l=[]
  while n:
    x=n%10
    l.append(x)
    n//=10
  
  l.reverse()
  return l


#print(to_digits(123))


def to_number(digits):
   for i in digits:
     print(i, end="")

#print(to_number([9,9,9,9,9]))


#### to_digits
return list(map(int, list(str(digits))))

#####
to_digits(digits)
s = str(digits)
l=[]
for i in s
i.append(int(i))

return l
####

###############################

def to_number(digits):
    s=0
    for digit in digits:
        s*=10
        s+=digit
    return s

#print(to_number([1,2,3]))


#########################

def fact(m):
  factN=1
  for i in range(1,m+1):
     factN = factN * i
  return factN

#print(fact(4))

def fact_digits(n):
  s=0
  while n>0:
    x=n%10
    factNum=fact(x)
    s+=factNum
    n//=10
  return s

#print(fact_digits(145))
#print(fact_digits(111))

#####################################


def palindrome(n):
    return n == n[::-1]

#print(palindrome('aba'))

def reverse_digit(n):
    temp=n
    s=0
    while temp>0:
        digit=temp%10
        s=s*10+digit
        temp//=10
    if(s==n):
        return True
    else:
        return False


#print(reverse_digit(123))

def reverseString(st):
    return st == st[:: -1]

#print(reverseString('abba'))

def palindrome(m):
    st_str=str(m)
        return st_str==st_str[::-1]


#####################################################


def count_vowels(str):
    count=0
    for i in str:
        if i == 'a' or i == 'e' or i == 'o' or i == 'i' or i == 'u' or i == 'y' or i == 'A' or i == 'E' or i == 'O' or i == 'I' or i == 'U' or i == 'Y':
            count+=1
    return count

#print(count_vowels('abcadsaoAUOu'))

################################################### 

def count_consonants(string):
   length = len(string)
   x = count_vowels(string)
   consonants = length-x
   return consonants

# print(count_consonants("Python"))
# print(count_consonants("Theistareykjarbunga"))


####################################################

def count_letter(string, char):
            count = 0
            for c in string:
                if c == char:
                    count += 1
            return count


def char_histogram(string):
    d={}
    for i in string:
        if i not in d:
            x=count_letter(string, i)
            d.update({i: x})
    return d

#print(char_histogram("Python!"))      
#print(char_histogram("AAAAaaa!!!"))


##################################################


def sum_matrix(m):
    s = sum(sum(m,[]))
    return s

# print(sum_matrix(([1,2],[3,4])))



def nan_expand(times):
    if times == 0:
        pritn("")
    elif times == 1:
        print("Not a NaN", end="")
    else:
        while times >= 1:
            print("Not a ", end="")
            times-=1
        return("NaN")

# print(nan_expand(3))


#############################################

def prime_num(n):
    if n <= 1: 
        return False
    if n <= 3: 
        return True
  
    # This is checked so that we can skip  
    # middle five numbers in below loop 
    if n % 2 == 0 or n % 3 == 0 : 
        return False
  
    i = 5
    while i * i <= n : 
        if n % i == 0 or n % (i + 2) == 0 : 
            return False
        i = i + 6
  
    return True
  

def prime_factorization(num):
    l=[]
    if prime_num(num) == True:
        l.append((num,1))
        return l
    for j in range(num//2+1,1,-1):
        count=0
        x = num
        if prime_num(j) == True and num%j == 0:
            while x > 0:
                if x % j == 0:
                    count = count + 1
                x //= j
        if x%j == 0:
            x//=j
        if count != 0:
            l.append((j,count))
            count=0
    return l


# print(prime_factorization(100))


##########################################################

def group(list):
    curr_list = []
    result = []
    for x in list:
        if x in curr_list:
            pass
        else:
            if curr_list != []:
                result.append(curr_list)
            curr_list = []
        curr_list.append(x) 
    result.append(curr_list)
    return result


# print(group([1, 1, 1, 2, 3, 1, 1]))
# print(group([1, 2, 1, 2, 3, 3]))



##########################################################

def word_counter():
    word=input('Enter word: ')
    print('You entered:', word)
    size=input('Enter matrix size NxM:')

    n=int(size.split(' ')[0])
    m=int(size.split(' ')[1])

    if len(word) > min([m,n]):
        return 'Invalid number of rows or col:'


    matrix = []
    row_inputed = 0
    print('Enter matrix: ')

    while row_inputted < n:
        row_inputted = input()
        row = row_inputted.strip().split(' ')  # strip maha prazniq string nakraq
        if len(row) != m:
            return 'Wrong input'

        matrix.append(row)
        row_inputted +=1

    word_occurances = 0

    for row in matrix:



#print(matrix)

#print(word,size)
    