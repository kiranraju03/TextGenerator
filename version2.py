import random
import string

def gen():
    input_length=input("Enter the length of the string to be generated : ")
    leng=int(input_length)
    i=0

    def generator():
        i=0

        while i!=leng:
            file=open("sample2.txt",'a')
            str1=random.choice(string.ascii_lowercase)
            file.write(str1)
            i+=1

        file=open("sample2.txt",'r')
        content=file.read()
        print(content)

    generator()

gen()
