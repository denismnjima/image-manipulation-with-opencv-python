import cv2

def is_image_blurry(image_path, threshold=100.0):
    # Load the image in grayscale
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    
    # Apply the Laplacian operator
    laplacian = cv2.Laplacian(image, cv2.CV_64F)
    
    # Calculate the variance
    variance = laplacian.var()
    
    # Check if the variance is below the threshold
    if variance < threshold:
        return True, variance
    else:
        return False, variance

# Example usage
image_path = 'assets/wallp.jpeg'
blurry, variance = is_image_blurry(image_path)
print(f"Is the image blurry? {'Yes' if blurry else 'No'}")
print(f"Laplacian Variance: {variance}")
