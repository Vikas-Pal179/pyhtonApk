# # main.py
# from kivy.app import App
# from kivy.uix.button import Button
# from kivy.uix.label import Label
# from kivy.uix.boxlayout import BoxLayout

# class MyApp(App):
#     def build(self):
#         # Create a layout
#         layout = BoxLayout(orientation='vertical')

#         # Create a label
#         self.label = Label(text='Hello World!')

#         # Create a button
#         button = Button(text='Click Me!')
#         button.bind(on_press=self.on_button_click)

#         # Add the label and button to the layout
#         layout.add_widget(self.label)
#         layout.add_widget(button)

#         return layout

#     def on_button_click(self, instance):
#         # Update the label text when the button is clicked
#         self.label.text = 'Button Clicked!'

# if __name__ == '__main__':
#     MyApp().run()


# main.py
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label

class CalculatorApp(App):
    def build(self):
        self.expression = ''
        layout = GridLayout(cols=4, spacing=10, padding=10)

        # Display label for expression
        self.label = Label(text='0', font_size=50, size_hint=(1, 0.5))
        layout.add_widget(self.label)

        # Define buttons for digits and operators
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            'C', '0', '=', '+'
        ]

        # Add buttons to layout
        for button in buttons:
            btn = Button(text=button, font_size=40)
            btn.bind(on_press=self.on_button_click)
            layout.add_widget(btn)

        return layout

    def on_button_click(self, instance):
        # Get text of the clicked button
        text = instance.text

        if text == 'C':  # Clear expression
            self.expression = ''
        elif text == '=':  # Evaluate expression
            try:
                result = str(eval(self.expression))
                self.expression = result
            except:
                self.expression = 'Error'
        else:
            self.expression += text

        # Update label text with current expression
        self.label.text = self.expression

if __name__ == '__main__':
    CalculatorApp().run()
