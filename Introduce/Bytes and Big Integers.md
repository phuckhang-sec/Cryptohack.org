- Lí thuyết: Các hệ thống mật mã như RSA hoạt động trên các con số, nhưng các thông điệp được tạo thành từ các ký tự. Chúng ta nên chuyển đổi các thông điệp của mình thành các con số như thế nào để có thể áp dụng các phép toán?
Cách phổ biến nhất là lấy các byte thứ tự của thông điệp, chuyển đổi chúng thành hệ thập lục phân và nối lại. Điều này có thể được hiểu là một số cơ số 16/hệ thập lục phân, và cũng được biểu diễn ở hệ cơ số 10/hệ thập phân.
  + Sử dụng hàm long_to_bytes() và bytes_to_long() trong thư viện pycryptodome của python

- Challenge: chuyển đổi cơ số nguyên sau trở lại thành thông điệp: 11515195063862318899931685488813747395775516287289682636499965282714637259206269
- Code:

![image](https://github.com/user-attachments/assets/618d0b27-c619-4cea-a619-ae981e556714)

- Flag: crypto{3nc0d1n6_4ll_7h3_w4y_d0wn}
