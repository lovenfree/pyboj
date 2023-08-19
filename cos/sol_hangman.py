

def solution(word, question):
    answer = []

    a = list(set(word))
    a.sort()
    cnt = 0

    # print(a)

    for i in question:
        if cnt == len(a):
            answer.append("SUCCESS")
            return answer

        for j in range(0, len(a)):
            # print(i, a[j])
            if i == a[j]:
                answer.append("Yes")
                cnt += 1
                break
        else:
            answer.append("No")
    else:
        if cnt+1 != len(a):
            answer.append("FAIL")
            return answer


if __name__ == "__main__":
    word = "happy"
    question = ["a", "e", "i", "o", "u", "p", "h", "x", "y", "j", "r"]
    # solution(word, question)
    print(solution(word, question))
