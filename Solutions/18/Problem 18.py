'''
By starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum total from top to bottom is 23.

   3
  7 4
 2 4 6
8 5 9 3

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom of the triangle below:

              75
             95 64
            17 47 82
           18 35 87 10
          20 04 82 47 65
         19 01 23 75 03 34
        88 02 77 73 07 63 67
       99 65 04 28 06 16 70 92
      41 41 26 56 83 40 80 70 33
     41 48 72 33 47 32 37 16 94 29
    53 71 44 65 25 43 91 52 97 51 14
   70 11 33 28 77 73 17 78 39 68 17 57
  91 71 52 38 17 14 91 43 58 50 27 29 48
 63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23

NOTE: As there are only 16384 routes, it is possible to solve this problem by trying every route. However, Problem 67, is the same challenge with a triangle containing one-hundred rows; it cannot be solved by brute force, and requires a clever method! ;o)
'''

# this code converts the string of numbers into a list of numbers
numbers = '''75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23'''

def str_to_list_of_ints(string, delimiter = " "):
    '''takes spaced listed numbers and returns a liust version of integers'''
    stri = string.split("\n")
    for i in range(len(stri)):
        stri[i] = stri[i].split(delimiter)
        for j in range(len(stri[i])):
            stri[i][j] = int(stri[i][j])
    return stri

def maximum_path_sum(nums):
    '''Works out the maximum path size in a triangle of integers stored as a left-aligned list of rows of integers'''
    
    #handle first two rows differently
    last = nums[1]
    last[0] += nums[0][0]
    last[1] += nums[0][0]
    
    for row in range(2, len(nums)):
        current = [0 for x in range(len(nums[row]))]
        current[0] = nums[row][0] + last[0]
        current[-1] = nums[row][-1] + last[-1]
        for i in range(1, len(nums[row])-1):
            current[i] = nums[row][i] + max(last[i], last[i-1])
        last = current
    
    return max(last)

print(maximum_path_sum(str_to_list_of_ints(numbers)))   