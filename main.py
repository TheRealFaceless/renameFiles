import os
import random

# List of directories to process
paths = [
    "C:/Users/Faceless/Pictures/Wallpapers1",
    "C:/Users/Faceless/Pictures/Wallpapers2",
    "C:/Users/Faceless/Pictures/Wallpapers3",
    "C:/Users/Faceless/Pictures/Wallpapers5",
]

used_numbers = []
count = 0;

for path in paths:
    for entry in os.listdir(path):
        entry_path = os.path.join(path, entry)

        if os.path.isfile(entry_path):
            while True:
                randint = random.randint(1, 10000)
                if randint not in used_numbers:
                    used_numbers.append(randint)
                    break

            # Generate new file path
            name, ext = os.path.splitext(entry)
            new_path = os.path.join(path, f"{name}_{randint}{ext}")

            try:
                os.rename(entry_path, new_path)
                print(f"Renamed {entry_path} to {new_path}")
                count = count + 1
            except FileNotFoundError:
                print(f"The file {entry_path} does not exist.")
            except Exception as e:
                print(f"An error occurred: {e}")


print(count)