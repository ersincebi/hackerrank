# Enter your code here. Read input from STDIN. Print output to STDOUT

import re

pattern=r'(#[0-9a-fA-F]{3,6}){1,2}[^\n ]'
inp = '#BED{color: #FfFdF8; background-color:#aef;font-size: 123px;background: -webkit-linear-gradient(top, #f9f9f9, #fff);}#Cab{background-color: #ABC;border: 2px dashed #fff;}'
print(re.findall(pattern,inp))
