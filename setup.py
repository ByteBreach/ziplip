import ziplip

# Example 1: Using ziplip from a Python script
password = ziplip.main(zip_file="file.zip", password_file="password.txt")
if password:
    print("Password found:", password)
else:
    print("Password not found.")

# Example 2: Using ziplip with silent mode from a Python script
password = ziplip.main(zip_file="file.zip", password_file="password.txt", silent=True)
if password:
    print("Password found:", password)
else:
    print("Password not found.")

# Example 3: Using ziplip with only-print mode from a Python script
password = ziplip.main(zip_file="file.zip", password_file="password.txt", only_pass=True)
if password:
    print("Password found:", password)
else:
    print("Password not found.")
