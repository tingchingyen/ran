from pptx_interface import Presentation

# Open an existing PowerPoint presentation
prs = Presentation("template.pptx")

# Find the first text box on the first slide
textbox = prs.slides[0].textboxes[0]

# Set the text of the text box
textbox.text = "test"

# Set the font size of the text box
textbox.font.size = 12
textbox.text = "test2"

# Set the font size of the text box
textbox.font.size = 8
# Save the modified PowerPoint presentation
prs.save("tmp.pptx")
with open("tmp.pptx", "rb") as file:
    btn = st.download_button(
            label="Download PPT",
            data=file,
            file_name="test.pptx",
            mime="application/vnd.openxmlformats-officedocument.presentationml.presentation"
          )