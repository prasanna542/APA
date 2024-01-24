import tkinter as tk
from tkinter import Button, Frame, Label, StringVar, OptionMenu, messagebox, filedialog
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from matplotlib.animation import FuncAnimation
import pygame
import serial
import serial.tools.list_ports
import numpy as np
import threading

class LiveGraphApp:
    def __init__(self, root):
        self.root = root
        self.root.title('Artery Pulse Analyzer')
        
        root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth()-50, root.winfo_screenheight()-50))

        self.root.configure(bg='#404040')

        self.is_running = threading.Event()
        self.recording_data = []
        self.is_recording = False
        self.update_interval = int(0)

        pygame.mixer.init()

        self.create_widgets()
        self.setup_serial()
        self.start_data_acquisition()
        self.animate()

        self.data_thread = None

    def create_widgets(self):
        main_frame = Frame(self.root, bg='black')
        main_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)

        self.fig = Figure(figsize=(12, 12), facecolor='#000000')
        self.ax1 = self.fig.add_subplot(311)  # 3 rows, 1 column, 1st subplot
        self.ax1.set_facecolor('#000000')
        self.ax1.grid(True, color='#555555', linestyle='--', linewidth=0.5)
        self.ax1.tick_params(axis='x', colors='white')
        self.ax1.tick_params(axis='y', colors='white')

        self.ax2 = self.fig.add_subplot(312)  # 3 rows, 1 column, 2nd subplot
        self.ax2.set_facecolor('#000000')
        self.ax2.grid(True, color='#555555', linestyle='--', linewidth=0.5)
        self.ax2.tick_params(axis='x', colors='white')
        self.ax2.tick_params(axis='y', colors='white')

        self.ax3 = self.fig.add_subplot(313)  # 3 rows, 1 column, 3rd subplot
        self.ax3.set_facecolor('#000000')
        self.ax3.grid(True, color='#555555', linestyle='--', linewidth=0.5)
        self.ax3.tick_params(axis='x', colors='white')
        self.ax3.tick_params(axis='y', colors='white')

        self.canvas = FigureCanvasTkAgg(self.fig, master=main_frame)
        self.canvas.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH, expand=1)

        control_frame = Frame(main_frame, bg='#000000')
        control_frame.pack(side=tk.RIGHT, fill=tk.Y, padx=2, pady=10, expand=0)

        self.serialLabel = Label(control_frame, text="Serial Port", bg='#000000', fg='#fe007e', font=("Lucida Sans", 10))
        self.serialLabel.pack(side=tk.TOP, pady=5, padx=5)

        self.port_var = StringVar(self.root)
        self.port_var.set("Select Port")

        self.port_menu = OptionMenu(control_frame, self.port_var, *["Select Port"])
        self.port_menu.config(bg='#000000', fg='white', width=10, font=("Lucida Sans", 10), highlightthickness=2, highlightbackground="grey")
        self.port_menu.pack(side=tk.TOP, pady=5, padx=5)

        self.baud_var = StringVar(self.root)
        self.baud_var.set("9600")
        baud_rates = ["9600", "19200", "38400", "57600", "115200"]

        self.baud_menu = OptionMenu(control_frame, self.baud_var, *baud_rates)
        self.baud_menu.config(bg='#000000', fg='white', width=10, font=("Lucida Sans", 10), highlightthickness=2, highlightbackground="grey")
        self.baud_menu.pack(side=tk.TOP, pady=5, padx=5)

        self.refresh_ports_button = Button(control_frame, text='Refresh Ports', command=self.update_ports_list, width=15, bg='#404040', fg='white', font=("Lucida Sans", 10))
        self.refresh_ports_button.pack(side=tk.TOP, pady=5, padx=5)

        self.update_ports_list()

        self.start_button = Button(control_frame, text='Start', command=self.start_animation, width=15, bg='#404040', fg='white', font=("Lucida Sans", 10))
        self.start_button.pack(side=tk.TOP, pady=5, padx=5)

        self.stop_button = Button(control_frame, text='Stop', command=self.stop_animation, state=tk.DISABLED, width=15, bg='#404040', fg='white', font=("Lucida Sans", 10))
        self.stop_button.pack(side=tk.TOP, pady=5, padx=5)

        self.baud_label = Label(control_frame, text="Record Option", bg='#000000', fg='#fe007e', font=("Lucida Sans", 10))
        self.baud_label.pack(side=tk.TOP, pady=(25,5), padx=5)

        self.start_recording_button = Button(control_frame, text='Start Recording', command=self.start_recording, width=15, bg='#404040', fg='white', font=("Lucida Sans", 10))
        self.start_recording_button.pack(side=tk.TOP, pady=5, padx=5)

        self.stop_recording_button = Button(control_frame, text='Stop Recording', command=self.stop_recording, state=tk.DISABLED, width=15, bg='#404040', fg='white', font=("Lucida Sans", 10))
        self.stop_recording_button.pack(side=tk.TOP, pady=5, padx=5)

    def setup_serial(self):
        self.ser = None

    def start_data_acquisition(self):
        self.data1 = np.zeros(6000)
        self.data2 = np.zeros(6000)
        self.data3 = np.zeros(6000)
        self.data_lock = threading.Lock()

        def acquire_data():
            while self.is_running.is_set():
                try:
                    line = self.ser.readline().decode().strip()
                    value1, value2, value3, timestamp = map(float, line.split(','))

                    with self.data_lock:
                        self.data1 = np.append(self.data1, value1)
                        self.data1 = self.data1[-6000:]

                        self.data2 = np.append(self.data2, value2)
                        self.data2 = self.data2[-6000:]

                        self.data3 = np.append(self.data3, value3)
                        self.data3 = self.data3[-6000:]

                        if self.is_recording:
                            self.recording_data.append((value1, value2, value3, timestamp))

                except (serial.SerialException, ValueError, IndexError):
                    pass

        self.acquire_data = acquire_data

    def animate(self):
        self.lines1, = self.ax1.plot(self.data1, label='Sensor 1', color='#34ebc9', linewidth=1.0)
        self.lines2, = self.ax2.plot(self.data2, label='Sensor 2', color='#ffcc00', linewidth=1.0)
        self.lines3, = self.ax3.plot(self.data3, label='Sensor 3', color='#ff00ff', linewidth=1.0)

        def update_plot(frame):
            with self.data_lock:
                self.lines1.set_ydata(self.data1)
                self.ax1.relim()
                self.ax1.autoscale_view(True, True, True)

            with self.data_lock:
                self.lines2.set_ydata(self.data2)
                self.ax2.relim()
                self.ax2.autoscale_view(True, True, True)

            with self.data_lock:
                self.lines3.set_ydata(self.data3)
                self.ax3.relim()
                self.ax3.autoscale_view(True, True, True)

        animation = FuncAnimation(self.fig, update_plot, interval=self.update_interval, cache_frame_data=False)

        self.ax1.set_xticks(np.arange(0, 6000, 1000))
        self.ax2.set_xticks(np.arange(0, 6000, 1000))
        self.ax3.set_xticks(np.arange(0, 6000, 1000))

        self.canvas.draw()
        self.root.mainloop()

    def start_animation(self):
        self.start_button.config(state=tk.DISABLED)
        self.stop_button.config(state=tk.NORMAL)

        with self.data_lock:
            self.data1 = np.zeros(6000)
            self.lines1.set_ydata(self.data1)
            self.ax1.relim()
            self.ax1.autoscale_view(True, True, True)

            self.data2 = np.zeros(6000)
            self.lines2.set_ydata(self.data2)
            self.ax2.relim()
            self.ax2.autoscale_view(True, True, True)

            self.data3 = np.zeros(6000)
            self.lines3.set_ydata(self.data3)
            self.ax3.relim()
            self.ax3.autoscale_view(True, True, True)

        selected_port = self.port_var.get()
        selected_baud = int(self.baud_var.get())

        if selected_port != "Select Port":
            try:
                self.ser = serial.Serial(selected_port, selected_baud, timeout=1)
                self.start_animation_thread()
            except serial.SerialException as e:
                self.show_error_message(f"Error opening serial port: {e}")
                self.stop_animation()

    def start_animation_thread(self):
        self.is_running.set()
        self.data_thread = threading.Thread(target=self.acquire_data, daemon=True)
        self.data_thread.start()

    def stop_animation(self):
        self.stop_button.config(state=tk.DISABLED)
        self.start_button.config(state=tk.NORMAL)

        self.is_running.clear()
        if self.data_thread and self.data_thread.is_alive():
            self.data_thread.join()

        if self.ser:
            self.ser.close()

    def start_recording(self):
        self.play_sound("csLRo1Kk.mp3") 
        self.start_recording_button.config(state=tk.DISABLED)
        self.stop_recording_button.config(state=tk.NORMAL)
        self.is_recording = True
        self.recording_data = []

    def play_sound(self, sound_file):
        try:
            pygame.mixer.music.load(sound_file)
            pygame.mixer.music.play()
        except pygame.error as e:
            print(f"Error playing sound: {e}")

    def stop_recording(self):
        self.play_sound("NpdthlD1.mp3") 
        self.stop_recording_button.config(state=tk.DISABLED)
        self.start_recording_button.config(state=tk.NORMAL)
        self.is_recording = False

        if self.recording_data:
            self.save_data()

    def save_data(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV files", "*.csv")])
        if file_path:
            try:
                with open(file_path, 'w') as file:
                    file.write("Value1, Value2, Value3, Timestamp\n")
                    for data_point in self.recording_data:
                        file.write(f"{data_point[0]}, {data_point[1]}, {data_point[2]}, {data_point[3]}\n")
                messagebox.showinfo("Success", "Data saved successfully.")
            except Exception as e:
                self.show_error_message(f"Error saving data: {e}")

    def update_ports_list(self):
        available_ports = [port.device for port in serial.tools.list_ports.comports()]
        menu = self.port_menu["menu"]
        menu.delete(0, "end")
        for port in available_ports:
            menu.add_command(label=port, command=lambda p=port: self.port_var.set(p))

    def show_error_message(self, message):
        messagebox.showerror("Error", message)

if __name__ == '__main__':
    root = tk.Tk()
    app = LiveGraphApp(root)
    root.mainloop()
