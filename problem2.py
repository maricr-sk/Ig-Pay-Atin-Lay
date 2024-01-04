##
def print_centered(text):
    list = text.split(" ")
    largestn = 0
    for n in list:
        if(len(n) > largestn):
            largestn = len(n)
    for j in list:
        j = j.strip()
    largestn = largestn + 4
    str = ""
    for n in range(largestn):
        str = str + "*"
    print(str)
    for n in list:
        la = "*"
        num = largestn - len(n)
        numb = num // 2
        for p in numb:
            la = la + " "
        la = la + n
        for l in range(numb, num):
            la = la + " "
        la = la + "*"
    print(la)
    print(str)

def main():
    print_centered("Python Rocks!")