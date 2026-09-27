class  QuizSystem:
  def menu(self):
    while True:
     print('1. start')
     print('2. view')
     print('3. exit')
     try:
        choice = int(input("enter choice "))
     except ValueError:
        print("enter only numbers ")
        continue
     if choice == 1:
      self.select_subject()
     elif choice == 2:
      self.view_result()
     elif choice == 3:
      print("exit")
      break
     else:
      print("invalid")
    print("complete")
  def select_subject(self):
    while True:
     print('select subject ')
     print('1. PYTHON')
     print('2. ENGLISH')
     print('3. MATHS')
     try:
       choice = int(input("enter choice "))
     except ValueError:
      print("enter only numbers ")
      continue
     if choice == 1:
      self.load_question("python.txt")
      break
     elif choice == 2:
      self.load_question("english.txt")
      break
     elif choice == 3:
      self.load_question("maths.txt")
      break
     else:
      print("invalid ")
    print("subject selected ")
  def load_question(self, filename):
    name = input("Enter your name ")

    try:
        with open(filename, "r") as file:
            score = 0
            total_question = 0

            for line in file:
                total_question = total_question + 1
                question, answer = line.split("|")
                print(question)

                answer = answer.strip()
                user_answer = input("Enter answer ")

                if user_answer.strip().lower() == answer.strip().lower():
                    print("Correct answer ")
                    score = score + 1
                else:
                    print("Invalid")

        print("QUIZ FINISHED")
        print("Score is: ", score)
        print("Total questions: ", total_question)

        percentage = (score / total_question) * 100
        print("Percentage:", percentage, "%")
        if percentage >= 50:
          result = "pass"
        else :
          result = "fail"
        print("RESULT" , result)

        with open("result.txt", "a") as file:
            file.write(f"Name: {name}\n")
            file.write(f"Score: {score}/{total_question}\n")
            file.write(f"Percentage: {percentage}%\n")
            file.write("----------------------\n")
            file.write(f"RESULT: {result}\n")

    except FileNotFoundError:
        print("File not found")
        return
  def view_result(self):
   with open("result.txt", "r") as file:
    print(file.read())

    

a = QuizSystem()
a.menu()
# a.select_subject()
