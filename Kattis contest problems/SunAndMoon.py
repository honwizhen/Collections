# You recently missed an eclipse and are waiting for the next one! To see any eclipse from your home, the sun and the moon must be in alignment at specific positions. You know how many years ago the sun was in the right position, and how many years it takes for it to get back to that position. You know the same for the moon. When will you see the next eclipse?

# Input
# The input consists of two lines.

# The first line contains two integers, and, where 
#  is how many years ago the sun was in the right position, and 
#  is how many years it takes for the sun to be back in that position.

# The second line contains two integers, 
#  and 
 
# , where 
#  is how many years ago the moon was in the right position, and 
#  is how many years it takes for the moon to be back in that position.

# Output
# Output a single integer, the number of years until the next eclipse. 
# The data will be set in such a way that there is not an eclipse happening right now and there will be an eclipse within the next 5000 years.

# Sample Input 1	Sample Output 1
# 3 10              7
# 1 2



ds, ys = map(int, input().split())
dm, ym = map(int, input().split())

for years in range(5000):
    if ((years + ys) % ds == 0 and (years + ym) % dm == 0):
        print(years)
        break


