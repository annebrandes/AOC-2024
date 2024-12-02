file = open("../Day-2/Day-2.txt","r")

safe_reports = 0

for report in file:
    report_list = report.split()
    print(report_list)
    
    acceptable_increasing = 0
    acceptable_decreasing = 0

    for i in range(len(report_list)-1):
        if (int(report_list[i+1]) - int(report_list[i]) > 0) and (int(report_list[i+1]) - int(report_list[i]) < 4):
            acceptable_increasing += 1
        if (int(report_list[i]) - int(report_list[i+1]) > 0) and (int(report_list[i]) - int(report_list[i+1]) < 4):
            acceptable_decreasing += 1

    if (acceptable_decreasing == (len(report_list)-1)) or (acceptable_increasing == (len(report_list)-1)):
        safe_reports += 1

print(safe_reports)