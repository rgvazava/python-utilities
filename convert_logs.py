import csv

# This script converts a plain text log file into a CSV file.
# I made this to practice reading and writing files in Python while learning automation.

def convert_to_csv(input_file, output_file):
    try:
        with open(input_file, "r") as infile, open(output_file, "w", newline="") as outfile:
            writer = csv.writer(outfile)
            writer.writerow(["Line Number", "Log Entry"])
            
            for line_number, line in enumerate(infile, start=1):
                cleaned = line.strip()
                writer.writerow([line_number, cleaned])
            
        print(f"Conversion complete. Saved as {output_file}")
    except FileNotFoundError:
        print("File not found. Please check the file name and try again.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    input_name = input("Enter the log file name (for example: log.txt): ").strip()
    output_name = input("Enter the CSV output file name (for example: result.csv): ").strip()
    convert_to_csv(input_name, output_name)
