import tkinter as tk
from tkinter import ttk
import os
import sys
from srt_slicer_logic import SRTSlicerLogic


class SRTSlicerUI:
    def __init__(self, master):
        self.master = master
        self.logic = SRTSlicerLogic()
        master.title("SRT Word-Level Timestamp Slicer")
        master.geometry("1280x720")
        master.configure(bg='#f0f0f0')

        # Set application icon
        self.set_app_icon()

        # Style
        self.style = ttk.Style()
        self.style.configure('TLabel', background='#f0f0f0', font=('Arial', 10))
        self.style.configure('TButton', font=('Arial', 10))

        # Main Container
        self.main_container = ttk.Frame(master, padding="10")
        self.main_container.pack(fill='both', expand=True, padx=10, pady=10)

        # Create all UI sections
        self.create_input_file_section()
        self.create_output_file_section()
        self.create_filename_section()
        self.create_distribution_section()
        self.create_processing_options()
        self.create_process_button()

        # Progress Bar
        self.progress = ttk.Progressbar(master, orient="horizontal", length=300, mode="determinate")
        self.progress.pack(pady=10)

        # Status Label
        self.status_label = ttk.Label(master, text="Ready to process", font=('Arial', 10, 'italic'))
        self.status_label.pack(pady=10)

    def set_app_icon(self):
        """Try to set the application icon from various possible locations"""
        try:
            icon_paths = [
                'app_icon1.ico',
                os.path.join(os.path.dirname(__file__), 'app_icon1.ico'),
                os.path.join(sys.path[0], 'app_icon1.ico')
            ]
            icon_path = next((path for path in icon_paths if os.path.exists(path)), None)
            if icon_path:
                self.master.iconbitmap(icon_path)
        except Exception as e:
            print(f"Error loading icon: {e}")

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
        pass

    def browse_input_file(self):
        """Open file dialog to select input SRT file."""
        from tkinter import filedialog
        filename = filedialog.askopenfilename(
            title="Select SRT File",
            filetypes=[("SRT Files", "*.srt"), ("Text Files", "*.txt"), ("All Files", "*.*")]
        )
        if filename:
            self.input_path.set(filename)
            self.auto_generate_output_path(filename)

    def auto_generate_output_path(self, input_path):
        """Automatically generate output file path."""
        if not self.auto_generate_var.get():
            return

        dir_path = os.path.dirname(input_path)
        base_name = os.path.splitext(os.path.basename(input_path))[0]

        prefix = self.prefix_var.get()
        suffix = self.suffix_var.get()
        output_filename = f"{prefix}{base_name}{suffix}{self.output_type_var.get()}"

        output_path = os.path.join(dir_path, output_filename)
        self.output_path.set(output_path)

    def browse_output_file(self):
        """Open file dialog to select output SRT file."""
        from tkinter import filedialog
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

    def process_srt(self):
        """Handle the SRT processing by delegating to the logic class."""
        from tkinter import messagebox

        input_file = self.input_path.get()
        output_file = self.output_path.get()

        if not input_file or not output_file:
            messagebox.showerror("Error", "Please select input and output files.")
            return

        try:
            # Configure logic with current settings
            self.logic.configure(
                input_file=input_file,
                output_file=output_file,
                distribution_method=self.distribution_var.get(),
                preserve_structure=self.preserve_var.get(),
                progress_callback=self.update_progress,
                status_callback=self.update_status
            )

            # Start processing
            self.logic.process()

            # Show success message
            messagebox.showinfo("Success", f"Word-level SRT created at:\n{output_file}")
            self.status_label.config(text="Processing Complete!")

        except Exception as e:
            messagebox.showerror("Error", str(e))
            self.status_label.config(text="Processing Failed")

    def update_progress(self, value):
        """Update the progress bar."""
        self.progress['value'] = value
        self.master.update_idletasks()

    def update_status(self, text):
        """Update the status label."""
        self.status_label.config(text=text)
        self.master.update_idletasks()


