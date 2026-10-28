
'''
{
"Math": {"s1": 85, "s2": 92, "s3": 87},
"English": {"s1": 78, "s2": 88, "s3": 80}
}
'''



marks = {
"s1": {"Math": 85, "English": 78},
"s2": {"Math": 92, "English": 88},
"s3": {"Math": 87, "English": 80}
}


def group_subjects(marks):
    result_dict={}
    stu_mark_dict = {}
    for stu, sub_mark in marks.items():
        for sub,mark in sub_mark.items():
            stu_mark_dict[stu]=mark
            if sub not in result_dict:
                result_dict[sub]=stu_mark_dict
                stu_mark_dict = {}
            else:
                current_dict=result_dict[sub]
                current_dict[stu]=mark
                result_dict[sub]=current_dict

    return result_dict

print(group_subjects(marks))


