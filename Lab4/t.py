import os

file_path = "sample-data.json"  # немесе толық жолды осында көрсет
if os.path.exists(file_path):
    print("Файл табылды!")
else:
    print("Файл табылмады, жолды тексер!")
