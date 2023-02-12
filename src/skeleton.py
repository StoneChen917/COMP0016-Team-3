from Backend import fuzzymatching
from Backend.Integration import readfile



pgone, text = readfile.ReadFile().exec("fr1.pdf")
print(pgone)
print("--------------------------------------------------------\n")
print(text)