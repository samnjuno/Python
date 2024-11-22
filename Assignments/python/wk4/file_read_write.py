def main():
    #Ask the user for filename
    input_filename = input("Enter the filename to read:")
    output_filename = "modified_" + input_filename #New file for modified content
    
    try:
        #Try to open the input file for reading
        with open(input_filename, "r")as infile:
            #Read the content of the file
            content = infile.read()
            print("File read successfully")
            
            #modify the content (convert to uppercase)
            with open(output_filename, "w") as outfile:
                outfile.write("modified_content")
                print(f"modified content written to '{output_filename}'.")
                
    except FileNotFoundError:
            print(f"error:The file '{input_filename}'does not exist .")
    except IOError:
             print(f"error: The file '{input_filename}'cannot be read.")       
    except Exception as e:
        print(f"An unexpected error occured: {e}")
if __name__ == "__main__":
    main()
            
        