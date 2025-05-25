def tao_tuple_tu_lista(lst):
    return tuple(lst)

# Nhập danh sách từ người dùng va su ly chuỗi
input_list = input("Nhập danh sách các số cách nhau bởi dấu phẩy: ")
numbers = list(map(int, input_list.split(',')))

# sử dụng hàm tao_tuple_tu_lista để tạo tuple từ danh sách
my_tuple = tao_tuple_tu_lista(numbers)
print("List:", numbers)
print("Tuple tu list:", my_tuple)