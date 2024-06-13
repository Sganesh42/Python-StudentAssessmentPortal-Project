from random import sample
from user import userdata
score=0

def menu():
    print("1.Add Q")
    print("2.Take Assesment")
    print("3.Get Score")
    print("4.Exit")

class InValidUserError(Exception):
    def __init__(self,m):
        self.msg=m
    def __str__(self):
        return self.msg


def addQuestion():
    print("*****Add Questions*****")
    print("\t1.Through Console")
    print("\t2.From File")
    c=int(input("Enter Your Choice:"))
    if c==1:
        print("---------Through Console---------")
        file=open("QBank.txt","a")
        Q=input("Enter the Question:")
        file.write(Q)
        file.write("#")
        op1=input("op1:")
        file.write(op1)
        file.write("#")
        op2=input("op2:")
        file.write(op2)
        file.write("#")
        op3=input("op3:")
        file.write(op3)
        file.write("#")
        op4=input("op4:")
        file.write(op4)
        file.write("#")
        ans=input("ANS:")
        file.write(ans)
        file.write("\n")
        file.close()
    elif c==2:
        print("---------Through File Copy---------")
        file=open("QBank.txt","a")
        source=input("Enter the file name:")
        ifile=open(source,"r")
        s=ifile.read()
        file.write(s)
        ifile.close()
        file.close()
    else:
        print("Invalid option")

questions=[]

def takeQuiz(q):
    global score
    score=0
    for e in q:
        #print(e[0])
        qp=e[0]
        ans=e[1]
        print(" Q :",qp[0])
        print("\t1 :",qp[1])
        print("\t2 :",qp[2])
        print("\t3 :",qp[3])
        print("\t4 :",qp[4])
        a=int(input("Enter the Correct choice :"))
        if int(ans)==a:
            score=score+1
        else:
            score=score-0.25


un=input("Enter the user name :")
pw=input("Enter the password :")
#userdata={"ganesh":'408',"sai":'406',"vamsi":'405'}
if userdata.get(un)==pw:
    print("Welcome to Assesment")
else:
    try:
        raise InValidUserError("Invalid user name or password")
    except InValidUserError as ob:
        print(ob)
        exit()

while True:
    menu()
    ch=int(input("Enter your choice:"))
    if ch==1:
        addQuestion()
    elif ch==2:
        print("*****Take Assesment*****")
        n=int(input("How many Qs would you like to have"))
        file=open("QBank.txt","r")
        for q in file:
            q=q.strip()
            qc=q.split("#")
            ans=qc[-1]
            qpromt=qc[:-1]
            questions.append([qpromt,ans])
        #print(questions)
        RL=sample(range(len(questions)),n)
        #print(RL)
        QL=[]
        for i in RL:
            QL.append(questions[i])
        #print(QL)
        takeQuiz(QL)
        file.close()
    elif ch==3:
        print("Your Score is :",score)
    else:
        print("Exiting from Application...")
        exit()
