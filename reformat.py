import csv

def csv_format_igbo():
    # Step 1: Reformat the file
    input_file = "gpt3.5_bbc_igbo.txt"
    output_file = "gpt3.5_bbc_igbo.csv"

    # Initialize variables to hold Pidgin and English sentences
    igbo_sentence = ""
    eng_sentence = ""

    with open(input_file, 'r', encoding="utf-8") as f:
        lines = f.readlines()

    # Write to the output CSV file
    with open(output_file, 'w', encoding="utf-8", newline="") as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(["Input_igbo", "Output_eng"])  # Write the header

        # Process each line
        for line in lines:
            line = line.strip()  
            if line.startswith("Igbo:"):
                igbo_sentence = line[5:].strip()  

            elif line.startswith("Eng:"):
                eng_sentence = line[5:].strip() 
                csv_writer.writerow([igbo_sentence, eng_sentence])


    # Step 2: Read the CSV and output the number of rows
    with open(output_file, 'r', encoding="utf-8") as csvfile:
        csv_reader = csv.reader(csvfile)
        row_count = sum(1 for row in csv_reader) - 1  # Subtract 1 for the header row

    print(f"The CSV file contains {row_count} rows.")

    
    return
def csv_format_pidgin():
    # Step 1: Reformat the file
    input_file = "gpt3.5_pidgin.txt"
    output_file = "gpt3.5_bbc_pidgin.csv"

    # Initialize variables to hold Pidgin and English sentences
    pid_sentence = ""
    eng_sentence = ""

    with open(input_file, 'r', encoding="utf-8") as f:
        lines = f.readlines()

    # Write to the output CSV file
    with open(output_file, 'w', encoding="utf-8", newline="") as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(["Input_pid", "Output_eng"])  # Write the header

        # Process each line
        for line in lines:
            line = line.strip()  # Remove extra whitespace
            if line.startswith("Pid:"):
                pid_sentence = line[5:].strip()  # Extract Pidgin sentence
                # if pid_sentence.startswith("1. ") or pid_sentence.startswith("2. ") :
                #     pid_sentence = pid_sentence[3:]
                # if pid_sentence[0] == '"' and pid_sentence[-1] == '"':
                #     pid_sentence = pid_sentence[1:-1]

            elif line.startswith("Eng:"):
                eng_sentence = line[5:].strip()  # Extract English sentence
                # if eng_sentence[0] == '"' and eng_sentence[-1] == '"':
                #     eng_sentence = eng_sentence[1:-1]

                # Write the pair into the CSV
                csv_writer.writerow([pid_sentence, eng_sentence])


    # Step 2: Read the CSV and output the number of rows
    with open(output_file, 'r', encoding="utf-8") as csvfile:
        csv_reader = csv.reader(csvfile)
        row_count = sum(1 for row in csv_reader) - 1  # Subtract 1 for the header row

    print(f"The CSV file contains {row_count} rows.")

    
    return

if __name__ == "__main__":
    csv_format_igbo()