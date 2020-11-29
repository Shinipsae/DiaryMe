# html
# open() : 파일객체 가져옴
# write() : 파일객체에 값을 씀
# close() : 파일객체를 닫음
f = open('testwrite.txt', 'w', encoding='utf-8')
f.write("파일 내용")
f.close()
    # with open('html_file.html', 'a') as html_file:
    # html_file.write(html_text) -> 기존 내용에 새로운 내용 추가가