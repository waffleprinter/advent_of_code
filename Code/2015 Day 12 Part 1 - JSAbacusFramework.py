def is_part_of_number(char):
    return (ord(char) in range(48, 58)) or (ord(char) == 45)


with open(r"Inputs\2015 Day 12- JSAbacusFramework.txt", 'r') as f:
    data = f.read()

    total_sum = 0
    current_number = ""

    for i in range(len(data) - 1):
        if not is_part_of_number(data[i]):
            if current_number:
                total_sum += int(current_number)
                current_number = ""
      
            continue
            
        current_number += data[i]

print(total_sum)
