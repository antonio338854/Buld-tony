from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class AlgebraApp(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        
        self.label = Label(text="Digite uma expressão (ex: 2 + 2):", font_size=20)
        self.input = TextInput(multiline=False, font_size=30)
        self.btn = Button(text="Resolver", background_color=(0, 0.7, 0.9, 1))
        self.btn.bind(on_press=self.calcular)
        
        self.result = Label(text="Resultado: ", font_size=25)

        self.layout.add_widget(self.label)
        self.layout.add_widget(self.input)
        self.layout.add_widget(self.btn)
        self.layout.add_widget(self.result)
        
        return self.layout

    def calcular(self, instance):
        try:
            # Usa eval para resolver a conta (simples para este exemplo)
            res = eval(self.input.text)
            self.result.text = f"Resultado: {res}"
        except Exception:
            self.result.text = "Erro na expressão!"

if __name__ == '__main__':
    AlgebraApp().run()
