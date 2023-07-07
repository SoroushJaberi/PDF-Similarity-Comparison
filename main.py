import tkinter as tk
from tkinter import filedialog
import pdfplumber
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import re
from PIL import Image, ImageTk



def pick_file():
    # Create a file dialog to select a PDF file
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename(filetypes=[("PDF Files", "*.pdf")])
    return file_path


def preprocess_text(text):
    # Remove special characters and reduce multiple spaces
    text = re.sub(r"[^\w\s]", "", text)
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def compare_pdfs():
    # Get the file paths of the PDF files to compare
    file1 = pick_file()
    file2 = pick_file()

    # Open the PDF files
    with pdfplumber.open(file1) as pdf1, pdfplumber.open(file2) as pdf2:

        # Get the text content of each PDF
        text1 = "\n".join([page.extract_text() for page in pdf1.pages])
        text2 = "\n".join([page.extract_text() for page in pdf2.pages])

        # Preprocess the text
        text1 = preprocess_text(text1)
        text2 = preprocess_text(text2)

        # Calculate the similarity score using cosine similarity based on TF-IDF
        vectorizer = TfidfVectorizer()
        tfidf_matrix = vectorizer.fit_transform([text1, text2])
        similarity_matrix = cosine_similarity(tfidf_matrix)
        similarity = similarity_matrix[0, 1]

        # Get the file names of the PDFs
        file1_name = file1.split("/")[-1]
        file2_name = file2.split("/")[-1]

        # Save the results to a text file
        with open("comparison_results.txt", "w") as f:
            f.write(f"Comparison Results\n\n")
            f.write(f"File 1: {file1_name}\n")
            f.write(f"File 2: {file2_name}\n")
            f.write(f"Similarity score: {similarity:.2f}\n")

        return f"The similarity score between {file1_name} and {file2_name} is {similarity:.2f}"


def show_similarity():
    # Create a GUI window
    root = tk.Tk()
    root.title("PDF Similarity Comparison")

    # Set the background and foreground colors
    root.configure(bg="white")

    # Set the window icon
    pdf_icon = Image.open("pdf_icon.png")
    pdf_icon = ImageTk.PhotoImage(pdf_icon)

    # Set the icon for the window
    root.iconphoto(True, pdf_icon)

    # Create a label widget to display the title
    title_label = tk.Label(root, text="PDF Similarity Comparison", font=("Helvetica", 16, "bold"), bg="white", fg="blue")
    title_label.pack(pady=10)

    # Create a label widget to display the similarity score
    similarity_label = tk.Label(root, text="", font=("Helvetica", 14), bg="white")
    similarity_label.pack(pady=10)

    def compare_pdf_files():
        similarity_score = compare_pdfs()
        similarity_label.config(text=similarity_score)

    def open_results_file():
        import os
        os.system("notepad.exe comparison_results.txt")

    # Create a frame to hold the buttons
    button_frame = tk.Frame(root,bg="white")
    button_frame.pack(pady=10)

    # Create a button widget to trigger the PDF comparison
    compare_button = tk.Button(button_frame, text="Compare PDFs", font=("Helvetica", 12), command=compare_pdf_files,
                               bg="red", fg="white")
    compare_button.pack(side=tk.LEFT, padx=10)

    # Create a button widget to open the results file
    save_button = tk.Button(button_frame, text="Open Results", font=("Helvetica", 12), command=open_results_file,
                            bg="red", fg="white")
    save_button.pack(side=tk.LEFT, padx=10)

    # Create a frame to hold the status message
    status_frame = tk.Frame(root, bg="white")
    status_frame.pack(pady=10)

    # Create a label widget to display the status message
    status_label = tk.Label(status_frame, text="Select two PDF files to compare", font=("Helvetica", 12),
                            bg="white")
    status_label.pack()

    def update_status(message):
        status_label.config(text=message)

    def clear_status():
        status_label.config(text="")

    def reset():
        clear_status()
        similarity_label.config(text="")

    # Create a frame to hold the reset button
    reset_frame = tk.Frame(root, bg="white")
    reset_frame.pack(pady=10)

    # Create a button widget to reset the GUI
    reset_button = tk.Button(reset_frame, text="Reset", font=("Helvetica", 12), command=reset, bg="red", fg="white")
    reset_button.pack()

    def show_file_dialog():
        # Reset the status message
        clear_status()

        # Create a file dialog to select a PDF file
        file_path = pick_file()
        if file_path:
            status_message = f"Selected file: {file_path}"
        else:
            status_message = "No file selected"
        update_status(status_message)

    # Create a frame to hold the file selection buttons
    file_frame = tk.Frame(root, bg="white")
    file_frame.pack(pady=10)

    # Create a button widget to open the file dialog for selecting the first PDF file
    file1_button = tk.Button(file_frame, text="Select PDF File 1", font=("Helvetica", 12), command=show_file_dialog,
                             bg="gray", fg="white")
    file1_button.pack(side=tk.LEFT, padx=10)

    # Create a button widget to open the file dialog for selecting the second PDF file
    file2_button = tk.Button(file_frame, text="Select PDF File 2", font=("Helvetica", 12), command=show_file_dialog,
                             bg="gray", fg="white")
    file2_button.pack(side=tk.LEFT, padx=10)

    # Start the GUI main loop
    root.mainloop()


# Run the GUI
show_similarity()
