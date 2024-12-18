import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import scrolledtext

appointments = {}  # Dictionary to store appointments: {appointment_id: {'pet_name': ..., 'owner_name': ..., 'date': ..., 'time': ...}}
next_appointment_id = 1  # Counter for assigning unique IDs


def register_appointment():
    """register a new appointment."""
    global next_appointment_id
    pet_type = input("Enter pet's type (e.g, dog, cat, hamster): ")
    owner_name = input("Enter owner's name: ")
    date = input("Enter appointment date (YYYY-MM-DD): ")
    time = input("Enter appointment time (HH:MM): ")
    reason = input("Enter appoinment reason (e.g., check up, vaccination, surgery): ")

    appointment = {
        'pet_type': pet_type,
        'owner_name': owner_name,
        'date': date,
        'time': time,
        'reason':reason
    }
    appointments[next_appointment_id] = appointment
    print(f"Appointment created with ID: {next_appointment_id}")
    next_appointment_id += 1


def view_appointment(appointment_id):
    """view an existing appointment."""
    if appointment_id in appointments:
        appointment = appointments[appointment_id]
        print(f"Appointment Details (ID: {appointment_id}):")
        print(f"  Pet Type: {appointment['pet_type']}")
        print(f"  Owner Name: {appointment['owner_name']}")
        print(f"  Date: {appointment['date']}")
        print(f"  Time: {appointment['time']}")
        print(f"  Reason: {appointment ['reason']}")
    else:
        print("Appointment not found.")


def update_appointment(appointment_id):
    """Updates an existing appointment."""
    if appointment_id in appointments:
        appointment = appointments[appointment_id]
        print(f"Current Appointment Details (ID: {appointment_id}):")
        print(appointment)  # Show current details for reference

        pet_type = input("Enter new pet's type (leave blank to keep current): ") or appointment['pet_type']
        owner_name = input("Enter new owner's name (leave blank to keep current): ") or appointment['owner_name']
        date = input("Enter new appointment date (YYYY-MM-DD, leave blank to keep current): ") or appointment['date']
        time = input("Enter new appointment time (HH:MM, leave blank to keep current): ") or appointment['time']
        reason = input("Enter new appointment reason (check up, vaccination, surgery):") or appointment ['reason']

        appointment = {
        'pet_type': pet_type,
        'owner_name': owner_name,
        'date': date,
        'reason':reason
    }
        print("Appointment updated successfully.")
    else:
        print("Appointment not found.")


def delete_appointment(appointment_id):
    """Deletes an existing appointment."""
    if appointment_id in appointments:
        del appointments[appointment_id]
        print("Appointment deleted successfully.")
    else:
        print("Appointment not found.")


def list_appointments():
    """Lists all appointments."""
    if appointments:
        print("All Appointments:")
        for appointment_id, details in appointments.items():
            print(f"ID: {appointment_id}, Pet: {details['pet_type']}, Owner: {details['owner_name']}, Date: {details['date']}, Time: {details['time']}")
    else:
        print("No appointments scheduled.")



while True:
    print("\nVet Appointment System Menu:")
    print("1. Register Appointment")
    print("2. View Appointment")
    print("3. Update Appointment")
    print("4. Delete Appointment")
    print("5. List Appointments")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        register_appointment()
    elif choice == '2':
        appointment_id = int(input("Enter appointment ID: "))
        view_appointment(appointment_id)
    elif choice == '3':
        appointment_id = int(input("Enter appointment ID: "))
        update_appointment(appointment_id)
    elif choice == '4':
        appointment_id = int(input("Enter appointment ID: "))
        delete_appointment(appointment_id)
    elif choice == '5':
        list_appointments()
    elif choice == '6':
        break
    else:
        print("Invalid choice. Please try again.")

#vet appointment GUI

appointments = {}
next_appointment_id = 1

def register_appointment():
    pet_type = pet_type_entry.get()
    owner_name = owner_name_entry.get()
    date = date_entry.get()
    time = time_entry.get()

    if not all([pet_type, owner_name, date, time]):
        messagebox.showerror("Error", "All fields are required.")
        return

    global next_appointment_id
    appointments[next_appointment_id] = {
        'pet_type': pet_type,
        'owner_name': owner_name,
        'date': date,
        'time': time,
        'reason': reason_entry
    }
    messagebox.showinfo("Success", f"Appointment registered with ID: {next_appointment_id}")
    next_appointment_id += 1
    clear_fields()
    list_appointments()

def view_appointment():
    try:
        appointment_id = int(appointment_id_entry.get())
        if appointment_id in appointments:
            appointment = appointments[appointment_id]
            view_text.delete("1.0", tk.END)
            view_text.insert(tk.END, f"Pet Type: {appointment['pet_type']}\n")
            view_text.insert(tk.END, f"Owner Name: {appointment['owner_name']}\n")
            view_text.insert(tk.END, f"Date: {appointment['date']}\n")
            view_text.insert(tk.END, f"Time: {appointment['time']}\n")
            view_text.insert(tk.END, f"Reason: {appointment['reason']}\n")
        else:
            messagebox.showwarning("Warning", "Appointment not found.")
    except ValueError:
        messagebox.showerror("Error", "Invalid appointment ID.")


def update_appointment():
    try:
        appointment_id = int(appointment_id_entry.get())
        if appointment_id in appointments:
            appointment = appointments[appointment_id]
            # Get updated values (simplified for brevity - you'd want better input validation)
            appointment['pet_type'] = pet_type_entry.get()
            appointment['owner_name'] = owner_name_entry.get()
            appointment['date'] = date_entry.get()
            appointment['time'] = time_entry.get()
            appointment['reason'] = reason_entry.get()
            messagebox.showinfo("Success", "Appointment updated successfully.")
            list_appointments()
        else:
            messagebox.showwarning("Warning", "Appointment not found.")
    except ValueError:
        messagebox.showerror("Error", "Invalid appointment ID.")

def delete_appointment():
    try:
        appointment_id = int(appointment_id_entry.get())
        if appointment_id in appointments:
            del appointments[appointment_id]
            messagebox.showinfo("Success", "Appointment deleted successfully.")
            list_appointments()
        else:
            messagebox.showwarning("Warning", "Appointment not found.")
    except ValueError:
        messagebox.showerror("Error", "Invalid appointment ID.")


def list_appointments():
    appointment_list.delete("1.0", tk.END)
    if appointments:
        for appointment_id, details in appointments.items():
            appointment_list.insert(tk.END, f"ID: {appointment_id}, Pet: {details['pet_type']}, Owner: {details['owner_name']}, Date: {details['date']}, Time: {details['time']}\n")
    else:
        appointment_list.insert(tk.END, "No appointments scheduled.\n")

def clear_fields():
    pet_type_entry.delete(0, tk.END)
    owner_name_entry.delete(0, tk.END)
    date_entry.delete(0, tk.END)
    time_entry.delete(0, tk.END)
    reason_entry.delete(0, tk.END)
    appointment_id_entry.delete(0, tk.END)
    view_text.delete("1.0", tk.END)



root = tk.Tk()
root.title("Vet Appointment System")

# Registration Section
pet_type_label = ttk.Label(root, text="Pet Type(e.g.,dog, cat, hamster):")
pet_type_label.grid(row=0, column=0, sticky=tk.W)
pet_type_entry = ttk.Entry(root)
pet_type_entry.grid(row=0, column=1)

owner_name_label = ttk.Label(root, text="Owner Name:")
owner_name_label.grid(row=1, column=0, sticky=tk.W)
owner_name_entry = ttk.Entry(root)
owner_name_entry.grid(row=1, column=1)

date_label = ttk.Label(root, text="Date (YYYY-MM-DD):")
date_label.grid(row=2, column=0, sticky=tk.W)
date_entry = ttk.Entry(root)
date_entry.grid(row=2, column=1)

time_label = ttk.Label(root, text="Time (HH:MM):")
date_label.grid(row=3, column=0, sticky=tk.W)
time_entry = ttk.Entry(root)
time_entry.grid(row=3, column=1)

reason_label = ttk.Label(root, text="Reason (e.g., check up, vaccination, surgery):")
reason_label.grid(row=4, column=0, sticky=tk.W)
reason_entry = ttk.Entry(root)
reason_entry.grid(row=4, column=1)


register_button = ttk.Button(root, text="Register Appointment", command=register_appointment)
register_button.grid(row=4, column=1)


# View, Update, Delete Section
appointment_id_label = ttk.Label(root, text="Appointment ID:")
appointment_id_label.grid(row=5, column=0, sticky=tk.W)
appointment_id_entry = ttk.Entry(root)
appointment_id_entry.grid(row=5, column=1)

view_button = ttk.Button(root, text="View Appointment", command=view_appointment)
view_button.grid(row=6, column=0)

update_button = ttk.Button(root, text="Update Appointment", command=update_appointment)
update_button.grid(row=6, column=1)

delete_button = ttk.Button(root, text="Delete Appointment", command=delete_appointment)
delete_button.grid(row=7, column=0, columnspan=2)

#View Text Area
view_text = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=40, height=5)
view_text.grid(row=8, column=0, columnspan=2)

# Appointment List
appointment_list_label = ttk.Label(root, text="Appointments:")
appointment_list_label.grid(row=9, column=0, sticky=tk.W)
appointment_list = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=40, height=10)
appointment_list.grid(row=10, column=0, columnspan=2)
list_appointments()

root.mainloop()