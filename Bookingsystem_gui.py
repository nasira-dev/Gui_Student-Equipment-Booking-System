import tkinter as tk
from tkinter import messagebox

# -------------------- DATA STRUCTURE (UNCHANGED) --------------------

equipment_list = [
    "Laptop 1", "Laptop 2",
    "Projector A", "Projector B",
    "Tablet 1", "Tablet 2"
]

bookings = []
booking_id_counter = 1


# -------------------- MAIN WINDOW --------------------

root = tk.Tk()
root.title("Student Equipment Booking System")
root.geometry("800x600")
root.configure(bg="#f2e4b3")  # Light background


# -------------------- FUNCTIONS (LOGIC UNCHANGED) --------------------

def add_equipment():
    name = entry_equipment.get().strip()
    if name:
        if name not in equipment_list:
            equipment_list.append(name)
            messagebox.showinfo("Success", "Equipment added successfully.")
        else:
            messagebox.showwarning("Warning", "Equipment already exists.")
    entry_equipment.delete(0, tk.END)


def record_booking():
    global booking_id_counter

    student = entry_student.get().strip()
    equipment = entry_booking_equipment.get().strip()
    date = entry_date.get().strip()

    if equipment not in equipment_list:
        messagebox.showwarning("Warning", "Equipment does not exist.")
        return

    for booking in bookings:
        if booking["equipment"] == equipment and booking["date"] == date:
            messagebox.showwarning("Warning", "Equipment already booked for this date.")
            return

    new_booking = {
        "id": booking_id_counter,
        "student": student,
        "equipment": equipment,
        "date": date
    }

    bookings.append(new_booking)
    booking_id_counter += 1

    messagebox.showinfo("Success", "Booking recorded successfully.")


def view_equipment():
    output.delete("1.0", tk.END)
    if not equipment_list:
        output.insert(tk.END, "No equipment available.\n")
    else:
        for item in equipment_list:
            output.insert(tk.END, f"{item}\n")


def view_bookings():
    output.delete("1.0", tk.END)
    if not bookings:
        output.insert(tk.END, "No bookings found.\n")
    else:
        for booking in bookings:
            output.insert(
                tk.END,
                f"ID: {booking['id']} | Student: {booking['student']} | "
                f"Equipment: {booking['equipment']} | Date: {booking['date']}\n"
            )


def search_by_student():
    name = entry_search_student.get().strip()
    output.delete("1.0", tk.END)
    found = False

    for booking in bookings:
        if booking["student"] == name:
            output.insert(
                tk.END,
                f"ID: {booking['id']} | Equipment: {booking['equipment']} | Date: {booking['date']}\n"
            )
            found = True

    if not found:
        output.insert(tk.END, "No bookings found.\n")


def cancel_booking():
    try:
        cancel_id = int(entry_cancel_id.get().strip())
    except ValueError:
        messagebox.showwarning("Warning", "Invalid ID.")
        return

    for booking in bookings:
        if booking["id"] == cancel_id:
            bookings.remove(booking)
            messagebox.showinfo("Success", "Booking cancelled successfully.")
            return

    messagebox.showwarning("Warning", "Booking ID not found.")


# -------------------- FRAME STRUCTURE --------------------

# Title Frame
frame_title = tk.Frame(root, bg="#f4f6f8")
frame_title.pack(pady=10)

tk.Label(frame_title,
         text="Student Equipment Booking System",
         font=("Arial", 18, "bold"),
         bg="#f4f6f8",
         fg="#2c3e50").pack()


# Input Frame
frame_input = tk.Frame(root, bg="#f4f6f8")
frame_input.pack(pady=10)

# Grid layout
tk.Label(frame_input, text="Equipment Name:", bg="#f4f6f8").grid(row=0, column=0, padx=5, pady=5, sticky="e")
entry_equipment = tk.Entry(frame_input, width=25)
entry_equipment.grid(row=0, column=1, padx=5, pady=5)

tk.Button(frame_input, text="Add Equipment",
          bg="#3498db", fg="white",
          width=18, command=add_equipment).grid(row=0, column=2, padx=5)

tk.Label(frame_input, text="Student Name:", bg="#f4f6f8").grid(row=1, column=0, padx=5, pady=5, sticky="e")
entry_student = tk.Entry(frame_input, width=25)
entry_student.grid(row=1, column=1, padx=5, pady=5)

tk.Label(frame_input, text="Booking Equipment:", bg="#f4f6f8").grid(row=2, column=0, padx=5, pady=5, sticky="e")
entry_booking_equipment = tk.Entry(frame_input, width=25)
entry_booking_equipment.grid(row=2, column=1, padx=5, pady=5)

tk.Label(frame_input, text="Date (DD-MM-YYYY):", bg="#f4f6f8").grid(row=3, column=0, padx=5, pady=5, sticky="e")
entry_date = tk.Entry(frame_input, width=25)
entry_date.grid(row=3, column=1, padx=5, pady=5)

tk.Button(frame_input, text="Record Booking",
          bg="#2ecc71", fg="white",
          width=18, command=record_booking).grid(row=3, column=2, padx=5)


# Action Frame
frame_actions = tk.Frame(root, bg="#f4f6f8")
frame_actions.pack(pady=10)

tk.Button(frame_actions, text="View Equipment",
          bg="#9b59b6", fg="white",
          width=20, command=view_equipment).grid(row=0, column=0, padx=5)

tk.Button(frame_actions, text="View All Bookings",
          bg="#e67e22", fg="white",
          width=20, command=view_bookings).grid(row=0, column=1, padx=5)


# Search Frame
frame_search = tk.Frame(root, bg="#f4f6f8")
frame_search.pack(pady=10)

tk.Label(frame_search, text="Search by Student:", bg="#f4f6f8").grid(row=0, column=0, padx=5)
entry_search_student = tk.Entry(frame_search, width=25)
entry_search_student.grid(row=0, column=1, padx=5)

tk.Button(frame_search, text="Search",
          bg="#16a085", fg="white",
          width=18, command=search_by_student).grid(row=0, column=2, padx=5)


tk.Label(frame_search, text="Cancel Booking ID:", bg="#f4f6f8").grid(row=1, column=0, padx=5)
entry_cancel_id = tk.Entry(frame_search, width=25)
entry_cancel_id.grid(row=1, column=1, padx=5)

tk.Button(frame_search, text="Cancel Booking",
          bg="#e74c3c", fg="white",
          width=18, command=cancel_booking).grid(row=1, column=2, padx=5)


# Output Frame
frame_output = tk.Frame(root, bg="#f4f6f8")
frame_output.pack(pady=15)

output = tk.Text(frame_output, width=90, height=10)
output.pack()


root.mainloop()