# Import the following modules
from io import BytesIO
import os
from captcha.image import ImageCaptcha

# Create an image instance of the given size


def cap(text):
    image = ImageCaptcha(width=280, height=90)

    # Image captcha text
    captcha_text = text

    # generate the image of the given text
    data = image.generate(captcha_text)
    print(data)

    # Create a BytesIO object to write image data
    image_bytes = BytesIO()
    image.write(captcha_text, image_bytes)

    # Reset the BytesIO object to beginning before saving
    image_bytes.seek(0)

    # Save the image to a file
    # with open("CAPTCHA.png", "wb") as f:
    #     f.write(image_bytes.read())
    # print("captcha created.")


    directory = "booking/static"
    # if not os.path.exists(directory):
    #     os.makedirs(directory)

    with open(os.path.join(directory, "CAPTCHA.png"), "wb") as f:
        f.write(image_bytes.read())
    print("captcha created.")
