# tactile
This code is proof of concept for an image to braille converter with hardware implementations.  The arm mounted Raspberry Pi reads a webcam input, then Google's Tesseract OCR interprets any significant text in the image, then, using GPIO, a finger mounted matrix of solenoids protrudes representing the text in braille, character by character.
