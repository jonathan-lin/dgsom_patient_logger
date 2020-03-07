from patientlogger_tools import *

excel_file = 'C:\obgyn.xlsx'
sheet_name = 'Gyn'

pt_data = get_pt_data(excel_file, sheet_name)

geckoBrowser = open_browser()
wait_for_load(geckoBrowser, 30)
open_log_encounter_page(geckoBrowser)

for pt in pt_data:
    print(pt)
    form = geckoBrowser.find_element_by_xpath('//form')
    set_specialty(form, pt['specialty'])
    set_date(form, pt['date'])
    set_responsibility(form, pt['responsibility'])
    set_setting(form, pt['setting'])
    set_age(form,pt['age'])
    set_diagnoses(form, pt['diagnoses'])
    set_procedures(form, pt['procedures'])
    set_clinical_skills(form, pt['clinicalskills'])
    check_honor_code(form)
    add_another(form)
    submit(form)

geckoBrowser.quit()
