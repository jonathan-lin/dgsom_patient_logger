def specialty(pt, browser):
    if pt['specialty_name'] == 'Ob':
        browser.find_element_by_id('specialty_14').click()
    elif pt['specialty_name'] == 'Gyn':
        browser.find_element_by_id('specialty_15').click()


def ptage(pt):
    age = pt['age']
    if age > 50:
        return 3
    elif age > 40:
        return 2
    elif age > 18:
        return 1
    elif age > 11:
        return 0


pt_ages = ['12-18',  # 0
           '19-40',  # 1
           '41-50',  # 2
           'Over 50',  # 3
           ]

settings = ['ER/Urgent Care',
            'Labor and Delivery',
            'OR',
            'Outpatient',
            'Urgent Care'
            ]
