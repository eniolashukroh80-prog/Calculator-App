from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
import math

class Calculator(App):

    def build(self):
        self.expression = ""

        layout = GridLayout(cols=1, padding=10, spacing=10)

        self.display = TextInput(
            multiline=False,
            readonly=True,
            halign="right",
            font_size=32
        )

        layout.add_widget(self.display)

        buttons = [
            ["sin", "cos", "tan", "√"],
            ["x²", "%", "C", "/"],
            ["7", "8", "9", "*"],
            ["4", "5", "6", "-"],
            ["1", "2", "3", "+"],
            ["0", ".", "="]
        ]

        for row in buttons:
            row_layout = GridLayout(cols=len(row), spacing=5)

            for item in row:
                btn = Button(text=item, font_size=22)
                btn.bind(on_press=self.button_press)
                row_layout.add_widget(btn)

            layout.add_widget(row_layout)

        return layout

    def button_press(self, instance):
        value = instance.text

        try:
            if value == "C":
                self.expression = ""
                self.display.text = ""

            elif value == "=":
                result = str(eval(self.expression))
                self.display.text = result
                self.expression = result

            elif value == "√":
                result = math.sqrt(float(self.display.text))
                self.display.text = str(result)
                self.expression = str(result)

            elif value == "x²":
                result = float(self.display.text) ** 2
                self.display.text = str(result)
                self.expression = str(result)

            elif value == "%":
                result = float(self.display.text) / 100
                self.display.text = str(result)
                self.expression = str(result)

            elif value == "sin":
                result = math.sin(math.radians(float(self.display.text)))
                self.display.text = str(result)
                self.expression = str(result)

            elif value == "cos":
                result = math.cos(math.radians(float(self.display.text)))
                self.display.text = str(result)
                self.expression = str(result)

            elif value == "tan":
                result = math.tan(math.radians(float(self.display.text)))
                self.display.text = str(result)
                self.expression = str(result)

            else:
                self.expression += value
                self.display.text = self.expression

        except:
            self.display.text = "Error"
            self.expression = ""

Calculator().run()