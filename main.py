import PyPDF2
from tkinter import Tk,filedialog
def get_files():
    no=int(input('Enter the number of files you are going to merge: '))
    i=0
    paths=[]
    while(i<no):
        root=Tk()
        root.withdraw()
        path=filedialog.askopenfilename(
            title='Select a pdf file',
            filetypes=[("Documents", "*.pdf")]
        )
        if path:  
            paths.append(path)
            i += 1
        else:
            print("No file selected. Please try again.")
        
    return paths    
def save_merged():
    
    root = Tk()
    root.withdraw()  
    
    save_path = filedialog.asksaveasfilename(
        title="Save Merged Pdf",
        defaultextension=".pdf", 
        filetypes=[("PDF", "*.pdf")] 
        
    )
    
    return save_path
    
def merge():
    listofpdfs=get_files()
    if listofpdfs:
        merger = PyPDF2.PdfWriter()

        for pdf in listofpdfs:
            merger.append(pdf)
        save_path=save_merged()
        if save_path:

            merger.write(save_path)
            
        else:
            print('No save path has been selected.')
    else:
        print('No file selected.')
merge()
