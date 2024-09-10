# import necessary libraries and function
from datetime import datetime

# python as usual
def current_time():
    return datetime.now()

# will run as script or on import
run_or_imported_at = current_time()
print(f"this was run or imported at {run_or_imported_at}")
print(f"{__name__ = :s}")

if __name__ == "__main__":
    # will only run if this is a script
    # won't be run if imported
    print("running as a script")
