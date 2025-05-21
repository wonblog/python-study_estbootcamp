
score = int(input("성적을 입력하세요. : "))
if score >= 90:
    print('A')
elif score < 90 and score >= 80:
    print('B')
elif score < 80 and score >= 70:
    print('C')
else:
    print('F')

