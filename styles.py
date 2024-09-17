STYLE_MAINWINDOW = '''
    background-color: rgb(255, 255, 255);
    font-size: 18px;
    font-weight: 550;
'''

STYLE_COMBOBOX = '''
QComboBox {
    border: 0.5px solid lightgrey;
    border-radius: 9px;
    padding: 1px 18px 1px 3px;
    min-width: 6em;
    box-shadow: 0px 0px 0px 0px;
    color: rgb(168, 168, 168);
    font-weight: 450;
}

QComboBox:hover {
    background-color: rgb(222, 240, 250);
}

QComboBox:!editable:on, QComboBox::drop-down:editable:on {
    background-color: rgb(222, 240, 250);
}

QComboBox::drop-down {
    subcontrol-origin: padding;
    subcontrol-position: top right;
    width: 15px;

    border-left-width: 1px;
    border-left-color: lightgrey;
    border-left-style: solid;         
    /*border-top-right-radius: 9px;      
    border-bottom-right-radius: 9px;*/
    
    border-radius: 9px;
}

QComboBox QAbstractItemView {
    selection-background-color: rgb(222, 240, 250);
    border-radius: 9px;
    outline: 0px;
}

QListView::item::focus {
    background-color: rgb(222, 240, 250);
    color: black;
    border-radius: 9px;
    border: 1px solid gray;
}

QComboBox::item::hover {
    background-color: rgb(222, 240, 250);
}

QAbstractItemView {
    border-radius: 9px;
    border: black;
    filter: drop-shadow(0px, 0px);
}

QLineEdit {
    color: black;
}
'''

STYLE_COMBOBOX_AFTER = '''
QComboBox {
    color: black; 
    font-weight: 450;
}
'''

STYLE_DOUBLESPINBOX = '''
QDoubleSpinBox {
    border: 0.5px solid lightgrey;
    border-radius: 9px;
    padding: 1px 18px 1px 3px;
    min-width: 6em;
    box-shadow: 0px 0px 0px 0px;
    color: rgb(168, 168, 168);
    font-weight: 450;
}

QDoubleSpinBox:hover {
    background-color: rgb(222, 240, 250);
}

QDoubleSpinBox::up-button
{
    subcontrol-origin: padding;
    subcontrol-position: top right;
    width: 15px;

    border-left-width: 1px;
    border-left-color: lightgrey;
    border-left-style: solid;         
    
    border-radius: 9px;
}

QDoubleSpinBox::down-button {
    subcontrol-origin: padding;
    subcontrol-position: bottom right;
    width: 15px;

    border-left-width: 1px;
    border-left-color: lightgrey;
    border-left-style: solid;         
    
    border-radius: 9px;
}

'''

STYLE_DOUBLESPINBOX_AFTER = '''
QDoubleSpinBox {
    color: black; 
    font-weight: 450;
}
'''

STYLE_BTN = '''
QPushButton {
    border: 0.5px solid rgb(128, 128, 128);
    border-radius: 9px;
    padding: 1px 18px 1px 3px;
    min-width: 6em;
    box-shadow: 0px 0px 0px 0px;
    color: black;
    font-weight: 450;
}

QPushButton:hover {
    background-color: rgb(222, 240, 250);
}

QPushButton:pressed {
    background-color: rgb(202, 220, 230)
}
'''