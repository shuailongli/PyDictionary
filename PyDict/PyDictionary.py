from __future__ import unicode_literals
from cmd import Cmd
import os
import re
from time import sleep
from AudioProcessor import speak
from youtube_dl import YoutubeDL
from google_trans_new import google_translator
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

class Vocaulary:
    def __init__(self):
        self.word=""
        self.meaning=""
        self.example=""
        self.number=0

class Sentence:
    def __init__(self):
        self.sentence=""
        self.number=0

class Listening:
    def __init__(self):
        self.id=""
        self.name=""
        self.link=""
        self.duration=""
        self.number=0

class MyPrompt(Cmd):
    prompt = 'PyDict> '
    intro = "Start English Learning Mode! Type ? to list commands"

    SpeechMode=True
    VocabularyMode=False
    ListeningMode=False
    SentenceMode=False
    
    words=[]
    sentences=[]
    audios=[]
    
    def ReadVocabulary(self):
        self.words=[]
        fread=open("storage/vocabulary.txt",'r')
        readlines=fread.read().split('\n')
        fread.close()
        linecount=0
        canread=False
        for line in readlines:
            linecount+=1
            #words=list(line.split(" "))
            if line=="###":
                canread=True
                linecount=0
                tmp_word=Vocaulary()
            if linecount==1 and canread: tmp_word.word=line
            if linecount==2 and canread: tmp_word.meaning=line
            if linecount==3 and canread: tmp_word.example=line
            if linecount==4 and canread:
                tmp_word.number=line
                self.words.append(tmp_word)
                canread=False

    def WriteVocabulary(self):
        fwrite=open("storage/vocabulary.txt",'w')
        for tmpword in self.words:
            fwrite.write("###\n")
            fwrite.write(tmpword.word+"\n")
            fwrite.write(tmpword.meaning+"\n")
            fwrite.write(tmpword.example+"\n")
            fwrite.write(str(tmpword.number)+"\n")
        fwrite.close()

    def ReadSentence(self):
        self.sentences=[]
        fread=open("storage/sentence.txt",'r')
        readlines=fread.read().split('\n')
        fread.close()
        linecount=0
        canread=False
        for line in readlines:
            linecount+=1
            #words=list(line.split(" "))
            if line=="###":
                linecount=0
                canread=True
                tmp_sentence=Sentence()
            if linecount==1 and canread: tmp_sentence.sentence=line
            if linecount==2 and canread:
                tmp_sentence.number=line
                self.sentences.append(tmp_sentence)
                canread=False

    def WriteSentence(self):
        fwrite=open("storage/sentence.txt",'w')
        for tmpsentence in self.sentences:
            fwrite.write("###\n")
            fwrite.write(tmpsentence.sentence+"\n")
            fwrite.write(str(tmpsentence.number)+"\n")
        fwrite.close()

    def ReadListening(self):
        self.audios=[]
        fread=open("storage/listening.txt",'r')
        readlines=fread.read().split('\n')
        fread.close()
        linecount=0
        canread=False
        for line in readlines:
            linecount+=1
            #words=list(line.split(" "))
            if line=="###":
                linecount=0
                canread=True
                tmp_audio=Listening()
            if linecount==1 and canread: tmp_audio.id=line
            if linecount==2 and canread: tmp_audio.name=line
            if linecount==3 and canread: tmp_audio.link=line
            if linecount==4 and canread: tmp_audio.duration=line
            if linecount==5 and canread:
                tmp_audio.number=line
                self.audios.append(tmp_audio)
                canread=False

    def WriteListening(self):
        fwrite=open("storage/listening.txt",'w')
        for tmpaudio in self.audios:
            fwrite.write("###\n")
            fwrite.write(tmpaudio.id+"\n")
            fwrite.write(tmpaudio.name+"\n")
            fwrite.write(tmpaudio.link+"\n")
            fwrite.write(tmpaudio.duration+"\n")
            fwrite.write(str(tmpaudio.number)+"\n")
        fwrite.close()
    
    
    def do_exit(self, inp):
        #print("Bye")
        return True
    
    def help_exit(self):
        print("     exit the application. Shorthand: x q Ctrl-D.")
    
    def do_set(self,inp):
        if not inp.strip():
            print("     set mute    : mute the sound while playing")
            print("     set unmute  : play the sound while playing")
        elif inp.strip()=="mute": self.SpeechMode=False
        elif inp.strip()=="unmute": self.SpeechMode=True
        else:
            print("     set mute    : mute the sound while playing")
            print("     set unmute  : play the sound while playing")

    def help_set(self):
        print("     set mute    : mute the sound while playing")
        print("     set unmute  : play the sound while playing")

    def complete_set(self, text, line, begidx, endidx):
        FRIENDS=["mute","unmute"]
        if not text:
            completions = FRIENDS[:]
        else:
            completions = [ f
                           for f in FRIENDS
                           if f.startswith(text)
                           ]
        return completions
    
    def do_add(self,inp):
        if (not len(list(inp.split(" ")))==1 or not inp.strip()) and not self.VocabularyMode and not self.ListeningMode and not self.SentenceMode:
                print("     add vocabulary   : add a new word")
                print("     add sentence     : add a new sentence")
                print("     add listening    : add a new audio for listening")
                return
        elif inp.strip()=="vocabulary" or self.VocabularyMode:
            word=input("word: ")
            meaning=input("meaning: ")
            example=input("example: ")
            if word in [ele.word for ele in self.words]: print("    "+word, "already exits")
            elif not word.strip(): print("      word cannot be empty.")
            else:
                print("---Added word: ")
                print("   *",word)
                print("   *",meaning)
                print("   *",example)
                self.ReadVocabulary()
                tmp_word=Vocaulary()
                tmp_word.word=word
                tmp_word.meaning=meaning
                tmp_word.example=example
                tmp_word.number=0
                self.words.append(tmp_word)
                self.WriteVocabulary()
        elif inp.strip()=="sentence" or self.SentenceMode:
            sentence=input("sentence: ")
            print("---Added sentence: ")
            print("   *",sentence)
            if not sentence.strip(): print("    sentence cannot be empty")
            else:
                self.ReadSentence()
                tmp_sentence=Sentence()
                tmp_sentence.sentence=sentence
                tmp_sentence.number=0
                self.sentences.append(tmp_sentence)
                self.WriteSentence()
        elif inp.strip()=="listening" or self.ListeningMode:
            link=input("Youtube link: ")
            if not link.strip():
                print("     link cannot be empty")
                return
            name=input("name: ")
            ydl_opts = {'format': 'bestaudio/best',
                'postprocessors': [{
                               'key': 'FFmpegExtractAudio',
                               'preferredcodec': 'mp3',
                               'preferredquality': '192',
                               }],
                'outtmpl': 'storage/ListeningAudio/%(id)s.%(ext)s',
                }
            ydl = YoutubeDL(ydl_opts)
            info_dict = ydl.extract_info(link, download=True)
            if not name.strip(): name=info_dict.get("title", None)
            id=info_dict.get("id", None)
            #os.system("cp storage/ListeningAudio/"+id+"* /Users/shuailongli/Library/Mobile\ Documents/com\~apple\~CloudDocs/Desktop/EnlighListening/")
            duration=info_dict.get("duration", None)
            duration=str(int(duration/60))+":"+str(duration%60)
            print("---Added vieo")
            print("   *",id)
            print("   *",name)
            print("   *",link)
            print("   *",duration)
            self.ReadListening()
            tmp_audio=Listening()
            tmp_audio.id=id
            tmp_audio.name=name
            tmp_audio.link=link
            tmp_audio.duration=duration
            tmp_audio.number=0
            self.audios.append(tmp_audio)
            self.WriteListening()

    def help_add(self):
        print("     add vocabulary   : add a new word")
        print("     add sentence     : add a new sentence")
        print("     add listening    : add a new audio for listening")

    def complete_add(self, text, line, begidx, endidx):
        FRIENDS=["vocabulary","sentence","listening"]
        if not text:
            completions = FRIENDS[:]
        else:
            completions = [ f
                           for f in FRIENDS
                           if f.startswith(text)
                           ]
        return completions

    def do_vocabulary(self,inp):
        self.VocabularyMode=True
        self.ListeningMode=False
        self.SentenceMode=False
        print("---entered vocabulary mode")

    def help_vocabulary(self):
        print("---enter the vocabulary review mode")

    def do_sentence(self,inp):
        self.VocabularyMode=False
        self.ListeningMode=False
        self.SentenceMode=True
        print("---entered sentence mode")
    
    def help_sentence(self):
        print("---enter the sentence review mode")

    def do_listening(self,inp):
        self.VocabularyMode=False
        self.ListeningMode=True
        self.SentenceMode=False
        print("---entered listening mode")

    def help_listening(self):
        print("---enter the listening practice mode")

    def do_all(self,inp):
        self.ReadVocabulary()
        self.ReadListening()
        self.ReadSentence()
        if not self.VocabularyMode and not self.ListeningMode and not self.SentenceMode:
            if not len(list(inp.split(" ")))==1 or not inp.strip():
                print("     all vocabulary   : display all words")
                print("     all sentence     : display all sentences")
                print("     all listening    : display all audios for listening")
                print("     or use 'all' after entering any mode")
                return
            elif inp.strip()=="vocabulary":
                for word in self.words:
                    print("   *",word.word)
                    print("   *",word.meaning)
                    print("   *",word.example)
                    print("   *",word.number)
                    print("---------------------")
            elif inp.strip()=="sentence":
                for sentence in self.sentences:
                    print("   *",sentence.sentence)
                    print("   *",sentence.number)
            elif inp.strip()=="listening":
                for audio in self.audios:
                    print("   *",audio.id)
                    print("   *",audio.name)
                    print("   *",audio.link)
                    print("   *",audio.duration)
                    print("   *",audio.number)
                    print("---------------------")
            else:
                print("     unknown command '{}'".format(inp))
                print("     all vocabulary   : display all words")
                print("     all sentence     : display all sentences")
                print("     all listening    : display all audios for listening")
                print("     or use 'all' after entering any mode")
                return
        elif self.VocabularyMode and not self.ListeningMode and not self.SentenceMode:
            if len(list(inp.split(" ")))>1:
                print("     all/all vocabulary  : display all words")
                print("     all sentence        : display all sentences")
                print("     all listening       : display all audios for listening")
                print("     or all+anything to search for")
                return
            elif inp.strip()=="vocabulary" or not inp.strip():
                for word in self.words:
                    print("   *",word.word)
                    print("   *",word.meaning)
                    print("   *",word.example)
                    print("   *",word.number)
                    print("---------------------")
            elif inp.strip()=="sentence":
                for sentence in self.sentences:
                    print("   *",sentence.sentence)
                    print("   *",sentence.number)
            elif inp.strip()=="listening":
                for audio in self.audios:
                    print("   *",audio.id)
                    print("   *",audio.name)
                    print("   *",audio.link)
                    print("   *",audio.duration)
                    print("   *",audio.number)
                    print("---------------------")
            else:
                tmpwords=[ele.word for ele in self.words]
                targetstr=inp.strip()
                findwords=[]
                for ele in tmpwords:
                    if re.match(targetstr+".+",ele) or targetstr==ele: findwords.append(ele)
                findwords.sort()
                for ele in findwords:
                    print("   *",self.words[tmpwords.index(ele)].word)
                    print("   *",self.words[tmpwords.index(ele)].meaning)
                    print("   *",self.words[tmpwords.index(ele)].example)
                    print("   *",self.words[tmpwords.index(ele)].number)
                    print("---------------------")
                
        elif not self.VocabularyMode and not self.ListeningMode and self.SentenceMode:
            if inp.strip()=="vocabulary":
                for word in self.words:
                    print("   *",word.word)
                    print("   *",word.meaning)
                    print("   *",word.example)
                    print("   *",word.number)
                    print("---------------------")
            elif inp.strip()=="sentence" or not inp.strip():
                for sentence in self.sentences:
                    print("   *",sentence.sentence)
                    print("   *",sentence.number)
            elif inp.strip()=="listening":
                for audio in self.audios:
                    print("   *",audio.id)
                    print("   *",audio.name)
                    print("   *",audio.link)
                    print("   *",audio.duration)
                    print("   *",audio.number)
                    print("---------------------")
            else:
                tmpsentences=[ele.sentence for ele in self.sentences]
                if not (inp.strip() in tmpsentences):
                    print(inp.strip()+" is not in notes")
                    return
                else:
                    target=self.sentences[tmpsentences.index(inp.strip())]
                    print("   *",target.sentence)
                    print("   *",target.number)
                    print("---------------------")
        elif not self.VocabularyMode and self.ListeningMode and not self.SentenceMode:
            if len(list(inp.split(" ")))>1:
                print("     all vocabulary      : display all words")
                print("     all sentence        : display all sentences")
                print("     all/all listening   : display all audios for listening")
                return
            elif inp.strip()=="vocabulary":
                for word in self.words:
                    print("   *",word.word)
                    print("   *",word.meaning)
                    print("   *",word.example)
                    print("   *",word.number)
                    print("---------------------")
            elif inp.strip()=="sentence":
                for sentence in self.sentences:
                    print("   *",sentence.sentence)
                    print("   *",sentence.number)
            elif inp.strip()=="listening" or not inp.strip():
                for audio in self.audios:
                    print("   *",audio.id)
                    print("   *",audio.name)
                    print("   *",audio.link)
                    print("   *",audio.duration)
                    print("   *",audio.number)
                    print("---------------------")
            else:
                print("     all vocabulary      : display all words")
                print("     all/all sentence    : display all sentences")
                print("     all listening       : display all audios for listening")
                return
        else: return

    def help_all(self):
        print("     display the notes")

    def complete_all(self, text, line, begidx, endidx):
        FRIENDS=["vocabulary","sentence","listening"]
        self.ReadVocabulary()
        self.ReadSentence()
        self.ReadListening()
        if self.VocabularyMode and not self.ListeningMode and not self.SentenceMode:
            FRIENDS.extend([ele.word for ele in self.words])
        if not self.VocabularyMode and not self.ListeningMode and self.SentenceMode:
            FRIENDS.extend([ele.sentence for ele in self.sentences])
        if not self.VocabularyMode and self.ListeningMode and not self.SentenceMode:
            FRIENDS.extend([ele.id for ele in self.audios])
        if not text:
            completions = FRIENDS[:]
        else:
            completions = [ f
                           for f in FRIENDS
                           if f.startswith(text)
                           ]
        return completions

    def do_play(self,inp):
        if self.VocabularyMode and not self.ListeningMode and not self.SentenceMode:
            self.ReadVocabulary()
            if not inp.strip():
                for word in self.words:
                    print("   *",word.word)
                    print("   *",word.meaning)
                    print("   *",word.example)
                    print("   *",word.number)
                    print("---------------------")
                    if self.SpeechMode:
                        speak(word.word)
                        speak(word.meaning)
                        speak(word.example)
                        sleep(1)
                    else: sleep(3)
            else:
                tmpwords=[ele.word for ele in self.words]
                if not (inp.strip() in tmpwords):
                    print(inp.strip()+" is not in notes")
                    return
                else:
                    target=self.words[tmpwords.index(inp.strip())]
                    print("   *",target.word)
                    print("   *",target.meaning)
                    print("   *",target.example)
                    print("   *",target.number)
                    print("---------------------")
                    if self.SpeechMode:
                        speak(target.word)
                        speak(target.meaning)
                        speak(target.example)
        elif not self.VocabularyMode and not self.ListeningMode and self.SentenceMode:
            self.ReadSentence()
            if not inp.strip():
                for sentence in self.sentences:
                    print("   *",sentence.sentence)
                    print("   *",sentence.number)
                    print("---------------------")
                    if self.SpeechMode:
                        speak(sentence.sentence)
                    else: sleep(3)
            else:
                tmpsentences=[ele.sentence for ele in self.sentences]
                if not (inp.strip() in tmpsentences):
                    print(inp.strip()+" is not in notes")
                    return
                else:
                    target=self.sentences[tmpsentences.index(inp.strip())]
                    print("   *",target.sentence)
                    print("   *",target.number)
                    print("---------------------")
                    if self.SpeechMode:
                        speak(target.sentence)
        elif not self.VocabularyMode and self.ListeningMode and not self.SentenceMode:
            self.ReadListening()
            if not self.SpeechMode:
                print("     Can't play audios in mute mode. Switch to umute mode by: set unmute")
            else:
                if not inp.strip():
                    for audio in self.audios:
                        print("   *",audio.id)
                        print("   *",audio.name)
                        print("   *",audio.link)
                        print("   *",audio.duration)
                        print("   *",audio.number)
                        print("---------------------")
                        os.system("afplay storage/ListeningAudio/"+audio.id+".mp3")
                else:
                    idlist=[ele.id for ele in self.audios]
                    if not (inp.strip() in idlist):
                        print(inp.strip()+" is not in notes")
                        return
                    audio=self.audios[idlist.index(inp)]
                    print("   *",audio.id)
                    print("   *",audio.name)
                    print("   *",audio.link)
                    print("   *",audio.duration)
                    print("   *",audio.number)
                    print("---------------------")
                    os.system("afplay storage/ListeningAudio/"+audio.id+".mp3")
        else:
            print("   enter vocabulary/sentence/listening mode")
            print("   play word/sentence/audio_id  : play elements in notes")
    
    def help_play(self):
        print("     play the note")

    def complete_play(self, text, line, begidx, endidx):
        self.ReadVocabulary()
        self.ReadSentence()
        self.ReadListening()
        if self.VocabularyMode and not self.ListeningMode and not self.SentenceMode:
            FRIENDS=[ele.word for ele in self.words]
        if not self.VocabularyMode and not self.ListeningMode and self.SentenceMode:
            FRIENDS=[ele.sentence for ele in self.sentences]
        if not self.VocabularyMode and self.ListeningMode and not self.SentenceMode:
            FRIENDS=[ele.id for ele in self.audios]
        if not text:
            completions = FRIENDS[:]
        else:
            completions = [ f
                       for f in FRIENDS
                       if f.startswith(text)
                       ]
        return completions

    def do_remove(self,inp):
        if self.VocabularyMode and not self.ListeningMode and not self.SentenceMode:
            self.ReadVocabulary()
            tmpwords=[ele.word for ele in self.words]
            if not (inp.strip() in tmpwords):
                print(inp.strip()+" is not in notes")
                return
            else: target=self.words[tmpwords.index(inp.strip())]
            print("Are you sure to remove: ")
            print("   *",target.word)
            print("   *",target.meaning)
            print("   *",target.example)
            print("   *",target.number)
            confirm=input("(y/n): ")
            if confirm=="y":
                self.words.remove(target)
                self.WriteVocabulary()
                print(target.word, "removed from notebook")
            else: return
        elif not self.VocabularyMode and not self.ListeningMode and self.SentenceMode:
            self.ReadSentence()
            tmpsentences=[ele.sentence for ele in self.sentences]
            if not (inp.strip() in tmpsentences):
                print(inp.strip()+" is not in notes")
                return
            else:
                target=self.sentences[tmpsentences.index(inp.strip())]
                print("---Are you sure to remove: ")
                print("   *",target.sentence)
                print("   *",target.number)
                confirm=input("(y/n): ")
                if confirm=="y":
                    self.sentences.remove(target)
                    self.WriteSentence()
                    print("sentence removed from notebook")
                else: return
        elif not self.VocabularyMode and self.ListeningMode and not self.SentenceMode:
            self.ReadListening()
            tmpaudios=[ele.id for ele in self.audios]
            if not (inp.strip() in tmpaudios):
                print("     "+inp.strip()+" is not in notes")
                return
            else:
                target=self.audios[tmpaudios.index(inp.strip())]
                print("---Are you sure to remove: ")
                print("   *",target.id)
                print("   *",target.name)
                print("   *",target.link)
                print("   *",target.duration)
                print("   *",target.number)
                confirm=input("(y/n): ")
                if confirm=="y":
                    self.audios.remove(target)
                    os.system("rm storage/ListeningAudio/"+target.id+"*")
                    #os.system("rm /Users/shuailongli/Library/Mobile\ Documents/com\~apple\~CloudDocs/Desktop/EnlighListening/"+target.id+"*")
                    self.WriteListening()
                    print(target.id, " removed from notebook")
                else: return
        else:
            print("   enter vocabulary/sentence/listening mode")
            print("   remove word/sentence/audio_id  : remove elements in notes")

    def help_remove(self):
        print("     remove elements")

    def complete_remove(self, text, line, begidx, endidx):
        self.ReadVocabulary()
        self.ReadSentence()
        self.ReadListening()
        if self.VocabularyMode and not self.ListeningMode and not self.SentenceMode:
            FRIENDS=[ele.word for ele in self.words]
        if not self.VocabularyMode and not self.ListeningMode and self.SentenceMode:
            FRIENDS=[ele.sentence for ele in self.sentences]
        if not self.VocabularyMode and self.ListeningMode and not self.SentenceMode:
            FRIENDS=[ele.id for ele in self.audios]
        if not text:
            completions = FRIENDS[:]
        else:
            completions = [ f
                           for f in FRIENDS
                           if f.startswith(text)
                           ]
        return completions
    
    def do_speak(self,inp):
        if not inp.strip():
            print("     speak sentence      : speak the sentence")
            return
        if not self.SpeechMode:
            print("      Can't speak in mute mode. Switch by 'set unmute'")
        else: speak(inp.strip())
            
    def help_speak(inp):
        print("     speak sentence      : speak the sentence")
    
    def do_translate(self,inp):
        if not inp.strip():
            print("     translate sentence      : translate the sentence to chinese")
            return
        elif len(list(inp.split(" ")))==1:
            chrome_options = Options()
            chrome_options.add_argument('--headless')
            chrome_options.add_argument('--window-size=1920x1080')
            driver = webdriver.Chrome(options=chrome_options,executable_path='./chromedriver')
            url = 'http://gdictchinese.freecollocation.com/search/?q='+inp
            driver.get(url)
            sleep(0.5)
            soup = BeautifulSoup(driver.page_source, 'html.parser')
            meanings=soup.find_all('div',class_='meaning')
            meaning_count=0
            if len(meanings)==0:
                translator = google_translator()
                name=translator.translate(inp,lang_tgt='zh-cn')
                print(name)
                return
            print()
            for meaning in meanings:
                meaning_count+=1
                print(str(meaning_count)+". "+meaning.contents[0])
                examples=meaning.find_all('div',class_='example')
                for example in examples:
                    print("   -"+example.text)
                print()
        else:
            translator = google_translator()
            name=translator.translate(inp,lang_tgt='zh-cn')
            print(name)
    
    def help_translate(inp):
        print("     speak sentence      : translate the sentence to chinese")
    
    def do_dictionary(self,inp):
        if not inp.strip():
            print("     dictionary vocabulary      : look up the vocabulary in dictionary")
            return


    def help_dictionary(inp):
        print("     dictionary vocabulary      : look up the vocabulary in dictionary")

    def default(self, inp):
        if inp == 'x' or inp == 'q':
            return self.do_exit(inp)
        print("     {}: command not found".format(inp))

if __name__ == '__main__':
    MyPrompt().cmdloop()
