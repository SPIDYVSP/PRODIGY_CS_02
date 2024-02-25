# PRODIGY_CS_02
A simple image encryption tool using pixal manipulation.

The provided Python script implements a simple image encryption tool using pixel manipulation. This tool employs a basic permutation-based encryption algorithm to scramble the pixel values of an image.

The encryption process involves the following steps:
1. The input image is opened and converted into a numpy array of pixel values.
2. A permutation key is used to generate a random order of indices.
3. The pixel values are flattened, and their order is shuffled based on the permutation key.
4. The shuffled pixel values are reshaped to their original image dimensions.
5. The resulting encrypted image is saved to a specified output path.

To decrypt the encrypted image, the same permutation key is used to reverse the permutation process, thereby restoring the original image.

While this implementation provides a basic level of encryption, it's important to note that it may not be suitable for secure applications. More robust encryption techniques, such as cryptographic algorithms, should be utilized for sensitive data.
