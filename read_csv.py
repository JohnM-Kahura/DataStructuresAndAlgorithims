# print("Enter the Student Major : ")
# major=input("Enter The Student Major: ")
# gpa=input("Enter The Student GPA: ")
major="bal"
gpa='3.5'
with open('GPAList.csv',"r") as q, open('GraduationDatesList.csv','r') as g,open('StudentMajorsList.csv','r') as s:
    gpa_list=q.read().split("\n")
    graduation_dates_list=g.read().split("\n")
    student_majors_list=s.read().split("\n")
    all_majors=[]
    # major list
    for student_details in student_majors_list:
        student_detail=student_details.split(',')
        studentIDs=student_detail[0]
        last_names=student_detail[1]
        first_names=student_detail[2]
        majors=student_detail[3]
        all_majors.append(majors)
        displinary_actions=student_detail[4]
        print(majors[0])
        
    for graduation_details in graduation_dates_list:
        graduation_detail=graduation_details.split(',')
        studentIDs=graduation_detail[0]        
        graduation_date=graduation_detail[1]
    for gpa_details in gpa_list:
        gpa_detail=gpa_details.split(',')
        studentIDs= gpa_detail[0]           
        gpas= gpa_detail[1]  
    print(all_majors) 
    if major not in all_majors:
        print("No Such Student")


        
        
