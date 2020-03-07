from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
import time
import re
import xlrd
import datetime

def open_browser():
    browser = webdriver.Firefox(executable_path=r'C:\geckodriver\geckodriver.exe')
    browser.get("https://gryphon.medsch.ucla.edu")
    return browser


def get_pt_data(loc, sheet_name):
    wb = xlrd.open_workbook(loc)
    sheet = wb.sheet_by_name(sheet_name)
    row_count = len(sheet._cell_values)
    column_count = len(sheet._cell_values[0])-2
    counter = 0
    setting = []
    diagnoses = []
    procedures = []
    clinicalskills = []
    while counter < row_count:
        if sheet.cell_value(counter,0) == 'Setting':
            setting.append(counter)
        if sheet.cell_value(counter,0) == 'Diagnoses':
            setting.append(counter-1)
            diagnoses.append(counter)
        if sheet.cell_value(counter,0) == 'Procedures':
            diagnoses.append(counter-1)
            procedures.append(counter)
        if sheet.cell_value(counter,0) == 'Clinical Skills':
            procedures.append(counter-1)
            clinicalskills.append(counter)
            clinicalskills.append(row_count-1)
        counter = counter + 1
    pt_list = []
    for i in range(column_count):
        pt = {}
        pt['specialty'] = sheet.cell_value(0,i+2)
        pt['date'] = str(datetime.datetime(*xlrd.xldate_as_tuple(sheet.cell_value(1,i+2), wb.datemode))).split()[0]
        for j in range(3):
            if sheet.cell_value(j+2,i+2) != '':
                pt['responsibility'] = sheet.cell_value(j+2,1)

        pt['age'] = sheet.cell_value(5,i+2)
        pt['specialty'] = sheet.cell_value(0, i + 2)
        for j in range(setting[0],setting[1]+1):
            if sheet.cell_value(j,i+2) != '':
                pt['setting'] = sheet.cell_value(j,1)

        diagnosis_list = []
        for j in range(diagnoses[0],diagnoses[1]+1):
            if sheet.cell_value(j,i+2) != '':
                diagnosis_list.append(sheet.cell_value(j,1))
        pt['diagnoses'] = diagnosis_list

        procedures_list = []
        for j in range(procedures[0],procedures[1]+1):
            if sheet.cell_value(j,i+2) != '':
                procedures_list.append(sheet.cell_value(j,1))
        pt['procedures'] = procedures_list

        clinicalskills_list = []
        for j in range(clinicalskills[0],clinicalskills[1]+1):
            if sheet.cell_value(j,i+2) != '':
                clinicalskills_list.append(sheet.cell_value(j,1))
        pt['clinicalskills'] = clinicalskills_list
        pt_list.append(pt)
    del wb
    return pt_list


def wait_for_load(browser, duration):
    WebDriverWait(browser, duration).until(EC.presence_of_element_located((By.ID, "bookmark-page")))


def open_log_encounter_page(browser):
    browser.get("https://gryphon.medsch.ucla.edu/clerkship")
    wait_for_load(browser, 30)
    browser.find_element_by_link_text('Log Encounter').click()
    wait_for_load(browser, 30)


def set_specialty(form, name):
    specialty_container = form.find_element_by_id('specialty-field-container')
    inputs = specialty_container.find_elements_by_xpath('//input')
    for i in inputs:
        labels = i.find_elements_by_xpath('../label')
        if len(labels)>0:
            if labels[0].text == name:
                i.click()


def set_date(form, date):
    date_field = form.find_element_by_id('encounter_date')
    for i in range(10):
        date_field.send_keys(Keys.BACK_SPACE)
        time.sleep(.1)
    time.sleep(1)
    date_field.send_keys(date)
    time.sleep(1)
    date_field.send_keys(Keys.ESCAPE)
    time.sleep(1)


def set_responsibility(form, responsibility):
    responsibilities = Select(form.find_element_by_id('responsibility_id'))
    responsibilities.select_by_visible_text(responsibility)


def set_setting(form, setting):
    settings = Select(form.find_element_by_id('setting_id'))
    settings.select_by_visible_text(setting)


def set_age(form, age):
    age_dropdown = form.find_element_by_id('agerange')
    age_selector = Select(age_dropdown)
    age_ranges = age_dropdown.find_elements_by_xpath('option')
    age_ranges_list = []
    for i in range(1,len(age_ranges)):
        values = re.findall('\d+',age_ranges[i].text)
        if len(values) > 1:
            age_ranges_list.append([int(values[0]), int(values[1])])
        else:
            if 'over' in age_ranges[i].text.lower():
                age_ranges_list.append([int(values[0])+1,200])
    for i in range(len(age_ranges_list)):
        if age_ranges_list[i][0] <= age <= age_ranges_list[i][1]:
            age_selector.select_by_index(i+1)


def set_diagnoses(form, diagnoses):
    diagnoses_table = form.find_elements_by_css_selector("table.diagnosis")
    for i in range(len(diagnoses_table)):
        if diagnoses_table[i].is_displayed():
            index = i
            break
    diagnoses_table = diagnoses_table[index].find_element_by_tag_name("tbody")
    diagnoses_fields = diagnoses_table.find_elements_by_tag_name('tr')
    for i in diagnoses_fields:
        try:
            checkbox = i.find_element_by_tag_name('input')
            diagnosis = i.find_element_by_tag_name('label')
            diagnoses_text = diagnosis.text
            print(diagnoses_text)
            for j in diagnoses:
                if diagnoses_text.lower() == j.lower():
                    checkbox.click()
        except:
            print('That\'s weird...')


def set_procedures(form,procedures):
    procedures_table = form.find_elements_by_css_selector("table.procedures")
    for i in range(len(procedures_table)):
        if procedures_table[i].is_displayed():
            index = i
            break
    procedures_table = procedures_table[index].find_element_by_tag_name("tbody")
    procedures_fields = procedures_table.find_elements_by_tag_name('tr')
    # print(len(procedures_fields))
    for i in procedures_fields:
        try:
            checkbox = i.find_element_by_tag_name('input')
            procedure = i.find_element_by_tag_name('label')
            procedure_text = procedure.text
            for j in procedures:
                if procedure_text.lower() == j.lower():
                    checkbox.click()
        except:
            print('That\'s weird...')


def set_clinical_skills(form, clinicalskills):
    skills_table = form.find_elements_by_css_selector("table.clinical-skills")
    for i in range(len(skills_table)):
        if skills_table[i].is_displayed():
            index = i
            break
    skills_table = skills_table[index].find_element_by_tag_name("tbody")
    skills_fields = skills_table.find_elements_by_tag_name('tr')
    print(len(skills_fields))
    for i in skills_fields:
        try:
            checkbox = i.find_element_by_tag_name('input')
            skill = i.find_element_by_tag_name('label')
            skills_text = skill.text
            for j in clinicalskills:
                if skills_text.lower() == j.lower():
                    checkbox.click()
        except:
            print('That\'s weird...')


def check_honor_code(form):
    form.find_element_by_id('honor_code').click()


def add_another(form):
    specialty = Select(form.find_element_by_id('post_action'))
    specialty.select_by_visible_text('Add another entry')


def submit(form):
    submit_button = form.find_element_by_css_selector("input.pull-right")
    submit_button.click()
    WebDriverWait(form, 30).until(EC.presence_of_element_located((By.CSS_SELECTOR, "input.pull-right")))
