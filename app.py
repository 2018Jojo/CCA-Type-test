print("Title of program: CCA Type test")
print()
print("Welcome to DHS! Please answer the following questions truthfully and we'll suggest a CCA type for you!")
print("Please respond with a number 1 - 5, where 1 is strongly disagree and 5 is strongly agree.")
print()

tech1 = input("I enjoy building and fixing things.")

outdoor1 = input("I don't mind sweating.")

music1 = input("I have a good sense of rhythm.")

tech2 = input("I want to learn new skills.")

outdoor2 = input("I am active.")

music2 = input("I play a musical instrument well.")


tech_final = int(tech1) + int(tech2)
outdoor_final = int(outdoor1) + int(outdoor2)
music_final = int(music1)+ int(music2)

print("Here's your final result!")

if tech_final > outdoor_final and tech_final > music_final:
  print("You might be suitable for Uniform Group!")
elif outdoor_final > music_final:
  print("You might be suitable for Sports!")
else:
  print("You might be suitable for Performing Arts!")

  
