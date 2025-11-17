import os
import sys
import win32com.client as win32
from PySide6.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit, QPushButton,
    QHBoxLayout, QVBoxLayout, QFileDialog, QPlainTextEdit,
    QMessageBox
)
from PySide6.QtCore import Qt


# ======= 설정값 (너 환경에 맞게 수정) =======

# 1) 템플릿 .btw (기존에 만든 라벨)
TEMPLATE_PATH = r"C:\Users\wnsgj\Desktop\통합 재고관리 프로그램\전체 통합 프로그램\lib\barcode_label.btw"

# 2) 기본 저장 위치 (선택 안 했을 때)
DEFAULT_OUTPUT_DIR = r"\\VanaM_NAS\VanaM_toShare\JH_Lee\Programs\통합재고관리프로그램\barcode"

# 3) 바코드 전용 프린터 이름 (윈도우 프린터 이름 그대로)
BARCODE_PRINTER_NAME = "ZDesigner GK420t"  # 예: "ZDesigner GK420t"


# ======= BarTender 관련 헬퍼 함수 =======

def create_btw_file(code_str: str, output_dir: str) -> str:
    """
    TEMPLATE_PATH 를 기반으로 QR_DATA 에 code_str 을 넣고
    output_dir\code_str.btw 파일을 생성한 뒤, 그 경로를 반환.
    """
    output_dir = os.path.abspath(output_dir)
    os.makedirs(output_dir, exist_ok=True)

    new_btw_path = os.path.join(output_dir, f"{code_str}.btw")

    bt_app = win32.Dispatch("BarTender.Application")
    bt_app.Visible = False  # UI 안 보이게

    try:
        fmt = bt_app.Formats.Open(TEMPLATE_PATH, False, "")
        fmt.SetNamedSubStringValue("QR_DATA", code_str)
        fmt.SaveAs(new_btw_path, True)   # 덮어쓰기 허용
        fmt.Close(1)  # 템플릿은 저장 안 함 (btDoNotSaveChanges)
    finally:
        bt_app.Quit(1)

    return new_btw_path


def print_btw_file(btw_path: str, printer_name: str, copies: int = 1) -> None:
    """
    이미 만들어진 btw_path 파일을 지정한 프린터로 출력.
    """
    btw_path = os.path.abspath(btw_path)
    if not os.path.exists(btw_path):
        raise FileNotFoundError(f"btw 파일을 찾을 수 없습니다: {btw_path}")

    bt_app = win32.Dispatch("BarTender.Application")
    bt_app.Visible = False

    try:
        fmt = bt_app.Formats.Open(btw_path, False, "")
        fmt.Printer = printer_name
        fmt.IdenticalCopiesOfLabel = copies
        fmt.PrintOut(False, False)   # 다이얼로그 없이 조용히 출력
        fmt.Close(1)
    finally:
        bt_app.Quit(1)


# ======= 간단한 PySide6 UI =======

class BarcodeToolWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("바코드 라벨 생성 / 출력 도구")
        self.resize(600, 250)

        # --- 위젯들 ---
        # 제품 코드(=파일명)
        self.code_label = QLabel("제품 코드 / 파일명 (예: W4P0BT-91):")
        self.code_edit = QLineEdit()
        self.code_edit.setPlaceholderText("여기에 코드 입력")

        # 출력 경로
        self.path_label = QLabel("저장 경로 (미선택 시 기본 경로 사용):")
        self.path_edit = QLineEdit()
        self.path_edit.setText(DEFAULT_OUTPUT_DIR)
        self.browse_button = QPushButton("경로 선택...")

        # 버튼들
        self.create_button = QPushButton("BTW 생성")
        self.print_button = QPushButton("라벨 프린트")

        # 로그 창
        self.log_edit = QPlainTextEdit()
        self.log_edit.setReadOnly(True)

        # --- 레이아웃 구성 ---
        main_layout = QVBoxLayout()

        # 코드 입력
        code_layout = QVBoxLayout()
        code_layout.addWidget(self.code_label)
        code_layout.addWidget(self.code_edit)
        main_layout.addLayout(code_layout)

        # 경로 입력 + 버튼
        path_layout = QVBoxLayout()
        path_layout.addWidget(self.path_label)

        path_row = QHBoxLayout()
        path_row.addWidget(self.path_edit)
        path_row.addWidget(self.browse_button)
        path_layout.addLayout(path_row)

        main_layout.addLayout(path_layout)

        # 버튼들
        button_layout = QHBoxLayout()
        button_layout.addWidget(self.create_button)
        button_layout.addWidget(self.print_button)
        main_layout.addLayout(button_layout)

        # 로그
        main_layout.addWidget(self.log_edit)

        self.setLayout(main_layout)

        # --- 시그널 연결 ---
        self.browse_button.clicked.connect(self.on_browse_clicked)
        self.create_button.clicked.connect(self.on_create_clicked)
        self.print_button.clicked.connect(self.on_print_clicked)

        # 내부 상태: 마지막으로 생성한 btw 경로 저장용
        self.last_btw_path: str | None = None

    # ===== 이벤트 핸들러 =====

    def append_log(self, text: str):
        self.log_edit.appendPlainText(text)

    def on_browse_clicked(self):
        dir_path = QFileDialog.getExistingDirectory(self, "저장 경로 선택", self.path_edit.text())
        if dir_path:
            self.path_edit.setText(dir_path)

    def on_create_clicked(self):
        code_str = self.code_edit.text().strip()
        if not code_str:
            QMessageBox.warning(self, "입력 오류", "제품 코드(파일명)를 입력하세요.")
            return

        output_dir = self.path_edit.text().strip() or DEFAULT_OUTPUT_DIR

        try:
            self.append_log(f"[INFO] btw 생성 중... 코드={code_str}, 경로={output_dir}")
            btw_path = create_btw_file(code_str, output_dir)
            self.last_btw_path = btw_path
            self.append_log(f"[OK] btw 생성 완료: {btw_path}")
            QMessageBox.information(self, "완료", f"btw 파일 생성 완료:\n{btw_path}")
        except Exception as e:
            self.append_log(f"[ERROR] btw 생성 실패: {e!r}")
            QMessageBox.critical(self, "에러", f"btw 생성 중 오류 발생:\n{e}")

    def on_print_clicked(self):
        code_str = self.code_edit.text().strip()
        output_dir = self.path_edit.text().strip() or DEFAULT_OUTPUT_DIR

        # 우선, 코드 기준으로 btw 경로 가정
        btw_path = None
        if code_str:
            candidate = os.path.join(output_dir, f"{code_str}.btw")
            if os.path.exists(candidate):
                btw_path = candidate

        # 코드가 없거나 파일이 없으면, 마지막 생성했던 파일 사용
        if btw_path is None:
            btw_path = self.last_btw_path

        if not btw_path or not os.path.exists(btw_path):
            QMessageBox.warning(
                self,
                "파일 없음",
                "출력할 btw 파일을 찾을 수 없습니다.\n"
                "먼저 'BTW 생성'으로 파일을 만든 뒤에 출력해 주세요."
            )
            return

        if BARCODE_PRINTER_NAME == "라벨프린터이름_여기에":
            QMessageBox.warning(
                self,
                "프린터 이름 설정 필요",
                "BARCODE_PRINTER_NAME 상수를 실제 프린터 이름으로 먼저 수정해 주세요."
            )
            return

        try:
            self.append_log(f"[INFO] 프린트 중... 파일={btw_path}, 프린터={BARCODE_PRINTER_NAME}")
            print_btw_file(btw_path, BARCODE_PRINTER_NAME, copies=1)
            self.append_log("[OK] 프린트 요청 완료")
            QMessageBox.information(self, "완료", "라벨 프린트 요청을 보냈습니다.")
        except Exception as e:
            self.append_log(f"[ERROR] 프린트 실패: {e!r}")
            QMessageBox.critical(self, "에러", f"프린트 중 오류 발생:\n{e}")


# ===== 메인 진입 =====

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = BarcodeToolWindow()
    win.show()
    sys.exit(app.exec())
