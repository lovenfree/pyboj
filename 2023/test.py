

def solution(phrase):
    i = 0
    for x in phrase:
        x = x.replace(" ", "")
        print(x)

        answer[i] = (len(x)*100)
        i += 1
    return answer


if __name__ == "__main__":
    a = ["Enjoy your life", "I LOVE YOU", "Just try"]
    answer = solution(a)
    print(answer)
