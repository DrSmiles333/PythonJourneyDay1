pain_level = int(input("What is your pain level from 1 to 10? "))
while pain_level < 1 or pain_level > 10:
    print("Please enter a valid pain level between 1 and 10.")
    pain_level = int(input("What is your pain level from 1 to 10? "))

if 1 <= pain_level <= 3:
    print("Mild pain, let's continue progressing current plan.")
elif 4 <= pain_level <7:
    print("Moderate pain, we'll modify today's session")
elif pain_level >= 7:
    print("Severe pain, flagging for clinician review before we proceed.")
night = input("Is the pain worse at night? (yes/no) ")
numbness = input("Is there numbness or tingling? (yes/no) ")
if numbness == "yes" and night == "yes" and pain_level >= 7:
    print("Immediate escalation recommended")
elif pain_level >= 7 and (numbness == "yes" or night == "yes"):
    print("Recommend escalation")
elif numbness == "yes" and night == "yes":
    print("Recommend escalation")
else:
    print("No red flags — proceed with plan.")