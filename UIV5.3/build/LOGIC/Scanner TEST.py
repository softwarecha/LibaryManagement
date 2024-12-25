import pytesseract
from PIL import Image
import cv2
import re
import os

# Set the path to Tesseract executable (skip this if Tesseract is in PATH)
# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def preprocess_image(image_path):
    """Preprocess the image for better OCR results."""
    # Load the image
    img = cv2.imread('C:\\Users\\softw\\OneDrive\\Pictures\\Camera Roll\\Test.jpg')

    # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Apply thresholding to make the text stand out
    _, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)

    # Optional: Apply some noise reduction (e.g., GaussianBlur)
    processed_img = cv2.GaussianBlur(thresh, (3, 3), 0)

    # Save the processed image temporarily
    temp_path = "Test.jpg"
    cv2.imwrite(temp_path, processed_img)
    return temp_path

def extract_text_from_image(image_path):
    """Extract text from the given image using Tesseract OCR."""
    # Preprocess the image
    processed_path = preprocess_image(image_path)

    # Use Tesseract to extract text from the processed image
    extracted_text = pytesseract.image_to_string(Image.open(processed_path))

    # Remove the temporary processed image
    os.remove(processed_path)

    return extracted_text

def find_name_in_text(text):
    """Search for a name pattern in the extracted text."""
    # Regex pattern to match names (assuming names contain only letters and spaces)
    name_pattern = r'[A-Z][a-z]+\s[A-Z][a-z]+'

    # Search for the first occurrence of a name
    match = re.search(name_pattern, text)
    if match:
        return match.group(0)  # Return the found name
    return None

def log_attendance(name):
    """Log the detected name to a text file for attendance tracking."""
    with open('attendance_log.txt', 'a') as file:
        file.write(f'{name}\n')

def main(image_path):
    """Main function to process the ID image and log attendance."""
    print("Processing the ID image...")

    # Extract text from the image
    extracted_text = extract_text_from_image(image_path)
    print("Extracted Text:\n", extracted_text)

    # Find the name in the extracted text
    name = find_name_in_text(extracted_text)

    if name:
        print(f"Detected Name: {name}")
        log_attendance(name)
        print(f"Attendance logged for {name}.")
    else:
        print("No valid name detected in the ID.")

# Example usage
# Provide the path to an ID card image
image_path = 'id_card_sample.jpg'
main(image_path)
