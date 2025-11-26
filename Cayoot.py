questions = [
    {
        "question" : "What is the capital of France?",
        "options" : ["A. Berlin" , "B. Madrid" , "C. Paris" , "D. Rome"],
        "answer" : "C. Paris",
        "type" : "mcq",
        },
    {
        "question" : "Which continent is Egypt located in?",
        "options" : ["A. Asia" , "B. Africa" , "C. Europ" , "D. South America"],
        "answer" : "B. Africa",
        "type" : "mcq",
    },
    {
         "question" : "Which ocean is the largest in the world?",
        "options" : ["A. Atlantic Ocean" , "B. Indian Ocean" , "C. Arctic Ocean" , "D. Pacific Ocean"],
        "answer" : "D. Pacific Ocean",
        "type" : "mcq",
    },
      {
         "question" : "Mount Everest is located in which mountain range?",
        "options" : ["A. Andes" , "B. Alps" , "C. Himalayas" , "D. Rockies"],
        "answer" : "C. Himalayas",
        "type" : "mcq",
    },
      {
         "question" : "Which country has the largest population?",
        "options" : ["A. India" , "B. USA" , "C. China" , "D. Russia"],
        "answer" : "A. India",
        "type" : "mcq",
    },
     {
         "question" : "Which river is the longest in the world?",
        "answer" : "nile",
        "type" : "typed",
    },
     {
         "question" : "Which country is completely landlocked by South Africa?",
        "answer" : "lesotho",
        "type" : "typed",
    }  ,
     {
         "question" : "What is the smallest country in the world by area?",
        "answer" : "vatican city",
        "type" : "typed",
    }  ,
     {
         "question" : "Which desert is the largest hot desert in the world?",
        "answer" : "sahara",
        "type" : "typed",
    }  ,
     {
         "question" : "Which U.S. state has the most volcanoes?",
        "answer" : "alaska",
        "type" : "typed",
    }  
 ]


#SETUP
from tkinter import *

#window
window = Tk()

window.geometry("600x600")
window.title("Cayoot!")

icon =PhotoImage(file='qoris.png')
window.iconphoto(True, icon)

window.config(background="#3f6ed4")






#Home Frame

home_frame = Frame(window, bg= "#3f6ed4")
home_frame.pack(fill="both", expand=True)




title_label = Label(home_frame, text="Cayoot!", 
              font=("Comic Sans MS", 20, "bold"), 
              fg='white', 
              bg='#3f6ed4'
              )
title_label.pack(pady=50)

name_label = Label(home_frame,text="Enter your username.", 
              font=("Comic Sans MS", 10), 
              fg='black', 
              bg='#3f6ed4',)
name_label.pack(pady=10)

name_entry = Entry(home_frame, font=('Comic Sans MS', 20))
name_entry.pack(pady=10)

loading_label = Label(window, text='Loading....', font=('Arial', 15), fg='white', bg="#3f6ed4")


def loading_quiz():
    username = name_entry.get().strip()

    if not username:
        name_label.config(text= "Please, enter your username.", fg="red")

    else:
        home_frame.forget()
        loading_label.pack(pady=200)
        window.after(1500, start_quiz)
        
        
def start_quiz():
    loading_label.forget()
    quiz_frame.pack(fill="both", expand='True')





start_button = Button(home_frame, text="Let's go!", font=('Comic Sans MS', 16), bg="#fa8d1e", command= loading_quiz )
start_button.pack(pady=10)








#Quiz Frame
quiz_frame = Frame(window, bg='#1157ed')

question_label=Label(quiz_frame, text="This is the question",
                     font=('Arial', 14, 'bold'),
                     fg='white',
                     bg='#150e7d')
question_label.pack(pady=15)

                #mcq
option_button1=Button(quiz_frame, text="A", font=("Arial", 12, 'bold'), bg="#eb1c1c")
option_button1.pack(pady=20)

option_button2=Button(quiz_frame, text="B", font=("Arial", 12, 'bold'), bg='#24f024')
option_button2.pack(pady=20)

option_button3=Button(quiz_frame, text="C", font=("Arial", 12, 'bold'), bg= '#ebdf26')
option_button3.pack(pady=20)

option_button4=Button(quiz_frame, text="D", font=("Arial", 12, 'bold'), bg='#fa8d1e')
option_button4.pack(pady=20)

                #typed
answer_entry = Entry(quiz_frame, font=('Arial', 20))

submit_button = Button(quiz_frame, text='Submit', font=('Arial', 16))

feedback_label = Label(quiz_frame, text="wrong/right", 
                      font=("Arial", 16),
                      fg='White',
                       bg='white')
feedback_label.pack(pady=20)

score_label = Label(quiz_frame, text= 'Score = 0',
                    font=('Arial', 9),
                    fg='white',
                    bg='#150e7d')
score_label.pack(pady=10)


                    #operations and funtions
                    #exple with the first_question
first_question = questions[0]
question_label.config(text= first_question['question'])

option_button1.config(text=first_question['options'][0], command=lambda: choose(first_question['options'][0]))
option_button2.config(text=first_question['options'][1], command=lambda: choose(first_question['options'][1]))
option_button3.config(text=first_question['options'][2], command=lambda: choose(first_question['options'][2]))
option_button4.config(text=first_question['options'][3], command=lambda: choose(first_question['options'][3]))


current_answer= first_question['answer']





score=0
current_index=0
                            #for mcq
def choose(selected_option):
    global score

    if selected_option == current_answer:
        feedback_label.config(text="Correct!", fg='white', bg='green')

        score += 10
        score_label.config(text= f'Score= {score}')

    else:
        feedback_label.config(text=f"Wrong! The correct is {current_answer}", bg= 'red', fg='white')
    if current_index < len(questions):
        window.after(1000, move)
    else:
        feedback_label.config(text="Quiz is done!")


                            #for typed
def submit_typed():
    global score
    global current_answer

    typed_answer = answer_entry.get().strip().lower()
    if typed_answer == current_answer.lower():
        feedback_label.config(text= 'Correct!')

        score +=20
        score_label.config(text= f"Score = {score}")

    else:
        feedback_label.config(text=f"Wrong. The answer is {current_answer}")

        score -=5
        score_label.config(text= f"Score = {score}")

    window.after(1000, move)
submit_button.config(command= submit_typed)

                            #let's move!



def move():
    global current_index
    global current_answer
    current_index +=1

    if current_index < len(questions):
        q = questions[current_index]
        question_label.config(text= q['question'])
    

        if q["type"] == 'mcq':
            option_button1.config(text=q['options'][0], command=lambda: choose(q['options'][0]))
            option_button2.config(text=q['options'][1], command=lambda: choose(q['options'][1]))
            option_button3.config(text=q['options'][2], command=lambda: choose(q['options'][2]))
            option_button4.config(text=q['options'][3], command=lambda: choose(q['options'][3]))

            current_answer= q['answer']

        else:
            answer_entry.pack(pady=30)
            submit_button.pack(pady=10)
            option_button1.forget()
            option_button2.forget()
            option_button3.forget()
            option_button4.forget()

            current_answer=q['answer']

            answer_entry.delete(0, END)
                


    else:
        feedback_label.config(text="Quiz done!")
        submit_button.forget()
        window.after(1000, end_screen)





#Score frame
score_frame = Frame(window, bg='#150e7d')

fscore_label = Label(score_frame, 
              text="You've got 100 points", 
              font=("Arial", 25, "bold"), 
              fg='white', 
              bg='#150e7d' )
fscore_label.pack(pady=50)


comment_label = Label(score_frame, text="Excelent", 
              font=("Arial", 10, "bold"), 
              fg='white', 
              bg='#150e7d')
comment_label.pack(pady=20)



def end_screen():
    global score

    quiz_frame.forget()
    score_frame.pack(fill='both', expand="True")

    fscore_label.config(text= f"You've got {score} points!")

    if score <= 50:
        comment_label.config(text="Bro... This is bad. You need to actually study. Don't play!")
    elif score > 100:
        comment_label.config(text="You crushed it! 🔥 You did great. Solid performance. Keep going like this.")
    else:
        comment_label.config(text="You're okay. Not impressive. Not terrible. You can do better if you focus.")

    


















window.mainloop()















