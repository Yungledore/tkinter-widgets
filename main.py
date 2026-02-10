import tkinter as tk
import random

def play(user):
    comp = random.choice(["rock", "paper", "scissor"])
    u_lbl.config(text=f"player: {user}")
    c_lbl.config(text=f"program: {comp}")
     
    if user == comp: res = "tie"
    elif (user == "rock" and comp == "scissor") or (user == "paper" and comp == "rock") or \
         (user == "scissor" and comp == "paper"): res = "you win"
    else: res = "program wins"
    res_lbl.config(text=res)



def reset():        

    u_lbl.config(text="player: -")
    c_lbl.config(text="program: -")
    res_lbl.config(text="Result")



root = tk.Tk()
root.title("rock paper scissors game")
u_lbl = tk.Label(root, text="player: -")
u_lbl.pack(side="left", padx=10)
c_lbl = tk.Label(root, text="program: -")
c_lbl.pack(side="right", padx=10)
res_lbl = tk.Label(root, text="Result", font=("Arial", 12, "bold"))
res_lbl.pack(pady=20)
btn_f = tk.Frame(root)
btn_f.pack()


for move in ["rock", "paper", "scissor"]:
    tk.Button(btn_f, text=move, command=lambda m=move: play(m)).pack(side="left")
tk.Button(root, text="Reset", fg="red", command=reset).pack(pady=10)
root.mainloop()