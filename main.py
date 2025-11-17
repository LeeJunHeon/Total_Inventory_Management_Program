# main.py 예시 (틀만)
import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from ui.main_window import Ui_Form  # ← 너가 pyuic6로 만든 메인 UI 모듈/클래스
from module.barcode_label_module import create_btw_file, print_btw_file


class MainWindow(QMainWindow, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # 예: 메인 UI에 있는 "바코드 생성" 버튼에 기능 연결
        # self.btn_generate_barcode.clicked.connect(self.on_generate_barcode_clicked)
        # self.btn_print_barcode.clicked.connect(self.on_print_barcode_clicked)

    def on_generate_barcode_clicked(self):
        code_str = "W4P0BT-91"  # 실제로는 UI에서 입력받은 값 사용
        btw_path = create_btw_file(code_str, None)  # 기본 경로 사용
        print(f"생성된 btw: {btw_path}")

    def on_print_barcode_clicked(self):
        code_str = "W4P0BT-91"
        # 기본 저장 위치 기준 btw 경로 계산 (이미 만들어져 있다고 가정)
        # 또는 위에서 저장해둔 btw_path를 멤버 변수로 들고 있어도 됨
        from module.barcode_label_module import DEFAULT_OUTPUT_DIR
        import os
        btw_path = os.path.join(DEFAULT_OUTPUT_DIR, f"{code_str}.btw")
        print_btw_file(btw_path, None, copies=1)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec())
