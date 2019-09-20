from math import *
#character_name = "Mike"
#character_age = 50
#print("There once was a man named " + character_name + ",")
#print("he was %d years old." % character_age)
#print("He really liked the name %s," % character_name)
#print("but didn't like being %d." % character_age)
#phrase = "Hello\nI'm Gabi"
#print(phrase.replace("Hello", "Bye"))

#my_num = -5
#print(str(my_num) + " is my favorite number")
#print(sqrt(16))

#name = input("Enter your name: ")
#print("Hello " + name + "! You are " + age)
#num1 = input("Enter a number: ")
#num2 = input("Enter another number: ")
#result = float(num1) + float(num2)
#print(result)
#color = input("Enter a color: ")
#plural_noun = input("Enter a plural noun: ")
#celebrity = input("Enter a celebrity: ")
#print("Roses are " + color)
#print(plural_noun + " are blue")
#print("I love " + celebrity)

#numbers = [45, 82, 15, 16, 23, 42]
#friends = ["Becky", "Margot", "Megan", "Ian", "Jenica", "Ian"]
#friends.sort()
#print(friends)
#numbers.sort()
#print(numbers)
#friends2 = friends.copy()

#coordinates = (4, 5)
#coordinates[1] = 10
#print(coordinates[0])

#def say_hi(name, age):
 #   print("Hello " + name + " you are " + age)
#say_hi("Gabi", "17")
#say_hi("Becky", "17")

#def cube(num):
 #   return num*num*num
#result = cube(5)
#print(result)

#is_female = False
#is_tall = True

#if is_female and is_tall:
 #   print("you are a female and tall")
#elif is_female and not(is_tall):
 #   print("you are a short female")
#elif is_tall and not (is_female):
 #   print("you are a female and tall")
#else:
 #   print("you are either not male or not tall or both")

#def max_num(num1, num2, num3):
     #if num1 >= num2 and num1 >= num3:
      #   return num1
     #elif num2 >= num1 and num2 >= num3:
      #   return num2
     #else:
      #   return num3
#print(max_num(300, 4, 5)

#num1 = float(input("Enter first number: "))
#op = (input("Enter operator: "))
#num2 = float(input("Enter second number: "))
#if op == "+":
#    print(num1 + num2)
#elif op == "-":
  #  print(num1 - num2)
#elif op == "/":
 #   print(num1 / num2)
#elif op == "*":
 #   print(num1 * num2)
#else:
 #   print("Invalid Operator")

#monthConversions = {
   # "Jan": "January",
#"Feb": "February",
 #   "Mar": "March",
 #   "Apr": "April",
 #   "May": "May",
 #   "Jun": "June",
 #   "Jul": "July",
 #   "Aug": "August",
 #   "Sep": "September",
 #   "Oct": "October",
 #   "Nov": "November",
 #   "Dec": "December",

#}

#print(monthConversions.get("Luv", "Not a valid key"))


#i = 1
#while i <= 10:
 #   print(i)
  #  i = i + 1 # same as i += 1

#print("Done with loop")

#secret_word = "giraffe"
#guess = ""
#guess_count = 0
#guess_limit = 3
#out_of_guesses = False
#while guess != secret_word and not(out_of_guesses):
#    if guess_count < guess_limit:
#        guess = input("Enter guess: ")
#        guess_count += 1
#    else:
#        out_of_guesses = True
#if out_of_guesses:
#    print("Out of guesses, YOU LOSE!")
#else:
#    print("You win")

#friends = ["Jim", "Karen", "Kevin"]
#for index in range(5):
 #   if index == 0:
  #      print("first iteration")
   # else:
    #    print("not first")

#def raise_to_power(base_num, pow_num):
 #   result = 1
 #   for index in range(pow_num):
 #       result = result * base_num
 #   return result

#print(raise_to_power(2, 3))

#number_grid = [
#    [1, 2, 3],
#    [4, 5, 6],
#    [7, 8, 9],
#    [0]
#]
#for row in number_grid:
#    for col in row:
#        print(col)

#def translate(phrase):
#    translation = ""
#    for letter in phrase:
#        if letter.lower() in "aeiou":
#            if letter.isupper():
#                translation = translation + "G"
#            else:
#                translation = translation + "g"
#        else:
#            translation = translation + letter
#    return translation

#print(translate(input("Enter a phrase: ")))

#try:
#    number = int(input("Enter a number: "))
#    print(number)
#except:
#    print("Invalid Input")

#example_file = open("Kivypractice.txt", "w")
#example_file.write("\nKelly - Customer Service")
#example_file.close()

#from Student import Student

#student1 = Student("Jim", "Business", 3.1, False)
#student2 = Student("Pam", "Art", 2.5, True)
#print(student2.gpa)

#from Question import Question

#question_prompts = [
 #   "What color are apples?\n(a) Red/Green\n(b) Purple\n(c) Orange\n\n",
 #   "What color are bananas?\n(a) Teal\n(b) Magenta\n(c) Yellow\n\n",
 #   "What color are strawberries?\n(a) Yellow\n(b) Red\n(c) Blue\n\n"
#]

#questions = [
 #   Question(question_prompts[0], "a"),
 #   Question(question_prompts[1], "c"),
 #   Question(question_prompts[2], "b"),
#]


#def run_test(questions):
#    score = 0
#    for question in questions:
#        answer = input(question.prompt)
#        if answer == question.answer:
#            score += 1
#        print("You got " + str(score) + "/" + str(len(questions)) + " Correct")

#run_test(questions)
#from Student import Student

#student1 = Student("Oscar", "Accounting", 3.5)
#student2 = Student("Phyllis", "Business", 3.1)

#print(student1.on_honor_roll())


