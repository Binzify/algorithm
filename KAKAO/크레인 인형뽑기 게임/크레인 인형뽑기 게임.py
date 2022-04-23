board = [
    [0, 0, 0, 0, 0],
    [0, 0, 1, 0, 3],
    [0, 2, 5, 0, 1],
    [4, 2, 4, 4, 2],
    [3, 5, 1, 3, 1],
]
moves = [1, 5, 3, 5, 1, 2, 1, 4]


def solution(board, moves):
    answer = 0
    stack = []  # 인형 뽑아서 넣을 장소
    for i in moves:  # 크레인의 이동 위치를 받아서
        for j in range(len(board)):  # 보드크기만큼 돌면서 크레인 하강
            if board[j][i - 1] == 0:  # 인형이 없으면
                continue  # 다음 한칸 아래로 이동
            else:  # 만약 인형이 있으면
                doll = board[j][i - 1]  # 인형 번호를 보관
                board[j][i - 1] = 0  # 해당 인형 제거했음을 표시
                stack.append(doll)  # 스택에다 넣어준다
                if len(stack) >= 2:  # 만약 스택에 인형 2개이상 찼다
                    if stack[-1] == stack[-2]:  # 맨 뒤의 2개 검사
                        stack.pop()  # 같으면 두 번 빼준다
                        stack.pop()
                        answer += 2  # 그리고 인형 빼준 개수 더하기
                break
    return answer


print(solution(board, moves))
