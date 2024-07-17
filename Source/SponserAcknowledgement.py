from manim import *
import pandas as pd
import requests
from PIL import Image
from io import BytesIO
import os
import cvo
from AbstractAnim import AbstractAnim

class SponsorVideo(AbstractAnim):
    def construct(self):
        # Load the CSV data
        csv_path = 'C:/Users/rg540/Desktop/NRIVA Sponsor Names.csv'
        data = pd.read_csv(csv_path)

        # Create a temporary directory to store downloaded images
        temp_dir = 'C:/Users/rg540/Desktop/temp_images'
        os.makedirs(temp_dir, exist_ok=True)

        for index, row in data.iterrows():
            
            # Load the background image
            background_image_path = 'C:/Users/rg540/Desktop/Background Image.png'
            background_image = ImageMobject(background_image_path)
            background_image.scale_to_fit_width(config.frame_width)
            background_image.scale_to_fit_height(config.frame_height)
            self.add(background_image)

            # Download image from URL
            image_url = row['Image URL']
            response = requests.get(image_url)
            img = Image.open(BytesIO(response.content))
            img_path = os.path.join(temp_dir, f'temp_image_{index}.png')
            img.save(img_path)

            # Text element p1 using C1 Name and O1 Name
            p1=cvo.CVO().CreateCVO(f"{row['C1 Name']}",f"{row['O1 Name']}").setPosition([-5,0,0])
            self.construct1(p1,p1)

            # Center image from URL
            center_image = ImageMobject(img_path)
            self.play(FadeIn(center_image))
            self.wait(1.5)
            # Remove p1 and center image from the scene
            
            self.clear()

# To render the scene
if __name__ == "__main__":
    from manim import config
    config.background_color = BLACK  # Set the background color
    scene = SponsorVideo()
    scene.render()
