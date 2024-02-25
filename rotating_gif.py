#!/usr/local/bin/.venv/bin/python
from PIL import Image
import imageio
import os
import sys
from rich.console import Console

console = Console()


def create_rotating_gif(image_path, duration, output_path="rotating_logo.gif"):
    # Load the image
    image = Image.open(image_path)

    # Determine the number of frames based on the desired rotation speed and duration
    frames_per_second = 24  # Adjust this for smoother or choppier animation
    total_frames = int(duration * frames_per_second)
    angle_per_frame = (
        360 / total_frames
    )  # Total rotation divided by the number of frames

    frames = []
    for frame in range(total_frames):
        # Rotate the image and append to frames list
        rotated_image = image.rotate(-frame * angle_per_frame, expand=True)
        frames.append(rotated_image)

    # Save the frames as a gif
    imageio.mimsave(output_path, frames, fps=frames_per_second)


if __name__ == "__main__":

    if len(sys.argv) < 2:
        console.print(
            "[red]Oops:[/red] You need to add a filename when running this script."
        )
        console.print("[green]Example: [/green]makeRotatingLogo /image/path/name.png ")
    else:
        image_path = sys.argv[1]
        # Customize these variables
        duration = 5  # Duration of the GIF in seconds

        # Create the GIF
        create_rotating_gif(image_path, duration)
