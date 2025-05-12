from PIL import Image


def remove_white_background(input_path, output_path, threshold=200):
    """
    Remove white background from a PNG image and save it with transparency

    Threshold is the value above which a pixel is considered white (default is 200)
    """

    image = Image.open(input_path).convert("RGBA")
    data = image.getdata()

    new_data = []

    for item in data:
        r, g, b, a = item

        if r > threshold and g > threshold and b > threshold:
            # Convert light pixels (background) to transparent
            new_data.append((255, 255, 255, 0))
        else:
            # Keep dark pixels (black lines)
            new_data.append((r, g, b, a))

    image.putdata(new_data)
    image.save(output_path, "PNG")

    print(f"Image saved to {output_path}")


if __name__ == "__main__":
    input_path = "input.png"  # Change to path of your input image
    output_path = "output.png"  # Change to desired output path

    remove_white_background(input_path, output_path)
