import time
def writedata(mdata):
    f=open('impdata','a+')
    f.write(str(mdata)+';-;')
    f.close()
def readdata(x):
    f=open('impdata','r+')
    raw=f.read()
    raw=raw.split(';-;')
    for i in range(len(raw)):
        raw[i]=raw[i].split('-_-')        
    #print(raw)
    #print(len(raw))
    for i in range(len(raw)-1):
        #print(raw[i][0])
        #print(str(raw[i][0])==str(x))
        if(str(raw[i][0])==str(x)):
            print("your password is :"+decrypt(str(raw[i][1])))
            #time.sleep(90000)
            return
            
    print( "NO PASSWORD MATCHED :( , sorry dude")
    return
    f.close()

    
def savethepass():
    print("enter the account for which you want to save id and password(all caps)")
    acinp=input()
    if(acinp.isupper()):
        print("enter the password of the "+acinp)
        passinp=input()
        if(len(passinp)>0):
            acinp=encrypt(acinp)
            passinp=encrypt(passinp)
            rawdata=acinp+"-_-"+passinp
            writedata(rawdata)
            return True
        else:
            return False
        return True
    else:
        print("cant't save the password, please type the account name in full CAPS")
        return False
def encrypt(mstr):
    n=len(mstr)
    newstr=""
    for i in mstr:
        if type(i)==type(1):
            newstr+=str(int(i+n))
        else:
            newstr+=chr(ord(i)+n)
    
    return newstr
def decrypt(mstr):
    n=len(mstr)
    newstr=""
    for i in mstr:
        if type(i)==type(1):
            newstr+=str(int(i-n))
        else:
            newstr+=chr(ord(i)-n)
    return newstr
def authenticate():
    x=1
    flag=True
    while(flag!=False):
        
        print('Enter Master Password to enter')
        ans=input()
        if(encrypt(ans)=='qn)}qn{n'):
            print('congrats you are the right person')
            return True
        else:
            if(flag==False or (x>=3)):
                flag=True
                return False
                #write logic here for something punitive
            else:
                print("you can try again : "+str((3-x))+" more times")
                x+=1
            

flag=authenticate()
if(flag==False):
    pass
else:
    print('do you want to save passwords or want to view')
    ans=input()
    if(ans=='save' or ans=='Save' or ans=='SAVE'):
        flag=savethepass()
        if(flag==True):
            print('password has been saved')
        else:
            print('sorry we could not save the password')
    else:
        print('please type the name of the password that want to search')
        ans=input()
        if(len(ans)>0):
            x=encrypt(ans)
            x=readdata(x)
            print(x)
print("this program will end itself in 10 seconds")
time.sleep(10)
    
