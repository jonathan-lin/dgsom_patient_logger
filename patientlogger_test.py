from patientlogger_tools import *

specialty = 'Ob'
date = '2020-01-01'
responsibility = 'Observed'
setting = 'ER/Urgent Care'
age = 46
diagnoses = ['Abnormal labor', 'Fetal heart rate abnormal','Infection']
procedures = ['Vaginal delivery', 'Basic BLS']
clinicalskills = ['Performed history','Pre-eclampsia labs']

geckoBrowser = open_browser()
wait_for_load(geckoBrowser, 30)
open_log_encounter_page(geckoBrowser)
form = geckoBrowser.find_element_by_xpath('//form')
set_specialty(form, specialty)
set_date(form, date)
set_responsibility(form, responsibility)
set_setting(form, setting)
set_age(form,43)
set_diagnoses(form, diagnoses)
set_procedures(form, procedures)
set_clinical_skills(form, clinicalskills)
check_honor_code(form)
add_another(form)
submit(form)
