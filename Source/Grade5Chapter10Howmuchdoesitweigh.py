import json
from manim import *
from numpy import size
from AbstractAnim import AbstractAnim

import cvo

class Howmuchdoesitweigh(AbstractAnim):
    def construct(self):
        self.RenderSkillbancLogo()
        self.kilogram()
        self.fadeOutCurrentScene()
        self.Example1()
        self.fadeOutCurrentScene()
        self.Question1()
        self.fadeOutCurrentScene()
        self.Question2()
        self.fadeOutCurrentScene()
        self.Question3()
        self.fadeOutCurrentScene()
        self.Example2()
        self.fadeOutCurrentScene()
        self.Q1()
        self.fadeOutCurrentScene()
        self.Q2()
        self.fadeOutCurrentScene()
        self.Q3()
        self.fadeOutCurrentScene()
        self.Q4()
        self.fadeOutCurrentScene()
        self.Q5()
        self.fadeOutCurrentScene()
        self.quintal()
        self.fadeOutCurrentScene()
        self.quintaltable()
        self.fadeOutCurrentScene()
        self.GithubSourceCodeReference()        
        


    def kilogram(self):
        # self.positionChoice = [[0,0,0],[-3,0,0],[3,0,0]]
        self.isRandom = False
        p10=cvo.CVO().CreateCVO("Kilogram","")
        p11=cvo.CVO().CreateCVO("1 Kilogram","1000grams")
        p12=cvo.CVO().CreateCVO(" Writtern as","Kg")
        p13=cvo.CVO().CreateCVO("Gram Writtern as","g")
        p10.cvolist.append(p11)
        p10.cvolist.append(p12)
        p10.cvolist.append(p13)
        self.setNumberOfCirclePositions(4)
        self.construct1(p10,p10)

    def Example1(self):
        text = Text("Example", color=YELLOW).scale(1)
        text.center()
        text.shift(UP * 3)
        self.play(Write(text))
        text2 =Text("Question 1:It is festival time and Raghu's mother is making \n""5 kg of laddoos. She gives Raghu this grocery list",color=GREEN).scale(0.65)
        text2.shift(UP * 2,LEFT )
        self.play(Write(text2))
        table_content = [
            ["Bengal gram flour", "2 kg"],
            ["Sugar", "3 kg"],
            ["Kishmish", "200 gms"],
            ["Kaaju", "150 gms"],
            ["Badam", "100 gms"],
        ]
        cell_height = 0.8
        cell_width = 4
        
        start_position = ORIGIN + UP * (len(table_content) * cell_height / 2)
        
        table = VGroup(*[
            VGroup(*[
                Tex(content, color=BLUE).move_to(start_position + np.array([i * cell_width, -j * cell_height, 0]))
                for i, content in enumerate(row)
            ])
            for j, row in enumerate(table_content)
        ])
        
        h_lines = VGroup(*[
            Line(
                start=start_position + np.array([-cell_width / 2, -j * cell_height - cell_height / 2, 0]),
                end=start_position + np.array([(len(table_content[0])) * cell_width - cell_width / 2, -j * cell_height - cell_height / 2, 0])
            )
            for j in range(len(table_content) + 1)
        ])
        
        extra_h_line_top = Line(
            start=start_position + np.array([-cell_width / 2, cell_height / 2, 0]),
            end=start_position + np.array([(len(table_content[0])) * cell_width - cell_width / 2, cell_height / 2, 0])
        )
        
        v_lines = VGroup(
            Line(
                start=start_position + np.array([-cell_width / 2, cell_height / 2, 0]),
                end=start_position + np.array([-cell_width / 2, -(len(table_content)) * cell_height + cell_height / 2, 0])
            ),
            Line(
                start=start_position + np.array([(len(table_content[0])) * cell_width - cell_width / 2, cell_height / 2, 0]),
                end=start_position + np.array([(len(table_content[0])) * cell_width - cell_width / 2, -(len(table_content)) * cell_height + cell_height / 2, 0])
            )
        )
        
        table_with_lines = VGroup(table, h_lines, v_lines, extra_h_line_top)
        table_with_lines.shift(LEFT * 1.4)
        table_with_lines.shift(DOWN * 1.5)
        self.play(Create(table_with_lines))
        
        self.wait(5)

    def Question1(self):
        question = Text(
            "(a) What is the total weight of dry fruits that Raghu has been asked to bring?",
            font_size=30, color=GREEN
        )
        question.to_edge(UP)
        self.play(Write(question))
        self.wait(1)

        # Dry fruit weights
        weights = [
            "Kishmish: 200 grams",
            "Kaaju: 150 grams",
            "Badam: 100 grams",
        ]
        weight_text = VGroup(*[Text(weight, font_size=36) for weight in weights])
        weight_text.arrange(DOWN, aligned_edge=LEFT)
        weight_text.next_to(question, DOWN, buff=1.0)
        self.play(FadeIn(weight_text, shift=DOWN))
        self.wait(1)

        # Summation
        equation_text = Text("Total weight of dry fruits:", font_size=36)
        equation_text.next_to(weight_text, DOWN, buff=1.0)
        self.play(FadeIn(equation_text, shift=DOWN))
        self.wait(1)

        # Equation
        equation = MathTex(
            "200 \\text{ grams} + 150 \\text{ grams} + 100 \\text{ grams} = 450 \\text{ grams}",
            font_size=45
        )
        equation.next_to(equation_text, DOWN, buff=0.5)
        self.play(FadeIn(equation, shift=DOWN))
        self.wait(2)

    def Question2(self):
        # Setting up the text for the question
        question = Text(
            "(b) Write the items on the list in the order of their weights, from \n""lightest to heaviest.",
            font_size=30, color=GREEN
        )
        question.to_edge(UP)
        self.play(Write(question))
        self.wait(1)

        # Items with weights in order from lightest to heaviest
        items = [
            "Badam: 100 grams",
            "Kaaju: 150 grams",
            "Kishmish: 200 grams",
            "Bengal gram flour: 2000 grams (2 kg)",
            "Sugar: 3000 grams (3 kg)"
        ]
        item_text = VGroup(*[Text(item, font_size=36) for item in items])
        item_text.arrange(DOWN, aligned_edge=LEFT, buff=0.5)

        self.play(FadeIn(item_text, shift=DOWN))
        self.wait(2)

    def Question3(self):
        # Setting up the text for the question
        question = Text(
            "(c) If Raghu's mother had to make 10 kg of laddoos, then how much more\n"" of each item would Raghu have to buy from the store?",
            font_size=24, color=GREEN
        )
        question.to_edge(UP)
        self.play(Write(question))
        self.wait(1)

        # Define the items and calculations
        items = [
            ("Bengal gram flour", "2 kg", "4 kg", "2 kg"),
            ("Sugar", "3 kg", "6 kg", "3 kg"),
            ("Kishmish", "200 grams", "400 grams", "200 grams"),
            ("Kaaju", "150 grams", "300 grams", "150 grams"),
        ]

        # Display calculations step by step
        item_texts = VGroup()
        for item in items:
            name, current, required, additional = item
            text = (f"{name}:\n"
                    f"Current amount: {current}\n"
                    f"Required amount for 10 kg laddoos: 2 x {current} = {required}\n"
                    f"Additional amount needed: {required} - {current} = {additional}")
            item_text = Text(text, font_size=24)
            item_texts.add(item_text)
        
        item_texts.arrange(DOWN, aligned_edge=LEFT)
        item_texts.next_to(question, DOWN, buff=0.5)


        self.play(FadeIn(item_texts[0], shift=DOWN))
        self.wait(1)
        self.play(FadeIn(item_texts[1], shift=DOWN))
        self.wait(1)
        self.play(FadeIn(item_texts[2], shift=DOWN))
        self.wait(1)
        self.play(FadeIn(item_texts[3], shift=DOWN))
        self.wait(2)

        # Fade out after Kishmish
        self.play(FadeOut(item_texts), FadeOut(question))
        self.wait(1)

        # Remaining items
        remaining_items = [
            ("Badam", "100 grams", "200 grams", "100 grams")
        ]

        remaining_item_texts = VGroup()
        for item in remaining_items:
            name, current, required, additional = item
            text = (f"{name}:\n"
                    f"Current amount: {current}\n"
                    f"Required amount for 10 kg laddoos: 2 x {current} = {required}\n"
                    f"Additional amount needed: {required} - {current} = {additional}")
            item_text = Text(text, font_size=24)
            remaining_item_texts.add(item_text)

        remaining_item_texts.to_edge(UP)
        self.play(FadeIn(remaining_item_texts, shift=DOWN))
        self.wait(1)
        

        # Summary of additional amounts needed
        summary = Text("Additional amount needed for 10 kg laddoos:", font_size=30, color=YELLOW)
        summary.next_to(remaining_item_texts,DOWN,buff=1.0)
        self.play(Write(summary))
        self.wait(1)

        additional_amounts = [
            "Bengal gram flour: 2 kg",
            "Sugar: 3 kg",
            "Kishmish: 200 grams",
            "Kaaju: 150 grams",
            "Badam: 100 grams"
        ]
        additional_text = VGroup(*[Text(amount, font_size=24) for amount in additional_amounts])
        additional_text.arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        additional_text.next_to(summary, DOWN, buff=0.5)

        self.play(FadeIn(additional_text, shift=DOWN))
        self.wait(2)


    def Example2(self):
        text2 =Text("Question 2:Vishal has a big scrap shop. Today, he has received\n"" 45 kg of old newspaper, 26 kg of scrap iron and 8 kg of waste\n"" plastic at his shop.",color=GREEN).scale(0.65)
        text2.shift(UP * 0,LEFT )
        self.play(Write(text2))


    def Q1(self):
        
        # Setting up the text for the question
        question = Text(
            "(a) What is the total weight of his scrap collection in the day?",
            font_size=30, color=GREEN
        )
        question.to_edge(UP)

        # Calculation for total weight using Text instead of MathTex
        calculation_part1 = Text(
            "45 kg (old newspaper) + 26 kg (scrap iron) + 8 kg (waste plastic)",
            font_size=28
        )
        calculation_part1.next_to(question, DOWN, buff=1)

        calculation_part2 = Text(
            "= 45kg + 26kg + 8kg",
            font_size=28
        )
        calculation_part2.next_to(calculation_part1, DOWN, buff=0.5)

        calculation_part3 = Text(
            "= 79 kg",
            font_size=28
        )
        calculation_part3.next_to(calculation_part2, DOWN, buff=0.5)

        # Conclusion
        conclusion = Text(
            "So, the total weight of his scrap collection is 79 kg.",
            font_size=24
        )
        conclusion.next_to(calculation_part3, DOWN, buff=0.5)

        # Adding elements to the scene
        self.play(Write(question))
        self.wait(1)
        self.play(Write(calculation_part1))
        self.wait(0.5)
        self.play(Write(calculation_part2))
        self.wait(0.5)
        self.play(Write(calculation_part3))
        self.wait(1)
        self.play(Write(conclusion))
        self.wait(2)

    def Q2(self):
        
        # Setting up the text for the question
        question = Text(
            "(b) Vishal paid ₹8 for every 1 kg old paper. How much would he pay for 45 kg?",
            font_size=30, color=GREEN
        )
        question.to_edge(UP)

        # Amount paid for 1 kg of old paper
        total_paid_per_kg = Text(
            "Vishal paid ₹8 for every 1 kg of old paper.", font_size=24
        )
        total_paid_per_kg.next_to(question, DOWN, buff=1)

        # Calculation for 45 kg of old paper using Text instead of MathTex
        calculation = Text(
            "45 kg × ₹8/kg = ₹360", font_size=28
        )
        calculation.next_to(total_paid_per_kg, DOWN, buff=0.5)

        # Conclusion
        conclusion = Text(
            "So, he would pay ₹360 for 45 kg of old paper.",
            font_size=24
        )
        conclusion.next_to(calculation, DOWN, buff=0.5)

        # Adding elements to the scene
        self.play(Write(question))
        self.wait(1)
        self.play(Write(total_paid_per_kg))
        self.wait(1)
        self.play(Write(calculation))
        self.wait(1)
        self.play(Write(conclusion))
        self.wait(2)

    def Q3(self):
        
        # Setting up the text for the question
        question = Text(
            "(c) Vishal paid ₹520 for all the scrap iron that he collected. How much did\n"" he pay for 1 kg of scrap iron?",
            font_size=30, color=GREEN
        )
        question.to_edge(UP)

        # Amount paid for all scrap iron
        total_paid = Text("Vishal paid ₹520 for 26 kg of scrap iron.", font_size=24)
        total_paid.shift(UP*2)

        # Calculation for cost per kg
        calculation = Text(
            "₹520 / 26 kg = ₹20/kg", font_size=28
        ).next_to(total_paid, DOWN, buff=0.5)

        # Conclusion
        conclusion = Text(
            "So, he paid ₹20 for 1 kg of scrap iron.",
            font_size=24
        ).next_to(calculation, DOWN, buff=0.5)

        # Adding elements to the scene
        self.add(question)
        self.play(Write(total_paid))
        self.play(Write(calculation))
        self.play(Write(conclusion))

        self.wait(2)
    
    def Q4(self):
        
        # Setting up the text for the question
        question = Text(
            "(d) If Vishal paid ₹1000 for all the material given above, then how much \n""did he pay for 8 kg of plastic material? How much did he pay for 1 kg of\n"" plastic material?",
            font_size=30, color=GREEN
        )
        question.to_edge(UP)

        # Amount paid for all materials
        total_paid = Text("Vishal paid ₹1000 for all the materials.", font_size=24)
        total_paid.shift(UP*2)

        # Total amount paid for old newspaper and scrap iron
        total_old_newspaper_scrap_iron = Text(
            "Amount paid for old newspaper and scrap iron: ₹360 (old newspaper) + ₹520 (scrap iron)\n"" = ₹880",
            font_size=24
        ).next_to(total_paid, DOWN, buff=0.5)

        # Amount paid for 8 kg of plastic material
        amount_paid_8kg = Text(
            "Amount paid for 8 kg of plastic material: ₹1000 - ₹880 = ₹120",
            font_size=24
        ).next_to(total_old_newspaper_scrap_iron, DOWN, buff=0.5)

        # Amount paid for 1 kg of plastic material
        amount_paid_1kg = Text(
            "Amount paid for 1 kg of plastic material: ₹120 / 8 = ₹15/kg",
            font_size=24
        ).next_to(amount_paid_8kg, DOWN, buff=0.5)

        # Conclusion
        conclusion = Text(
            "So, he paid ₹120 for 8 kg of plastic material and ₹15 for 1 kg of plastic material.",
            font_size=24
        ).next_to(amount_paid_1kg, DOWN, buff=0.5)

        # Adding elements to the scene
        self.add(question)
        self.play(Write(total_paid))
        self.play(Write(total_old_newspaper_scrap_iron))
        self.play(Write(amount_paid_8kg))
        self.play(Write(amount_paid_1kg))
        self.play(Write(conclusion))

        self.wait(2)

    def Q5 (self):
         # Setting up the text for the question
        question = Text(
            "(e) Vishal sold each of the three items for ₹3 per kg more than \n""what he had purchased them for. So, how much he earned\n"" in the day?",
            font_size=24, color=GREEN
        )
        question.to_edge(UP)

        # Old newspaper calculations
        old_newspaper = Text("Old newspaper:", font_size=24, color=YELLOW)
        old_newspaper.next_to(question, DOWN, buff=0.1)

        old_newspaper_price = Text(
            "Selling price per kg = 8 + 3 = 11/kg", font_size=24
        ).next_to(old_newspaper, DOWN, buff=0.1)

        old_newspaper_total = Text(
            "Total selling price = 45 kg × 11/kg = 495", font_size=24
        ).next_to(old_newspaper_price, DOWN, buff=0.1)

        # Scrap iron calculations
        scrap_iron = Text("Scrap iron:", font_size=24, color=YELLOW)
        scrap_iron.next_to(old_newspaper_total, DOWN, buff=0.1)

        scrap_iron_price = Text(
            "Selling price per kg = 20 + 3 = 23/kg", font_size=24
        ).next_to(scrap_iron, DOWN, buff=0.1)

        scrap_iron_total = Text(
            "Total selling price = 26 kg × 23/kg = 598", font_size=24
        ).next_to(scrap_iron_price, DOWN, buff=0.1)

        # Plastic material calculations
        plastic_material = Text("Plastic material:", font_size=24, color=YELLOW)
        plastic_material.next_to(scrap_iron_total, DOWN, buff=0.1)

        plastic_material_price = Text(
            "Selling price per kg = 15 + 3 = 18/kg", font_size=24
        ).next_to(plastic_material, DOWN, buff=0.1)

        plastic_material_total = Text(
            "Total selling price = 8 kg × 18/kg = 144", font_size=24
        ).next_to(plastic_material_price, DOWN, buff=0.1)

        # Total amount earned by selling
        total_amount_earned = Text(
            "Total amount earned by selling:", font_size=24
        ).next_to(plastic_material_total, DOWN, buff=0.1)

        total_amount_earned_value = Text(
            "495 + 598 + 144 = 1237", font_size=24
        ).next_to(total_amount_earned, DOWN, buff=0.1)

        # Total cost of materials purchased
        total_cost = Text(
            "The total cost of materials purchased: 1000", font_size=24
        ).next_to(total_amount_earned_value, DOWN, buff=0.3)

        # Total profit earned
        total_profit = Text(
            "Total profit earned: 1237 - 1000 = 237", font_size=24
        ).next_to(total_cost, DOWN, buff=0.2)

        # Vishal's earnings in the day
        earnings = Text(
            "So, Vishal has earned ₹237 in the day.", font_size=24
        ).next_to(total_profit, DOWN, buff=0.2)

        # Adding elements to the scene
        self.add(question)
        self.play(Write(old_newspaper))
        self.play(Write(old_newspaper_price))
        self.play(Write(old_newspaper_total))
        self.play(Write(scrap_iron))
        self.play(Write(scrap_iron_price))
        self.play(Write(scrap_iron_total))
        self.play(Write(plastic_material))
        self.play(Write(plastic_material_price))
        self.play(Write(plastic_material_total))
        self.play(Write(total_amount_earned))
        self.play(Write(total_amount_earned_value))
        self.play(Write(total_cost))
        self.play(Write(total_profit))
        self.play(Write(earnings))

        self.wait(2)


    def quintal(self):
        self.isRandom = False
        p10=cvo.CVO().CreateCVO("1 Quintal","")
        p11=cvo.CVO().CreateCVO("100 kilograms","")
        p10.cvolist.append(p11)
        self.setNumberOfCirclePositions(2)
        self.construct1(p10,p10)
    
    def quintaltable(self):
        table_content = [
            ["Item", "No. of\nbags", "Weight of\neach bag", "Total\nweight\n(kg)", "Total\nweight\n(quintals)"],
            ["Onions", "20", "40 kg", "800 kg", "80 quintals"],
            ["Paddy", "18", "75 kg", "1350 kg", "135 quintals"],
            ["Red gram", "10", "70 kg", "700 kg", "70 quintals"],
        ]
        
        cell_height = 1.5
        cell_width = 2
        start_position = ORIGIN + UP * (len(table_content) * cell_height / 2)
        
        # Scale factors for headings and body content
        heading_scale = 1
        content_scale = 1

        table = VGroup(*[
            VGroup(*[
                Tex(content.replace("\n", "\\\\"), font_size=36 if j == 0 else 24).move_to(start_position + np.array([i * cell_width, -j * cell_height, 0]))
                for i, content in enumerate(row)
            ]).scale(heading_scale if j == 0 else content_scale)
            for j, row in enumerate(table_content)
        ])

        h_lines = VGroup(*[
            Line(
                start=start_position + np.array([-cell_width / 2, -j * cell_height - cell_height / 2, 0]),
                end=start_position + np.array([(len(table_content[0])) * cell_width - cell_width / 2, -j * cell_height - cell_height / 2, 0])
            )
            for j in range(len(table_content) + 1)
        ])

        extra_h_line_top = Line(
            start=start_position + np.array([-cell_width / 2, cell_height / 2, 0]),
            end=start_position + np.array([(len(table_content[0])) * cell_width - cell_width / 2, cell_height / 2, 0])
        )

        v_lines = VGroup(*[
            Line(
                start=start_position + np.array([i * cell_width - cell_width / 2, cell_height / 2, 0]),
                end=start_position + np.array([i * cell_width - cell_width / 2, -(len(table_content)) * cell_height + cell_height / 2, 0])
            )
            for i in range(len(table_content[0]) + 1)
        ])

        table_with_lines = VGroup(table, h_lines, v_lines, extra_h_line_top)
        table_with_lines.shift(LEFT * 5)
        table_with_lines.shift(DOWN * 1.5)

        title = Tex("Example", color=YELLOW).scale(1.2)
        title.next_to(table_with_lines, UP*2, buff=0.5)
        title1 = Tex("(1 quintal = 100 kilograms)", color=WHITE).scale(1)
        title1.next_to(title, DOWN, buff=0.3)

        self.play(Create(title))
        self.play(Create(title1))
        self.play(Create(table_with_lines))

        self.wait(5)
    

    def SetDeveloperList(self): 
       self.DeveloperList="Potluri Divya Reddy" 

    def SetSourceCodeFileName(self):
       self.SourceCodeFileName="Grade5Chapter10Howmuchdoesitweigh.py"

if __name__ == "__main__":
    scene = Howmuchdoesitweigh()
    scene.render()