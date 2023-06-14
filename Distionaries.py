# student_score={} #empty_Distionary
# student_score["Harry"]=81
# student_score["Ron"]=78
# student_score["Hermione"]=99
# student_score["Draco"]=74
# student_score["Neville"]=62
# #print(student_score)
# student_grade={}
# for key in student_score:
#     score = student_score[key]
#     if score > 90:
#         student_grade[key]="outstanding"
#     elif score > 80:
#         student_grade[key]="Exceed Exception"
#     elif score >70:
#         student_grade[key]="Accepteable"
#     else:
#         student_score[key]="Fail"
#
# print(student_grade)
from click import clear

travel_log=[
    {
        "country":"France",
        "cites_visited":["parise","lille","Dijon"],
        "total_vist":12
    },
    {
        "country":"germany",
        "cities_visite":["Berulin","Hambun","Stuttgart"],
        "total_vist":5
    }
]
def add_element(country,cities_visite,total_vist):
    new_distionaries={}
    new_distionaries["country"]=country
    new_distionaries["cities_visite"]=cities_visite
    new_distionaries["total_vist"]=total_vist
    travel_log.append(new_distionaries)


add_element("Russia",["Moscow","saint petersub"],2)
# travel_log.append({
#     "country":"Russia",
#     "cities_visite":["Moscow","saint petersub"],
#     "total_vist":2
# })
print(travel_log)


clear()