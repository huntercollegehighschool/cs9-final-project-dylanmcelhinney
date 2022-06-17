#Use of this page is optional. If you use code here, make sure either import page3 or from page3 import * appear on your main.py page.

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