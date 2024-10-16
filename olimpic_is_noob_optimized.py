n = int(input("Enter n: "))
positions = list(map(int, input("Enter positions: ").split()))

base_words = ["chipi", "chapa", "dubi", "daba"]

def create_message(num):
    message = ""
    for i in range(num):
        message += base_words[i % 4]
    return message

def func_chipi(i):
    if i == 0:
        return base_words[0]
    else:
        return f"{func_chipi(i-1)}{base_words[i % 4]*i}{func_chipi(i-1)}"  # F(i) = F(i-1) + คำตำแหน่งที่[i%4]*i + F(i-1)

s = func_chipi(n)
# print("s = ",s)
def find_char(position):
    if position <= len(s):
        return s[position - 1]
    else:
        return "Position out of bounds"

for pos in positions:
    print(find_char(pos))