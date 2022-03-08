#######################################################
#
# COSC 140 Homework 3: ghost
#
#######################################################

def load_wordlist():
    '''
    Function written for you that reads contents of words.txt and 
    returns a list of words, each word in uppercase.
    '''
    wordlist = []
    with open("words.txt") as infile:
        for line in infile:
            wordlist.append(line.strip().upper())
    return wordlist

  
def getletter (name):
    #if input is NOT a single letter of the alphabet
  while True:
    letter = input (name + ", please enter a letter.")
    if len(letter) != 1 or letter == " " or not letter.isalpha(): 
      # print an error message and tell player to enter another letter
      print (name + ', the letter you have entered is not valid. Please enter a single letter, no space or illegal characters.')
      # if it is a valid letter, add letter to ghostword string, then print what the current word is, then leave the loop      
    else: 
      return letter.upper()

# getletter('rachel')


def fullword(ghostword, words):
  if len(ghostword) > 3 and ghostword in words:
    return True
  return False
 
def  startsword (ghostword, words):
  for line in words:
    if line.startswith(ghostword):
      return True
  return False 

def checklost (ghostword, words):
  if fullword (ghostword, words) == True or startsword (ghostword, words) == False: 
    return True
  return False
  #true means someone lost
  #false means keep going, no one lost



  
def main():
  words = load_wordlist()
  print(f"{len(words)} words loaded.")

  #ask player for their name and then capitalize the first letter of their names
  playercount = 1 
  
  player1 = input (str("Player one, please enter your name."))
  player1= player1.capitalize()
  player2 = input (str ("Player two, please enter your name."))
  player2= player2.capitalize()
 

  ghostword= ""
  playernum = 1 
  while checklost (ghostword, words) == False:
    if playernum == 1:
      letter = getletter (player1)
      ghostword += letter.upper()
      print ("Your current word is now: " +
ghostword)
      playernum += 1
    elif playernum == 2:
      letter = getletter (player2)
      ghostword += letter.upper()
      print ("Your current word is now: " +
ghostword)
      playernum -= 1
  print ("Game over! Ghostword is not valid.")
  
 



main()
