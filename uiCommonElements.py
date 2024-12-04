from nicegui import ui
from nicegui.elements.mixins.color_elements import color
from nicegui.events import ValueChangeEventArguments

def show(event: ValueChangeEventArguments):
    name = type(event.sender).__name__
    ui.notify(f'{name}: {event.value}')

ui.button('Haz Clic', on_click=lambda: ui.notify(' Hiciste Clic'))
with ui.row():
    ui.checkbox('Acepto los Terminos...', on_change=show)
    ui.switch('Activado/Desactivado', on_change=show)
ui.radio(['Perro', 'Gato', 'Perico'], value='Gato', on_change=show).props('inline')
with ui.row():
    ui.input('Escribe tu Nombre', on_change=show)
    ui.select(['ISC', 'ITics','Arquitectura'], value='ISC', on_change=show)
ui.link('Para mas informacion', '/documentation').classes('mt-80')

ui.run()