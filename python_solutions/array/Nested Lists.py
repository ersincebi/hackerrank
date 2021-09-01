lst = [['Harry', 37.21],['Berry', 37.21],['Tina', 37.2],['Akriti', 41],['Harsh', 39]]
    
second_highest = sorted(list(set([marks for name, marks in lst])))[1]

print('\n'.join([a for a,b in sorted(lst) if b == second_highest]))