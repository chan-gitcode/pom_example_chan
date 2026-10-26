import json
from pathlib import Path

class PathFile:
    ROOT = Path(__file__).resolve().parent.parent
    RESOURCES_DIR = ROOT / "resources"

    @staticmethod
    def read_json_data(path_file_name: str):
        """
        Đọc và phân tách (parse) dữ liệu từ một tệp JSON trong thư mục resources.

        Args:
            path_file_name (str): Tên file hoặc đường dẫn tương đối (Ví dụ: 'van_thu_nhan.json')

        Returns:
            dict: Đối tượng Dictionary chứa nội dung JSON.
        """
        path_file = PathFile.RESOURCES_DIR / path_file_name

        with path_file.open("r", encoding="utf-8") as file:
            return json.load(file)

    def get_string_file(path_file_name: str) -> str:
        """
        Chuyển đổi đường dẫn tương đối của file nguồn thành đường dẫn tuyệt đối dạng String thuần (phục vụ việc gắn file upload cho Playwright).

        Args:
            path_file_name (str): Đường dẫn tương đối từ resources (VD: 'upload_files/test.png').

        Returns:
            str: Đường dẫn tuyệt đối của file.
        """
        path_file = PathFile.RESOURCES_DIR / path_file_name
        return str(path_file)    
