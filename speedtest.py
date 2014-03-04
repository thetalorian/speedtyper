#!/usr/bin/python
# -*- coding: utf-8 -*-
import random
import time
import sys
import curses
import locale
from string import Template

locale.setlocale(locale.LC_ALL,"")

class TestSettings:
  def __init__(self):
    settings = open('settings', "r")
    self.testlength = int(settings.readline().rstrip())
    self.level = int(settings.readline().rstrip())
    self.errlimit = int(settings.readline().rstrip())
    punct = int(settings.readline().rstrip())
    if punct == 1:
      self.usePunct = True
    else:
      self.usePunct = False
    settings.close()
    
class SpeedTest:
  def __init__(self, settings):
    self.level = settings.level
    
class Interface:
 
  def __init__(self, settings):
    self.settings = settings
    self.mode = "menu"
    self.exit = False
    self.stdscr = curses.initscr()


  def start(self):
    #Set up curses
    curses.cbreak()
    curses.curs_set(0)

    while 1:
      if self.mode == "menu":
        self.menumode()
      elif self.mode == "test":
        self.testmode()
      elif self.mode == "score":
        self.scoremode()

      if self.exit == True:
        break

    curses.nocbreak(); self.stdscr.keypad(0); curses.echo()
    curses.endwin()
    """
      elif mode == "test" and len(test) == 0:
        mode = "menu"
        stdscr.erase()
        stdscr.addstr(0,0,"Test complete")
        end = time.time()
        
        stdscr.addstr(2,0, 'Characters: ' + str(chars))
        stdscr.addstr(3,0, 'Words:      ' + str(atestlength))
        stdscr.addstr(4,0, 'Time: ' +  str(end-start) + "sec.")
        stdscr.addstr(5,0, '      ' +  str((end-start)/60) + "min.")
    
        werr = (failed / float(given)) * 100
        terr = (cerased / float(ctyped)) * 100
        err = (werr + terr) / 2
        if err > errlimit:
          record = False
        stdscr.addstr(7,0, 'Word Errors: ' + str(failed) + ' of ' + str(given) + ", " + str(werr) + "%")
        stdscr.addstr(8,0, 'Backspaces: ' + str(cerased) + ' of ' + str(ctyped) + " characters typed, " + str(terr) + "%")
        ##provide wpm based on average estimate of 5 characters per word, to
        ##ofset tests with predominately longer or shorter words
        secs = (end - start) - pausetime
        wpm = atestlength / (secs / 60)
        awpm = (chars / 5 ) / (secs / 60)
        stdscr.addstr(10,0, "Words per minute: " + str(wpm),curses.A_BOLD)
        stdscr.addstr(12,0, "Adjusted Words per minute: " + str(awpm),curses.A_BOLD)
        stdscr.addstr(13,0, "             Current Best: " + str(high[level - 1]))
        if record and awpm > high[level - 1]:
          stdscr.addstr(14,2,"You got a new top score!",curses.A_REVERSE)
          high[level - 1] = awpm
          settingchange = True
        if err > errlimit:
          stdscr.addstr(15,2,"Try to reduce errors.")
        c = stdscr.getch()
      elif mode == "pause":
        stdscr.erase()
        stdscr.addstr(1,8, 'Paused',curses.A_REVERSE)
        stdscr.addstr(2,8,str(testlength-len(test)) + "/" + str(testlength))
        stdscr.addstr( 4, 8,"\" < > P Y F G C R L ? +", curses.A_DIM)
        stdscr.addstr( 5, 8, "' , . p y f g c r l / =")
        stdscr.addstr( 7, 8, " A O E U I D H T N S _", curses.A_DIM)
        stdscr.addstr( 8, 8, " a o e u i d h t n s -")
        stdscr.addstr(10, 8, " : Q J K X B M W V Z", curses.A_DIM)
        stdscr.addstr(11, 8, " ; q j k x b m w v z")
        stdscr.addstr(13, 10, "Use 'q' to abort")
        c = stdscr.getch()
        pauseend = time.time()
        pausetime = pausetime + pauseend - pausestart
        mode = "test"
        if c == ord('q'):
          atestlength = testlength - len(test)
          record = False
          test = []
    
    if settingchange :
      settings = open('settings',"w")
      settings.write(str(testlength)+"\n")
      settings.write(str(level)+"\n")
      settings.write(str(errlimit)+"\n")
      settings.write(str(punct)+"\n")
      for score in high:
        settings.write(str(score)+"\n")
      """

  def menumode(self):
    stdscr = self.stdscr
    stdscr.erase()
    stdscr.addstr(0, 8, "Welcome to Dvorak Typing Trainer", curses.A_REVERSE)
    stdscr.addstr(2, 4, "Number of Words (W):" + str(self.settings.testlength))
    stdscr.addstr(" (E)rror Threshold: " + str(self.settings.errlimit)+ "%")
    stdscr.addstr(3, 4, "Level (L):" + str(self.settings.level))
    """
    if self.settings.level == 9:
      stdscr.addstr(" " + testword)
  
    stdscr.addstr(4, 5, "1: aoeuhtns (start positions)")
        stdscr.addstr(4, 35,"Top: " + str(high[0]) )
        stdscr.addstr(5, 5, "2: aoeuidhtns (home row)")
        stdscr.addstr(5, 35,"Top: " + str(high[1]) )
        stdscr.addstr(6, 5, "3: home row + cfklmprv")
        stdscr.addstr(6, 35,"Top: " + str(high[2]) )
        stdscr.addstr(7, 5, "4: home row + bgjqwxyz")
        stdscr.addstr(7, 35,"Top: " + str(high[3]) )
        stdscr.addstr(8, 5, "5: all letters")
        stdscr.addstr(8, 35,"Top: " + str(high[4]) )
        stdscr.addstr(9, 5, "6: home row + ',.[]/=;")
        stdscr.addstr(9, 35, "Top: " + str(high[5]))
        stdscr.addstr(10, 5, "7: home row + \"<>{}?+:")
        stdscr.addstr(10, 35, "Top: " + str(high[6]))
        stdscr.addstr(11, 5, "8: all keys")
        stdscr.addstr(11, 35, "Top: " + str(high[7]))
        stdscr.addstr(12, 5, "9: single word")
        stdscr.addstr(12, 35, "Top: " + str(high[8]))
        stdscr.addstr(13, 8, "g to Go, q to Quit, c to Change Word L9, r to Reset Scores")
        if punct:
          stdscr.addstr(14,2,"Punctuation")
        stdscr.move(14,10)
        stdscr.refresh()
        if level == 9 and testword == "":
          stdscr.addstr(14,0,"Test Word: ")
          testword = stdscr.getstr()
    """
        
    c = stdscr.getch()
    if c == ord('q'):
      self.exit = True
    elif c == ord('g'):
      self.mode = "test"
      
    """
        if c == ord('w'):
          settingchange = True
          stdscr.addstr(14,0,"New word count: ")
          testlength = int(stdscr.getstr())
        elif c == ord('c'):
          testword = ""
        elif c == ord('l'):
          settingchange = True
          stdscr.addstr(14,0,"New level: ")
          level = int(stdscr.getstr())
        elif c == ord('e'):
          settingchange = True
          stdscr.addstr(14,0,"New threshold: ")
          errlimit = int(stdscr.getstr())
        elif c == ord('r'):
          settingchange = True
          stdscr.addstr(14,0,"Reset Score for Level (0 for all): ")
          rlevel = int(stdscr.getstr())
          if rlevel == 0:
            for x in range(0,len(high)):
              high[x] = 0.0
          else:
            high[rlevel - 1] = 0.0
        elif c == ord('p'):
          settingchange = True
          if punct == 1:
            punct = 0
          else:
            punct = 1
        elif c == ord('g'):
          test = createtest()
        
        elif c == ord('q'):
          break
      """

  def testmode(self):
    test = speedTest(self.settings)
    stdscr = self.stdscr

    stdscr.erase()
    stdscr.addstr(1,8,str(test.startlength-len(test)) + "/" + str(testlength),curses.A_REVERSE)
    stdscr.addstr(5,5,test[0], viewat)
    if len(test) > 1:
      stdscr.addstr(4,5,test[1])
    if len(test) > 2:
      stdscr.addstr(3,5,test[2], curses.A_DIM)
    stdscr.addstr(7,6,word)
    while 1:
      c = stdscr.getch()
      if c == ord(' '):
        given = given + 1
        if word == test[0]:
          chars = chars + len(test[0])
          test.pop(0)
          viewat = curses.A_BOLD
        else:
          failed = failed + 1
          viewat = curses.A_REVERSE
        word = ""
        break
      elif c == 127:
        word = word[:-1]
        cerased = cerased + 1
        stdscr.addstr(7,6,word)
        stdscr.clrtoeol()
      #elif c == ord('+'):
      #  mode = "menu"
      #  break
      elif c == 10:
        mode = "pause"
        pausestart = time.time()
        break
      else :
        #stdscr.addstr(15,0,str(c) + "                 ")
        stdscr.refresh()
        ctyped = ctyped + 1
        word = word + chr(c)

def main():
  settings = TestSettings()
  interface = Interface(settings)
  interface.start()
  
if __name__ == "__main__":
  main()







"""
def okforlevel(newword, testchars) : 
  ok = True
  for letter in newword :
    ok = ok and letter in testchars
  return ok

def addpunct(word) :
  possiblepunct = []
  possiblepunct.append(Template('$word1$word2'))
  possiblepunct.append(Template('$word1$word2'))
  possiblepunct.append(Template('$word1$word2'))
  possiblepunct.append(Template('"$word1$word2"'))
  possiblepunct.append(Template("'$word1$word2'"))
  possiblepunct.append(Template('{$word1$word2}'))
  possiblepunct.append(Template('<$word1$word2>'))
  possiblepunct.append(Template('$word1$word2,'))
  possiblepunct.append(Template('$word1$word2.'))
  possiblepunct.append(Template('$word1$word2:'))
  possiblepunct.append(Template('$word1$word2;'))
  possiblepunct.append(Template('$word1$word2?'))
  possiblepunct.append(Template('$word1/$word2'))
  possiblepunct.append(Template('$word1\\$word2'))
  possiblepunct.append(Template('($word1$word2)'))
  possiblepunct.append(Template('[$word1$word2]'))
  possiblepunct.append(Template('$word1-$word2'))
  possiblepunct.append(Template('$word1-fucking-$word2'))
  possiblepunct.append(Template('$word1=$word2'))
  possiblepunct.append(Template('${word1}_$word2'))
  possiblepunct.append(Template('$word1+$word2'))
  possiblepunct.append(Template('$word1|$word2'))
  appliedpunct = random.choice(possiblepunct)
  splitpoint = random.randint(1,len(word))
  newword = appliedpunct.substitute(word1=word[:splitpoint], word2=word[splitpoint:])
  return newword

def creattest() :
  #Activating test mode, initializing test
  mode = "test"
  #Setting available characters
  testchars = "aoeuhtns"
  if level > 1 :
    testchars = testchars + "id"
  if level == 3 :
    testchars = testchars + "cfklmprv"
  if level == 4 :
    testchars = testchars + "bgjqwxyz"
  if level == 5 or level == 8:
    testchars = "abcdefghijklmnopqrstuvwxyz"
  if level == 6 :
    testchars = testchars + "',.[]/=;()"
  if level == 7 :
    testchars = testchars + "\"<>{}?+:"
  if level == 8 :
    testchars = testchars + "',.[]/=;\"<>{}?+:"
  #Initializing word set
  test = []
  testwords = 0
  while testwords < testlength :
    if level == 9:
      test.append(testword)
      testwords = testwords + 1
    else:
      newword = random.choice(words)
      if newword not in test and okforlevel(newword, testchars):
        test.append(newword)
        testwords = testwords + 1
  #Add punctuation
  if punct == 1:
    x = 0
    for word in test:
      test[x] = addpunct(word)
      x += 1
  word = ""
  pausetime = 0
  given = 0
  failed = 0
  ctyped = 0
  cerased = 0
  record = True
  atestlength = testlength
  viewat = curses.A_BOLD
  chars = 0
  start = time.time()

#Pull initial settings from file
settingchange = False
#Start main loop
words = [line.strip() for line in open('dict')]
mode = "menu"
testword = ""
while 1:
  if mode == "menu":
    stdscr.erase()
    stdscr.addstr(0, 8, "Welcome to Dvorak Typing Trainer", curses.A_REVERSE)
    stdscr.addstr(2, 4, "Number of Words (W):" + str(testlength))
    stdscr.addstr(" (E)rror Threshold: " + str(errlimit)+ "%")
    stdscr.addstr(3, 4, "Level (L):" + str(level))
    if level == 9:
      stdscr.addstr(" " + testword)
    stdscr.addstr(4, 5, "1: aoeuhtns (start positions)")
    stdscr.addstr(4, 35,"Top: " + str(high[0]) )
    stdscr.addstr(5, 5, "2: aoeuidhtns (home row)")
    stdscr.addstr(5, 35,"Top: " + str(high[1]) )
    stdscr.addstr(6, 5, "3: home row + cfklmprv")
    stdscr.addstr(6, 35,"Top: " + str(high[2]) )
    stdscr.addstr(7, 5, "4: home row + bgjqwxyz")
    stdscr.addstr(7, 35,"Top: " + str(high[3]) )
    stdscr.addstr(8, 5, "5: all letters")
    stdscr.addstr(8, 35,"Top: " + str(high[4]) )
    stdscr.addstr(9, 5, "6: home row + ',.[]/=;")
    stdscr.addstr(9, 35, "Top: " + str(high[5]))
    stdscr.addstr(10, 5, "7: home row + \"<>{}?+:")
    stdscr.addstr(10, 35, "Top: " + str(high[6]))
    stdscr.addstr(11, 5, "8: all keys")
    stdscr.addstr(11, 35, "Top: " + str(high[7]))
    stdscr.addstr(12, 5, "9: single word")
    stdscr.addstr(12, 35, "Top: " + str(high[8]))
    stdscr.addstr(13, 8, "g to Go, q to Quit, c to Change Word L9, r to Reset Scores")
    if punct:
      stdscr.addstr(14,2,"Punctuation")
    stdscr.move(14,10)
    stdscr.refresh()
    if level == 9 and testword == "":
      stdscr.addstr(14,0,"Test Word: ")
      testword = stdscr.getstr()
    
    c = stdscr.getch()
    if c == ord('w'):
      settingchange = True
      stdscr.addstr(14,0,"New word count: ")
      testlength = int(stdscr.getstr())
    elif c == ord('c'):
      testword = ""
    elif c == ord('l'):
      settingchange = True
      stdscr.addstr(14,0,"New level: ")
      level = int(stdscr.getstr())
    elif c == ord('e'):
      settingchange = True
      stdscr.addstr(14,0,"New threshold: ")
      errlimit = int(stdscr.getstr())
    elif c == ord('r'):
      settingchange = True
      stdscr.addstr(14,0,"Reset Score for Level (0 for all): ")
      rlevel = int(stdscr.getstr())
      if rlevel == 0:
        for x in range(0,len(high)):
          high[x] = 0.0
      else:
        high[rlevel - 1] = 0.0
    elif c == ord('p'):
      settingchange = True
      if punct == 1:
        punct = 0
      else:
        punct = 1
    elif c == ord('g'):
      test = createtest()
    elif c == ord('q'):
      break
  elif mode == "test" and len(test) > 0:
    stdscr.erase()
    stdscr.addstr(1,8,str(testlength-len(test)) + "/" + str(testlength),curses.A_REVERSE)
    stdscr.addstr(5,5,test[0], viewat)
    if len(test) > 1:
      stdscr.addstr(4,5,test[1])
    if len(test) > 2:
      stdscr.addstr(3,5,test[2], curses.A_DIM)
    stdscr.addstr(7,6,word)
    while 1:
      c = stdscr.getch()
      if c == ord(' '):
        given = given + 1
        if word == test[0]:
          chars = chars + len(test[0])
          test.pop(0)
          viewat = curses.A_BOLD
        else:
          failed = failed + 1
          viewat = curses.A_REVERSE
        word = ""
        break
      elif c == 127:
        word = word[:-1]
        cerased = cerased + 1
        stdscr.addstr(7,6,word)
        stdscr.clrtoeol()
      #elif c == ord('+'):
      #  mode = "menu"
      #  break
      elif c == 10:
        mode = "pause"
        pausestart = time.time()
        break
      else :
        #stdscr.addstr(15,0,str(c) + "                 ")
        stdscr.refresh()
        ctyped = ctyped + 1
        word = word + chr(c)
  elif mode == "test" and len(test) == 0:
    mode = "menu"
    stdscr.erase()
    stdscr.addstr(0,0,"Test complete")
    end = time.time()
    
    stdscr.addstr(2,0, 'Characters: ' + str(chars))
    stdscr.addstr(3,0, 'Words:      ' + str(atestlength))
    stdscr.addstr(4,0, 'Time: ' +  str(end-start) + "sec.")
    stdscr.addstr(5,0, '      ' +  str((end-start)/60) + "min.")

    werr = (failed / float(given)) * 100
    terr = (cerased / float(ctyped)) * 100
    err = (werr + terr) / 2
    if err > errlimit:
      record = False
    stdscr.addstr(7,0, 'Word Errors: ' + str(failed) + ' of ' + str(given) + ", " + str(werr) + "%")
    stdscr.addstr(8,0, 'Backspaces: ' + str(cerased) + ' of ' + str(ctyped) + " characters typed, " + str(terr) + "%")
    ##provide wpm based on average estimate of 5 characters per word, to
    ##ofset tests with predominately longer or shorter words
    secs = (end - start) - pausetime
    wpm = atestlength / (secs / 60)
    awpm = (chars / 5 ) / (secs / 60)
    stdscr.addstr(10,0, "Words per minute: " + str(wpm),curses.A_BOLD)
    stdscr.addstr(12,0, "Adjusted Words per minute: " + str(awpm),curses.A_BOLD)
    stdscr.addstr(13,0, "             Current Best: " + str(high[level - 1]))
    if record and awpm > high[level - 1]:
      stdscr.addstr(14,2,"You got a new top score!",curses.A_REVERSE)
      high[level - 1] = awpm
      settingchange = True
    if err > errlimit:
      stdscr.addstr(15,2,"Try to reduce errors.")
    c = stdscr.getch()
  elif mode == "pause":
    stdscr.erase()
    stdscr.addstr(1,8, 'Paused',curses.A_REVERSE)
    stdscr.addstr(2,8,str(testlength-len(test)) + "/" + str(testlength))
    stdscr.addstr( 4, 8,"\" < > P Y F G C R L ? +", curses.A_DIM)
    stdscr.addstr( 5, 8, "' , . p y f g c r l / =")
    stdscr.addstr( 7, 8, " A O E U I D H T N S _", curses.A_DIM)
    stdscr.addstr( 8, 8, " a o e u i d h t n s -")
    stdscr.addstr(10, 8, " : Q J K X B M W V Z", curses.A_DIM)
    stdscr.addstr(11, 8, " ; q j k x b m w v z")
    stdscr.addstr(13, 10, "Use 'q' to abort")
    c = stdscr.getch()
    pauseend = time.time()
    pausetime = pausetime + pauseend - pausestart
    mode = "test"
    if c == ord('q'):
      atestlength = testlength - len(test)
      record = False
      test = []

if settingchange :
  settings = open('settings',"w")
  settings.write(str(testlength)+"\n")
  settings.write(str(level)+"\n")
  settings.write(str(errlimit)+"\n")
  settings.write(str(punct)+"\n")
  for score in high:
    settings.write(str(score)+"\n")

#chars = 0
#while len(test) > 0:
#  print test[0] + " (", 
#  if len(test) > 1 :
#    print test[1],
#  if len(test) > 2 :
#    print test[2],
#  print ")"
#  uinput = raw_input(": ")
#  if (uinput == test[0]) :
#    chars = chars + len(test[0])
#    test.pop(0)
#
#end = time.time()
#print 'Characters: %s Time: %s seconds' % (chars, end-start)
##provide wpm based on average estimate of 7 characters per word, to
##ofset tests with predominately longer or shorter words
#wpm = (chars / 7 ) / ((end-start) / 60)
#print "Words per minute: %s" % (wpm)

"""
