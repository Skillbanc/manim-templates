from manim import *
import pandas as pd
import os
import fnmatch
from AbstractAnim import AbstractAnim
import cvo

# Read Excel data into a pandas DataFrame
xlsx_path = "/Users/hridaybhushan/Downloads/ConventionRegistrations.xlsx"
df = pd.read_excel(xlsx_path, sheet_name='Sheet2')  # Adjust sheet_name as per your Excel file

class MyAnimation(AbstractAnim):
    def construct(self):
        self.setNameWithImage()
        #self.readAndWrite()

    def setNameWithImage(self):
        
        # Folder containing final images
        images_folder = "/Users/hridaybhushan/Downloads/2024 St Louis Donor Sponsor List"
        
        # List of possible file extensions to check
        image_extensions = ['.png', '.jpg', '.jpeg']  # Add more extensions as needed
        #CircleColor=self.colorChoice.copy()
        # Loop through each row in the Excel data
        for index, row in df.iterrows():
            self.setBackgroundImage()

            # Extract registration number
            registration_no = row['Registration ID']
            

            #c1o1 diagram
            name = row['Display Name']
            sponsorship_category = row['Sponsorship Category']
            o1_name = f"{name} Garu"  # Assuming "Garu" suffix as per previous instructions
            c1_name = f"{sponsorship_category} Sponsor"
            o1 = Text(o1_name, font_size=26)
            c1 = Text(c1_name, font_size=30)
            c1.move_to(LEFT * 3).scale(0.1)
            o1.next_to(c1, DOWN*1.75).scale(0.1)

            #if len(self.colorChoice)==0:
                #self.colorChoice=CircleColor()
            
            
            
            
            # Initialize variable to store found image path
            found_image_path = None
            
            # Try each extension in the list
            for ext in image_extensions:
                # Construct image filename based on registration ID and current extension
                image_filename = f"{registration_no}_*{ext}"
                
                # Find matching image file
                matching_images = [file for file in os.listdir(images_folder) if fnmatch.fnmatch(file, image_filename)]
                
                if matching_images:
                    # Take the first matching image (assuming one exists)
                    found_image_path = os.path.join(images_folder, matching_images[0])
                    break  # Stop searching further extensions if a match is found
            
            if found_image_path:
                center_image = ImageMobject(found_image_path)
                
                center_image.scale_to_fit_height(2)
                center_image.scale_to_fit_width(4)
                center_image.move_to(RIGHT * 3)
                center_image.scale(0.1)
                
                
                # Animation sequence
                
                self.play(center_image.animate.scale(10), o1.animate.scale(8), c1.animate.scale(8), run_time=2)
                self.wait(8)
                self.clear()
                
            else:
                self.setBackgroundImage()
                o1 = Text(o1_name, font_size=26).scale(0.1)
                c1 = Text(c1_name, font_size=30).scale(0.1)
                o1.next_to(c1, DOWN*1.75)
                self.play(o1.animate.scale(10), c1.animate.scale(10), run_time=2)
                self.wait(8)
                # If no matching image found, skip displaying it
                continue

    def setBackgroundImage(self):

        # Background image
            background_image_path = '/Users/hridaybhushan/Downloads/Digital Background.png'
            background = ImageMobject(background_image_path)
            background.scale_to_fit_width(config.frame_width)
            background.scale_to_fit_height(config.frame_height)
            self.add(background)
            
    def readAndWrite(self):
       
        
        CircleColor=self.colorChoice.copy()
        # Loop through each row in the Excel data
        for index, row in df.iterrows():
            
            # Extract registration number
            registration_no = row['Registration ID']
            

            #c1o1 diagram
            name = row['Name']
            sponsorship_category = row['Sponsorship Category']
            o1_name = f"{name} Garu"  # Assuming "Garu" suffix as per previous instructions
            c1_name = f"{sponsorship_category} Sponsor"
            print(c1_name + ':' + o1_name)

                    


# To render the scene
if __name__ == "__main__":
    
    scene = MyAnimation()
    scene.render()