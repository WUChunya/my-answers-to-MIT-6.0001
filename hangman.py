# Problem Set 2, hangman.py
# Name: 
# Collaborators:
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()
secret_word = choose_word(wordlist)
secret_word_list = list(secret_word)
letters_guessed = list()
secret_word_list_copy = secret_word_list.copy()
print("---------------------Previous------------------------")

def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    wrong_guess_times = 0
    if secret_word_list not in letters_guessed:
        wrong_guess_times += 1
    if wrong_guess_times > 0:
        return False
    else:
        return True 
    #the variation wrong_guess_times counts how many words in secret_word_list are missed in guessing.
    #as long as the counts is bigger than 0, the secret word hasn't be totally guessed.

print("secret_word =",secret_word)
print("secret_word_list =",secret_word_list)
print("letters_guessed =",letters_guessed)
print(is_word_guessed(secret_word, letters_guessed)) 
#print every important objects out to check if it's correct.

print("Did you win the game?")
if is_word_guessed(secret_word, letters_guessed) == False:
    print("sorry, you need to continue." )
else: 
    print("Yeah congratulations!")
#add another small part to visualize the output better.       
print("---------------------Question1A------------------------")

    


def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    secret_word_list_copy = secret_word_list.copy()
    # the secret_word_list is a List(mutable). Copy once to prevent changing the original data. 
    for words in secret_word_list_copy:
        if words not in letters_guessed:
    #this two lines select words which were not found yet and should be hiden
            position = secret_word_list_copy.index(words)
            #to find out the order of hidden part in secret word
            secret_word_list_copy[position] = '_ '
        #replace them with underscore followed by a space as required
    return secret_word_list_copy


print(get_guessed_word(secret_word, letters_guessed))
print(secret_word_list)
#to check if the original list was changed
print("---------------------Question1B------------------------")



def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    letters_guessed_copy = letters_guessed.copy()
    available_letters=[]
    for words in string.ascii_lowercase:
        if words not in letters_guessed_copy:
            available_letters += words
    return available_letters

print(get_available_letters(letters_guessed))    
#very much alike question1B. just replace the initeration from secret_word_list_copy to available_letters
print("---------------------Question1C------------------------")



def hangman(secret_word):
        #basic conditions for the funcition
        print("Welcome to the game Hangman! ")
        print("I am thinking of a word that is ", len(secret_word) ," letters long." )
        print("----------------------------------------------------")
        available_letters = string.ascii_lowercase
        letters_guessed = list()
        time=0      
        n=6 #chances for player
        x=3 #warning chances
        vowel = ("e","i","o","a")
        
        #basic loops for game circle within n times
        while time < n: 
            print("Available letters:", available_letters)
            print("You have ", n-time ," guesses left.")
            print("You have ", x ," warnings left.")
            letter = str(input("Please guess a letter:​",))
            if letter in string.ascii_uppercase:
                    letter = letter.lower()
            if letter in letters_guessed:
                print("Oops! You've already guessed that letter. ")
                if x > 0:
                    x -=1
                    time -= 1
            letters_guessed += letter#this step adds a guessed letter
            available_letters = "".join(get_available_letters(letters_guessed))
            secret_word_list_copy = get_guessed_word(secret_word, letters_guessed)#these 2 steps get a new available letter list
            if letter not in string.ascii_lowercase:
                if x > 0    :
                    x -= 1
                    time -= 1
                    print("Oops! That is not a valid letter. You have ",x ,"warnings left:",secret_word_list_copy)
                if x <= 0:
                    print("Oops! That is not a valid letter. You have no warnings left:",secret_word_list_copy)
                    
            if letter in secret_word_list:
                print("Good guess:",secret_word_list_copy)
                time -=1
                if "_ " not in secret_word_list_copy:
                    single_letters = len(list(set(letters_guessed)))
                    total_score = (n-time) * (single_letters)
                    print("Your total score for this game is:", total_score)
                    return "Congratulations, you won! "
                    break
            else:
                print("Oops! That letter is not in my word: ",secret_word_list_copy)
                if letter in vowel:
                    time += 1
            time += 1
            if time == n:
                print("guessing finished.")#ends the loop and notice the player
                if "_ " in secret_word_list_copy:
                    return "Sorry, you ran out of guesses. The word was",secret_word+"."
                if "_ " not in secret_word_list_copy:
                    return "Congratulations, you won! Your total score for this game is 0."
# print(hangman(secret_word))    
# print("---------------------Question2-------------------------------")




def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    my_word = my_word.replace(" ","")
    my_word = list(my_word)
    other_word = list(other_word)
    miss = 0
    if len(my_word) == len(other_word):
        for i in range(len(my_word)):
            if my_word[i] != other_word[i] and my_word[i] != "_":
                miss += 1
            i += 1
        if miss == 0:
            return True
        else:
            return False
    else: 
        return False

my_word = "a_ p le"
other_word = "apple"
print(match_with_gaps(my_word, other_word))
print("---------------------Question3A------------------------")



def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
              Keep in mind that in hangman when a letter is guessed, all the positions
              at which that letter occurs in the secret word are revealed.
              Therefore, the hidden letter(_ ) cannot be one of the letters in the word
              that has already been revealed.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    word_list = str()
    #other_word = ["apple","appse","apple","banana","if"]test
    other_word = load_words()
    my_word = "".join(my_word)
    for word in other_word:
        if match_with_gaps(my_word, word) == True:
            word = "".join(word) 
            word_list += (word + " ")
    if word_list == []:
        print("No matches found.")
        return None
    else: 
        return word_list
   
my_word = ['s', '_ ', 'r', '_ ', '_ ', '_ ', '_ ', 'm']
print(show_possible_matches(my_word))

#print(my_word.join(""))
print("---------------------Question3B------------------------")

def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''
    #basic conditions for the funcition
    print("Welcome to the game Hangman! ")
    print("I am thinking of a word that is ", len(secret_word) ," letters long." )
    print("----------------------------------------------------")
    available_letters = string.ascii_lowercase
    letters_guessed = list()
    time=0      
    n=100 #chances for player
    x=3 #warning chances
    vowel = ("e","i","o","a")
    
    #basic loops for game circle within n times
    while time < n: 
        print("Available letters:", available_letters)
        print("You have ", n-time ," guesses left.")
        print("You have ", x ," warnings left.")
        print("-----------------------------------")
        letter = str(input("Please guess a letter:​",))
        if letter in string.ascii_uppercase:
                letter = letter.lower()
        if letter in letters_guessed and letter != "*":
            print("Oops! You've already guessed that letter. ")
            if x > 0:
                x -=1
                time -= 1
        letters_guessed += letter#this step adds a guessed letter
        available_letters = "".join(get_available_letters(letters_guessed))
        secret_word_list_copy = get_guessed_word(secret_word, letters_guessed)#these 2 steps get a new available letter list
        if letter not in string.ascii_lowercase and letter != "*":
            if x > 0    :
                x -= 1
                time -= 1
                print("Oops! That is not a valid letter. You have ",x ,"warnings left:","".join(secret_word_list_copy))
            if x <= 0:
                print("Oops! That is not a valid letter. You have no warnings left:","".join(secret_word_list_copy))
        if letter == "*":
             print("Possible word matches are: ",show_possible_matches(secret_word_list_copy))
             time -= 1         
        if letter in secret_word_list:
            print("Good guess:","".join(secret_word_list_copy))
            time -=1
            if "_ " not in secret_word_list_copy:
                single_letters = len(list(set(letters_guessed)))
                total_score = (n-time) * (single_letters)
                print("Your total score for this game is:", total_score)
                return "Congratulations, you won! "
                break
        else:
            if letter != "*":#question:why I have to add this line or the output of input "*" will include the output of this "else"?
                print("Oops! That letter is not in my word: ","".join(secret_word_list_copy))
                if letter in vowel:
                    time += 1
        time += 1
        
        if time == n:
            print("guessing finished.")#ends the loop and notice the player
            if "_ " in secret_word_list_copy:
                return "Sorry, you ran out of guesses. The word was",secret_word+"."
            if "_ " not in secret_word_list_copy:
                return "Congratulations, you won! Your total score for this game is 0."
            print("-----------------------------------")

print(hangman_with_hints(secret_word))
  

# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    
    secret_word = choose_word(wordlist)
    hangman(secret_word)

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    #secret_word = choose_word(wordlist)
    #hangman_with_hints(secret_word)


