import csv
import os 
import tabula 
from datetime import datetime
from argparse import ArgumentParser 


class ReadPdf:
    def __init__(self) -> None:
        self.pdf_path = self.myparser()[0]
        self.password = self.myparser()[1]
        self.naming = datetime.now().strftime("%Y-%m-%d_%H:%M:%S")        
        
        self.base = os.path.dirname(os.path.abspath(__file__))
        self.pdf_source = os.path.join(self.base, self.pdf_path)
        self.output_dir = os.path.join(self.base, 'output')
        self.extracted_csv = os.path.join(self.base,'file.csv')
        self.output_file = os.path.join(self.output_dir,f"{self.naming}.csv")

        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir)

    def myparser(self):
        """
        _summary_: Function used to parse the pdf file you want to extract
        Returns:
            _type_: file-path and password as strings
        """
        parser = ArgumentParser(description="Inputs file, passwd to be analyzed")
        parser.add_argument("file", metavar="file", type=str, help="file.pdf")
        parser.add_argument("passwd", type=str, help="000111")

        args = parser.parse_args()
        return args.file, args.passwd
    
    def create_csv(self):
        """
            _summary_: Converts the pdf into a csv for easier formatting
        """
        tabula.convert_into(self.pdf_source, self.extracted_csv, output_format="csv", pages='all', password=self.password)
    
    def read_csv(self):
        """
            _summary_: Formats the extracted pdf tables into a cleaner version and stores in output directory
        """
        self.create_csv()

        line = ['Receipt No.', 'Completion Time', 'Details', 'Transaction Status', 'Paid In', 'Withdrawn', 'Balance', '']
        store_rows = []
        with open(self.extracted_csv, 'r') as f:
            reader = csv.reader(f, delimiter=',')
            for row in reader:
                if len(row) > 3 and row != line:
                    store_rows.append(row)
        
        table1 = store_rows[:10] # Transaction Summary
        table2 = store_rows[10:][::-1] # Mpesa Transactions in ascending order of date
        with open(self.output_file, 'w') as f:
            writer = csv.writer(f, delimiter=',')
            writer.writerow(line)
            writer.writerows(table2)
        
def main():
    read = ReadPdf()
    read.read_csv()

if __name__ == "__main__":
    main()