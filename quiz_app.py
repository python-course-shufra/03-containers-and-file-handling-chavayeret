import sys
import random


def main():
     print(sys.argv[1])
    mikz=sys.argv[1:]
    num=sys.argv[2:]
    def quiz(mikz,num):
        with open(rf'question\{mikz}.txt', mode="r")as ques:
            for line in ques:
                l=random(line)
            l.strip()
            quest,rait,no1,no2,no3=l.split()
            questi=[rait,no1,no2,no3]
            questi1=list(random.shuffle(questi))
            print(quest)
            for i in enumerate(questi1):
                print(f'\n.join({questi1[i]})')
            print('select the correct answer: ')
            answer=sys.argv[1:]
            answers=[]
            if questi1[answer]==rait:
                answers[answer]='1'
        return sum(list(map(quiz,num)))
        if __name__ == '__main__':
             main()


if __name__ == '__main__':
    main()
