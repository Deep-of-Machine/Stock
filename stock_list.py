file_path = "코스피 종목코드.txt"

with open(file_path) as f:
    lines = f.readlines()

lines = [line.rstrip('\n') for line in lines]
print(lines)
