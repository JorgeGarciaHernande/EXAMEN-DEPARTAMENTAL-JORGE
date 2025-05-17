import sys
from PyQt5 import uic, QtWidgets, QtCore
import serial

qtCreatorFile = "interfaz 1.ui"  # Nombre del archivo .ui
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyMainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def _init_(self):
        super()._init_()
        self.setupUi(self)

        self.arduino = None

        try:
            self.arduino = serial.Serial('COM4', baudrate=9600, timeout=1)
            print("Conectado a COM4")
        except Exception as e:
            print(f"No se pudo conectar al Arduino: {e}")
            self.arduino = None

        # Timer para leer datos del sensor
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.leer_valor)
        self.timer.start(500)

        # Botón para detener/reanudar lectura
        self.pushButton.setText("Detener lectura")
        self.pushButton.clicked.connect(self.toggle_lectura)

        # Checkboxes para encender/apagar LEDs manualmente
        self.checkBox.stateChanged.connect(lambda: self.controlar_led(10, self.checkBox))
        self.checkBox_2.stateChanged.connect(lambda: self.controlar_led(9, self.checkBox_2))
        self.checkBox_3.stateChanged.connect(lambda: self.controlar_led(8, self.checkBox_3))

    def leer_valor(self):
        if self.arduino and self.arduino.inWaiting():
            try:
                valor = self.arduino.readline().decode('utf-8').strip()
                if valor.isdigit():
                    self.listWidget.addItem(f"Valor LDR: {valor}")
                    if self.listWidget.count() > 20:
                        self.listWidget.takeItem(0)
            except Exception as e:
                print(f"Error leyendo del Arduino: {e}")

    def toggle_lectura(self):
        if self.timer.isActive():
            self.timer.stop()
            self.pushButton.setText("Reanudar lectura")
            print("Lectura detenida.")
        else:
            self.timer.start(500)
            self.pushButton.setText("Detener lectura")
            print("Lectura reanudada.")

    def controlar_led(self, pin, checkbox):
        if self.arduino:
            estado = checkbox.isChecked()
            comando = f"{pin}:{1 if estado else 0}\n"
            self.arduino.write(comando.encode('utf-8'))
            print(f"LED en pin {pin} -> {'ON' if estado else 'OFF'}")

if __name__ == "_main_":
    app = QtWidgets.QApplication(sys.argv)
    window = MyMainWindow()
    window.show()
    sys.exit(app.exec_())