# Create a new text file named "my_file.txt" in write mode ('w')
with open("my_file.txt", "w") as file:
    # Write three lines of text to the file
    file.write("Hello, world!\n")
    file.write("12345\n")
    file.write("This is line three.\n")

print("File 'my_file.txt' created successfully.")


# Open the file in read mode
with open("my_file.txt", "r") as file:
    content = file.read()

# Print the content
print(content)


# Open the file in append mode ('a')
with open("my_file.txt", "a") as file:
    # Add new lines
    file.write("\nThis is a new line.")
    file.write("\nAnother line added.")

# Verify the changes
with open("my_file.txt", "r") as file:
    content = file.read()
    print(content)



    # Open the file in append mode ('a')
    with open("my_file.txt", "a") as file:
        # Add new lines
        file.write("\nThis is a new line.")
        file.write("\nAnother line added.")
except FileNotFoundError:
    print("File not found. Make sure 'my_file.txt' exists.")
except PermissionError:
    print("Permission denied. Check file permissions.")
finally:
    # Close the file (whether an exception occurred or not)
    file.close()
