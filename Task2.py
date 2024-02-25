from PIL import Image

def encrypt_image(input_image_path, output_image_path, key):
    # Open the image
    img = Image.open(input_image_path)
    pixels = img.load()
    
    # Encrypt each pixel
    width, height = img.size
    for y in range(height):
        for x in range(width):
            r, g, b = pixels[x, y]
            r ^= key
            g ^= key
            b ^= key
            pixels[x, y] = (r, g, b)
    
    # Save the encrypted image
    img.save(output_image_path)
    print("Image encrypted successfully!")

def decrypt_image(input_image_path, output_image_path, key):
    # Open the encrypted image
    img = Image.open(input_image_path)
    pixels = img.load()
    
    # Decrypt each pixel
    width, height = img.size
    for y in range(height):
        for x in range(width):
            r, g, b = pixels[x, y]
            r ^= key
            g ^= key
            b ^= key
            pixels[x, y] = (r, g, b)
    
    # Save the decrypted image
    img.save(output_image_path)
    print("Image decrypted successfully!")

# Example usage:
input_image_path = r"C:\Users\acer\Music\VSP Task 2\demo.jpeg"
encrypted_image_path = r"C:\Users\acer\Music\VSP Task 2\encrypted_image.jpeg"
decrypted_image_path = r"C:\Users\acer\Music\VSP Task 2\decrypted_image.jpg"
encryption_key = 123  # You can use any integer value as the encryption key

# Encrypt the image
encrypt_image(input_image_path, encrypted_image_path, encryption_key)

# Decrypt the image
decrypt_image(encrypted_image_path, decrypted_image_path, encryption_key)
