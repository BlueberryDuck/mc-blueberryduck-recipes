import os
import zipfile

ZIP_FILENAME = "BlueberryDuckRecipes.zip"
DATA_FOLDER = "data"
MCMETA_FILE = "pack.mcmeta"


def zip_datapack():
    with zipfile.ZipFile(ZIP_FILENAME, "w", zipfile.ZIP_DEFLATED) as zipf:
        # Add the 'data' folder and its contents
        if os.path.isdir(DATA_FOLDER):
            for root, dirs, files in os.walk(DATA_FOLDER):
                for file in files:
                    file_path = os.path.join(root, file)
                    arcname = os.path.relpath(file_path, os.getcwd())
                    zipf.write(file_path, arcname)
        else:
            print(f"Warning: {DATA_FOLDER} folder not found.")

        # Add the pack.mcmeta file
        if os.path.isfile(MCMETA_FILE):
            zipf.write(MCMETA_FILE, MCMETA_FILE)
        else:
            print(f"Warning: {MCMETA_FILE} not found.")


if __name__ == "__main__":
    zip_datapack()
    print(f"Created {ZIP_FILENAME}")
