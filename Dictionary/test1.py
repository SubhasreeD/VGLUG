n={}
def start():
    print(" 1.add \n 2.delete \n 3.modify \n 4.view \n 5.exit")
    choice=int(input("your choice:"))
    match(choice):
        case 1:
            global key,values
            key=[input()]
            values=[input()]
            for i in range(len(key)):
                    a=key[i]
                    n[a]= values[i]
            print(n)
            start()
        case 2:
            b=input()
            del n[b]
            start()
        case 3:
            for i in range(len(key)):
                c=input()
                if(key[i]==c):
                    n[key[i]]=input()
                else:
                    n.update({c:input()})
            print(n)
            start()
        case 4:
            print(n)
            print("do you want to continue yes->6")
            choice=int(input("your choice:"))
            if(choice==6):
                start()
            else:
                exit()
        case 5:
            exit()
        case _:
            print("invalid choice")
start()

        
    
