from nicegui import ui

ui.icon('thumb_down', color='red').classes('text-9xl')
ui.markdown('This is **Markdown**.')
ui.html('This is <strong>HTML</strong>.')
with ui.row():
    ui.label('PABLO').style('color: #A04AA7; font-weight: bold;font-family: "Times New Roman", serif; font-size: 30px;')
    ui.label('Tailwind').classes('font-serif')
    ui.label('Quasar').classes('q-ml-xl')
ui.link('NiceGUI on GitHub', 'https://github.com/zauberzeug/nicegui')

ui.run()