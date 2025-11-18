# main.py
import sys

from PySide6.QtWidgets import (
    QApplication,
    QWidget,
    QVBoxLayout,
    QTableWidget,
)
from PySide6.QtCore import Qt

from ui.main_window import Ui_Form


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        # 디자이너에서 만든 UI 붙이기
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        # 창 제목
        self.setWindowTitle("재고 관리 프로그램")

        # 하단 테이블 영역들 실제 QTableWidget으로 세팅
        self._setup_tables()

        # 버튼 시그널 연결 (지금은 빈 함수)
        self._connect_signals()

    # ──────────────────────────────────────────────
    # 테이블 영역 세팅
    # ──────────────────────────────────────────────
    def _setup_tables(self):
        # 메인시트 (탭1)
        self.tab1_mainSheet_table = QTableWidget(self)
        layout = QVBoxLayout(self.ui.tab1_mainSheet_tableWidget)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addWidget(self.tab1_mainSheet_table)

        # 탭2 – 웨이퍼/타겟/가스/기자재 보유현황
        self.tab2_waferInventory_table = QTableWidget(self)
        l = QVBoxLayout(self.ui.tab2_waferInventory_tableWidget)
        l.setContentsMargins(0, 0, 0, 0)
        l.addWidget(self.tab2_waferInventory_table)

        self.tab2_targetInventory_table = QTableWidget(self)
        l = QVBoxLayout(self.ui.tab2_targetInventory_tableWidget)
        l.setContentsMargins(0, 0, 0, 0)
        l.addWidget(self.tab2_targetInventory_table)

        self.tab2_gasInventory_table = QTableWidget(self)
        l = QVBoxLayout(self.ui.tab2_gasInventory_tableWidget)
        l.setContentsMargins(0, 0, 0, 0)
        l.addWidget(self.tab2_gasInventory_table)

        self.tab2_equipmentInventory_table = QTableWidget(self)
        l = QVBoxLayout(self.ui.tab2_equipmentInventory_tableWidget)
        l.setContentsMargins(0, 0, 0, 0)
        l.addWidget(self.tab2_equipmentInventory_table)

        # 탭3 – 기간별 상세/집계
        self.tab3_periodDetail_table = QTableWidget(self)
        l = QVBoxLayout(self.ui.tab3_periodDetail_tableWidget)
        l.setContentsMargins(0, 0, 0, 0)
        l.addWidget(self.tab3_periodDetail_table)

        self.tab3_itemGroupSummary_table = QTableWidget(self)
        l = QVBoxLayout(self.ui.tab3_itemGroupSummary_tableWidget)
        l.setContentsMargins(0, 0, 0, 0)
        l.addWidget(self.tab3_itemGroupSummary_table)

    # ──────────────────────────────────────────────
    # 버튼 시그널 연결 (지금은 자리만 만들어 둠)
    # ──────────────────────────────────────────────
    def _connect_signals(self):
        # 탭1 버튼들
        self.ui.tab1_new_pushButton.clicked.connect(self.on_tab1_new)
        self.ui.tab1_save_pushButton.clicked.connect(self.on_tab1_save)
        self.ui.tab1_barcodeLink_pushButton.clicked.connect(self.on_tab1_barcode_link)
        self.ui.tab1_delete_pushButton.clicked.connect(self.on_tab1_delete)
        self.ui.tab1_exportEcvelCsv_pushButton.clicked.connect(self.on_tab1_export)

        # 탭3 엑셀/CSV 내보내기
        self.ui.tab3_exportEcvelCsv_pushButton.clicked.connect(self.on_tab3_export)

    # ──────────────────────────────────────────────
    # 슬롯 함수들 – 나중에 실제 로직 채우면 됨
    # ──────────────────────────────────────────────
    def on_tab1_new(self):
        print("탭1: 신규 클릭")

    def on_tab1_save(self):
        print("탭1: 저장 클릭")

    def on_tab1_barcode_link(self):
        print("탭1: 바코드 연동 클릭")

    def on_tab1_delete(self):
        print("탭1: 삭제 클릭")

    def on_tab1_export(self):
        print("탭1: 엑셀/CSV 내보내기 클릭")

    def on_tab3_export(self):
        print("탭3: 엑셀/CSV 내보내기 클릭")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec())
