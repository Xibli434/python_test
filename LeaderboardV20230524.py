from tkinter import *
from tkinter import simpledialog
from tkinter import messagebox
import random
import time
window=Tk()
myForwardX=1
myForwardY=1
Leader=[]
def LeaderboardSort(oldList, oldnameList):
    
    messagebox.showinfo("Sort my Score history")
    '''for j in range(10,1,-1):
        #print(j)
    
        for i in range(j):
            if oldList[i]<oldList[i+1]:
               sub=oldList[i]
            subname=oldnameList[i]
            oldList[i]=oldList[i+1]
            oldnameList[i]=oldnameList[i+1]
            oldList[i+1]=sub
            oldnameList[i+1]=subname'''
        
                
    print(oldList)

#for test leadboard sort structure
def testLeaderboard():
    testList=[1,2,3,5,7,8,0,0,0,0]
    testnameList=['a','b','c'] 
    LeaderboardSort(testList, testnameList)


canvas=Canvas(window,width=500,height=400,background="blue")
canvas.pack()
squareHandle=canvas.create_rectangle(30,35,150,50,fill="indigo",outline="black",activefill="white")
scoreText=StringVar()
scoreText.set("Your Score: ")
myLabel=Label(window,textvariable=scoreText,width=20).pack()

ovalHandle=canvas.create_oval(300,300,500,350,fill="aquamarine",outline="white",activefill="black")
def moveGraph(event):
    if event.keysym=="Up":
        canvas.move(ovalHandle,0,-20)
    if event.keysym=="Down":
        canvas.move(ovalHandle,0,20)
    if event.keysym=="Left":
        canvas.move(ovalHandle,-20,0)
    if event.keysym=="Right":
        canvas.move(ovalHandle,20,0)
 #move keys for player
myScore=0  
def movesquare(): 
    global myForwardX,myForwardY,myScore  
    myco=canvas.coords(squareHandle)
        
    myX1, myY1,myX2,myY2=myco
    collison0bjList=canvas.find_overlapping(myX1,myY1,myX2,myY2)
    #window.title(myForwardY)
  
    if ovalHandle in collison0bjList:
        myForwardY=-1
        #window.title(myForwardY)
        
        
        myScore=myScore+1
        scoreText.set("Your score is: " + str(myScore))
        window.title(myScore)
    if myX1>450:
        myForwardX=-1
    if myX1<30:
        myForwardX=1

 
    if myY1<20:
        myForwardY=1
    if myY1>450:
        #process for gameover
        myForwardY=-1
        Leaderboard=[]
        
    
      

    openHandle=open("history.log","a+")
    openHandle.seek(0)
    historyTxt=openHandle.read()
    myUsername=simpledialog.askstring("Congradulations for Your Score","What is Your Name") 
    openHandle.write('\n'+myUsername+'\n'+" ,"+ str(myScore))
    openHandle.seek(0)
    record=openHandle.read()
    messagebox.askretrycancel("Leader Board",record)
       
    openHandle.close()
        
    if messagebox.askretrycancel(title="Andrew's Game",message="Game over!Do you want to try again or end the game"):
            myUsername2=simpledialog.askstring("my_game","how is the experience")
         
            if len(myUsername2)<=1:
                myUsername2="Mysterio"
            myUsername2=myUsername2+","+str(myScore)
            openHandle.write('\n'+myUsername2)
            openHandle.close()
            myForwardX=1
            myForwardY=1
            myScore=0
            scoreText.set("Your Score:"+str(myScore))
            canvas.coords(squareHandle,80,100,90,150)
            myX1=80
            myX2=100
            myY1=90  
            myY2=150
    else:
            openHandle.close()
            window.quit()
  

    
    canvas.coords(squareHandle,myX1+ myForwardX *3,myY1+myForwardY*3,myX2+myForwardX*3,myY2+myForwardY*3)
    window.update()
    canvas.after(10,movesquare)
    
oldList=[]
movesquare()
startButton=Button(window,text="Start Game",command=movesquare).pack()
#remember to comment above 2 lines after testing
testButton=Button(window,text="test leadboard",command=testLeaderboard).pack()


canvas.bind_all('<KeyPress-Up>', moveGraph)
canvas.bind_all('<KeyPress-Down>', moveGraph)
canvas.bind_all('<KeyPress-Left>', moveGraph)
canvas.bind_all('<KeyPress-Right>', moveGraph)
    
button=Button(window,text="Bye",command=window.quit,fg="red")
window.mainloop()



    


