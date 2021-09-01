# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

for _ in range(int(input().strip())):
    if re.match(r'[789]\d{9}$',input().strip()):   
        print('YES')  
    else:  
        print('NO')