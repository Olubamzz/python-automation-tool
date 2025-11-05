import pandas as pd
import os

class DataCleaner:
    def __init__(self, file_path):
        self.file_path = file_path
        self.data = None

    def load_data(self):
        if not os.path.exists(self.file_path):
            raise FileNotFoundError("The specified file does not exist.")
        self.data = pd.read_csv(self.file_path)
        print(f"✅ Loaded {len(self.data)} rows successfully.")

    def remove_duplicates(self):
        if self.data is None:
            raise ValueError("Data not loaded yet.")
        before = len(self.data)
        self.data.drop_duplicates(inplace=True)
        print(f"🧹 Removed {before - len(self.data)} duplicate rows.")

    def fill_missing(self, column, value):
        if column in self.data.columns:
            missing = self.data[column].isnull().sum()
            self.data[column].fillna(value, inplace=True)
            print(f"🧩 Filled {missing} missing values in '{column}'.")

    def save_cleaned_data(self, output_path):
        self.data.to_csv(output_path, index=False)
        print(f"💾 Cleaned data saved to {output_path}")

if __name__ == "__main__":
    cleaner = DataCleaner("sales_data.csv")
    cleaner.load_data()
    cleaner.remove_duplicates()
    cleaner.fill_missing("price", 0)
    cleaner.save_cleaned_data("cleaned_sales.csv")


Added core data cleaning module
