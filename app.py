import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter.ttk import Progressbar
from telegram import Bot

def upload_file():
    bot_token = bot_token_entry.get()
    chat_id = chat_id_entry.get()

    bot = Bot(token=bot_token)
    file_path = filedialog.askopenfilename()

    if file_path:
        try:
            with open(file_path, 'rb') as file:
                total_bytes = file.seek(0, 2)  # Get total file size
                file.seek(0)

                sent_bytes = 0
                chunk_size = 1024  # You can modify this chunk size as needed

                while True:
                    chunk = file.read(chunk_size)
                    if not chunk:
                        break

                    bot.send_document(chat_id=chat_id, document=chunk)
                    sent_bytes += len(chunk)

                    # Update progress bar
                    progress = min(int((sent_bytes / total_bytes) * 100), 100)
                    progress_var.set(progress)
                    root.update_idletasks()

                messagebox.showinfo("Success", "File uploaded successfully!")
                progress_var.set(0)  # Reset progress bar
        except Exception as e:
            messagebox.showerror("Error", f"Failed to upload file: {str(e)}")

# Create GUI
root = tk.Tk()
root.title("Telegram File Uploader")

bot_token_label = tk.Label(root, text="Bot Token:")
bot_token_label.pack()
bot_token_entry = tk.Entry(root)
bot_token_entry.pack()

chat_id_label = tk.Label(root, text="Chat ID:")
chat_id_label.pack()
chat_id_entry = tk.Entry(root)
chat_id_entry.pack()

progress_var = tk.IntVar()
progress_bar = Progressbar(root, variable=progress_var, maximum=100)
progress_bar.pack(fill='x', padx=10, pady=5)

upload_button = tk.Button(root, text="Upload File", command=upload_file)
upload_button.pack(pady=20)

root.mainloop()
