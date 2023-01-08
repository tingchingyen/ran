import openpyxl
import streamlit as st

# Open an existing PowerPoint presentation
wb = openpyxl.load_workbook("template.pptx", read_only=False, keep_vba=True)

# Get the first slide
slide = wb.worksheets[0]

# Find the first text box on the slide
textbox = slide.cell(row=1, column=1).value

# Set the text of the text box
textbox.text = "test"

# Set the font size of the text box
textbox.font.size = 12

# Save the modified PowerPoint presentation
wb.save("tmp.pptx")


with open("tmp.pptx", "rb") as file:
    btn = st.download_button(
            label="Download PPT",
            data=file,
            file_name="test.pptx",
            mime="application/vnd.openxmlformats-officedocument.presentationml.presentation"
          )