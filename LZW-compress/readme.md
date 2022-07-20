
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
   
- Nguyên tắc hoạt động của phương pháp nén LZW như sau:
   + Một xâu ký tự là một tập hợp từ hai ký tự trở lên.
   + Nhớ tất cả các xâu ký tự đã gặp và gán cho nó một dấu hiệu (token) riêng.
   + Nếu lần sau gặp lại xâu ký tự đó, xâu ký tự sẽ được thay thế bằng dấu hiệu của nó
- Phần quan trọng nhất của phương pháp nén này là phải tạo một mảng rất lớn dùng để lưu giữ các xâu ký tự đã gặp (Mảng này được gọi là "Từ điển"). Khi các byte dữ liệu cần nén được đem đến, chúng liền được giữ lại trong một bộ đệm chứa (Accumulator) và đem so sánh với các chuỗi đã có trong "từ điển". Nếu chuỗi dữ liệu trong bộ đệm chứa không có trong "từ điển" thì nó được bổ sung thêm vào "từ điển" và chỉ số của chuỗi ở trong "từ điển" chính là dấu hiệu của chuỗi. Nếu chuỗi trong bộ đệm chứa đã có trong "từ điển" thì dấu hiệu của chuỗi được đem ra thay cho chuỗi ở dòng dữ liệu ra. Có bốn quy tắc để thực hiện việc nén dữ liệu theo thuật toán LZW là:
   - Quy tắc 1: 256 dấu hiệu đầu tiên được dành cho các ký tự đơn (0 - 0ffh).
   - Quy tắc 2: Cố gắng so sánh với "từ điển" khi trong bộ đệm chứa đã có nhiều hơn hai ký tự.
   - Quy tắc 3: Các ký tự ở đầu vào (Nhận từ tập tin sẽ được nén) được bổ sung vào bộ đệm chứa đến khi chuỗi ký tự trong bộ đệm chứa không có trong "từ điển".
   - Quy tắc 4: Khi bộ đệm chứa có một chuỗi mà trong "từ điển" không có thì chuỗi trong bộ đệm chứa được đem vào "từ điển". Ký tự cuối cùng của chuỗi ký tự trong bộ đệm chứa phải ở lại trong bộ đệm chứa để tiếp tục tạo thành chuỗi mới.

- Ví dụ: Các bước để mã hoá chuỗi "!BAN!BA!BAA!BAR!" như sau (Bảng 4. 1):
   + Bước 1: Ký tự thứ nhất ‘!’ được cất vào bộ đệm chứa để chuẩn bị tạo nên một chuỗi.
   + Bước 2: Ký tự thứ hai ‘B’ nối thêm vào sau ký tự !. Vì trong "từ điển" chưa có chuỗi "!B" nên chuỗi này được thêm vào "từ điển" và được gán dấu hiệu là 100h (Vì từ 000h đến 0ffh được dành riêng cho các ký tự đơn: Quy tắc 1). ‘!’ được gửi ra còn ‘B’ phải ở lại trong bộ đệm chứa.
   + Bước 3: Ký tự thứ ba ‘A’ thêm vào sau ‘B’. Chuỗi "BA" cũng chưa có trong "từ điển" nên nó được thêm vào "từ điển" và gán dấu hiệu là 101h. ‘A’ ở lại trong bộ đệm chứa còn ‘B’ được gửi ra.
   + Bước 4: Ký tự thứ tư ‘N’ thêm vào sau ‘A’ tạo thành chuỗi "AN" cũng chưa có trong "từ điển" nên được thêm vào "từ điển" và có dâu hiệu là 102h. ‘N’ ở lại trong bộ đệm chứa còn ‘A’ được gửi ra.
   + Bước 5: Ký tự thứ năm ‘!’ thêm vào sau ‘N’ để tạo thành chuỗi "N!", "N!" được thêm vào "từ điển" với dấu hiệu là 103h. ‘!’ ở lại còn ‘N’ được gửi ra.
   + Bước 6: Ký tự thứ sáu ‘B’ thêm vào sau ‘!’. Lần này thì chuỗi "!B" đã có trong "từ điển" nên không có ký tự nào được gửi ra. "!B" tiếp tục ở lại trong "từ điển" để tạo ra chuỗi mới.
   + Bước 7: Ký tự thứ bảy ‘A’ thêm vào sau ‘B’ để tạo thành chuỗi "!BA", do "!BA" không có trong "từ điển" nên nó được thêm vào "từ điển" và gán dấu hiệu là 104h đồng thời dấu hiệu 100h được gửi ra thay cho "!B" (Quy tắc 4). A tiếp tục ở lại trong bộ đệm chứa để tạo thành chuỗi mới.

- Các bước trên cứ thế tiếp tục cho đến khi hết tập tin cần nén. Việc giảm kích thước chỉ thực sự bắt đầu tại bước 7 khi mà một dấu hiệu 12 bits là <100h> được gửi ra thay cho hai byte "B!".
