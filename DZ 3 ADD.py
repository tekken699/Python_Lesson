from sys import argv


with open("bakery.csv", "a", encoding="utf-8") as write:
    with open("bakery.csv", "r", encoding="utf-8") as read:
        if len(argv) > 1 and [i for i in argv[1:] if "." in i and i.replace(".", "").isdigit()]:
            if round(float(argv[1]), 3) < 99999.999:
                print(f"{round(float(argv[1]),3):>010}", file=write)
            else:
                print("Number must be less than 99999,999")
        else:
            print(read.read())