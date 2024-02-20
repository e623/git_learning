def extract_lines_with_string(file_path, target_string):  
    with open(file_path, 'r') as file:  
        lines = file.readlines()  
  
    extracted_lines = [line for line in lines if target_string in line]  
    return extracted_lines  
  
# Example usage  
file_path = 'example.txt'  
target_string = 'particular'  
  
extracted_lines = extract_lines_with_string(file_path, target_string)  
for line in extracted_lines:  
    print(line.strip())
