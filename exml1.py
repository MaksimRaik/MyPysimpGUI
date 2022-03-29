import numpy as np
import PySimpleGUI as sg

menu = [ [ 'File', [ 'Open', 'Exit' ] ],
         [ 'View', [ 'Max size', 'Norm size' ] ],
         [ 'Model', [ 'Equation of State', 'Mixture Component' ] ],
         [ 'Calculation', [ 'Parametrs' ] ]]

toolbar = [
    [ sg.Button( 'Open', button_color=('grey', sg.COLOR_SYSTEM_DEFAULT), pad=(0,0), key='-open-') ],
    [sg.Button( 'Parametrs', button_color=('grey', sg.COLOR_SYSTEM_DEFAULT), pad=(0,0), key='-parametrs-') )],
]

layout = [

            [ sg.Menu( menu ) ],
            [ sg.Frame( '', toolbar, title_color='white',
                        background_color=sg.COLOR_SYSTEM_DEFAULT, pad=(0, 0)) ],
            [ sg.Button( 'Open' ), sg.Text( ' Pressure ' ), sg.Input(), sg.Text( 'Temperature' ), sg.Input(),
             sg.Button( 'Start' ), sg.Button( 'Plot' ) ],


          ]

window = sg.Window('PySimpleTest', layout)

event, values = window.read()
window.close()



