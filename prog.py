import random
class karaoke :
    def __init__(self,name):
        self.name = name
        self.names = []
        self.musics 
        
    
    def __setSong__(self,nom):
        self.names.append(nom)
        
        
    def __play__(self):
        game = "on"
        playerAmount = 0
        playerStorage= []
        selectSong = 0


        print("how many peapole are playing ?")

        playerAmount = int(input())

        for i in range (playerAmount):
            print("enter your name here :")
            playerStorage.append(player(input()))
            print("welcome",playerStorage[i].name)

        while (game == "on"):

            print("choose a song")
            for i in range(self.musics):
                print("[1] :",self.names[i])
                
            selectSong = int(input())

            print("good Song playing.exe")

            for i in range(playerAmount):
                score = random.randint(50,100)
                print("player", playerStorage[i].name ,"you made a score of",score ,"/100")
                playerStorage[i].__setScore__(selectSong,score)

            print("what's next ? :")
            print("next song   [1]")
            print("show score  [2]")
            print("end here    [3]")

            awnser = int(input())
            if(awnser == 3):
                game == False

                break # sale mais efficace
            
            if(awnser == 2):
                print("who want to see his/her score ?")
                for i in range(playerAmount):
                    print(playerStorage[i].name,"    [",i,"]")

                rep = int(input())
                playerStorage[rep].__sortScore__()
                
                


class player :
    def __init__(self,name):
        karaoke.__init__(self,name)
        self.name = name
        self.scoreBoard = [0,0,0,0,0]
        
        self.bestScore = 0
        self.bestSong = 0
        
        self.worstScore = 200
        self.worstSong =0
    
    def __setScore__(self,song,newScore):
        if(self.scoreBoard[song]< newScore):
            self.scoreBoard[song] = newScore
    
    def __sortScore__(self):
        
        for i in range(5):
            
            if( self.bestScore < self.scoreBoard[i]):
                self.bestScore = self.scoreBoard[i]
                self.bestSong = i
                
            if(self.worstScore >self.scoreBoard[i]):
                self.worstScore = self.scoreBoard[i]
                self.worstSong = i
                
        print("your best score is",self.bestScore,"on the song number",self.bestSong)
        print("and your worst score is",self.worstScore,"ont the music number",self.worstSong)
        
        print("here are all your score on all song :")
        
        for i in range(5):
            print ("song",i + 1,":",self.scoreBoard[i])
            

#main 
print("create a karaoke :")
karaokeA = karaoke(input())

print("how many songs do you want ?")
rep = int(input())

karaokeA.musics = rep

for i in range(rep):
    print("choose a song name :")
    karaokeA.__setSong__(input())
    
    
karaokeA.__play__
    
#j'ai arrèter par manque de temps, excusez moi.