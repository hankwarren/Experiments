from pathlib import Path

# the comprehension returns a list
files = [f for f in Path('../images').iterdir() if f.is_file()]
print(type(files))

print("- newline sep ---------------------")
print(*files, sep="\n")
print("- array ---------------------")
print(files)

print("- for loop ---------------------")
for file in sorted(files):
    print(file)
print("- done ---------------------")