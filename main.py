"""
Name(s): Dylan McElhinney
Name of Project: Mad Libs Final Project
"""

#Write the main part of your program here. Use of the other pages is optional.

import random

num = random.randint(1,4)
def story1():
  noun1 = (input("Enter a noun: "))
  noun2 = (input("Enter another noun: "))
  place1 = (input("Enter the name of a place: "))
  verb1 = (input("Enter a verb: "))
  verb2 = (input("Enter another verb: "))
  verb3 = (input("Enter a third verb: "))
  adjective1 = (input("Enter an adjective: "))
  adjective2 = (input("Enter another adjective: "))
  adverb1 = (input("Enter an adverb: "))
  story = "Once upon a time there was a", noun1, "that liked to", verb1, "every day. This", noun1, "had a", adjective1, "best friend who they liked to", verb1, "with. One day, these", adjective2, "friends decided to", verb2, "several miles to", place1, "together, but realized halfway through that they had left their", noun2, "at home. Without this", adjective2, noun2, "the friends could not go home, so when they reached", place1, "they", verb3, "a house and assumed the identities of the people who lived there. The best friends lived", adverb1,"ever after. The End."
  return(story)

def story2():
  noun1 = (input("Enter a noun: "))
  noun2 = (input("Enter another noun: "))
  noun3 = (input("Enter a third noun: "))
  verb1 = (input("Enter a verb: "))
  verb2 = (input("Enter another verb: "))
  adjective1 = (input("Enter an adjective: "))
  adjective2 = (input("Enter another adjective: "))
  adverb1 = (input("Enter an adverb: "))
  place1 = (input("Enter a place: "))
  place2 =(input("Enter another place: "))
  story = "Once upon a time, a", noun1, "lived", adverb1, "at a", adjective1, place1, "where they often", verb1,". To escape the boredom of everyday life at this", place1, "they occasionally went away to", place2, "where they owned the local", noun2,". The people of this", place2, verb2, "this", noun2, "and gave him a lot of", adjective2, noun3, "for it. The", noun1, "enjoyed the company of the people in the", place2,". The End."
  return(story)

def story3():
  noun1 = input("Enter a noun: ")
  noun2 = input("Enter another noun: ")
  noun3 = input("Enter a third noun: ")
  verb1 = input("Enter a verb: ")
  verb2 = input("Enter another verb: ")
  adjective1 = input("Enter an adjective: ")
  adjective2 = input("Enter another adjective: ")
  adverb1 = input("Enter an adverb: ")
  name1 = input("Enter a name: ")
  name2 = input("Enter another name: ")
  story = "Once upon a time, there was a", noun1, "named", name1, "She was a", adjective1, noun2, "who", adverb1, verb1, "her", noun3, "She was also very", adjective2,". One day, she was walking around and met", name2, "who she became friends with immediately. Later, though, this friend betrayed her by committing the crime of", verb2, "and they never spoke again. The End."
  return(story)

def story4():
  noun1 = input("Enter a noun: ")
  noun2 = input("Enter another noun: ")
  adjective1 = input("Enter an adjective: ")
  adjective2 = input("Enter another adjective: ")
  adjective3 = input("Enter a third adjective: ")
  adjective4 = input("Enter a fourth adjective: ")
  place1 = input("Enter a place: ")
  story = "There once was a kingdom in", place1, "filled with many", adjective1, "people. The people were so", adjective1, "because they had a", adjective2, "ruler. In this land of", noun1, "there was a legend that one day the king would be overthrown. One day, the local", noun2, "who was very", adjective3,", decided to take matters into their own hands and overthrow the king because they thought he was too", adjective4,". However, this", noun2, "was caught in the act and arrested. But, the king didn't know what the", noun2, "had started... The End."
  return(story)

if(num == 1):
  print(story1())
elif(num == 2):
  print(story2())
elif(num == 3):
  print(story3())
else:
  print(story4())
  
