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
        id_input = input("Nhập mã học sinh mới: ").strip().upper()
        valid = True
        for student in book:
            if student.get("id") == id_input:
                print(f"Lỗi: Mã học sinh {id_input} đã tồn tại! Vui lòng nhập mã khác.")
                valid = False
                break
        if valid == True:
            break
    new_name = input("Nhập tên học sinh: ").strip().title()
    new_score_math = input("Nhập điểm Toán: ")
    while not (new_score_math.count(".") == 1 and new_score_math.replace(".", "").isdigit()) or not (float(new_score_math) >= 0 and float(new_score_math) <= 10):
        print("Điểm không hợp lệ, Vui lòng nhập lại: ")
        new_score_math = input("Nhập điểm Toán: ")
    new_score_english = input("Nhập điểm Anh: ")
    while not (new_score_english.count(".") == 1 and new_score_english.replace(".", "").isdigit()) or not (float(new_score_english) >= 0 and float(new_score_english) <= 10):
        print("Điểm không hợp lệ, Vui lòng nhập lại: ")
        new_score_english = input("Nhập điểm Anh: ")
    new_student = {
        "id": id_input,
        "name": new_name,
        "info": (float(new_score_math),float(new_score_english))
    }
    book.append(new_student)
    print(f"Thành công: Đã thêm sinh viên {id_input} vào hệ thống!")

def update_scores(book):
    id_input = input("Nhập mã sinh viên cần cập nhật: ").strip().upper()
    valid = True 
    for index,student in enumerate(book):
        if id_input == student.get("id"):
            new_score_math = input("Nhập điểm Toán mới: ")
            while not (new_score_math.count(".") == 1 and new_score_math.replace(".", "").isdigit()) or not (float(new_score_math) >= 0 and float(new_score_math) <= 10):
                print("Điểm không hợp lệ, Vui lòng nhập lại: ")
                new_score_math = input("Nhập điểm Toán mới: ")
            new_score_english = input("Nhập điểm Anh mới: ")
            while not (new_score_english.count(".") == 1 and new_score_english.replace(".", "").isdigit()) or not (float(new_score_english) >= 0 and float(new_score_english) <= 10):
                print("Điểm không hợp lệ, Vui lòng nhập lại: ")
                new_score_english = input("Nhập điểm Anh mới: ")
            student["info"] = (float(new_score_math),float(new_score_english))
            print(f"Thành công: Đã cập nhật điểm cho sinh viên {id_input}!")
            valid = False
            break
    if valid == True:
        print("Không tìm thấy sinh viên này")

def delete_student(book):
    id_input = input("Nhập mã sinh viên cần cập nhật: ").strip().upper()
    valid = True 
    for index,student in enumerate(book):
        if id_input == student.get("id"):
            book.pop(index)
            print(f"Thành công: Đã xóa hồ sơ sinh viên {id_input} khỏi hệ thống")
            valid = False
            break
    if valid == True:
        print("Không tìm thấy sinh viên này")
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
        update_scores(grade_book)
        print()
    elif choose == "4":
        delete_student(grade_book)
        print()
    elif choose == "5":
        print("Chương trình kết thúc")
        break
    else:
        print("Lựa chọn không hợp lệ")
        print()