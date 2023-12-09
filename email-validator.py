email=input("Email your Email: ") #g@g.in
k=0
j=0
d=0
if len(email)>=6:
    if email[0].isalpha():
        if ("@" in email) and (email.count('@')==1):
            if (email[-4]==".")^(email[-3]=="."):
                for i in email:
                    if i.isspace():
                        k=1
                    elif i.isalpha():
                        if i==i.upper():
                            j=1
                    elif i.isdigit():
                        continue
                    elif i=="_" or i=="." or i=="@":
                        continue
                    else:
                        d=1
                if k==1 or j==1 or d==1:
                    print("There should not be any spaces, capital letters and special character.(except '_', '.', '@')")
            else:
                print("Wrong Email. 'Dot' should be only on third last or fourth last position")
        else:
            print("Wrong Email. Exactly one '@' required")
    else:
        print("Wrong Email. First letter of email should be alpha-numeric.")
else:
    print("Wrong Email. Email too short step 1")

