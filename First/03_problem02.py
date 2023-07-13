# 웹사이트 게시판폼을 작성 중인데, 게시물 총 건수와 한 페이지당 탑재가능한 게시물 수를 입력했을 때 총 페이지 수를 출력
# m 총 게시물 수
# n 한페이지 당 게시물 수
#
#
# total_page = 0
#
# total_post = int(input("게시물 총 건수를 입력하세요. \n"))
# post_per_page = int(input("한 페이지당 탑재 가능한 게시물 수를 입력하세요. \n"))
#
# if total_post % post_per_page != 0:
#     total_page = total_post // post_per_page
#     total_page += 1
#
# print(f"총 게시물 {total_post}개를 한페이지당 {post_per_page}개로 배치하면 총 {total_page}페이지가 나옵니다.")


def getTotalPage(m, n):  # 함수정의
    if m % n != 0:
        page = m // n + 1
    else:
        page = m // n
    return page


page = getTotalPage(2, 10)
print(page)
