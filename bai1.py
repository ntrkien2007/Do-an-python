def tinh_combo(so_ga, so_khoai):
    combo_theo_ga = so_ga // 3
    combo_so_khoai = so_khoai
    so_combo = min(combo_theo_ga, combo_so_khoai)
    so_ga_dung = so_combo * 3
    ga_le = so_ga - so_ga_dung
    return so_combo, ga_le


# test case theo dau bai
com_bo, ga_le = tinh_combo(200, 200)
print(com_bo)
print(ga_le)