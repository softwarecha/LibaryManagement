import cv2

def detect_words(image_path):
    # Load the image
    image = cv2.imread(image_path)

    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply thresholding to convert the image to binary
    _, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY_INV)

    # Find contours in the binary image
    contours, _ = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Initialize a list to store the detected words
    words = []

    # Iterate over the contours
    for contour in contours:
        # Get the bounding rectangle of the contour
        x, y, w, h = cv2.boundingRect(contour)

        # Filter out small contours
        if w > 10 and h > 10:
            # Extract the word region from the image
            word = image[y:y+h, x:x+w]

            # Append the word to the list
            words.append(word)

    return words

# Example usage
image_path = "Test.jpg"
detected_words = detect_words(image_path)

# Display the detected words
for word in detected_words:
    cv2.imshow('Word', word)
    cv2.waitKey(0)

# Close all windows
cv2.destroyAllWindows()
