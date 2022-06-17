#Use of this page is optional. If you use code here, make sure either import page1 or from page1 import * appear on your main.py page.
#Story 1:

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