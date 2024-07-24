import tkinter as tk
import time

class CountdownTimer:
    def __init__(self, root):
        self.root = root
        self.root.title("Countdown Timer")

        self.label = tk.Label(root, font=("Helvetica", 48), text="00:00")
        self.label.pack(pady=20)

        self.entry = tk.Entry(root, font=("Helvetica", 24))
        self.entry.pack(pady=10)

        self.start_button = tk.Button(root, text="Start", font=("Helvetica", 18), command=self.start_timer)
        self.start_button.pack()

        self.stop_button = tk.Button(root, text="Stop", font=("Helvetica", 18), command=self.stop_timer, state=tk.DISABLED)
        self.stop_button.pack(pady=10)

        self.seconds_left = 0
        self.timer_running = False

    def start_timer(self):
        if not self.timer_running:
            try:
                self.seconds_left = int(self.entry.get())
                self.update_label()
                self.timer_running = True
                self.start_button.config(state=tk.DISABLED)
                self.stop_button.config(state=tk.NORMAL)
                self.countdown()
            except ValueError:
                self.label.config(text="Invalid input")

    def stop_timer(self):
        self.timer_running = False
        self.start_button.config(state=tk.NORMAL)
        self.stop_button.config(state=tk.DISABLED)

    def countdown(self):
        while self.seconds_left > 0 and self.timer_running:
            self.update_label()
            time.sleep(1)
            self.seconds_left -= 1
        if self.timer_running:
            self.label.config(text="Time's up!")
            self.timer_running = False
            self.start_button.config(state=tk.NORMAL)
            self.stop_button.config(state=tk.DISABLED)

    def update_label(self):
        minutes = self.seconds_left // 60
        seconds = self.seconds_left % 60
        self.label.config(text=f"{minutes:02d}:{seconds:02d}")

def main():
    root = tk.Tk()
    app = CountdownTimer(root)
    root.mainloop()

if __name__ == "__main__":
    main()
