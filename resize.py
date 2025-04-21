from PIL import Image
import os

target_size = (1080, 1080)

def resize_images_in_folder(folder_path):
    output_folder = os.path.join(folder_path)
    os.makedirs(output_folder, exist_ok=True)

    for filename in os.listdir(folder_path):
        if filename.lower().endswith((".png", ".jpg", ".jpeg")):
            img_path = os.path.join(folder_path, filename)
            try:
                with Image.open(img_path) as img:
                    img_resized = img.resize(target_size, Image.Resampling.LANCZOS)
                    save_path = os.path.join(output_folder, filename)
                    img_resized.save(save_path)
                    print(f"Resized and saved: {save_path}")
            except Exception as e:
                print(f"Failed to process {filename}: {e}")


your_directory = "C:\\Users\\Admin\\Desktop\\Page 1"
resize_images_in_folder(your_directory)