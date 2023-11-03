def search():
    take_list=input("enter a number separeted by comma? ")
    list=take_list.split(",")

    length=len(list)
    for i in range(length):
        list[i]=int(list[i])

    step=0
    start=0
    end=length-1
    target=int(input("enter target number? "))
    while start<=end:
        print(f"steps:{step}"+" "+str(list[start:end+1]))
        middle=(start+end)//2
        step+=1
        if target==list[middle]:
            print("target found")
            res=input("Dou you want to continue(y/n)?")
            if res=='y':
                search()
            else:
                print("have a nice day!")
            break
        elif target>list[middle]:
            start=middle+1 
        else:
            end=middle-1

    if start>end:
        print("target is not in the list")
        res=input("Dou you want to continue(y/n)?")
        if res=='y':
            search()
        else:
            print("have a nice day!")
search()