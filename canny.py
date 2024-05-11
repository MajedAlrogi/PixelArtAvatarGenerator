import cv2
import os

def process_images(input_dir, output_dir):
    # Create the output directory if it does not exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # List all files in the input directory
    for filename in os.listdir(input_dir):
        # Construct the full file path
        input_path = os.path.join(input_dir, filename)
        
        # Check if the file is an image (simple check based on file extension)
        if input_path.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.tif', '.tiff')):
            # Load the image
            image = cv2.imread(input_path)
            
            if image is not None:
                # Convert the image to grayscale
                gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
                
                # Apply Canny Edge Detector
                edges = cv2.Canny(gray_image, threshold1=100, threshold2=200)
                
                # Construct the output path
                output_path = os.path.join(output_dir, filename)
                
                # Save the edges to a new file
                cv2.imwrite(output_path, edges)
                print(f"Processed '{filename}' and saved to '{output_path}'")
            else:
                print(f"Warning: Could not open or find the image '{input_path}'.")

# Example usage
input_directory = 'Sprite_1024'  # Replace with your input directory path
output_directory = 'Canny_1024' # Replace with your output directory path
process_images(input_directory, output_directory)

