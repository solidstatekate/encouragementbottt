print("Title of program: Encouragement bot")
print()
while True:
  description = input("Could you describe how you feel in a sentence?")

  list_of_words = description.split()

  feelings_list = []
  encouragement_list = []
  counter = 0
  
  for each_word in list_of_words:
    
    if each_word == "upset":
      feelings_list.append("sad")
      encouragement_list.append("tomorrow will be a better day, never give up and stay positive! you will get through this!")
      counter += 1
    if each_word == "happy":
      feelings_list.append("happy")
      encouragement_list.append("to keep smiling")
      counter += 1
    if each_word == "tired":
      feelings_list.append("tired")
      encouragement_list.append("perhaps you are just feeling lethargic because you didn't get sufficient sleep. remember to sleep enough and take good care of your health!")
      counter += 1
      
if each_word == "exhausted":
      feelings_list.append("exhausted")
      encouragement_list.append("jiayou! You can do it!")
      counter += 1
     if each_word == "lonely":
      feelings_list.append("lonely")
      encouragement_list.append("i'll be your friend!")
      counter += 1
 if each_word == "angry
      feelings_list.append("angry")
      encouragement_list.append("Calm down, don't act rash!")
      counter += 1

  if counter == 0:
    
      output = "Sorry I don't really understand. Please use different words?"

  elif counter == 1:
    
      output = "It seems that you are feeling quite " + feelings_list[0] + ". However, bear in mind that "+ encouragement_list[0] + "! Hope you feel better :)"  

  else:

    feelings = ""    
    for i in range(len(feelings_list)-1):
      feelings += feelings_list[i] + ", "
    feelings += "and " + feelings_list[-1]
    
    encouragement = ""    
    for j in range(len(encouragement_list)-1):
      encouragement += encouragement_list[i] + ", "
    encouragement += "and " + encouragement_list[-1]

    output = "It seems that you are feeling quite " + feelings + ". Well, always remember "+ encouragement + "! Hope you feel better :)"

  print()
  print(output)
  print()
