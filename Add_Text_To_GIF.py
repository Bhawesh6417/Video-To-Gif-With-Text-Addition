from PIL import Image, ImageDraw, ImageFont, ImageSequence
from moviepy.editor import ImageSequenceClip
import numpy as np  

def add_text_to_gif(input_gif_path, output_gif_path, text, font_path, font_size, text_color):
    # Open the original GIF
    original_gif = Image.open(input_gif_path)
    
    # Create a list to hold the modified frames
    frames = []
    
    try:
        # Load the font
        font = ImageFont.truetype(font_path, font_size)
    except IOError:
        # Fall back to default font
        font = ImageFont.load_default()
        print("Warning: Could not load the specified font. Using default font.")
    
    # Iterate through each frame in the original GIF
    for frame in ImageSequence.Iterator(original_gif):
        # Convert the frame to RGBA mode
        frame = frame.convert("RGBA")
        
        # Get the dimensions of the frame
        width, height = frame.size
        
        # Calculate text size and position
        text_bbox = ImageDraw.Draw(Image.new('RGBA', (1, 1))).textbbox((0, 0), text, font=font)
        text_width = text_bbox[2] - text_bbox[0]
        text_height = text_bbox[3] - text_bbox[1]
        text_x = (width - text_width) // 2  # Center the text horizontally
        text_y = height - text_height - 10  # 10 pixels from the bottom
        
        # Create a drawing context
        d = ImageDraw.Draw(frame)
        
        # Add text to the frame
        d.text((text_x, text_y), text, font=font, fill=text_color)
        
        # Append the modified frame to the list of frames
        frames.append(frame)
    
    # Save the frames as a new GIF
    frames[0].save(output_gif_path, save_all=True, append_images=frames[1:], loop=0)

    return frames

# Parameters for adding text
input_gif_path = 'input.gif'  # Path to your input GIF
output_gif_path = 'output.gif'  # Path to save the output GIF
output_video_path = 'output.mp4'  # Path to save the output video
print("Enter Text to add in GIF: ")
text =input()  # Text to add
font_path = 'dejavu-sans-bold.ttf'  # Specify the path to the font file
font_size = 60 # Font size (adjust as needed)
text_color = (255, 255, 255, 255)  # Text color (R, G, B, A)
duration = 2  # Duration of the video in seconds

# Add text to the GIF and get modified frames
frames = add_text_to_gif(input_gif_path, output_gif_path, text, font_path, font_size, text_color)

