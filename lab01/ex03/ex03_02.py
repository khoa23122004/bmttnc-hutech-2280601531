def dao_nguoc_list(lst):
   return lst[::-1]  

# Nhập danh sách từ người dùng va su ly chuỗi
input_list = input("Nhập danh sách các số cách nhau bởi dấu phẩy: ")
numbers = list(map(int, input_list.split(',')))

# sử dụng hàm dao_nguoc_list để đảo ngược danh sách
list_dao_nguoc = dao_nguoc_list(numbers)
print("Danh sách sau khi đảo ngược:", list_dao_nguoc)