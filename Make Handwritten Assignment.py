import pywhatkit as pw
text=""" 
Hello!
My name is Zoya Rana.
This text is converted into Handwritten.
"""
pw.text_to_handwriting(text,save_to="handwritten.png")
print("Handwritten image saved successfully")