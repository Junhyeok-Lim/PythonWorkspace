from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel, QPushButton, QDockWidget, QTextEdit, QVBoxLayout, QWidget

class MyMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Create the main layout
        layout = QVBoxLayout()

        # Create your existing frame (the one you want to keep)
        self.existing_frame = QWidget()
        layout.addWidget(self.existing_frame)

        # Set the main layout
        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

        # Create a QDockWidget to hold the ExpSlice content
        self.dock = QDockWidget("ExpSlice Content", self)
        self.dock.setWidget(QTextEdit("This is the ExpSlice content to be displayed."))

        # Add the QDockWidget to the left dock area
        self.addDockWidget(Qt.LeftDockWidgetArea, self.dock)

        # Create a button to toggle the visibility of the dock widget
        self.button = QPushButton("Toggle ExpSlice")
        layout.addWidget(self.button)

        # Connect the button click event to the method to toggle the dock widget
        self.button.clicked.connect(self.toggle_exp_slice)

    def toggle_exp_slice(self):
        self.dock.setVisible(not self.dock.isVisible())