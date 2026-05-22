def tinh_tong_le(n):
    return sum(range(1, n + 1, 2))


# --- KIỂM THỬ (TEST CASES) ---

def run_tests():
    test_cases = [1, 10]

    for n in test_cases:
        ket_qua = tinh_tong_le(n)

        if n == 1:
            chi_tiet = "Số lẻ duy nhất là 1"
        else:
            chi_tiet = "Các số lẻ là: " + ", ".join(map(str, range(1, n + 1, 2)))

        print(f"Với n = {n:2} => Tổng = {ket_qua:2} | ({chi_tiet})")


if __name__ == "__main__":
    run_tests()