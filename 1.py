def solution(n):
    answer = 0
    for i in range(n):
        if i % 3 == 0 or i % 5 == 0:
            answer += i

    return answer

print(solution(n=int(input())))