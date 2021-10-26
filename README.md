#Hamgman game with Tkinter
import random
import tkinter
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk
import os
import sys
import string

window = Tk()
window.title("Hangman")
window.option_add('*Font', 'Broadway 14')
window.geometry("880x600")
window.resizable(False, False)
hang_photo1 = ImageTk.PhotoImage(file = 'hang1.jpg')
hang_photo2 = ImageTk.PhotoImage(file = 'hang2.jpg')
hang_photo3 = ImageTk.PhotoImage(file = 'hang3.jpg')
hang_photo4 = ImageTk.PhotoImage(file = 'hang4.jpg')
hang_photo5 = ImageTk.PhotoImage(file = 'hang5.jpg')


span = len(string.ascii_uppercase)
#print('span:', span)

pic = Label(window)
pic.grid(row=4, column=0, columnspan=span)

words = ["apple", "pear", "apricot", "orange", "lemon", "watermelon", "grapes", "banana", "kiwi"]
rand_word = random.choice(words).upper()
print(rand_word)
emty_list = []
word_list = emty_list + ["_"] * len(rand_word)
word_string = "".join(word_list)
moves = 5

Label(window, text = "The word: ").grid(row = 1, column = 1, columnspan = span)
the_word = Label(window, text=word_list).grid(row = 2, column = 1, columnspan = span)


def disable_button(btn):
    if btn["state"] == NORMAL:
        btn["state"] = DISABLED
    else:
        btn["state"] = NORMAL

def restart_program():
    window.destroy()
    #python = sys.executable
    #os.execl(python, python, * sys.argv)
    os.startfile("hangman_GUI.py")

def check_words(letter):
    index_list = []
    for i in range(0, len(rand_word)):
        if rand_word[i] == letter:
            index_list.append(i)
    if letter in rand_word:
        for j in index_list:
            word_list[j] = letter
        #guess = Label(window, text="YOU GUESSED!")
        #guess.grid(row=3, column = 1)
        guess_msg = messagebox.showinfo(title = "CORRECT!", message="YOU GUESSED!")
        the_word = Label(window, text=word_list)
        the_word.grid(row=2, column = 1, columnspan = span)
    else:
        global  moves
        #guess = Label(window, text="      WRONG!      ")
        #guess.grid(row=3, column = 1)
        guess_msg = messagebox.showwarning(title="WRONG!", message="YOU DIDN'T GUESS!")
        moves -= 1
        moves_left = Label(window, text="You have "+str(moves)+ " moves left")
        moves_left.grid(row=3, column = 1, columnspan = span)
        # guess.grid(row=3, column = 1)
        if moves == 4:
            pic = Label(window, image = hang_photo1).grid(row = 4, column = 3, columnspan = 26)
        elif moves == 3:
            pic = Label(window, image=hang_photo2).grid(row=4, column=3, columnspan = 26)
        elif moves == 2:
            pic = Label(window, image=hang_photo3).grid(row=4, column=3, columnspan = 26)
        elif moves == 1:
            pic = Label(window, image=hang_photo4).grid(row=4, column=3, columnspan = 26)
        elif moves == 0:
            pic = Label(window, image=hang_photo5).grid(row=4, column=3, columnspan = 26)
            lose_msg = messagebox.askyesno(title="You lose!", message="You lose!Pay again?")
            if lose_msg == 'yes':
                restart_program()


def check_winner():
    a_string = ''.join(word_list)
    if a_string == rand_word:
        #Label(window, text = "WINNER! ").grid(row = 4, column = 3)
        win_msg = messagebox.askyesno(title = "YOU WIN!",message="You win! Play again?")
        if win_msg == 'yes':
            restart_program()

A = Button(text ="A", command = lambda: [check_words("A"), check_winner(), disable_button(A)])
A.grid(row = 0, column = 0)
B = Button(text ="B", command = lambda: [check_words("B"), check_winner(), disable_button(B)])
B.grid(row = 0, column = 1)
C = Button(text ="C", command = lambda: [check_words("C"), check_winner(), disable_button(C)])
C.grid(row = 0, column = 2)
D = Button(text ="D", command = lambda: [check_words("D"), check_winner(), disable_button(D)])
D.grid(row = 0, column = 3)
E = Button(text ="E", command = lambda: [check_words("E"), check_winner(), disable_button(E)])
E.grid(row = 0, column = 4)
F = Button(text ="F", command = lambda: [check_words("F"), check_winner(), disable_button(F)])
F.grid(row = 0, column = 5)
G = Button(text ="G", command = lambda: [check_words("G"), check_winner(), disable_button(G)])
G.grid(row = 0, column = 6)
H = Button(text ="H", command = lambda: [check_words("H"), check_winner(), disable_button(H)])
H.grid(row = 0, column = 7)
I = Button(text ="I", command = lambda: [check_words("I"), check_winner(), disable_button(I)])
I.grid(row = 0, column = 8)
J = Button(text ="J", command = lambda: [check_words("J"), check_winner(), disable_button(J)])
J.grid(row = 0, column = 9)
K = Button(text ="K", command = lambda: [check_words("K"), check_winner(), disable_button(K)])
K.grid(row = 0, column = 10)
L = Button(text ="L", command = lambda: [check_words("L"), check_winner(), disable_button(L)])
L.grid(row = 0, column = 11)
M = Button(text ="M", command = lambda: [check_words("M"), check_winner(), disable_button(M)])
M.grid(row = 0, column = 12)
N = Button(text ="N", command = lambda: [check_words("N"), check_winner(), disable_button(N)])
N.grid(row = 0, column = 13)
O = Button(text ="O", command = lambda: [check_words("O"), check_winner(), disable_button(O)])
O.grid(row = 0, column = 14)
P = Button(text ="P", command = lambda: [check_words("P"), check_winner(), disable_button(P)])
P.grid(row = 0, column = 15)
Q = Button(text ="Q", command = lambda: [check_words("Q"), check_winner(), disable_button(Q)])
Q.grid(row = 0, column = 16)
R = Button(text ="R", command = lambda: [check_words("R"), check_winner(), disable_button(R)])
R.grid(row = 0, column = 17)
S = Button(text ="S", command = lambda: [check_words("S"), check_winner(), disable_button(S)])
S.grid(row = 0, column = 18)
T = Button(text ="T", command = lambda: [check_words("T"), check_winner(), disable_button(T)])
T.grid(row = 0, column = 19)
U = Button(text ="U", command = lambda: [check_words("U"), check_winner(), disable_button(U)])
U.grid(row = 0, column = 20)
V = Button(text ="V", command = lambda: [check_words("V"), check_winner(), disable_button(V)])
V.grid(row = 0, column = 21)
W = Button(text ="W", command = lambda: [check_words("W"), check_winner(), disable_button(W)])
W.grid(row = 0, column = 22)
X = Button(text ="X", command = lambda: [check_words("X"), check_winner(), disable_button(X)])
X.grid(row = 0, column = 23)
Y = Button(text ="Y", command = lambda: [check_words("Y"), check_winner(), disable_button(Y)])
Y.grid(row = 0, column = 24)
Z = Button(text ="Z", command = lambda: [check_words("Z"), check_winner(), disable_button(Z)])
Z.grid(row = 0, column = 25)
play_again = Button(text = "Play again", command = restart_program).grid(row =6, column =3, columnspan = span)

#letter_buttons = [A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q, R, S, T, U, V, W, X, Y, Z]
window.mainloop()
