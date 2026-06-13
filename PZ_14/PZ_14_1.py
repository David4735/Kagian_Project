import tkinter as tk
from tkinter import ttk, messagebox

def register():
    if not(entry_first.get().strip() and entry_last.get().strip() and entry_email.get().strip()):
        return messagebox.showwarning("Validation", "Please fill in Name and Email.")
    messagebox.showinfo("Success", f"Registered!\n\nName: {entry_first.get()} {entry_last.get()}\nCompany: {entry_company.get()}\nEmail: {entry_email.get()}\nPhone: ({entry_area.get()}) {entry_phone.get()}\nSubject: {combo_subject.get()}\nExisting customer: {'Yes' if var_customer.get() == 'yes' else 'No'}")

root=tk.Tk()
root.title("Event Registration Form")
root.configure(bg="white")
root.resizable(0,0)
tk.Label(root,text="EVENT REGISTRATION FORM",bg="#1a1a2e",fg="white",font=("Segoe UI",13,"bold")).pack(fill="x",ipady=14)
m=tk.Frame(root,bg="white",padx=40,pady=20)
m.pack(fill="both",expand=True)
for t,r in [("Name:",0),("Company:",3),("Email:",5),("Phone:",7),("Subject:",10)]:
    tk.Label(m,text=t,bg="white",font=("Segoe UI",10,"bold")).grid(row=r,column=0,sticky="w",pady=(10,0))
entry_first=tk.Entry(m,bg="#ebebeb",font=("Segoe UI",10),width=16)
entry_first.grid(row=1,column=1,padx=(0,8),ipady=5)
entry_last=tk.Entry(m,bg="#ebebeb",font=("Segoe UI",10),width=16)
entry_last.grid(row=1,column=2,ipady=5)
entry_company=tk.Entry(m,bg="#ebebeb",font=("Segoe UI",10))
entry_company.grid(row=4,column=1,columnspan=2,sticky="we",ipady=5)
entry_email=tk.Entry(m,bg="#ebebeb",font=("Segoe UI",10))
entry_email.grid(row=6,column=1,columnspan=2,sticky="we",ipady=5)
entry_area=tk.Entry(m,bg="#ebebeb",font=("Segoe UI",10),width=7)
entry_area.grid(row=8,column=1,sticky="w",ipady=5)
entry_phone=tk.Entry(m,bg="#ebebeb",font=("Segoe UI",10),width=22)
entry_phone.grid(row=8,column=2,sticky="w",ipady=5)
combo_subject=ttk.Combobox(m,values=["Workshop","Networking","Conference","Seminar","Other"],state="readonly")
combo_subject.set("Choose option")
combo_subject.grid(row=11,column=1,columnspan=2,sticky="we",ipady=4)
var_customer=tk.StringVar(value="yes")
tk.Label(m,text="Are you an existing customer?",bg="white",font=("Segoe UI",10,"bold")).grid(row=13,column=0,columnspan=3,sticky="w",pady=(14,4))
for i,(t,v) in enumerate([("Yes","yes"),("No","no")]):
    tk.Radiobutton(m,text=t,variable=var_customer,value=v,bg="white").grid(row=14,column=i,sticky="w",padx=(0,16))
tk.Button(m,text="REGISTER",bg="#e8294a",fg="white",font=("Segoe UI",10,"bold"),command=register,padx=24,pady=8).grid(row=15,column=0,columnspan=3,sticky="w",pady=(14,4))
tk.Frame(root,bg="#7b68ee",height=4).pack(fill="x",side="bottom")
root.mainloop()