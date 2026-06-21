import importlib

try:
    openpyxl = importlib.import_module("openpyxl")
except ImportError:
    import subprocess
    import sys
    try:
        print("openpyxl not found; attempting to install it...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "openpyxl"])
        importlib.invalidate_caches()
        openpyxl = importlib.import_module("openpyxl")
        print("openpyxl installed successfully.")
    except Exception as install_err:
        print("Failed to install openpyxl. Please install it manually (pip install openpyxl).")
        raise install_err

def auto_fit_columns(input_file, output_file):
    try:
        workbook = openpyxl.load_workbook(input_file)
        
        for sheet_name in workbook.sheetnames:
            sheet = workbook[sheet_name]
            
            for col in sheet.columns:
                max_length = 0
                column = col[0].column_letter
                
                for cell in col:
                    try:
                        if len(str(cell.value)) > max_length:
                            max_length = len(str(cell.value))
                    except:
                        pass
                
                adjusted_width = (max_length + 2)
                sheet.column_dimensions[column].width = adjusted_width
                
        workbook.save(output_file)
        print(f"Columns auto-sized successfully and saved to {output_file}")

    except FileNotFoundError:
        print(f"Error: The file '{input_file}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")


input_excel_file = "output_adjusted.xlsx"
output_excel_file = "output_formatted.xlsx"

auto_fit_columns(input_excel_file, output_excel_file)