class chessplayer:
 
    def __init__ (self, name, year, roll_number, current_rating,L):
        self.current_rating=current_rating
        self.year=year
        self.roll_number=roll_number
        self.name=name
        self.L=L
        
    def age(self):
        from datetime import date
        today = date.today()
        m= today.year
        l=m-self.year
        return l
 
    def unrated(self):
        s=0
        for i in L:
            if(i[0]=="+"):
                s+=int(i[1:])+400
            elif(i[0]=="-"):
                s+=int(i[1:])-400
            elif(i[0]=="="):
                s+=int(i[1:])
            else:
                print("INVALID INPUT")
        return s/len(L)

    def diffRating(self):
        list=[]
        for j in self.L:
            list.append(self.current_rating-int(j[1:]))

        s=0
        for i in list:
            if(i>500):
                s+=99
            elif(i>400):
                s+=92
            elif(i>300):
                s+=86
            elif(i>200):
                s+=76
            elif(i>100):
                s+=66
            elif(i>50):
                s+=57
            elif(i>25):
                s+=53
            elif(i>=0):
                s+=50
            if(i<-500):
                s+=1
            elif(i<-400):
                s+=8
            elif(i<-300):
                s+=14
            elif(i<-200):
                s+=24
            elif(i<=-100):
                s+=34
            elif(i<-50):
                s+=43
            elif(i<-25):
                s+=47
            elif(i<=0):
                s+=50
        return s/100

    def ActualScore(self):
        s=0.0
        for i in L:
            if(i[0]=="+"):
                s+=1
            elif(i[0]=="-"):
                s+=0
            elif(i[0]=="="):
                s+=0.5
        return s

    def elo(self,m):
        self.m=m
        k= round(obj.ActualScore()-obj.diffRating(),2)
        if k>=0:
            b=True
        else:
            b=False

        if(m<30):
            if(b==True):
                self.current_rating+=25*k
            else:
                self.current_rating-=25*k
        else:
            if(self.current_rating<2400):
                if(b==True):
                    self.current_rating+=15*k
                else:
                    self.current_rating-=15*k
            elif(self.current_rating>2400):
                if(b==True):
                    self.current_rating+=10*k
                else:
                    self.current_rating-=10*k
        return self.current_rating


print("Enter your name: ")
name=input()
 
print("Enter your year of birth: ")
year=int(input())
 
print("Enter your roll number: ")
roll_number=int(input())
 
print("Enter your current rating: ")
current_rating = float(input()) 

print("Enter you game history (opponent's rating) space separated with sign: ")
X=input().split()
L=list(X)

if current_rating !=0:
    print("Enter the number of games you have played in your career: ")
    m=int(input())

obj= chessplayer(name, year, roll_number, current_rating,L)
 
print()
print("***************************************")
print("Name", obj.name)
print("Age", obj.age())
print("Roll no", obj.roll_number)
 
if current_rating ==0:
    print("Your Performance rating is: ",obj.unrated())

else:
    print("Your New Rating is: ",obj.elo(m))
print()
print("***************************************")