def arithmetic_arranger(problems, show_answers=False):
    operators = ['+', '-']
    lis_first_num=[]# Số đầu tiên
    lis_second_num=[]
    lis_operator=[]
    lis_dash=[]# hàng số 3 chỉ  bao gồm dash(-)
    lis_second_row=[]# hàng số 2 bao gồm dâu+ hoặc - và số thứ 2
    answers = []
    # check xem nếu số phương trình cần tính toán lớn hơn 5 hay ko
    if len(problems) >5:
        return 'Error: Too many problems.'
    else:
        for prob in problems:
            a=prob.split()# tách từ phương trình ra
            first_num=a[0]# số đầu tiên của phương trình
            operator=a[1]# dấu của phương trình
            lis_operator.append(operator)# them dấu của phương trình vào list
            second_num=a[2]# số thứ 2 của phương trình để thực hiện phép tính toan
            lis_second_num.append(second_num)# thêm số thứ 2 vào list
            if operator not in operators:
                return "Error: Operator must be '+' or '-'."
            if not first_num.isdigit() or not second_num.isdigit():
                return "Error: Numbers must only contain digits."
            if int(first_num) >= 10000 or int(second_num) >= 10000:
                return 'Error: Numbers cannot be more than four digits.'

            num_of_dash=(max(len(first_num), len(second_num))+1)
            lis_dash.append((num_of_dash+1)*'-')
            first_line=first_num.rjust(num_of_dash+1)
            second_line=second_num.rjust(num_of_dash)
            op=operator.ljust(num_of_dash).strip()
            lis_second_row.append(op+second_line)
            lis_first_num.append(first_line)
            if operator == '+':
                answer=int(first_num)+int(second_num)
                answers_row=str(answer).rjust(num_of_dash+1)
                answers.append(answers_row)
            if operator == '-':
                answer=int(first_num)-int(second_num)
                answers_row=str(answer).rjust(num_of_dash+1)
                answers.append(answers_row)
    first_row='    '.join(lis_first_num)
    second_row='    '.join(lis_second_row)
    dash_row='    '.join(lis_dash)
    answer_row='    '.join(answers)
    arrangement=first_row+'\n'+second_row+'\n'+dash_row
    if show_answers:
        answer_row=first_row+'\n'+second_row+'\n'+dash_row+'\n'+answer_row
        return answer_row

    return arrangement

print(f'\n{arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])}')
print(f'\n{arithmetic_arranger(["1 + 2", "1 - 9380"])}')
print(f'\n{arithmetic_arranger(["3 + 855", "3801 - 2", "45 + 43", "123 + 49"])}')
print(f'\n{arithmetic_arranger(["11 + 4", "3801 - 2999", "1 + 2", "123 + 49", "1 - 9380"])}')
print(f'\n{arithmetic_arranger(["44 + 815", "909 - 2", "45 + 43", "123 + 49", "888 + 40", "653 + 87"])}')
print(f'\n{arithmetic_arranger(["3 / 855", "3801 - 2", "45 + 43", "123 + 49"])}')
print(f'\n{arithmetic_arranger(["24 + 85215", "3801 - 2", "45 + 43", "123 + 49"])}')
print(f'\n{arithmetic_arranger(["98 + 3g5", "3801 - 2", "45 + 43", "123 + 49"])}')
print(f'\n{arithmetic_arranger(["3 + 855", "988 + 40"], True)}')
print(f'\n{arithmetic_arranger(["32 - 698", "1 - 3801", "45 + 43", "123 + 49", "988 + 40"], True)}')
