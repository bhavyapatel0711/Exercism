def round_scores(student_scores: list) -> list:
    """Round all provided student scores.

    :param student_scores: list - of student exam scores.
    :return: list - of rounded student exam scores.
    """
    return [round(score) for score in student_scores]   

def count_failed_students(student_scores: list) -> int:
    """Count the number of failing students out of the group provided.

    :param student_scores: list - of student exam scores.
    :return: int - count of student scores at or below 40.
    """
    return len([score for score in student_scores if score <= 40])

def above_threshold(student_scores: list, threshold: int) -> list:
    """Return a list of student scores that are above the threshold.

    :param student_scores: list - of student exam scores.
    :param threshold: int - the minimum score required to be considered above threshold.
    :return: list - of student exam scores that are above the threshold.
    """
    return [score for score in student_scores if score >= threshold]

def letter_grades(highest: int) -> list:
    """Create a list of grade thresholds based on the provided highest grade.

    :param highest: int - the highest exam score.
    :return: list - of lower threshold scores for each D-A letter grade interval.
    """
    step = (highest - 40) // 4
    return [41 + step*i for i in range(0, 4)] 

def student_ranking(student_scores: list, student_names: list) -> list: 
    """Organize the student's rank, name, and grade information in ascending order.

    :param student_scores: list - of student exam scores.
    :param student_names: list - of student names.
    :return: list - of strings in format ["<rank>. <student name>: <score>"].
    """
    ranked_students = sorted(zip(student_scores, student_names), reverse=True)
    return [f"{rank + 1}. {name}: {score}" for rank, (score, name) in enumerate(ranked_students)]

def perfect_score(student_info: list) -> list:
    """Determine if any student has achieved a perfect score of 100.

    :param student_info: list - of [<student name>, <score>] lists.
    :return: str - name of the first student to achieve a perfect score, or "No perfect score." if there is none.
    """
    for name, score in student_info:
        if score == 100:
            return [name, 100]
    return []