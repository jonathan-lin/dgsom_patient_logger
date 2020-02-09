from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
import time

from patientloggerconstants import responsibilities, settings, pt_ages, complaints, diagnoses, procedures, skills

data = [
    {
        'specialty_name': 'GS - Clinical prob.',
        'date': '2020-02-05',
        'responsibility': 1,
        'settings': 0,
        'age': 27,
        'gender': 'f',
        'complaints': [8],
        'diagnoses': [7],
        'procedures': [],
        'skills': [2, 3, 4, 5, 6]
    }
]

browser = webdriver.Firefox(executable_path=r'C:\geckodriver\geckodriver.exe')
browser.get("https://gryphon.medsch.ucla.edu")

WebDriverWait(browser, 30).until(EC.presence_of_element_located((By.ID, "bookmark-page")))
print('done')
browser.get("https://gryphon.medsch.ucla.edu/clerkship")
WebDriverWait(browser, 30).until(EC.presence_of_element_located((By.ID, "bookmark-page")))
browser.find_element_by_link_text('Log Encounter').click()
WebDriverWait(browser, 30).until(EC.presence_of_element_located((By.ID, "bookmark-page")))

for pt in data:
    print(pt)
    # Select specialty
    specialty = Select(browser.find_element_by_id('specialty_id'))
    specialty.select_by_visible_text(pt['specialty_name'])

    # Set encounter date
    date = browser.find_element_by_id('encounter_date')
    for i in range(10):
        date.send_keys(Keys.BACK_SPACE)
    date.send_keys(pt['date'])
    time.sleep(1)
    date.send_keys(Keys.ESCAPE)
    time.sleep(1)

    # Set responsibility
    responsibility = Select(browser.find_element_by_id('responsibility_id'))
    responsibility.select_by_visible_text(responsibilities[pt['responsibility']])

    # Set settings
    setting = Select(browser.find_element_by_id('setting_id'))
    setting.select_by_visible_text(settings[pt['settings']])

    # Set patient age
    # TODO: Add support for patients < 1 yr
    ptage = Select(browser.find_element_by_id('agerange'))
    age = pt['age']
    index = 0;
    if age > 80:
        index = 11
    elif age >= 71:
        index = 10
    elif age >= 61:
        index = 8
    elif age >= 51:
        index = 6
    elif age >= 41:
        index = 5
    elif age >= 31:
        index = 4
    elif age >= 21:
        index = 3
    elif age >= 12:
        index = 2
    elif age >= 6:
        index = 7
    elif age >= 1:
        index = 0
    ptage.select_by_visible_text(pt_ages[index])

    # Set patient gender
    gender = pt['gender']
    if gender == 'f':
        browser.find_element_by_id('gender_2').click()
    elif gender == 'm':
        browser.find_element_by_id('gender_1').click()
    elif gender == 't':
        browser.find_element_by_id('gender_3').click()

    # Set patient complaints
    complaints_table = browser.find_elements_by_css_selector("table.complaints")
    for i in range(len(complaints_table)):
        if complaints_table[i].is_displayed():
            index = i
    complaints_table = complaints_table[i].find_element_by_tag_name("tbody")
    complaint_fields = complaints_table.find_elements_by_tag_name('tr')
    for i in complaint_fields:
        checkbox = i.find_element_by_tag_name('input')
        complaint_name = i.find_element_by_tag_name('label')
        complaint_text = complaint_name.text
        for j in pt['complaints']:
            # print(j)
            # print(complaints[pt['specialty_name']][j])
            if complaint_text == complaints[pt['specialty_name']][j]:
                checkbox.click()

    # Set patient diagnoses
    diagnoses_table = browser.find_elements_by_css_selector("table.diagnosis")
    for i in range(len(diagnoses_table)):
        if diagnoses_table[i].is_displayed():
            index = i
    diagnoses_table = diagnoses_table[index].find_element_by_tag_name("tbody")
    diagnoses_fields = diagnoses_table.find_elements_by_tag_name('tr')
    # print(len(diagnoses_fields))
    for i in diagnoses_fields:
        checkbox = i.find_element_by_tag_name('input')
        diagnosis = i.find_element_by_tag_name('label')
        diagnoses_text = diagnosis.text
        for j in pt['diagnoses']:
            if diagnoses_text == diagnoses[pt['specialty_name']][j]:
                checkbox.click()

    # Set patient procedures
    procedures_table = browser.find_elements_by_css_selector("table.procedures")
    for i in range(len(procedures_table)):
        if procedures_table[i].is_displayed():
            index = i
    procedures_table = procedures_table[index].find_element_by_tag_name("tbody")
    procedures_fields = procedures_table.find_elements_by_tag_name('tr')
    # print(len(procedures_fields))
    for i in procedures_fields:
        checkbox = i.find_element_by_tag_name('input')
        procedure = i.find_element_by_tag_name('label')
        procedure_text = procedure.text
        for j in pt['procedures']:
            if procedure_text == procedures[pt['specialty_name']][j]:
                checkbox.click()

    # Set skills used
    # TODO: Add support for interpreting imaging/lab results
    skills_table = browser.find_elements_by_css_selector("table.clinical-skills")
    for i in range(len(skills_table)):
        if skills_table[i].is_displayed():
            index = i
    skills_table = skills_table[index].find_element_by_tag_name("tbody")
    skills_fields = skills_table.find_elements_by_tag_name('tr')
    print(len(skills_fields))
    for i in skills_fields:
        checkbox = i.find_element_by_tag_name('input')
        skill = i.find_element_by_tag_name('label')
        skills_text = skill.text
        for j in pt['skills']:
            if skills_text == skills[pt['specialty_name']][j]:
                checkbox.click()

    # Check the honor code box
    browser.find_element_by_id('honor_code').click()

    # Choose to log another encounter
    specialty = Select(browser.find_element_by_id('post_action'))
    specialty.select_by_visible_text('Add another entry')

    # Submit
    submit_button = browser.find_element_by_css_selector("input.pull-right")
    submit_button.click()

    # Wait for the submit button to appear again so you know you have made it through the auto-forward page
    WebDriverWait(browser, 30).until(EC.presence_of_element_located((By.CSS_SELECTOR, "input.pull-right")))

browser.close()
