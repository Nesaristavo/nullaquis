from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt

class LoadModelWidget(QtWidgets.QWidget):
    def __init__(self, *args, **kwargs):
        super(LoadModelWidget, self).__init__(*args, **kwargs)
        
        # ------------------------ GUI Components ------------------------
        self.setFixedHeight(100)
        self._container = QtWidgets.QGroupBox(self)
        self._container.setSizePolicy(QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding))
        self._container.setFixedHeight(100)
        self._container.setFixedWidth(210)
        
        layout = QtWidgets.QGridLayout()
        self._model_to_select_label = QtWidgets.QLabel("Selected model")
        layout.addWidget(self._model_to_select_label, 0, 0)
        self._model_to_select_list = QtWidgets.QComboBox()
        layout.addWidget(self._model_to_select_list, 0, 1)
        
        # ... (other widget setup code)

        self._remove_btn = QtWidgets.QPushButton("Remove model")
        layout.addWidget(self._remove_btn, 8, 0)
        
        # Hide some widgets initially
        self._bottom_radius_label.setVisible(False)
        self._bottom_radius_edit.setVisible(False)
        # ... (other widget visibility settings)
        
        self._container.setLayout(layout)
        # -------------------- Other attributes --------------------
        # (additional attributes or methods can be defined here)
