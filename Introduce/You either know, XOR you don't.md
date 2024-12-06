- Challenge: I've encrypted the flag with my secret key, you'll never be able to guess it. Remember the flag format and how it might help you in this challenge!: 0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104
- Phân tích:
  + Do flag có dạng "crypto{" nên ta sẽ thử XOR cipher với key = "crypto{" để kiểm tra nó có phài là key hay không. 
  + Ta được kết quả: myXORke+y_Q\x0bHOMe$~seG8bGURN\x04DFWg)a|\x1dTM!an\x7f. Do xuất hiện đoạn "myXORkey" khá đáng ngờ, ta thứ XOR cipher với key = "myXORkey"
  + Phán đoán của ta đa đúng, sau khi thay key = "myXORkey" ta nhận được flag.
- Code:
 
    ![image](https://github.com/user-attachments/assets/0dd28fd5-085b-4bca-a8ce-563127af1b5a)
  
- Flag: crypto{1f_y0u_Kn0w_En0uGH_y0u_Kn0w_1t_4ll}
