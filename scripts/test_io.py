import argparse

def standardIO():
    a = input("pls input the number:\n")
    print(a)


def fileIO():
    #read file
    with open("e:\\output.txt", "rb") as fd:
        for line in fd.readlines():
            print(line)
    #write file
    # with open("e:\\output.txt", "a") as fd:
    #     lines = "fafafafxxxxx"
    #     fd.writelines(lines)
if __name__ == "__main__":
    fileIO()