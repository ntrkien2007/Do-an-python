import random
from collections import deque


def simulate_canteen(total_time=30):
    queue = deque()  # Hàng chờ chứa thời điểm đến của sinh viên
    wait_times = []  # Danh sách lưu thời gian chờ của từng người
    server_busy_until = 0  # Thời điểm mà nhân viên phục vụ sẽ rảnh

    print(f"{'Thời gian':<10} | {'Sự kiện'}")
    print("-" * 45)

    for current_minute in range(total_time + 1):
        # 1. Sinh viên đến mỗi 2 phút
        if current_minute % 2 == 0:
            queue.append(current_minute)
            print(f"Phút {current_minute:>2}: 1 SV mới đến. Hàng chờ: {len(queue)}")

        # 2. Kiểm tra phục vụ sinh viên
        # Nếu nhân viên đang rảnh và có người đang chờ
        if current_minute >= server_busy_until and queue:
            arrival_time = queue.popleft()  # Lấy người đầu tiên ra

            # Thời gian chờ = Thời điểm hiện tại - Thời điểm đến
            wait_time = current_minute - arrival_time
            wait_times.append(wait_time)

            # Tính thời gian phục vụ ngẫu nhiên 1-3 phút
            service_duration = random.randint(1, 3)
            server_busy_until = current_minute + service_duration

            print(f"Phút {current_minute:>2}: Đang phục vụ (Chờ: {wait_time}p, Xong lúc: {server_busy_until}p)")

    # 3. Tính toán kết quả (Phải nằm trong hàm hoặc sau khi gọi hàm)
    print("-" * 45)
    if wait_times:
        avg_wait = sum(wait_times) / len(wait_times)
        print(f"Tổng số sinh viên đã phục vụ: {len(wait_times)}")
        print(f"Thời gian chờ trung bình: {avg_wait:.2f} phút")
    else:
        print("Không có sinh viên nào được phục vụ.")


if __name__ == "__main__":
    simulate_canteen(30)