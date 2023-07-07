# PDF-Similarity-Comparison
 The "PDF Similarity Comparison" code is a Python application with a GUI that compares the textual similarity between two PDF files using TF-IDF and cosine similarity.

The provided code is a PDF similarity comparison tool implemented using Python and the Tkinter library for creating the graphical user interface (GUI). It allows users to select two PDF files, preprocess the text content of the files, and calculate the similarity score between them using the cosine similarity algorithm based on TF-IDF (Term Frequency-Inverse Document Frequency).

Here's a breakdown of the algorithms used in the code:

PDF Parsing: The code uses the "pdfplumber" library to open and extract the text content from PDF files. It iterates through each page of the selected PDFs and concatenates the extracted text.

Text Preprocessing: The extracted text from each PDF is preprocessed to remove special characters and reduce multiple spaces. This step aims to normalize the text and improve the accuracy of the similarity comparison.

TF-IDF Vectorization: The code utilizes the "TfidfVectorizer" class from the "sklearn.feature_extraction.text" module to convert the preprocessed text into a numerical representation using TF-IDF. TF-IDF assigns weights to words based on their frequency in the document and inverse frequency in the corpus. This representation captures the importance of words in distinguishing between documents.

Cosine Similarity: The "cosine_similarity" function from the "sklearn.metrics.pairwise" module calculates the cosine similarity between the TF-IDF vectors of the two PDFs. Cosine similarity measures the cosine of the angle between two vectors and provides a similarity score ranging from 0 to 1. A higher score indicates a higher similarity between the PDFs.

User Interface: The Tkinter library is used to create a GUI window with various elements such as labels, buttons, and frames. The GUI provides a user-friendly interface for selecting PDF files, triggering the comparison process, displaying the similarity score, and opening the results file.

Overall, this code combines PDF parsing, text preprocessing, TF-IDF vectorization, and cosine similarity calculation to enable users to compare the similarity between two PDF files and obtain a numerical similarity score. The GUI enhances the usability of the tool by providing a visual interface for interaction.
