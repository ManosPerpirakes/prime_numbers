from PyQt5.QtWidgets import QApplication, QTextEdit, QPushButton, QVBoxLayout, QWidget, QLineEdit, QHBoxLayout

def fromf():
    global limit1
    limit1 = input_prompt.text()

def tof():
    global limit2
    limit2 = input_prompt.text()

def findf():
    global total
    global limit1
    global limit2
    try:
        limit1 = int(limit1)
        limit2 = int(limit2)
        counter1 = 2
        counter2 = 0
        while limit1 < 11 and limit1 <= limit2:
            while (limit1 / 2) >= counter1:
                if limit1 % counter1 == 0:
                    counter2 += 1
                    break
                counter1 += 1
            if counter2 == 0:
                total += str(limit1) + "\n"
            limit1 += 1
            counter1 = 2
            counter2 = 0
        while limit1 >= 11 and limit1 <= limit2:
            while (limit1 / 4) >= counter1:
                if limit1 % counter1 == 0:
                    counter2 += 1
                    break
                counter1 += 1
            if counter2 == 0:
                total += str(limit1) + "\n"
            limit1 += 1
            counter1 = 2
            counter2 = 0
    except:
        total += "unfathomable\n"
    total += '\n'
    display.setText(total)

app = QApplication([])
w = QWidget()
w.setWindowTitle("Prime numbers")
w.resize(1000, 800)
display = QTextEdit()
input_prompt = QLineEdit()
input_prompt.setPlaceholderText('Type here:')
pb1 = QPushButton("from")
pb2 = QPushButton("to")
pb3 = QPushButton("find")
l1 = QHBoxLayout()
l2 = QVBoxLayout()
l1.addWidget(display)
l2.addWidget(input_prompt)
l2.addWidget(pb1)
l2.addWidget(pb2)
l2.addWidget(pb3)
l1.addLayout(l2)
w.setLayout(l1)
w.show()
total = 'From which to which number do you wish to see the prime numbers?\n\n'
display.setText(total)
pb1.clicked.connect(fromf)
pb2.clicked.connect(tof)
pb3.clicked.connect(findf)
app.exec_()