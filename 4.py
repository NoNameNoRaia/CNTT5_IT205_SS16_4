student_records = [
    {
        "student_id": "SV001",
        "name": "Nguyễn Văn A",
        "math": 8.5,
        "physics": 7.0,
        "chemistry": 9.0
    },
    {
        "student_id": "SV002",
        "name": "Trần Thị B",
        "math": 4.0,
        "physics": 5.5,
        "chemistry": 5.0
    },
    {
        "student_id": "SV003",
        "name": "Lê Văn C",
        "math": 9.5,
        "physics": 9.0,
        "chemistry": 8.5
    }
]

def display_menu():
    print("""
===== HỆ THỐNG QUẢN LÝ ĐIỂM THI RIKKEI UNIVERSITY =====
1. Xem bảng điểm và học lực
2. Cập nhật điểm thi sinh viên
3. Báo cáo thống kê (Đỗ/Trượt)
4. Tìm sinh viên Thủ khoa
5. Thoát chương trình
======================================================
""")

def calculate_average(student):
    return (
        student["math"] +
        student["physics"] +
        student["chemistry"]
    ) / 3

def classify_student(avg):

    if avg >= 8:
        return "Giỏi"

    elif avg >= 6.5:
        return "Khá"

    elif avg >= 5:
        return "Trung bình"

    return "Yếu"

def validate_score():

    while True:

        try:
            score = float(
                input("Nhập điểm mới: ")
            )

            if 0 <= score <= 10:
                return score

            print(
                "Điểm số không hợp lệ. Vui lòng nhập từ 0 đến 10!"
            )

        except ValueError:

            print(
                "Lỗi: Vui lòng nhập số!"
            )

def display_grades(records):

    if len(records) == 0:
        print(
            "Hệ thống chưa có dữ liệu sinh viên."
        )
        return

    print("\n--- BẢNG ĐIỂM SINH VIÊN ---")

    for index, student in enumerate(records, start=1):

        avg = calculate_average(student)

        rating = classify_student(avg)

        print(
            f"{index}. "
            f"[{student['student_id']}] "
            f"{student['name']} | "
            f"Toán: {student['math']} | "
            f"Lý: {student['physics']} | "
            f"Hóa: {student['chemistry']} | "
            f"ĐTB: {avg:.2f} - {rating}"
        )

    print("-" * 40)

def update_student_score(records):

    student_id = input(
        "Nhập mã sinh viên cần cập nhật: "
    ).strip().upper()

    found = None

    for student in records:

        if student["student_id"] == student_id:
            found = student
            break

    if found is None:

        print(
            f"Không tìm thấy sinh viên mang mã {student_id} trong hệ thống!"
        )
        return

    print("""
1. Toán
2. Lý
3. Hóa
""")

    subject = input(
        "Chọn môn học: "
    )

    score = validate_score()

    match subject:

        case "1":
            found["math"] = score
            subject_name = "Toán"

        case "2":
            found["physics"] = score
            subject_name = "Lý"

        case "3":
            found["chemistry"] = score
            subject_name = "Hóa"

        case _:
            print(
                "Môn học không hợp lệ!"
            )
            return

    print(
        f">> Đã cập nhật điểm {subject_name} "
        f"của sinh viên '{found['name']}' "
        f"thành {score}"
    )

def generate_report(records):

    if len(records) == 0:

        print(
            "Hệ thống chưa có dữ liệu sinh viên."
        )

        return

    passed = 0
    failed = 0

    for student in records:

        avg = calculate_average(student)

        if avg >= 5:
            passed += 1
        else:
            failed += 1

    total = len(records)

    pass_percent = passed / total * 100
    fail_percent = failed / total * 100

    print("\n--- BÁO CÁO HỌC VỤ ---")

    print(
        f"Tổng số sinh viên: {total}"
    )

    print(
        f"Số lượng qua môn: "
        f"{passed} sinh viên "
        f"({pass_percent:.2f}%)"
    )

    print(
        f"Số lượng trượt: "
        f"{failed} sinh viên "
        f"({fail_percent:.2f}%)"
    )

def find_valedictorian(records):

    if len(records) == 0:

        print(
            "Hệ thống chưa có dữ liệu sinh viên."
        )

        return

    top_student = max(
        records,
        key=calculate_average
    )

    avg = calculate_average(
        top_student
    )

    print("\n--- VINH DANH THỦ KHOA ---")

    print(
        f"Sinh viên: {top_student['name']}"
    )

    print(
        f"Mã: {top_student['student_id']}"
    )

    print(
        f"Điểm Trung Bình: {avg:.2f}"
    )

def main():

    while True:

        display_menu()

        choice = input(
            "Chọn chức năng (1-5): "
        )

        match choice:

            case "1":
                display_grades(
                    student_records
                )

            case "2":
                update_student_score(
                    student_records
                )

            case "3":
                generate_report(
                    student_records
                )

            case "4":
                find_valedictorian(
                    student_records
                )

            case "5":

                print(
                    "Cảm ơn bạn đã sử dụng hệ thống!"
                )

                break

            case _:

                print(
                    "Lựa chọn không hợp lệ!"
                )

main()