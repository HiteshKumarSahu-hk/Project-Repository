import pikepdf

# user settings
pdf_path = r"C:\\Hitesh\\Important docs\\2025-26\\Syllabus\\English.pdf"
new_user_pw = "hitesh"
new_owner_pw = "1234"
# If the PDF already has a password, put it here; otherwise leave as None
#old_pw = None
old_pw = "hitesh"


def perms():
    # try the modern signature, fall back if pikepdf version differs
    try:
        return pikepdf.Permissions(
            extract=False,
            print_lowres=False,
            print_highres=False,
            modify_annotations=False,
            modify_contents=False,
            annotate=False
        )
    except TypeError:
        try:
            return pikepdf.Permissions(
                extract=False,
                print_lowres=False,
                print_highres=False,
                modify=False,
                annotate=False
            )
        except TypeError:
            return pikepdf.Permissions(extract=False)

enc = pikepdf.Encryption(user=new_user_pw, owner=new_owner_pw, allow=perms(), R=6)

# open (try no-password first, then try old_pw if provided)
try:
    try:
        pdf = pikepdf.open(pdf_path, allow_overwriting_input=True)
    except pikepdf.PasswordError:
        if old_pw:
            pdf = pikepdf.open(pdf_path, password=old_pw, allow_overwriting_input=True)
        else:
            print("Error: file is password-protected. Set old_pw and try again.")
            raise SystemExit(1)

    pdf.save(pdf_path, encryption=enc)
    pdf.close()
    print("Done: PDF encrypted ->", pdf_path)

except Exception as e:
    print("Encryption failed:", type(e)._name_, e)
    raise SystemExit(1)

# quick verification
print("Verifying...")
try:
    pikepdf.open(pdf_path)
    print("Verification failed: opened without password.")
except pikepdf.PasswordError:
    print("Verification OK: password required to open the file.")
except Exception as e:
    print("Verification error:", type(e)._name_, e)