f = open("yesterday.txt", 'r')
yesterday_lyric = ""
while True:
    line = f.readline()
    if not line:
        break
    yesterday_lyric = yesterday_lyric + line.strip() + "\n"
f.close()

'''
#대소문자 구분 제거
n_of_yesterday = yesterday_lyric.upper().count("YESTERDAY") 
print("Number of a Word 'YESTERDAY'", n_of_yesterday)
'''


'''
Yesterday 노래엔 Yesterday 라는 말이 몇 번 나올까?
대소문자를 구분하여 “Yesterday”와 “yesterday”의
개수를 나눠서 세는 프로그램을 작성하세요.
'''
n_of_Yesterday = yesterday_lyric.count("Yesterday") 
n_of_yesterday = yesterday_lyric.count("yesterday") 
print("Number of a Word 'Yesterday'", n_of_Yesterday)
print("Number of a Word 'Yesterday'", n_of_yesterday)



