from doctest import master
import re
# import readline
from tkinter import *
from tkinter import messagebox
import tkinter as tk
from tkinter import messagebox
from tkinter.ttk import Combobox
import pyrebase
from tkcalendar import DateEntry



import tkinter as tk
from tkinter import Button, Frame, Label, StringVar, OptionMenu, messagebox, filedialog
from matplotlib import ticker
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from matplotlib.animation import FuncAnimation
import pygame
import serial
import serial.tools.list_ports
import numpy as np
import threading
import time

from tp import LiveGraphApp




# global  entry_name_for_signup,   entry_username_for_signup,   entry_confirm_password_for_signup,   entry_password_for_signup 
# global frameforsignup, frameforlogin


firebaseConfig = {
    'apiKey': "AIzaSyAc0lGU3SkNpq_3im9HXBDeEIfz9sE6OYs",
    'authDomain': "arterypulseanalyzer.firebaseapp.com",
    'databaseURL': "https://arterypulseanalyzer.firebaseio.com",
    'projectId': "arterypulseanalyzer",
    'storageBucket': "arterypulseanalyzer.appspot.com",
    'messagingSenderId': "367434956236",
    'appId': "1:367434956236:web:30f044b0c21dffd5ecb169"
}

firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()


# =======================================================================================================================================================================





# ===========================================================================================================================================================================

# def update_ports_list():
#         global available_ports, menu, port_menu

#         available_ports = [port.device for port in serial.tools.list_ports.comports()]
#         menu = port_menu["menu"]
#         menu.delete(0, "end")
#         for port in available_ports:
#             menu.add_command(label=port, command=lambda p=port: port_var.set(p))

# ========================================================================================================================================================================
def take_recording():
    tp = tk.Toplevel(master)
    LiveGraphApp(tp)
    

#     global is_running, recording_data, is_recording, update_interval, sample_count

    
#     is_running = threading.Event()
#     recording_data = []
#     is_recording = False
#     update_interval = int(0)

#     sample_count = 0

#     pygame.mixer.init()

#     global sensor1values,sensor2values,sensor3values

#     sensor1values = np.zeros(5000)
#     sensor2values = np.zeros(5000)
#     sensor3values = np.zeros(5000)


#     global frame_for_graph
#     frame_for_graph= Frame(root,bg="black")
#     frame_for_graph.pack(side=LEFT,expand=1,fill=BOTH)



#     global fig_sensor1,fig_sensor2, fig_sensor3, ax_sensor1, ax_sensor2, ax_sensor3

#     fig_sensor1 = Figure(figsize=(6, 1), facecolor='#000000')
#     ax_sensor1 = fig_sensor1.add_subplot(111)
#     ax_sensor1.set_facecolor('#000000')
#     ax_sensor1.grid(True, color='#555555', linestyle='--', linewidth=0.5)
#     ax_sensor1.tick_params(axis='x', colors='white')
#     ax_sensor1.tick_params(axis='y', colors='white')

#     fig_sensor2 = Figure(figsize=(6, 1), facecolor='#000000')
#     ax_sensor2 = fig_sensor2.add_subplot(111)
#     ax_sensor2.set_facecolor('#000000')
#     ax_sensor2.grid(True, color='#555555', linestyle='--', linewidth=0.5)
#     ax_sensor2.tick_params(axis='x', colors='white')
#     ax_sensor2.tick_params(axis='y', colors='white')

#     fig_sensor3 = Figure(figsize=(6, 1), facecolor='#000000')
#     ax_sensor3 = fig_sensor3.add_subplot(111)
#     ax_sensor3.set_facecolor('#000000')
#     ax_sensor3.grid(True, color='#555555', linestyle='--', linewidth=0.5)
#     ax_sensor3.tick_params(axis='x', colors='white')
#     ax_sensor3.tick_params(axis='y', colors='white')

       
#     global canvas_sensor1, canvas_sensor2, canvas_sensor3
#     canvas_sensor1 = FigureCanvasTkAgg(fig_sensor1, master= frame_for_graph)
#     canvas_sensor1.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

#     canvas_sensor2 = FigureCanvasTkAgg(fig_sensor2, master=frame_for_graph)
#     canvas_sensor2.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

#     canvas_sensor3 = FigureCanvasTkAgg(fig_sensor3, master=frame_for_graph)
#     canvas_sensor3.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)









#     global frame_for_control_buttons
#     frame_for_control_buttons = Frame(root,bg="red")
#     frame_for_control_buttons.pack(side=RIGHT,fill=Y,expand=0)




#     serialLabel = Label(frame_for_control_buttons, text="Serial Port", bg='#000000', fg='#fe007e', font=("Lucida Sans", 10))
#     serialLabel.pack(side=tk.TOP, pady=5, padx=5)

#     global port_var
#     port_var = tk.StringVar()
#     port_var.set("Select Port")


# #  gender_options = ["Male", "Female", "Other"]
# #     gender_var = tk.StringVar()
# #     gender_dropdown = Combobox(frame_for_add_patient, textvariable=gender_var, values=gender_options)
# #     gender_dropdown.pack(pady=(0))


#     global port_menu
#     port_menu = OptionMenu(frame_for_control_buttons, port_var, *["Select Port"])
#     port_menu.config(bg='#000000', fg='white', width=10, font=("Lucida Sans", 10), highlightthickness=2, highlightbackground="grey")
#     port_menu.pack(side=tk.TOP, pady=5, padx=5)


#     global baud_var,baud_menu
#     baud_var = StringVar()
#     baud_var.set("9600")
#     baud_rates = ["9600", "19200", "38400", "57600", "115200"]

#     baud_menu = OptionMenu(frame_for_control_buttons, baud_var, *baud_rates)
#     baud_menu.config(bg='#000000', fg='white', width=10, font=("Lucida Sans", 10), highlightthickness=2, highlightbackground="grey")
#     baud_menu.pack(side=tk.TOP, pady=5, padx=5)

#     refresh_ports_button = Button(frame_for_control_buttons, text='Refresh Ports', command=update_ports_list, width=15, bg='#404040', fg='white', font=("Lucida Sans", 10))
#     refresh_ports_button.pack(side=tk.TOP, pady=5, padx=5)

#     update_ports_list()


#     global start_button,stop_button
#     start_button = Button(frame_for_control_buttons, text='Start', command=start_animation, width=15, bg='#404040', fg='white', font=("Lucida Sans", 10))
#     start_button.pack(side=tk.TOP, pady=5, padx=5)

#     stop_button = Button(frame_for_control_buttons, text='Stop', command=stop_animation, state=tk.DISABLED, width=15, bg='#404040', fg='white', font=("Lucida Sans", 10))
#     stop_button.pack(side=tk.TOP, pady=5, padx=5)

#     record_label = Label(frame_for_control_buttons, text="Record Option", bg='#000000', fg='#fe007e', font=("Lucida Sans", 10))
#     record_label.pack(side=tk.TOP, pady=(25,5), padx=5)



#     global start_recording_button, stop_recording_button
#     start_recording_button = Button(frame_for_control_buttons, text='Start Recording', command=start_recording, width=15, bg='#404040', fg='white', font=("Lucida Sans", 10))
#     start_recording_button.pack(side=tk.TOP, pady=5, padx=5)

#     stop_recording_button = Button(frame_for_control_buttons, text='Stop Recording', command=stop_recording, state=tk.DISABLED, width=15, bg='#404040', fg='white', font=("Lucida Sans", 10))
#     stop_recording_button.pack(side=tk.TOP, pady=5, padx=5)


#     # Add a label to display the sampling rate
#     global sampling_rate_label
#     sampling_rate_label = Label(frame_for_control_buttons, text="Sampling Rate: 0 Hz", bg='#000000', fg='#fe007e', font=("Lucida Sans", 10))
#     sampling_rate_label.pack(side=tk.TOP, pady=5, padx=5)

#     legend_frame = Frame(frame_for_control_buttons, bg='#000000')
#     legend_frame.pack(side=tk.BOTTOM, fill=tk.X, expand=0)

#     sensor1_legend = Label(legend_frame, text="Sensor 1", fg='#34ebc9', bg='#000000', font=("Lucida Sans", 10))
#     sensor1_legend.pack(side=tk.LEFT, padx=5)

#     sensor2_legend = Label(legend_frame, text="Sensor 2", fg='#ff6347', bg='#000000', font=("Lucida Sans", 10))
#     sensor2_legend.pack(side=tk.LEFT, padx=5)

#     sensor3_legend = Label(legend_frame, text="Sensor 3", fg='#555555', bg='#000000', font=("Lucida Sans", 10))
#     sensor3_legend.pack(side=tk.LEFT, padx=5)


#     global toggle_visibility_sensor1_button, toggle_visibility_sensor2_button, toggle_visibility_sensor3_button
#     toggle_visibility_sensor1_button = Button(
#             frame_for_control_buttons,
#             text='Hide Graph 1',
#             command=toggle_sensor1_visibility,
#             width=15,
#             bg='#404040',
#             fg='white',
#             font=("Lucida Sans", 10)
#         )
#     toggle_visibility_sensor1_button.pack(side=tk.TOP, pady=5, padx=5)

#     toggle_visibility_sensor2_button = Button(
#             frame_for_control_buttons,
#             text='Hide Graph 2',
#             command=toggle_sensor2_visibility,
#             width=15,
#             bg='#404040',
#             fg='white',
#             font=("Lucida Sans", 10)
#         )
#     toggle_visibility_sensor2_button.pack(side=tk.TOP, pady=5, padx=5)

#     toggle_visibility_sensor3_button = Button(
#             frame_for_control_buttons,
#             text='Hide Graph 3',
#             command=toggle_sensor3_visibility,
#             width=15,
#             bg='#404040',
#             fg='white',
#             font=("Lucida Sans", 10)
#         )
#     toggle_visibility_sensor3_button.pack(side=tk.TOP, pady=5, padx=5)





#     btn_to_go_back = Button(frame_for_control_buttons,text="go back",command=lambda:(frame_for_control_buttons.destroy(),frame_for_graph.destroy(),open_module()))
#     btn_to_go_back.pack(side=BOTTOM,expand=0)

#     setup_serial()
#     start_data_acquisition()
#     animate()

#     global data_thread
#     data_thread = None


# ==========================================================================================================================================================================
# def setup_serial():
#     ser = None

# =========================================================================================================================================================================
    
# def start_data_acquisition():
#     global data_lock
#     data_lock = threading.Lock()

#     def acquire_data():
#         while is_running.is_set():
#             try:
#                 line = serial.readline().decode().strip()
#                 value1, value2,value3, timestamp = map(float, line.split(','))

#                 with data_lock:
#                     sensor1values = np.append(sensor1values, value1)
#                     sensor1values = sensor1values[-5000:]

#                     sensor2values = np.append(sensor2values, value2)
#                     sensor2values = sensor2values[-5000:]

#                     sensor3values = np.append(sensor3values, value3)
#                     sensor3values = sensor2values[-5000:]



#                     if is_recording:
#                         recording_data.append((value1, value2,value3, timestamp))


#                         # Increment the sample count for every new sample
#                     sample_count += 1

#                         # Update the sampling rate label
                    
#                     current_time = time.time()
#                     if current_time - last_update_time >= 1:
#                         # Update the sampling rate label
#                         update_sampling_rate_label()
#                         last_update_time = current_time
#                         # self.update_sampling_rate_label()     

#             except (serial.SerialException, ValueError, IndexError):
#                 pass

#     acquire_data = acquire_data

# # ==================================================================================================================================================================
    
# def update_sampling_rate_label():
#         # Update the sampling rate label based on the sample count
#         sampling_rate = sample_count
#         sampling_rate_label.config(text=f"Sampling Rate: {sampling_rate} Hz")
#         sample_count = 0  # Reset the sample count for the next second
        

# # =================================================================================================================================
        
# def animate():
#     global lines_sensor1, lines_sensor2, lines_sensor3
#     lines_sensor1, = ax_sensor1.plot(sensor1values, label='Sensor 1', color='#34ebc9', linewidth=1.0)
#     lines_sensor2, = ax_sensor2.plot(sensor2values, label='Sensor 2', color='#ff6347', linewidth=1.0)
#     lines_sensor3, = ax_sensor3.plot(sensor3values, label='Sensor 3', color='#555555', linewidth=1.0)

   

#     def update_plot():
#         with data_lock:
#             lines_sensor1.set_ydata(sensor1values)
#             ax_sensor1.relim()
#             ax_sensor1.autoscale_view(True, True, True)

#         with data_lock:
#             lines_sensor2.set_ydata(sensor2values)
#             ax_sensor2.relim()
#             ax_sensor2.autoscale_view(True, True, True)

#         with data_lock:
#             lines_sensor3.set_ydata(sensor3values)
#             ax_sensor3.relim()
#             ax_sensor3.autoscale_view(True, True, True)

#         canvas_sensor1.draw()
#         canvas_sensor2.draw()
#         canvas_sensor3.draw()

#             # Set tick label font size for Sensor 1 graph
#         ax_sensor1.tick_params(axis='x', labelsize=8)
#         ax_sensor1.tick_params(axis='y', labelsize=8)

#         # Set tick label font size for Sensor 2 graph
#         ax_sensor2.tick_params(axis='x', labelsize=8)
#         ax_sensor2.tick_params(axis='y', labelsize=8)

#         # Set tick label font size for Sensor 3 graph
#         ax_sensor3.tick_params(axis='x', labelsize=8)
#         ax_sensor3.tick_params(axis='y', labelsize=8)

#             # Format x-axis tick labels to represent 1000 as 1, 2000 as 2, etc.
#         ax_sensor1.xaxis.set_major_formatter(ticker.FuncFormatter(lambda x, pos: f'{int(x/1000)}'))
#         ax_sensor2.xaxis.set_major_formatter(ticker.FuncFormatter(lambda x, pos: f'{int(x/1000)}'))
#         ax_sensor3.xaxis.set_major_formatter(ticker.FuncFormatter(lambda x, pos: f'{int(x/1000)}'))

#     animation = FuncAnimation(fig_sensor1, update_plot, interval=update_interval, cache_frame_data=False)

#     ax_sensor1.set_xticks(np.arange(0, 5000, 1000))
#     ax_sensor2.set_xticks(np.arange(0, 5000, 1000))
#     ax_sensor3.set_xticks(np.arange(0, 5000, 1000))

#     root.mainloop()

# # ================================================================================================================================================

# def start_animation():
#     start_button.config(state=tk.DISABLED)
#     stop_button.config(state=tk.NORMAL)

#     with data_lock:
#         sensor1values = np.zeros(5000)
#         sensor2values = np.zeros(5000)
#         sensor3values = np.zeros(5000)
#         lines_sensor1.set_ydata(sensor1values)
#         lines_sensor2.set_ydata(sensor2values)
#         lines_sensor3.set_ydata(sensor3values)
#         ax_sensor1.relim()
#         ax_sensor1.autoscale_view(True, True, True)
#         ax_sensor2.relim()
#         ax_sensor2.autoscale_view(True, True, True)
#         ax_sensor3.relim()
#         ax_sensor3.autoscale_view(True, True, True)

#     selected_port = port_var.get()
#     selected_baud = int(baud_var.get())

#     if selected_port != "Select Port":
#         try:
#             ser = serial.Serial(selected_port, selected_baud, timeout=1)
#             start_animation_thread()
#         except serial.SerialException as e:
#             show_error_message(f"Error opening serial port: {e}")
#             stop_animation()

# # ==============================================================================================================================================================
            
# def start_animation_thread(self):
#     global data_thread, is_running
#     is_running.set()
#     data_thread = threading.Thread(target = "acquire_data", daemon=True)
#     data_thread.start()

# # ================================================================================================================================================================
    
# def stop_animation(self):
#     stop_button.config(state=tk.DISABLED)
#     start_button.config(state=tk.NORMAL)

#     is_running.clear()
#     if data_thread and data_thread.is_alive():
#         data_thread.join()

#     if serial:
#         serial.close()

# # ================================================================================================================================================================
        
# def start_recording(self):
#     play_sound("csLRo1Kk.mp3") 
#     start_recording_button.config(state=tk.DISABLED)
#     stop_recording_button.config(state=tk.NORMAL)

#     global is_recording,recording_data
#     is_recording = True
#     recording_data = []

# # ===============================================================================================================================================================
    
# def play_sound(sound_file):
#     try:
#         pygame.mixer.music.load(sound_file)
#         pygame.mixer.music.play()
#     except pygame.error as e:
#         print(f"Error playing sound: {e}")

# # ================================================================================================================================================
        

# def stop_recording(self):
#     play_sound("NpdthlD1.mp3") 
#     stop_recording_button.config(state=tk.DISABLED)
#     start_recording_button.config(state=tk.NORMAL)
#     global is_recording
#     is_recording = False

#     if recording_data:
#         save_data()

# # ====================================================================================================================================================================
        

# def save_data():
#     file_path = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV files", "*.csv")])
#     if file_path:
#         try:
#             with open(file_path, 'w') as file:
#                 file.write("Sensor1, Sensor2, Sensor3, Timestamp\n")
#                 for data_point in recording_data:
#                     file.write(f"{data_point[0]}, {data_point[1]}, {data_point[2]},{data_point[3]}\n")
#             messagebox.showinfo("Success", "Data saved successfully.")
#         except Exception as e:
#             show_error_message(f"Error saving data: {e}")

# # ===================================================================================================================================================================
            



# def toggle_sensor1_visibility():
#     toggle_visibility(lines_sensor1, canvas_sensor1, fig_sensor1, toggle_visibility_sensor1_button,1)

# def toggle_sensor2_visibility():
#     toggle_visibility(lines_sensor2, canvas_sensor2, fig_sensor2, toggle_visibility_sensor2_button,2)

# def toggle_sensor3_visibility():
#     toggle_visibility(lines_sensor3, canvas_sensor3, fig_sensor3, toggle_visibility_sensor3_button,3)


# # ================================================================================================================================================================

# def toggle_visibility(lines, canvas, fig, toggle_button,no):
#     if lines.get_visible():
#         lines.set_visible(False)
#         canvas.get_tk_widget().pack_forget()
#         toggle_button.config(text= f'Show Graph {no}')
#     else:
#         lines.set_visible(True)
#         canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
#         toggle_button.config(text= f'Hide Graph {no}')

#     canvas.draw()

# ==================================================================================================================================================================
    
def show_error_message(message):
    messagebox.showerror("Error", message)

# ==================================================================================================================================================================
def validate_name(name):
    # Allow only letters in the name
    return bool(re.match("^[a-zA-Z]+$", name))

def validate_phone(phone):
    # Allow only numbers in the phone number
    return bool(re.match("^[0-9]+$", phone))

def validate_email(email):
    # Use a simple regex for basic email validation
    return bool(re.match(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$", email))

def validate_city(city):
    # Allow only letters in the city
    return bool(re.match("^[a-zA-Z]+$", city))


# =========================================================================================================================================================================
    
def next_button_logic():

    global entry_for_name_add_patient, gender_dropdown, entry_for_email_add_patient, entry_for_phone_add_patient, dob_entry, state_dropdown, entry_for_city_add_patient

    name = entry_for_name_add_patient.get()
    gender = gender_dropdown.get()
    email = entry_for_email_add_patient.get()
    phone = entry_for_phone_add_patient.get()
    dob = dob_entry.get()
    state = state_dropdown.get()
    city = entry_for_city_add_patient.get()

  

    if not name or not gender or not email or not phone or not dob or not state or not city:
        messagebox.showerror("Signup Error", "Please enter complete details.")
        return 

    elif not validate_email(email):
        messagebox.showerror("Signup Error", "Invalid email address.")
        return
    
    elif not validate_name(name):
        messagebox.showerror("Signup Error", "Invalid name. Only letters are allowed.")
        return

    elif not validate_phone(phone):
        messagebox.showerror("Signup Error", "Invalid phone number. Only numbers are allowed.")
        return

    elif not validate_city(city):
        messagebox.showerror("Signup Error","Invalid city. Only letters are allowed.")
        return
    
       
# ==========================================================================================================================================================================        

def add_patient():

    global entry_for_name_add_patient, gender_dropdown, entry_for_email_add_patient, entry_for_phone_add_patient, dob_entry, state_dropdown, entry_for_city_add_patient

    frame_for_add_patient = Frame(root,bg="#38B18E")
    frame_for_add_patient.pack(side=tk.TOP, fill=BOTH, expand=1, pady=0)


    label_for_name_add_patient = Label(frame_for_add_patient,text="Name",bg="#38B18E")
    label_for_name_add_patient.pack(pady=(10,5))
    entry_for_name_add_patient = Entry(frame_for_add_patient)
    entry_for_name_add_patient.pack(pady=0)

     # Dropdown menu for gender
    
    label_for_gender_add_patient = Label(frame_for_add_patient,text="Gender",bg="#38B18E")
    label_for_gender_add_patient.pack(pady=(10,5))

    gender_options = ["Male", "Female", "Other"]
    gender_var = tk.StringVar()
    gender_dropdown = Combobox(frame_for_add_patient, textvariable=gender_var, values=gender_options)
    gender_dropdown.pack(pady=(0))

    label_for_email_add_patient = Label(frame_for_add_patient,text="Email",bg="#38B18E")
    label_for_email_add_patient.pack(pady=(10,5))
    entry_for_email_add_patient = Entry(frame_for_add_patient)
    entry_for_email_add_patient.pack(pady=0)

    label_for_phone_add_patient = Label(frame_for_add_patient,text="Phone",bg="#38B18E")
    label_for_phone_add_patient.pack(pady=(10,5))
    entry_for_phone_add_patient = Entry(frame_for_add_patient)
    entry_for_phone_add_patient.pack(pady=0)


    # DateEntry widget for Date of Birth
    label_for_dob_add_patient = Label(frame_for_add_patient,text="Date of Birth",bg="#38B18E")
    label_for_dob_add_patient.pack(pady=(10,5))

    dob_var = tk.StringVar()
    dob_entry = DateEntry(frame_for_add_patient, textvariable=dob_var, date_pattern='yyyy/mm/dd', showweeknumbers=False, selectbackground="#38B18E")
    dob_entry.pack(pady=0)

     # Dropdown menu for state (all states of India)
    
    label_for_state_add_patient = Label(frame_for_add_patient,text="State",bg="#38B18E")
    label_for_state_add_patient.pack(pady=(10,5))


    state_options = [
        "Andhra Pradesh", "Arunachal Pradesh", "Assam", "Bihar", "Chhattisgarh", "Goa", "Gujarat",
        "Haryana", "Himachal Pradesh", "Jharkhand", "Karnataka", "Kerala", "Madhya Pradesh",
        "Maharashtra", "Manipur", "Meghalaya", "Mizoram", "Nagaland", "Odisha", "Punjab", "Rajasthan",
        "Sikkim", "Tamil Nadu", "Telangana", "Tripura", "Uttar Pradesh", "Uttarakhand", "West Bengal"
    ]
    state_var = tk.StringVar()
    state_dropdown = Combobox(frame_for_add_patient, textvariable=state_var, values=state_options)
    state_dropdown.pack(pady=0)

    label_for_city_add_patient = Label(frame_for_add_patient,text="City",bg="#38B18E")
    label_for_city_add_patient.pack(pady=(10,5))
    entry_for_city_add_patient = Entry(frame_for_add_patient)
    entry_for_city_add_patient.pack(pady=0)

    btn_next_add_patient = Button(frame_for_add_patient,text="Next",width=30,command=lambda:(next_button_logic()))
    btn_next_add_patient.pack(pady=(30,5))

    btn_to_go_back = Button(frame_for_add_patient,text="go back",command=lambda:(frame_for_add_patient.destroy(),open_module()))
    btn_to_go_back.pack(pady=10)

def upload_recording():
    # Function to handle the Upload Recording button click

    def select_files():
        # Function to open file dialog and select CSV files
        files = filedialog.askopenfilenames(
            title="Select CSV Files",
            filetypes=[("CSV files", "*.csv")]
        )
        for file in files:
            listbox_files.insert("end", file)

    def upload_files():
        # Function to handle the Upload button click
        selected_files = listbox_files.get(0, "end")
        # Perform further processing with the selected files (e.g., read and analyze)

    # Create a new frame for the Upload Recording function
    upload_frame = Frame(root, bg="#38B18E")
    upload_frame.pack(side="top", fill="both", expand=1, pady=10)

   

    # Listbox to display selected files
    listbox_files = Listbox(upload_frame, selectmode="none", width=50, height=10)
    listbox_files.pack(pady=10)

     # Button to open file dialog and select CSV files
    btn_select_files = Button(upload_frame, text="Select Files", command=select_files, width=15, height=2)
    btn_select_files.pack(pady=10)

    # Button to upload selected files
    btn_upload = Button(upload_frame, text="Upload", command=upload_files, width=15, height=2)
    btn_upload.pack(pady=10)

    btn_go_back = Button(upload_frame,text="back",command=lambda:(upload_frame.destroy(),open_module()))
    btn_go_back.pack(side=BOTTOM,anchor=SW)

def analyze_recording():
    pass

def Patients_list():
    pass







# ===========================================================================================================================================================================

#logic about modules

def open_module():
    

    # Create the first frame and set its height
    frame_modules = tk.Frame(root, bg="#38B18E")
    frame_modules.pack(side=tk.TOP, fill=BOTH, expand=1, pady=0)

    btn_module1 = Button(frame_modules, text="Take Recording", width=15, height=2,command=lambda:(take_recording(),frame_modules.destroy()))
    btn_module1.pack(side=TOP, padx=0, pady=(50,10))

    btn_module2 = Button(frame_modules, text="Add Patient", width=15, height=2,command=lambda:(add_patient(),frame_modules.destroy()))
    btn_module2.pack(side=TOP, padx=0, pady=10)

    btn_module3 = Button(frame_modules, text="Upload Recording", width=15, height=2,command=lambda:(upload_recording(),frame_modules.destroy()))
    btn_module3.pack(side=TOP, padx=0, pady=10)

    btn_module4 = Button(frame_modules, text="Analyze Recording", width=15, height=2, command=analyze_recording)
    btn_module4.pack(side=TOP, padx=0, pady=10)

    btn_module5 = Button(frame_modules, text="Patients", width=15, height=2, command=Patients_list)
    btn_module5.pack(side=TOP, padx=0, pady=10)




# ========================================================================================================================================================================
    

def send_reset_email():
    email = entry_for_reset_email.get()

    # Validate email format
    if not email:
        messagebox.showerror("Error", "Please enter your email address.")
        return
    elif not re.match(r"[^@]+@[^@]+\.[^@]+", email):
        messagebox.showerror("Error", "Invalid email address.")
        return

    try:
        auth.send_password_reset_email(email)
        messagebox.showinfo("Password Reset", f"Password reset email sent to {email}")
        loginnow()
        frame_for_forgot_password.destroy()
    except Exception as e:
        messagebox.showerror("Error", f"Error sending reset email: {e}")



# this code is to show forgot password screen 
        
def forgotPassword():
    global entry_for_reset_email, frame_for_forgot_password

    frame_for_forgot_password = Frame(root,bg="#38B18E")
    frame_for_forgot_password.pack(side=TOP,fill=BOTH,expand=True)

    label_for_email = Label(frame_for_forgot_password,text="Enter Your Email")
    label_for_email.pack(pady=(30,10))

    entry_for_reset_email = Entry(frame_for_forgot_password)
    entry_for_reset_email.pack(pady=5)

    btn_for_reset_email = Button(frame_for_forgot_password, text="verify",command=send_reset_email)
    btn_for_reset_email.pack(pady=(5))


    btn_for_login = Button(frame_for_forgot_password,text="go to login page ->",command=lambda:(frame_for_forgot_password.destroy(),loginnow()),bg="#38b18e",border=0)
    btn_for_login.pack(pady=5)






# ========================================================================================================================================================================


# Function to handle the signup page 
def signupnow():

    # previous.destroy()
    
    global  entry_name_for_signup,   entry_username_for_signup,   entry_confirm_password_for_signup,   entry_password_for_signup , frameforsignup


    frameforsignup = Frame(root,bg="#38B18E")
    frameforsignup.pack(side=TOP, fill=BOTH,expand=True)
  

    label_name_for_signup = Label(frameforsignup, text="enter your name",bg="#38B18E")
    label_name_for_signup.pack(pady=(10,0))

    entry_name_for_signup = Entry(frameforsignup)
    entry_name_for_signup.pack()


    label_username_for_signup = Label(frameforsignup, text="enter your email",bg="#38B18E")
    label_username_for_signup.pack()

    entry_username_for_signup = Entry(frameforsignup)
    entry_username_for_signup.pack()

    label_password_for_signup = Label(frameforsignup, text="password",bg="#38B18E")
    label_password_for_signup.pack()
  

    entry_password_for_signup = Entry(frameforsignup, show="*")
    entry_password_for_signup.pack()


    label_confirm_password_for_signup = Label(frameforsignup, text="confirm password",bg="#38B18E")
    label_confirm_password_for_signup.pack()

    entry_confirm_password_for_signup = Entry(frameforsignup, show="*")
    entry_confirm_password_for_signup.pack()


    btn_login_for_signup = Button(frameforsignup, text="crate account",command=validate_signup)
    btn_login_for_signup.pack(pady=10)

    btn_forgot_password_for_signup = Button(frameforsignup,text="already have an account? login ",bg="#38B18E",border=0, command=lambda:(loginnow(),frameforsignup.destroy()))
    btn_forgot_password_for_signup.pack()


   



# def validate_email(email):
#     # Simple email validation using a regular expression
#     pattern = re.compile(r"[^@]+@[^@]+\.[^@]+")
#     return bool(re.match(pattern, email))



def validate_signup():
    global entry_password_for_signup, entry_username_for_signup,  entry_confirm_password_for_signup, entry_name_for_signup
    email = entry_username_for_signup.get()
    password = entry_password_for_signup.get()
    confirmPass = entry_confirm_password_for_signup.get()
    nameOfUser = entry_name_for_signup.get()

    if not email or not password or not confirmPass or not nameOfUser:
        messagebox.showerror("Signup Error", "Please enter complete details.")
    elif not validate_email(email):
        messagebox.showerror("Signup Error", "Invalid email address.")
    elif len(password) < 6:
        messagebox.showerror("Signup Error", "Password must be at least 6 characters.")
    else:
        try:
            auth.create_user_with_email_and_password(email, password)
            messagebox.showinfo("Signup", "Account created successfully!")
        except:
            messagebox.showerror("Signup Error", "Error creating account")



# ===================================================================================================================================================================

#function to show login validation
def login_validation():
    global entry_password,entry_username

    email = entry_username.get()
    password = entry_password.get()

    try:
        auth.sign_in_with_email_and_password(email, password)
        messagebox.showinfo("Login", "Logged in successfully!")
        frameforlogin.destroy()
        frame2.destroy()
        open_module()
    except:
        messagebox.showerror("Login Error", "Invalid username or password")



# Function to show the login page click
def loginnow():

    # previous.destroy()
    global entry_username, entry_password, frameforlogin

    frameforlogin = Frame(root,bg="#38B18E")
    frameforlogin.pack(side=TOP,fill=BOTH,expand=TRUE)

    # Create and place widgets
    label_username = Label(frameforlogin, text="Username:",bg="#38B18E")
    label_username.pack()

    # Label(frameforlogin,height=1,width=10).pack()

    entry_username = Entry(frameforlogin)
    entry_username.pack()

    label_password = Label(frameforlogin, text="Password:",bg="#38B18E")
    label_password.pack()

    entry_password = Entry(frameforlogin, show="*")
    entry_password.pack()

    btn_login = Button(frameforlogin, text="Login",command=login_validation)
    btn_login.pack(pady=10)

    btn_forgot_password = Button(frameforlogin,text="forgot password?",bg="#38B18E",border=0,command= lambda: (forgotPassword(),frameforlogin.destroy()))
    btn_forgot_password.pack()

    btn_create_account = Button(frameforlogin,text="don't have an account? create one",bg="#38B18E",border=0,command=lambda:(frameforlogin.destroy(),signupnow()))
    btn_create_account.pack()






# ============================================================================================================================================================================
# main window
    
root = Tk()
root.title("Artery Pulse Analyzer")

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

x_position = (screen_width - 925) // 2
y_position = (screen_height - 700) // 2

root.geometry(f'925x600+{x_position}+{y_position}')
root.configure(bg='#fff')

current_user = auth.current_user
if current_user:
    # If the user is already logged in, directly open the main app window
    open_module()

else:


    # top of top frame 
    frame0 = Frame(root, bg="#38b18e")
    frame0.pack(expand=0, fill=X, side=TOP)

    # Load the image file (make sure the file format is supported, e.g., GIF)
    image_path = "logo.png"
    original_img = PhotoImage(file=image_path)

    # Set the desired height and width
    new_height = 3000
    new_width = 2000

    # Resize the image
    # resized_img = original_img.subsample(original_img.width() // new_width, original_img.height() // new_height)

    # Create a Label widget to display the resized image
    img_label = tk.Label(frame0, image=original_img,bg="#38b18e")
    img_label.pack(side=LEFT,pady=10)
    # img_label.pack(side=LEFT)


    # Top frame
    frame1 = Frame(root, bg="#38B18E")
    frame1.pack(expand=True, fill="both",side=TOP)

    # maintext = Label(frame1, text="Engineering next \ngeneration smart \ndiagnostic tools for better \nclinical outcomes", font=("arial", 40), bg="#38b18e",fg="white").pack(pady=100)
    loginNow = Button(frame1, text="Login", background="white", command=lambda:(loginnow(),frame1.destroy()) ,width=20,height=3).pack( padx=10,pady=(200,10),side=TOP,expand=0)
    signupNow = Button(frame1, text="Signup", background="white", command=lambda: (signupnow(),frame1.destroy()),width=20,height=3).pack( padx=10,side=TOP,expand=0)

    # Footer frame. This frame is for footer
    frame2 = Frame(root)
    frame2.pack(side=BOTTOM, fill=X,expand=0)

    # Copyright text
    copyright_text = "Copyright © 2024 Acuradyne Systems"
    copyright_label = Label(frame2, text=copyright_text)
    copyright_label.pack(pady=10)

root.mainloop()
