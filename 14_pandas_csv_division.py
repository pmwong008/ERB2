from datetime import datetime
import pandas as pd

class DivisionError(RuntimeError):
    def __init__(self, message):
        self.message = message

def divide_numbers(numerator, denominator):
    if denominator == 0:
        raise DivisionError("Division by zero")
    return numerator / denominator

def generate_file_name():
    now = datetime.now()
    timestamp = now.strftime("%Y%m%d_%H%M%S")
    return f"result_{timestamp}.csv"

def main(file_name):
    try:
        df = pd.read_csv(file_name)

        results = []

        for index, row in df.iterrows():
            try:
                num = int(row['numerator'])
                denom = int(row['denominator'])

                result = divide_numbers(num, denom)
                results.append(result)
            except DivisionError as e:
                print(f"DivisionError: {e} at index {index}")
                results.append(None)
            except ValueError as e:
                print(f"ValueError: {e} at index {index}")
                results.append(None)
        df["result"] = results

        output_file = generate_file_name()
        df.to_csv(output_file, index=False)
        print(f"Saved to {output_file}")

    except FileNotFoundError as e:
        print(f"FileNotFoundError: {e}")

if __name__ == "__main__":
    main("14_pandas_csv_division.csv")