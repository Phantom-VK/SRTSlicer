import tkinter as tk

from srt_slicer_ui import SRTSlicerUI


def main():
    root = tk.Tk()
    app = SRTSlicerUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()