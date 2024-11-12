import os
import shutil
import csv
from tqdm import tqdm
def save_images_from_csv(csv_file, source_dir, target_dir):
    with open(csv_file, mode='r') as file:
        reader = csv.DictReader(file)
        for row in tqdm(reader):
            image_id = row["ImageId"]
            class_name = row["PredictionString"].split()[0]
            
            # Create the class directory if it doesn't exist
            class_dir = os.path.join(target_dir, class_name)
            os.makedirs(class_dir, exist_ok=True)
            
            # Source and target file paths
            source_path = os.path.join(source_dir, f"{image_id}.JPEG")
            target_path = os.path.join(class_dir, f"{image_id}.JPEG")
            
            # Copy the image to the target directory
            if os.path.exists(source_path):
                shutil.copy2(source_path, target_path)
            else:
                print(f"Source image {source_path} does not exist.")

# Example usage
csv_file_path = "LOC_val_solution.csv"
source_directory = "./ILSVRC/Data/CLS-LOC/val"
target_directory = "./ILSVRC/Data/CLS-LOC/classy-val"
save_images_from_csv(csv_file_path, source_directory, target_directory)