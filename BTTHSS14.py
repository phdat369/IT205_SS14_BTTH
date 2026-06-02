grade_book = [
    {"id": "SV01", "name": "Nguyễn Văn A", "info": (8.5, 7.0)},
    {"id": "SV02", "name": "Trần Thị B", "info": (6.0, 9.0)}
]

def display_grades(book):
    print("--- BẢNG ĐIỂM HỌC SINH ---")
    print(f"{"Mã SV": <5} | {"Tên học sinh": <15} | {"Điểm Toán": <15} | {"Điểm Anh": <15} | {"ĐTB": <5}")
    print("------------------------------------------------------------------")
    for student in book:
        print(f"{student.get("id"): <5} | {student.get("name"): <15} | {student.get("info")[0]: <15} | {student.get("info")[1]: <15} | {(student.get("info")[1]+student.get("info")[0])/2: <5}")
    print("------------------------------------------------------------------")

def add_student(book):

while True:
    choose = input("""==== HỆ THỐNG QUẢN LÝ ĐIỂM SỐ ====
1. Xem bảng điểm học sinh
2. Thêm hồ sơ học sinh mới
3. Cập nhật điểm số
4. Xóa hồ sơ học sinh
5. Thoát chương trình
=============================================================
Chọn chức năng (1-5): """)
    if choose == "1":
        display_grades(grade_book)
        print()
    elif choose == "2":
         add_student(grade_book)
        print()
    elif choose == "3":
        print()
    elif choose == "4":
        print()
    elif choose == "5":
        print("Chương trình kết thúc")
    else:
        print("Lựa chọn không hợp lệ")
        print()