import json

def questions(file_path):
     file_path = "write your file path here"

     with open(file_path, 'r') as file:
          data_question = json.load(file)
     return file_path

def request(data_question):
     result = 0

     for index, question in enumerate(data_question):
          print(f"  Difficulty. {question["difficulty"]}")
          print(f"Category: {question["category"]}")
          print(f"Question:\n{index+1} / {question["question"]}")

          for i, option in enumerate(question["options"], 1):
               print(f"{i}. {option}")

          while True:
               try:
                    user_input = int(input("Enter the number of your answer: "))
                    if 1 <= user_input <= len(question["options"]):
                         break
                    else:
                         print("Invalid input!")
               except ValueError:
                    print("Invalid input! Please Enter a valid Number!")

          if question["options"][user_input-1] == question["answer"]:
               result += 1
     return result

def show_result(result, data_question):
     print("#______________")
     print(f"Correct Answers:\t{result} correct answers from {data_question} questions answered!")

def main():
     file_path = "data_questions.json"
     data_question = questions(file_path)
     result = request(data_question)
     show_result(result, len(data_question))

if __name__ == "__main__":
     main()
     