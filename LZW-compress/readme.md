
<h4> Nén ảnh theo phương pháp LZW </h4>

- Ra đời: Năm 1984, Terry Welch đã cải tiến giải thuật LZ thành một giải thuật mới hiệu quả hơn và đặt tên là LZW
- Định nghĩa: Phương pháp nén từ điển dựa trên việc xây dựng từ điển lưu các chuỗi ký tự có tần suất lặp lại cao và thay thế bằng từ mã tương ứng mỗi khi gặp lại chúng. Giải thuật LZW hay hơn các giải thuật trước nó ở kỹ thuật tổ chức từ điển cho phép nâng cao tỉ lệ nén.
- Ứng dụng: Giải thuật nén LZW được sử dụng để nén các loại văn bản, ảnh đen trắng, ảnh màu, ảnh đa mức xám... và là chuẩn nén cho các dạng ảnh GIF và TIFF. Mức độ hiệu quả của LZW không phụ thuộc vào số bít màu của ảnh
- Phương pháp: LZW xây dựng một từ điển lưu các mẫu có tần suất xuất hiện cao trong ảnh. Từ điển là tập hợp những cặp từ vựng và nghĩa của nó(từ vựng là các từ mã được sắp xếp theo thứ tự nhất định-nghĩa là một chuối con trong dữ liệu ảnh)
+ Do kích thước bộ nhớ không phải vô hạn và để đảm bảo tốc độ tìm kiếm, từ điển chỉ giới hạn 4096 ở phần tử dùng để lưu lớn nhất là 4096 giá trị của các từ mã. Như vậy độ dài lớn nhất của từ mã là 12 bits (4096 = 212). Cấu trúc từ điển như sau:
   - 256 từ mã đầu tiên theo thứ tự từ 0...255 chữa các số nguyên từ 0...255. Đây là mã của 256 kí tự cơ bản trong bảng mã ASCII. 
   - Từ mã thứ 256 chứa một mã đặc biệt là “mã xóa” (CC – Clear Code)
   - Từ mã thứ 257 chứa mã kết thúc thông tin (EOI – End Of Information)
   - Các từ mã còn lại (từ 258 đến 4095) chứa các mẫu thương lặp lại trong ảnh