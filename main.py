
import os 
import pandas as pd 
from pydub import AudioSegment
from gtts import gTTS




#pip install pyaudio 
#pip install pandas 
#pip install pydub 
#pip install gTTS
#This function convert text in to  speech filename.mp3 uesed package gtts
def texttospeech(text,filename):
    mytext=str(text)
    language='hi'
    myobj=gTTS(text=mytext,lang=language,slow=True)
    myobj.save(filename)
    
#This function returns pydub audio segment 
def mergemp3(audios):
    combined=AudioSegment.empty()
    for audio in audios:
        combined+=AudioSegment.from_mp3(audio)
    return combined    

    
# This function break mp3 in to pieces or part to part 
def generateSkeleton():
    audio=AudioSegment.from_mp3('railway.mp3')
     # 1 generate ktipaya dhayan dijiye 
    start=88000
    finish=90200
    audioprocessed=audio[start:finish]
    audioprocessed.export("1_hindi.mp3",format="mp3")
     # 2 is from city
    


    # 3- generate sey chalkar 
        #audio=AudioSegment.from_mp3("railway.mp3")
    start=91000
    finish=92200
    audioprocessed=audio[start:finish]
    audioprocessed.export("3_hindi.mp3",format="mp3")
    # 4 is via city 


    # 5 generte key raste 
    start =94000
    finish=95000
    audioprocessed=audio[start:finish]
    audioprocessed.export("5_hindi.mp3",format="mp3")

    #6 is to city 



    #7 generate  janeywaley gadi sankhya
    start=96000
    finish=98900
    audioprocesed=audio[start:finish]
    audioprocesed.export("7_hindi.mp3",format="mp3")

    # 8 is train no and name 

    #Generate kuch hi samaye mey platform sankhya
    start=105500
    finish=108200
    audioprocessed=audio[start:finish]
    audioprocesed.export("9_hindi.mp3",format="mp3")
     # 10 is platform number 

    # 11  Generate parr a rahi hey 
    start=109000
    finish=112250
    audioprocesed=audio[start:finish]
    audioprocesed.export("11_hindi.mp3",format="mp3")



    
#This function takes only excel file  name filename that is used in function which use pandas lib to read the file 
def generateanouncement(filename):
    df=pd.read_excel(filename)
    print(df)
    for index,item in  df.iterrows():


    #2 Generator from city
        texttospeech(item['from'],'2_hindi.mp3')
#4 Generator via city 
        texttospeech(item['via'],'4_hindi.mp3')

#6 Generator to city 
        texttospeech(item['to'],'6_hindi.mp3')
#8 Generator train no and name
        texttospeech(item['train_no'] + "  " + item['train_name'],'8_hindi.mp3')
#10 Generator platform number 
        texttospeech(item['platform'],'10_hindi.mp3')

        audios=[f"{i}_hindi.mp3"  for i in range(1,12)]
        anouncement=mergemp3(audios)
        anouncement.export(f"Anoumcement_{item['train_no']}_{item[index +1]}.mp3",format="mp3")


 





if __name__=="__main__":
    print("Generating section ")
    generateSkeleton()
    print("Now Generating Anouncement")
    generateanouncement("announce_hindi.xlsx")