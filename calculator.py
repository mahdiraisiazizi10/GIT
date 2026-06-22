import customtkinter as ctk


ctk.set_appearance_mode("dark")  
ctk.set_default_color_theme("blue") 

class ModernCalculator(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("modern calculator")
        self.geometry("360x520")
        self.resizable(False, False)


        self.expression = ""


        self.display = ctk.CTkEntry(
            self, 
            width=340, 
            height=70, 
            font=("Arial", 32), 
            justify="right",
            border_width=0,
            fg_color="#212121",
            text_color="#FFFFFF"
        )
        self.display.pack(padx=10, pady=20)
        self.display.insert(0, "0")


        self.create_buttons()

    def create_buttons(self):

        button_frame = ctk.CTkFrame(self, fg_color="transparent")
        button_frame.pack(padx=10, pady=5)


        buttons = [
            ('C', 0, 0, '#E53935', '#C62828'), ('(', 0, 1, '#424242', '#616161'), (')', 0, 2, '#424242', '#616161'), ('/', 0, 3, '#00ACC1', '#00838F'),
            ('7', 1, 0, '#303030', '#424242'), ('8', 1, 1, '#303030', '#424242'), ('9', 1, 2, '#303030', '#424242'), ('*', 1, 3, '#00ACC1', '#00838F'),
            ('4', 2, 0, '#303030', '#424242'), ('5', 2, 1, '#303030', '#424242'), ('6', 2, 2, '#303030', '#424242'), ('-', 2, 3, '#00ACC1', '#00838F'),
            ('1', 3, 0, '#303030', '#424242'), ('2', 3, 1, '#303030', '#424242'), ('3', 3, 2, '#303030', '#424242'), ('+', 3, 3, '#00ACC1', '#00838F'),
            ('0', 4, 0, '#303030', '#424242'), ('.', 4, 1, '#303030', '#424242'), ('=', 4, 2, '#2E7D32', '#1B5E20')
        ]

        for text, row, col, fg_color, hover_color in buttons:

            colspan = 2 if text == '=' else 1
            
            btn = ctk.CTkButton(
                button_frame, 
                text=text, 
                font=("Arial", 22, "bold"),
                width=75 if text != '=' else 160,
                height=65,
                corner_radius=15, 
                fg_color=fg_color,
                hover_color=hover_color,
                text_color="#FFFFFF",
                command=lambda t=text: self.on_button_click(t)
            )
            btn.grid(row=row, column=col, columnspan=colspan, padx=5, pady=5)

    def on_button_click(self, char):
        if char == 'C':
            self.expression = ""
            self.update_display("0")
        elif char == '=':
            try:
  
                result = str(eval(self.expression))
                self.update_display(result)
                self.expression = result 
            except Exception:
                self.update_display("Error")
                self.expression = ""
        else:

            if self.expression == "" and char not in ['+', '-', '*', '/', ')']:
                self.expression = char
            else:
                self.expression += char
            self.update_display(self.expression)

    def update_display(self, text):
        self.display.delete(0, ctk.END)
        self.display.insert(0, text)

if __name__ == "__main__":
    app = ModernCalculator()
    app.mainloop()