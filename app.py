from fpdf import FPDF
import os

def generate_pdf(policyno):
    # save FPDF() class into a 
    # variable pdf
    pdf = FPDF()
    
    # Add a page
    pdf.add_page()
    
    # set style and size of font 
    # that you want in the pdf
    pdf.set_font("Arial", size = 15)
    
    # create a cell
    pdf.cell(200, 10, txt = policyno, 
            ln = 1, align = 'C')

    # save the pdf with name .pdf
    pdf.output(f"{policyno}.pdf")

    #print("Dir Name: ", os.path.abspath("api.py"))
    return os.path.abspath(f"{policyno}.pdf")