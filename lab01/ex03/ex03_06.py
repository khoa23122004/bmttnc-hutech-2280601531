def xoa_phan_tu(dictionary, key):
    if key in dictionary:
        del dictionary[key]
        return True
    else:
        return False

# Sử dụng hàm và in kết quả
my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
key_to_delete = 'b'
result = xoa_phan_tu(my_dict, key_to_delete)
if result:
    print(f"Đã xóa phần tử với key '{key_to_delete}', my_dict = ", my_dict)
else:
    print(f"Không tìm thấy phần tử với key '{key_to_delete}'")