def solution(numbers, hand):
    answer = ''
    # numbers = [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]
    # hand = "right"
    # answer = ''
    phone = {
        1: (0, 0),
        2: (0, 1),
        3: (0, 2),
        4: (1, 0),
        5: (1, 1),
        6: (1, 2),
        7: (2, 0),
        8: (2, 1),
        9: (2, 2),
        '*': (3, 0),
        0: (3, 1),
        '#': (3, 2),
    }

    l_finger = '*'  # 왼손구락 시작은 *
    r_finger = '#'  # 오른손가락 시작 #

    for num in numbers:
        if num in [1, 4, 7]:  # 왼쪽 번호가 나오면 왼쪽 표시하기
            answer += 'L'
            l_finger = num  # 왼손누른 후 위치 이동
        elif num in [3, 6, 9]:  # 오른쪽 번호가 나오면 오른쪽 표시하기
            answer += 'R'
            r_finger = num  # 오른손누른 후 위치 이동
        else:  # 남은 중앙 숫자들
            # 딕셔너리에서 위치를 꺼낸다음, 현재 왼쪽 또는 오른쪽 손가락이 위치한 위치와 거리를 비교해서 어떤 손가락을 쓸건지 확인
            target = phone[num]  # 타겟넘버 위치
            l_position = phone[l_finger]  # 왼쪽 위치
            r_position = phone[r_finger]  # 오른쪽 위치
            # 절대값!!!(음수 나올 수 있음) 앞의 위치 - 앞의 위치 + 뒤의 위치 - 뒤의 위치 인덱스
            l_distance = abs(target[0] - l_position[0]) + abs(target[1] - l_position[1])
            r_distance = abs(target[0] - r_position[0]) + abs(target[1] - r_position[1])

            # 계산한 값 비교하기 = 작은 값이 더 가깝다는 의미
            if l_distance < r_distance:  # 왼쪽이 더 가까운 경우
                answer += 'L'
                l_finger = num  # 왼쪽 손가락 위치 이동
            elif l_distance > r_distance:  # 오른쪽이 더 가까운 경우
                answer += 'R'
                r_finger = num  # 오른 손가락 위치 이동
            else:  # 둘이 거리가 같은 경우에는 어느 손잡이인지 확인하고 넣기
                if hand == 'left':
                    answer += 'L'
                    l_finger = num
                else:
                    answer += 'R'
                    r_finger = num
    return answer
