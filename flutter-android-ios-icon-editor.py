from PIL import Image
import os

def create_icons(image_path):
    # Define sizes and their corresponding folder names
    sizes = {
        'mipmap-hdpi': (72, 72),
        'mipmap-mdpi': (48, 48),
        'mipmap-xhdpi': (96, 96),
        'mipmap-xxhdpi': (144, 144),
        'mipmap-xxxhdpi': (192, 192),
        'ios/Icon-App-20x20@1x': (20, 20),
        'ios/Icon-App-20x20@2x': (40, 40),
        'ios/Icon-App-20x20@3x': (60, 60),
        'ios/Icon-App-1024x1024@1x': (1024, 1024)
    }

    # Open the original image
    with Image.open(image_path) as img:
        # Loop through the sizes dictionary
        for folder, size in sizes.items():
            # Create the directory if it doesn't exist
            os.makedirs(folder, exist_ok=True)
            # Resize the image
            resized_img = img.resize(size, Image.ADAPTIVE)
            # Save the resized image in the appropriate folder with the correct name
            file_name = os.path.join(folder, 'ic_launcher.png') if 'mipmap' in folder else os.path.join(folder, 'icon.png')
            resized_img.save(file_name)
            print(f"Saved {file_name}")

# Example usage
image_path = 'path/to/your/image.png'  # Replace with your image path
create_icons(image_path)