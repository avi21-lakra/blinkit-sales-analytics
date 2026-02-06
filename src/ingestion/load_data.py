import kagglehub
import os
import shutil

RAW_DATA_DIR = "data/raw"

def load_blinkit_data():
    print("📥 Downloading Blinkit dataset...")
    dataset_path = kagglehub.dataset_download("akxiit/blinkit-sales-dataset")

    os.makedirs(RAW_DATA_DIR, exist_ok=True)

    for file in os.listdir(dataset_path):
        if file.endswith(".csv"):
            src = os.path.join(dataset_path, file)
            dst = os.path.join(RAW_DATA_DIR, file)
            shutil.copy(src, dst)
            print(f"✅ Copied: {file}")

    print("🎉 Data successfully loaded into data/raw")

if __name__ == "__main__":
    load_blinkit_data()
