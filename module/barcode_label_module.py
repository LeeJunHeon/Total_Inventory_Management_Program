# module/barcode_label_module.py

import os
import win32com.client as win32

# 1) 템플릿 .btw (기존에 만든 라벨)
#    → BarTender Designer에서 만든 barcode_label.btw 의 전체 경로
TEMPLATE_PATH = r"C:\Users\wnsgj\Desktop\통합 재고관리 프로그램\전체 통합 프로그램\lib\barcode_label.btw"

# 2) 기본 저장 위치 (사용자가 별도 경로를 지정하지 않았을 때 사용)
#    → NAS 경로 등 공용 저장소
DEFAULT_OUTPUT_DIR = r"\\VanaM_NAS\VanaM_toShare\JH_Lee\Programs\통합재고관리프로그램\barcode"

# 3) 바코드 전용 프린터 이름 (윈도우 '프린터 및 스캐너'에 나오는 이름 그대로 사용)
BARCODE_PRINTER_NAME = "ZDesigner GK420t"  # 예: "ZDesigner GK420t"


def create_btw_file(code_str: str, output_dir: str | None = None) -> str:
    """
    BarTender 템플릿(TEMPLATE_PATH)을 기반으로 QR_DATA에 code_str을 넣고,
    지정된 output_dir에 'code_str.btw' 파일을 생성한 후, 그 전체 경로를 반환한다.

    Parameters
    ----------
    code_str : str
        라벨에 찍힐 코드 (예: 'W4P0BT-91').
        템플릿 내부에서 Named Data Source 이름이 'QR_DATA'인 객체에 이 값이 들어간다.
    output_dir : str | None
        저장할 폴더 경로.
        None 이거나 빈 문자열이면 DEFAULT_OUTPUT_DIR 을 사용한다.

    Returns
    -------
    new_btw_path : str
        생성된 .btw 파일의 전체 경로.
    """
    # output_dir를 지정하지 않으면 기본 경로 사용
    if not output_dir:
        output_dir = DEFAULT_OUTPUT_DIR

    # 절대 경로로 변환 + 폴더 없으면 생성
    output_dir = os.path.abspath(output_dir)
    os.makedirs(output_dir, exist_ok=True)

    # 새 btw 파일 경로: [output_dir]\[code_str].btw
    new_btw_path = os.path.join(output_dir, f"{code_str}.btw")

    # BarTender Application COM 객체 생성 (UI는 보이지 않게)
    bt_app = win32.Dispatch("BarTender.Application")
    bt_app.Visible = False

    try:
        # 템플릿 .btw 열기
        fmt = bt_app.Formats.Open(TEMPLATE_PATH, False, "")

        # 템플릿 내 Named Data Source 'QR_DATA'에 code_str 값 채우기
        fmt.SetNamedSubStringValue("QR_DATA", code_str)

        # 새 파일로 저장 (이미 같은 이름이 있으면 덮어쓰기 True)
        fmt.SaveAs(new_btw_path, True)

        # 템플릿은 변경사항 저장 없이 닫기 (원본 유지)
        # 1 = btDoNotSaveChanges
        fmt.Close(1)
    finally:
        # BarTender 종료
        bt_app.Quit(1)

    return new_btw_path


def print_btw_file(btw_path: str, printer_name: str | None = None, copies: int = 1) -> None:
    """
    이미 생성된 .btw 파일을 지정한 프린터로 바로 출력한다.

    Parameters
    ----------
    btw_path : str
        출력할 .btw 파일의 전체 경로.
    printer_name : str | None
        사용할 프린터 이름.
        None 이면 BARCODE_PRINTER_NAME 상수를 사용한다.
    copies : int
        출력할 장 수(동일 라벨 복사본 개수).
    """
    # 프린터 이름을 지정하지 않으면 기본 바코드 프린터 사용
    if printer_name is None:
        printer_name = BARCODE_PRINTER_NAME

    btw_path = os.path.abspath(btw_path)
    if not os.path.exists(btw_path):
        raise FileNotFoundError(f"btw 파일을 찾을 수 없습니다: {btw_path}")

    # BarTender Application COM 객체 생성
    bt_app = win32.Dispatch("BarTender.Application")
    bt_app.Visible = False

    try:
        # btw 파일 열기
        fmt = bt_app.Formats.Open(btw_path, False, "")

        # 사용할 프린터 설정
        fmt.Printer = printer_name

        # 출력 장 수 설정
        fmt.IdenticalCopiesOfLabel = copies

        # 프린트 (다이얼로그 없이 조용히 출력)
        # PrintOut(ShowDialog=False, WaitForCompletion=False)
        fmt.PrintOut(False, False)

        # 변경사항 저장 없이 닫기
        fmt.Close(1)
    finally:
        # BarTender 종료
        bt_app.Quit(1)
