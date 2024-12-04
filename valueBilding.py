from nicegui import ui

class Demo:
    def __init__(self):
        self.number = 1
        self.show_more = False

demo = Demo()
checkbox = ui.checkbox('Ver Materias', value=False)
button = ui.button('Haz Clic', on_click=lambda: toggle_elements())
button.bind_visibility_from(checkbox, 'value')

additional_elements = ui.column()
additional_elements.visible = False
with additional_elements:
    ui.slider(min=1, max=4).bind_value(demo, 'number')
    ui.toggle({1: 'POO', 2: 'INTEGRAL', 3: 'LINEAL', 4: 'PROBABILIDAD'}).bind_value(demo, 'number')
    ui.number().bind_value(demo, 'number')

# Función para alternar la visibilidad de los elementos adicionales
def toggle_elements():
    demo.show_more = not demo.show_more
    additional_elements.visible = demo.show_more  # Actualiza la visibilidad

ui.run()
