PDF Encryption Project (Using Python & pikepdf)

This is small Python project where I encrypt PDF files using the pikepdf library. The script allows me to add a user password, an owner password, and also block things like printing, extracting text, editing, etc. I made this project to understand how file security works in Python.

What This Project Does

- Encrypts any PDF file you select
- Adds password protection
- Blocks printing & copying
- Works even if the PDF already has a password
- Verifies if encryption was successful

Requirements

Install pikepdf before running the script:
pip install pikepdf

How to Use

1. Set your PDF path and passwords inside the script:
pdf_path = r"C:\Hitesh\Important docs\2025-26\Syllabus\English.pdf"
new_user_pw = "hitesh"
new_owner_pw = "1234"
old_pw = "hitesh"   # only if PDF already has a password
2. Run the file:
python encrypt_pdf.py
3. Output you will get:
Done: PDF encrypted -> C:\Hitesh\Important docs\2025-26\Syllabus\English.pdf
Verification OK: password required to open the file.

How the Script Works (Simple Explanation)

- A function perms() is used to set restrictions
- pikepdf.Encryption() is used to add passwords
- The script tries to open the PDF normally
- If it fails, it tries opening using the old password
- Finally, it saves the encrypted version with new passwords
- At the end, it checks if the PDF is secured properly

Why I Made This Project

I wanted to practice:
- Python file handling
- Using external libraries
- Understanding how encryption works
- Creating small real-world useful tools
This project can be used to protect notes, assignments, college PDFs, etc.

Conclusion

This PDF Encryption project helped me understand how to use Python for security-based tasks. It is simple but useful, and can be extended to build a complete File Protection tool.
