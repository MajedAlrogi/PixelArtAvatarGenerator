from PIL import Image
import argparse
import os

def enlarge_and_crop_directory(input_dir, output_dir, target_size=(1024, 1024)):
    """
    Enlarge and crop all images in a directory and save them to another directory.

    Args:
    - input_dir (str): Path to the input directory containing images.
    - output_dir (str): Path where the output images will be saved.
    - target_size (tuple): Desired output size as (width, height).
    """
    # Ensure output directory exists
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    # List all files in the input directory
    for file_name in os.listdir(input_dir):
        input_path = os.path.join(input_dir, file_name)
        
        # Skip directories and non-image files
        if os.path.isdir(input_path) or not file_name.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
            continue
        
        # Open the original image
        img = Image.open(input_path)
        
        # Calculate the scale factor, ensuring the smallest side is scaled to the target size
        scale_factor = max(target_size[0] / img.size[0], target_size[1] / img.size[1])
        
        # Calculate new size to maintain aspect ratio
        new_size = (int(img.size[0] * scale_factor), int(img.size[1] * scale_factor))
        
        # Resize the image
        img_resized = img.resize(new_size, Image.ANTIALIAS)
        
        # Calculate coordinates for cropping to the target size
        left = (img_resized.width - target_size[0]) / 2
        top = (img_resized.height - target_size[1]) / 2
        right = (img_resized.width + target_size[0]) / 2
        bottom = (img_resized.height + target_size[1]) / 2
        
        # Crop the image
        img_cropped = img_resized.crop((left, top, right, bottom))
        
        # Construct the output path
        output_path = os.path.join(output_dir, file_name)
        
        # Save the cropped image
        img_cropped.save(output_path)

def main():
    parser = argparse.ArgumentParser(description='Enlarge and crop images in a directory.')
    parser.add_argument('input_dir', type=str, help='Path to the input directory containing images.')
    parser.add_argument('output_dir', type=str, help='Path where the output images will be saved.')
    #parser.add_argument('--width', type=int, default=1024, help='Width of the output images.')
    #parser.add_argument('--height', type=int, default=1024, help='Height of the output images.')

    args = parser.parse_args()

    #target_size = (args.width, args.height)
    enlarge_and_crop_directory(args.input_dir, args.output_dir)

if __name__ == '__main__':
    main()
