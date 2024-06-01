
while True:
    
    print("\t\t\t\t_________________________________________")
    print("\t\t\t\t|SELECT ONE OF THE OPTION:\t\t|")
    print("\t\t\t\t|1. TDP With Backtracking (Koushik):\t|")
    print("\t\t\t\t|2. LL(1) Parser (Rishav):\t\t|")
    print("\t\t\t\t|3. LR(0) Parser (Shweta):\t\t|")
    print("\t\t\t\t|4. SLR(1) Parser (Arya):\t\t|")
    print("\t\t\t\t|5. CLR(1) Parser (Krishna):\t\t|")
    print("\t\t\t\t|6. exit\t\t\t\t|")
    print("\t\t\t\t|_______________________________________|")
    print("\t\t\t\tChoices:",end="")
    num=int(input())
    if num==1:
        print("Created in Dynamic Manner :\n")
        import Parser_Back_Koushik
        print("\t\t\t\t_________________________________________")
        print("\t\t\t\t|Do you want to Stop input N/n\t\t|")
        print("\t\t\t\t|Press enter to Continue...\t\t|")
        print("\t\t\t\t|_______________________________________|")
        
        j=input()
        if j=='N' or j=='n':
            break
    elif num==2:
        print("Created in Static Manner :\n")
        import LL1_Rishav
        print("\t\t\t\t_________________________________________")
        print("\t\t\t\t|Do you want to Stop input N/n\t\t|")
        print("\t\t\t\t|Press enter to Continue...\t\t|")
        print("\t\t\t\t|_______________________________________|")

        j=input()
        if j=='N' or j=='n':
            break
    elif num==3:
        print("Created in Dynamic Manner :\n")
        import LR0_shweta
        print("\t\t\t\t_________________________________________")
        print("\t\t\t\t|Do you want to Stop input N/n\t\t|")
        print("\t\t\t\t|Press enter to Continue...\t\t|")
        print("\t\t\t\t|_______________________________________|")
        j=input()
        if j=='N' or j=='n':
            break
    elif num==4:
        print("Created in Static Manner :\n")
        import SLR1_arya
        print("\t\t\t\t_________________________________________")
        print("\t\t\t\t|Do you want to Stop input N/n\t\t|")
        print("\t\t\t\t|Press enter to Continue...\t\t|")
        print("\t\t\t\t|_______________________________________|")

        j=input()
        if j=='N' or j=='n':
            break
    elif num==5:
        print("Created in Dynamic Manner :\n")
        import clr_krishna
        clr_krishna.main()
        print("\t\t\t\t_________________________________________")
        print("\t\t\t\t|Do you want to Stop input N/n\t\t|")
        print("\t\t\t\t|Press enter to Continue...\t\t|")
        print("\t\t\t\t|_______________________________________|")

        j=input()
        if j=='N' or j=='n':
            break
    elif num==6:
        exit()
    else:
        print("Please Enter The Correct ")
    