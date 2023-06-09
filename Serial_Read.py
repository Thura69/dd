from guizero import App, Text, TextBox, PushButton, Slider

app = App(title="Hello world")
welcome_message = Text(app, text="Welcome to my app",
                       size=40, color="white", font="Times New Roman")

my_name = TextBox(app)


def say_my_name():
    welcome_message.value = my_name.value


def change_text_size(slider_value):
    welcome_message.size = slider_value


text_size = Slider(app, command=change_text_size, start=10, end=80)
update_text = PushButton(app, command=say_my_name, text="Display my name")


app.display()
