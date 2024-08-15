import tkinter as tk
from tkinter import messagebox

# Dummy data for candidates
candidates = ["SHANTHINI", "SATHIYA", "ILAN","NOTA"]

# Dictionary to store votes
votes = {candidate: 0 for candidate in candidates}

def submit_vote():
    selected_candidate = candidate_var.get()
    if selected_candidate in votes:
        votes[selected_candidate] += 1
        messagebox.showinfo("Vote Cast", f"Your vote for {selected_candidate} has been recorded!")
    else:
        messagebox.showerror("Error", "Please select a valid candidate.")

def show_results():
    
    results_message = "\n".join([f"{candidate}: {vote} votes" for candidate, vote in votes.items()])
    messagebox.showinfo("Voting Results", results_message)

# Main window
root = tk.Tk()
root.title("Online Voting System")

# Configure main window
root.geometry("500x600")  # Set window size
root.resizable(False, False)  # Disable resizing
root.configure(bg='#f0f0f0')  # Set background color

# Variable to hold the selected candidate
candidate_var = tk.StringVar()

# Create widgets
multi_line_text = "Election Commission Of India\n(2025-2030)"
l1=tk.Label(root, text=multi_line_text, font=('Helvetica', 20, 'bold'), bg='#f0f0f0',fg="red")
l1.pack(pady=10)

for candidate in candidates:
    tk.Radiobutton(root, text=candidate, variable=candidate_var, value=candidate, 
                   font=('Arial', 15), bg='#f0f0f0', selectcolor='lightblue', 
                   indicatoron=0, padx=10, pady=5).pack(padx=50,pady=20)

tk.Button(root, text="Submit Vote", command=submit_vote, 
          font=('Arial', 17), bg='#4CAF50', fg='white', 
          padx=10, pady=5, relief='raised', bd=2).pack(padx=5,pady=13)

tk.Button(root, text="Show Results", command=show_results, 
          font=('Arial', 17), bg='#2196F3', fg='white', 
          padx=10, pady=5, relief='raised', bd=2).pack(pady=5)

# Start the Tkinter event loop
root.mainloop()
