# Code Your Own Code Project:
# There are three levels in the game
levels = ['easy','medium','hard']
blanks = ['__1__', '__2__', '__3__', '__4__']
# EASY
easyLevel = "__1__ is an __2__, object-oriented, high-level programming __3__ with __4__ semantics.\n"
easyLevel_answers = ["python", "interpreted", "language", "dynamic"]

# MEDIUM
mediumLevel = "__1__ high-level built in data __2__, combined with dynamic typing and dynamic binding, make it very attractive for Rapid __3__ Development (AD), as well as for use as a __4__ or glue language to connect existing components together. \n"
mediumLevel_answers = ["python", "structures", "application", "scripting"]

# HARD
hardLevel = "__1__ is simple, easy to learn syntax emphasizes readability and therefore reduces the __2__ of program maintenance. __1__ supports modules and packages, which encourages program modularity and code reuse. The __1__ interpreter and the extensive standard __3__ are available in source or __4__ form without charge for all major platforms and can be freely distributed."
hardLevel_answers = ['python','cost','library','binary']
# Dictionary: 'from Previous review'
game_data = {
   'easy': {
        'quiz': easyLevel,
        'answers': easyLevel_answers
    },
   'medium': {
        'quiz': mediumLevel,
        'answers': mediumLevel_answers
    },
   'hard': {
        'quiz': hardLevel,
        'answers': hardLevel_answers
    }
}
# ====================================================================================================
# Test_Answer(UserSelection): this is the main function, tests user's answers after level selection
# output: print out filled text if all answers are correct
def test_answers(UserSelection):
      global blanks
      fillblanks = 0
      print game_data[UserSelection]['quiz']
      testanswers = game_data[UserSelection]['answers']
      replace = game_data[UserSelection]['quiz']
      while fillblanks < len(blanks):
             UserAnswer = raw_input('What is the answer of blank __'+ str(fillblanks + 1)+'__ ? ')
             if UserAnswer.lower() == testanswers[fillblanks]:
               print 'Great! blank (' + str(fillblanks + 1) + ') filled correctly\n'
               replace = replace.replace(blanks[fillblanks], testanswers[fillblanks])
               fillblanks += 1
               print replace
             else:
               print '\nUncorrect! please, try again...\n'
      print 'BRAVO! You Succeed'
# ====================================================================================================
#palygame(): this function ask user to select a level
def play_game():
     print '---Welcome To Fill Blanks game!---\n'
     UserSelection = raw_input('Please, select the level you want to play: EASY, MEDIUM, or HARD\n')
     print '\nyou are select '+ str(UserSelection).upper() + ' level...\n'
     if UserSelection.lower() in levels:
        return test_answers(UserSelection.lower())
     else:
      print '\nSORRY! your selcetion is NOT available\n'
      return play_game()
print play_game()


# Previous version of the project (before reviewed)
# =====================================================================================================
# easycase():this function  plays level easy if user input == 'easy', to fill all blanks inside easy level text.
# output: print all blanks filled with correct answers
# def easycase():
#   global easyLevel
#   global easyLevel_answers
#   global blanks
#   blank = 0
#   while blank < len(easyLevel_answers):
#        User_Answer = raw_input(' What is the answer of blank __'+ str(blank + 1)+'__ ?')
#        if User_Answer.lower() == easyLevel_answers[blank]:
#           print 'Great! blank (' + str(blank + 1) + ') filled correctly'
#           easyLevel = easyLevel.replace(blanks[blank], easyLevel_answers[blank])
#           blank += 1
#           print 'correct!'
#           print easyLevel
#        else:
#             print 'Uncorrect! please, try again...'
#   print 'BRAVO! you successed'

# =====================================================================================================
# mediumcase():this function  plays level medium if user input == 'medium', to fill all blanks inside medium level text
# output: print all blanks filled with correct answers
# def mediumcase():
#   global mediumLevel
#   global mediumLevel_answers
#   global blanks
#   blankM = 0
#   while blankM < len(mediumLevel_answers):
#        User_Answer = raw_input(' What is the answer of blank __'+ str(blankM + 1)+'__ ?')
#        if User_Answer.lower() == mediumLevel_answers[blankM]:
#           print 'Great! blank (' + str(blankM + 1) + ') filled correctly'
#           mediumLevel = mediumLevel.replace(blanks[blankM], mediumLevel_answers[blankM])
#           blankM += 1
#           print 'correct!'
#           print mediumLevel
#        else:
#             print 'Uncorrect! please, try again...'
#   print 'BRAVO! you successed'

# =====================================================================================================
# hardcase():this function  plays level hard if user input == 'hard', to fill all blanks inside hard level text.
# output: print all blanks filled with correct answers
# def hardcase():
#   global hardLevel
#   global hardLevel_answers
#   global blanks
#   blankH = 0
#   while blankH < len(hardLevel_answers):
#        User_Answer = raw_input(' What is the answer of blank __'+ str(blankH + 1)+'__ ?')
#        if User_Answer.lower() == hardLevel_answers[blankH]:
#           print 'Great! blank (' + str(blankH + 1) + ') filled correctly'
#           hardLevel = hardLevel.replace(blanks[blankH], hardLevel_answers[blankH])
#           blankH += 1
#           print hardLevel
#        else:
#             print 'Uncorrect! please, try again...'
#   print 'BRAVO! you successed'
# ====================================================================================================
#palygame(): this function is the main function, plays user's selection of levels
# def playgame():
#     UserSelection = raw_input('Welcome to FILL BLANKS game.\nPlease, select the level you want to play: EASY, MEDIUM, or HARD\n')
#     print 'you are select '+ str(UserSelection).upper() + ' level...\n'
#     if UserSelection == 'easy':
#         print easyLevel
#         return easycase()
#     elif UserSelection == 'medium':
#         print mediumLevel
#         return mediumcase()
#     elif UserSelection == 'hard':
#         print hardLevel
#         return hardcase()
#     else:
#         print 'SORRY! your selcetion is NOT available'
#         return playgame()
#
# print playgame()
