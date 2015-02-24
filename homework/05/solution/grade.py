def removeMin(scores):
    min = scores[0]
    for score in scores:
        if score < min:
            min = score
    scores.remove(min)
    return scores


def add(scores):
    res = 0
    for score in scores:
        res = res + score
    return res

def grade(quiz,homework,project,exam):
    quizTotal = add(removeMin(removeMin(quiz)))
    homeworkTotal = add(removeMin(removeMin(homework)))
    passingScore = quizTotal + exam
    score = quizTotal + homeworkTotal + project + exam
    maxPassingScore = 650
    maxScore = 1700
    # print [passingScore,maxPassingScore,score,maxScore]
    if (score < 0.6 * maxScore) or (passingScore < 0.6 * maxPassingScore):
        return "R"
    elif score >= 0.9 * maxScore:
        return "A"
    elif score >= 0.8 * maxScore:
        return "B"
    elif score >= 0.7 * maxScore:
        return "C"
    else:
        return "D"

def forecast(quiz,homework,project,exam):
    quizTotal = add(removeMin(removeMin(quiz)))
    homeworkTotal = add(removeMin(removeMin(homework)))
    passingScore = quizTotal
    score = quizTotal + homeworkTotal
    maxPassingScore = len(quiz) * 50
    maxScore = maxPassingScore + len(homework) * 100
    # score
    if project != -1:
         score = score + project
         maxScore = maxScore + 250
    if exam != -1:
        passingScore = passingScore + exam
        score = score + exam
        maxPassingScore = maxPassingScore + 250
        maxScore = maxScore + 250
    # grade
    # print [passingScore,maxPassingScore,score,maxScore]
    if (score < 0.6 * maxScore) or (passingScore < 0.6 * maxPassingScore):
        return "R"
    elif score >= 0.9 * maxScore:
        return "A"
    elif score >= 0.8 * maxScore:
        return "B"
    elif score >= 0.7 * maxScore:
        return "C"
    else:
        return "D"