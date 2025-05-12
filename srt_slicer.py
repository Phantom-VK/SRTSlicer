import sys
import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import os
import re
from datetime import datetime, timedelta


class SRTSlicerApp:
    def __init__(self, master):
        self.master = master
        master.title("SRT Word-Level Timestamp Slicer")
        master.geometry("700x600")
        master.configure(bg='#f0f0f0')

        # Set application icon
        try:
            # Try to load icon from multiple possible locations
            icon_paths = [
                'app_icon.ico',  # Current directory
                os.path.join(os.path.dirname(__file__), 'app_icon.ico'),  # Script directory
                os.path.join(sys.path[0], 'app_icon.ico')  # Executable directory
            ]

            # Find the first existing icon
            icon_path = next((path for path in icon_paths if os.path.exists(path)), None)

            if icon_path:
                master.iconbitmap(icon_path)
            else:
                print("Icon file not found. Using default icon.")
        except Exception as e:
            print(f"Error loading icon: {e}")

        # Style
        self.style = ttk.Style()
        self.style.configure('TLabel', background='#f0f0f0', font=('Arial', 10))
        self.style.configure('TButton', font=('Arial', 10))

        # Main Container
        self.main_container = ttk.Frame(master, padding="10")
        self.main_container.pack(fill='both', expand=True, padx=10, pady=10)

        # Input File Frame
        self.create_input_file_section()

        # Output File Frame
        self.create_output_file_section()

        # Custom Filename Frame
        self.create_filename_section()

        # Distribution Method Frame
        self.create_distribution_section()

        # Processing Options Frame
        self.create_processing_options()

        # Process Button
        self.create_process_button()

        # Progress Bar
        self.progress = ttk.Progressbar(master, orient="horizontal", length=300, mode="determinate")
        self.progress.pack(pady=10)

        # Status Label
        self.status_label = ttk.Label(master, text="Ready to process", font=('Arial', 10, 'italic'))
        self.status_label.pack(pady=10)

    def create_input_file_section(self):
        """Create input file selection section."""
        input_frame = ttk.LabelFrame(self.main_container, text="Input File", padding="10")
        input_frame.pack(fill='x', pady=5)

        # File Path Entry
        self.input_path = tk.StringVar()
        input_entry = ttk.Entry(input_frame, textvariable=self.input_path, width=60)
        input_entry.pack(side='left', padx=(0, 10), expand=True, fill='x')

        # File Picker Button
        input_picker = ttk.Button(input_frame, text="Browse", command=self.browse_input_file)
        input_picker.pack(side='left')

        # File Type Selection
        self.input_type_var = tk.StringVar(value=".srt")
        input_type_label = ttk.Label(input_frame, text="File Type:")
        input_type_label.pack(side='left', padx=(10, 0))
        input_type_combo = ttk.Combobox(input_frame, textvariable=self.input_type_var,
                                        values=[".srt", ".txt", "*.*"], width=5)
        input_type_combo.pack(side='left', padx=(5, 0))

    def create_output_file_section(self):
        """Create output file selection section."""
        output_frame = ttk.LabelFrame(self.main_container, text="Output File", padding="10")
        output_frame.pack(fill='x', pady=5)

        # File Path Entry
        self.output_path = tk.StringVar()
        output_entry = ttk.Entry(output_frame, textvariable=self.output_path, width=60)
        output_entry.pack(side='left', padx=(0, 10), expand=True, fill='x')

        # File Picker Button
        output_picker = ttk.Button(output_frame, text="Browse", command=self.browse_output_file)
        output_picker.pack(side='left')

        # Output Type Selection
        self.output_type_var = tk.StringVar(value=".srt")
        output_type_label = ttk.Label(output_frame, text="File Type:")
        output_type_label.pack(side='left', padx=(10, 0))
        output_type_combo = ttk.Combobox(output_frame, textvariable=self.output_type_var,
                                         values=[".srt", ".txt", "*.*"], width=5)
        output_type_combo.pack(side='left', padx=(5, 0))

    def create_filename_section(self):
        """Create custom filename section."""
        filename_frame = ttk.LabelFrame(self.main_container, text="Custom Filename", padding="10")
        filename_frame.pack(fill='x', pady=5)

        # Prefix Option
        prefix_label = ttk.Label(filename_frame, text="Prefix:")
        prefix_label.pack(side='left', padx=(0, 5))
        self.prefix_var = tk.StringVar(value="word_level_")
        prefix_entry = ttk.Entry(filename_frame, textvariable=self.prefix_var, width=20)
        prefix_entry.pack(side='left', padx=(0, 10))

        # Suffix Option
        suffix_label = ttk.Label(filename_frame, text="Suffix:")
        suffix_label.pack(side='left', padx=(10, 5))
        self.suffix_var = tk.StringVar()
        suffix_entry = ttk.Entry(filename_frame, textvariable=self.suffix_var, width=20)
        suffix_entry.pack(side='left')

        # Auto-generate Checkbox
        self.auto_generate_var = tk.BooleanVar(value=True)
        auto_generate_check = ttk.Checkbutton(
            filename_frame,
            text="Auto Generate",
            variable=self.auto_generate_var,
            command=self.toggle_filename_fields
        )
        auto_generate_check.pack(side='left', padx=(10, 0))

    def create_distribution_section(self):
        """Create distribution method section."""
        distribution_frame = ttk.LabelFrame(self.main_container, text="Distribution Method", padding="10")
        distribution_frame.pack(fill='x', pady=5)

        self.distribution_var = tk.StringVar(value="equal")

        # Equal Time Radio
        equal_radio = ttk.Radiobutton(
            distribution_frame,
            text="Equal Time",
            variable=self.distribution_var,
            value="equal"
        )
        equal_radio.pack(side='left', padx=(0, 10))

        # Word Length Radio
        word_length_radio = ttk.Radiobutton(
            distribution_frame,
            text="Word Length",
            variable=self.distribution_var,
            value="word_length"
        )
        word_length_radio.pack(side='left')

    def create_processing_options(self):
        """Create processing options section."""
        options_frame = ttk.LabelFrame(self.main_container, text="Processing Options", padding="10")
        options_frame.pack(fill='x', pady=5)

        # Preserve Subtitle Structure
        self.preserve_var = tk.BooleanVar(value=True)
        preserve_check = ttk.Checkbutton(
            options_frame,
            text="Preserve Original Subtitle Structure",
            variable=self.preserve_var
        )
        preserve_check.pack(side='left')

    def create_process_button(self):
        """Create process button."""
        process_button = ttk.Button(
            self.main_container,
            text="Process SRT",
            command=self.process_srt
        )
        process_button.pack(pady=10)

    def toggle_filename_fields(self):
        """Toggle filename fields based on auto-generate checkbox."""
        state = 'disabled' if self.auto_generate_var.get() else 'normal'
        # You might want to add more fields to disable/enable here
        # For now, just as an example:
        # self.prefix_entry.configure(state=state)
        # self.suffix_entry.configure(state=state)
        pass

    def browse_input_file(self):
        """Open file dialog to select input SRT file."""
        filename = filedialog.askopenfilename(
            title="Select SRT File",
            filetypes=[("SRT Files", "*.srt"), ("Text Files", "*.txt"), ("All Files", "*.*")]
        )
        if filename:
            self.input_path.set(filename)
            # Auto-generate output path if needed
            self.auto_generate_output_path(filename)

    def auto_generate_output_path(self, input_path):
        """Automatically generate output file path."""
        if not self.auto_generate_var.get():
            return

        # Get directory and filename
        dir_path = os.path.dirname(input_path)
        base_name = os.path.splitext(os.path.basename(input_path))[0]

        # Generate output filename
        prefix = self.prefix_var.get()
        suffix = self.suffix_var.get()
        output_filename = f"{prefix}{base_name}{suffix}{self.output_type_var.get()}"

        # Set full output path
        output_path = os.path.join(dir_path, output_filename)
        self.output_path.set(output_path)

    def browse_output_file(self):
        """Open file dialog to select output SRT file."""
        filename = filedialog.asksaveasfilename(
            title="Save Word-Level SRT File",
            defaultextension=self.output_type_var.get(),
            filetypes=[
                ("SRT Files", "*.srt"),
                ("Text Files", "*.txt"),
                ("All Files", "*.*")
            ]
        )
        if filename:
            self.output_path.set(filename)

    def parse_timestamp(self, timestamp_str):
        """Convert timestamp string to datetime object."""
        return datetime.strptime(timestamp_str, '%H:%M:%S,%f')

    def generate_word_timestamps(self, start_time, end_time, words):
        """Generate individual timestamps for each word based on selected distribution method."""
        total_duration = (self.parse_timestamp(end_time) - self.parse_timestamp(start_time)).total_seconds()

        # If only one word, return entire timestamp for that word
        if len(words) == 1:
            return [(start_time, end_time, words[0])]

        # Distribution method selection
        if self.distribution_var.get() == "equal":
            # Equal time distribution
            time_per_word = total_duration / len(words)

            word_timestamps = []
            for i, word in enumerate(words):
                word_start_time = (self.parse_timestamp(start_time) + timedelta(seconds=i * time_per_word)).strftime(
                    '%H:%M:%S,%f')[:-3]
                word_end_time = (self.parse_timestamp(start_time) + timedelta(
                    seconds=(i + 1) * time_per_word)).strftime('%H:%M:%S,%f')[:-3]
                word_timestamps.append((word_start_time, word_end_time, word))

            return word_timestamps

        else:
            # Word length-based distribution
            total_chars = sum(len(word) for word in words)

            word_timestamps = []
            current_start = self.parse_timestamp(start_time)

            for word in words:
                # Proportional time based on word length
                word_proportion = len(word) / total_chars
                word_duration = total_duration * word_proportion

                word_start_time = current_start.strftime('%H:%M:%S,%f')[:-3]
                current_start += timedelta(seconds=word_duration)
                word_end_time = current_start.strftime('%H:%M:%S,%f')[:-3]

                word_timestamps.append((word_start_time, word_end_time, word))

            return word_timestamps

    def process_srt(self):
        """Main SRT processing method."""
        # Validate input
        input_file = self.input_path.get()
        output_file = self.output_path.get()

        if not input_file or not output_file:
            messagebox.showerror("Error", "Please select input and output files.")
            return

        try:
            # Read input file
            with open(input_file, 'r', encoding='utf-8') as f:
                content = f.read()

            # Reset progress
            self.progress['value'] = 0
            self.status_label.config(text="Processing...")
            self.master.update_idletasks()

            # Subtitle block extraction regex
            subtitle_pattern = re.compile(
                r'(\d+)\n(\d{2}:\d{2}:\d{2},\d{3}) --> (\d{2}:\d{2}:\d{2},\d{3})\n(.+?)(?=\n\n|\Z)', re.DOTALL)

            word_level_srt = []
            global_counter = 1

            # Find all subtitle blocks
            matches = list(subtitle_pattern.finditer(content))

            for i, match in enumerate(matches):
                # Update progress
                self.progress['value'] = (i / len(matches)) * 100
                self.master.update_idletasks()

                start_time = match.group(2)
                end_time = match.group(3)
                dialog = match.group(4).strip()

                # Split dialog into words
                words = dialog.split()

                # Generate word-level timestamps
                word_timestamps = self.generate_word_timestamps(start_time, end_time, words)

                # Preserve original subtitle structure or not
                if self.preserve_var.get():
                    # Maintain original subtitle context
                    subtitle_entry = f"Original Subtitle: {dialog}\n\n"
                    word_level_srt.append(subtitle_entry)

                # Prepare word-level SRT content
                for word_start, word_end, word in word_timestamps:
                    word_level_srt.append(f"{global_counter}\n{word_start} --> {word_end}\n{word}\n\n")
                    global_counter += 1

            # Write to output file
            with open(output_file, 'w', encoding='utf-8') as f:
                f.writelines(word_level_srt)

            # Final update
            self.progress['value'] = 100
            self.status_label.config(text="Processing Complete!")
            messagebox.showinfo("Success", f"Word-level SRT created at:\n{output_file}")

        except Exception as e:
            messagebox.showerror("Error", str(e))
            self.status_label.config(text="Processing Failed")


def main():
    root = tk.Tk()
    app = SRTSlicerApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()