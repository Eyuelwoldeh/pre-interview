import os
import subprocess
import time
import csv
from dotenv import load_dotenv

# load environment variables from .env file
load_dotenv()

# for these paths, make sure to create the appropriate .env file and store the ENTIRE path in each variable name (or use os.path.expanduser())
queries_directory = os.getenv("QUERIES_DIRECTORY")
cvc5_executable = os.getenv("CVC5_EXECUTABLE")
output_csv = os.getenv("OUTPUT_CSV")

def parse_result(output, error):
    if "unsat" in output.lower():
        return "UNSAT"
    elif "sat" in output.lower():
        return "SAT"
    elif "timeout" in error.lower():
        return "TIMEOUT"
    else:
        return "UNKNOWN"

def run_queries():
    results = []

    for root, _, files in os.walk(queries_directory):
        for file in files:
            if file.endswith(".smt2"):
                file_path = os.path.join(root, file)
                print(f"Running: {file}")

                start_time = time.time()
                try:
                    result = subprocess.run(
                        [cvc5_executable, "--tlimit=60000", file_path], 
                        capture_output=True, text=True, check=False
                    )
                    time_taken = round(time.time() - start_time, 4)
                    status = parse_result(result.stdout, result.stderr)

                    # storing our results
                    results.append([file, status, time_taken])
                    print(f"{file} → {status} ({time_taken}s)")
                
                except Exception as e:
                    print(f"Error running {file}: {e}")

    # dumping results from list all at once
    with open(output_csv, mode="w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["QueryName", "Result", "ElapsedTime"])
        writer.writerows(results)

    print(f"\n Results saved to {output_csv}") # debug statement

if __name__ == "__main__":
    run_queries()
