import re


def is_valid_phone(number: str) -> bool:
    """
    Kiểm tra số điện thoại Việt Nam hợp lệ (10 số, bắt đầu bằng 0).
    """
    # Xử lý trường hợp người dùng lỡ tay nhập thừa dấu cách ở đầu/cuối
    number = number.strip()

    # Regex: Bắt đầu bằng 0, tiếp theo là 9 chữ số
    pattern = r"^0\d{9}$"

    if re.match(pattern, number):
        return True
    return False


def main():
    print("--- CHƯƠNG TRÌNH KIỂM TRA SỐ ĐIỆN THOẠI ---")

    while True:
        # Nhập dữ liệu từ bàn phím
        user_input = input("\nNhập số điện thoại cần kiểm tra (hoặc 'q' để thoát): ")

        # Thoát vòng lặp nếu nhập 'q'
        if user_input.lower() == 'q':
            print("Cảm ơn bạn đã sử dụng chương trình!")
            break

        # Kiểm tra và thông báo kết quả
        if is_valid_phone(user_input):
            print(f"✅ Số '{user_input}' là số điện thoại HỢP LỆ.")
        else:
            print(f"❌ Số '{user_input}' KHÔNG hợp lệ.")
            print("Gợi ý: Số điện thoại phải có 10 chữ số và bắt đầu bằng số 0.")


if __name__ == "__main__":
    main()