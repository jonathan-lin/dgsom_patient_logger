responsibilities = ['Observed',
                    'Actively participated in patient care',
                    'Didactics']
settings = ['Clinic',
            'ER',
            'Hospital Wards',
            'OR']
pt_ages = ['1-5',  # 0
           '1-6 months',  # 1
           '12-20',  # 2
           '21-30',  # 3
           '31-40',  # 4
           '41-50',  # 5
           '51-60',  # 6
           '6-11',  # 7
           '61-70',  # 8
           '7-11 months',  # 9
           '71-80',  # 10
           '80+',  # 11
           'Newborn'  # 12
           ]

complaints = {
    'Emergency Medicine': ['Abdominal pain',  # 0
                           'Acid-base disturbance',  # 1
                           'Breast lump',  # 2
                           'Fluid and electrolyte disturbance',  # 3
                           'Multisystem trauma',  # 4
                           'Rectal bleeding',  # 5
                           'Rectal pain/discomfort',  # 6
                           'Varicose veins',  # 7
                           'Other complaint'],  # 8
    'GS - Periop. care': ['Abdominal pain',  # 0
                          'Acid-base disturbance',  # 1
                          'Breast lump',  # 2
                          'Fluid and electrolyte disturbance',  # 3
                          'Multisystem trauma',  # 4
                          'Rectal bleeding',  # 5
                          'Rectal pain/discomfort',  # 6
                          'Varicose veins',  # 7
                          'Other complaint'],  # 8
    'Orthopaedics': ['Abdominal pain',  # 0
                     'Acid-base disturbance',  # 1
                     'Breast lump',  # 2
                     'Fluid and electrolyte disturbance',  # 3
                     'Multisystem trauma',  # 4
                     'Rectal bleeding',  # 5
                     'Rectal pain/discomfort',  # 6
                     'Varicose veins',  # 7
                     'Other complaint'],  # 8
    'GS - Clinical prob.': ['Abdominal pain',  # 0
                            'Acid-base disturbance',  # 1
                            'Breast lump',  # 2
                            'Fluid and electrolyte disturbance',  # 3
                            'Multisystem trauma',  # 4
                            'Rectal bleeding',  # 5
                            'Rectal pain/discomfort',  # 6
                            'Varicose veins',  # 7
                            'Other complaint'],  # 8
}

diagnoses = {
    'Emergency Medicine': ['Abdominal pain',  # 0
                           'Chest pain',  # 1
                           'IV placement',  # 2
                           'Laceration',  # 3
                           'Orthopedic injury',  # 4
                           'Shortness of breath',  # 5
                           'Trauma resuscitation',  # 6
                           'Other diagnosis'  # 7
                           ],
    'GS - Periop. care': ['Fluids and electrolytes',  # 0
                          'Informed consent',  # 1
                          'Postoperative care',  # 2
                          'Preop eval',  # 3
                          'Wound/Intestinal stoma management',  # 4
                          'Other diagnosis'  # 5
                          ],
    'GS - Clinical prob.': ['Appendicitis',  # 0
                            'Biliary/Pancreatic disease',  # 1
                            'Bowel obstruction',  # 2
                            'Colorectal/Anorectal disease',  # 3
                            'Esophageal/Gastric disease',  # 4
                            'Hernias',  # 5
                            'Surgical infections',  # 6
                            'Thyroid and PARTHY disease',  # 7
                            'Trauma (blunt/penetrating)',  # 8
                            'Other diagnosis'  # 9
                            ],
    'Orthopaedics': ['Arthritis',  # 0
                     'Dislocations',  # 1
                     'Fractures',  # 2
                     'Ligament and tendon injuries',  # 3
                     'Ortho emgcy - compartment syndrome',  # 4
                     'Ortho emgcy - joint infection',  # 5
                     'Ortho emgcy - open fractures',  # 6
                     'Osteoporosis',  # 7
                     'Other diagnosis'  # 8
                     ]
}

procedures = {'Emergency Medicine': ['Basic BLS',
                                     'Drawing venous blood',
                                     'Starting an IV',
                                     'Suturing',
                                     'Other Procedure'
                                     ],
              'GS - Periop. care': ['Basic BLS',
                                    'Drawing venous blood',
                                    'Starting an IV',
                                    'Suturing',
                                    'Other Procedure'
                                    ],
              'GS - Clinical prob.': ['Basic BLS',
                                      'Drawing venous blood',
                                      'Starting an IV',
                                      'Suturing',
                                      'Other Procedure'
                                      ],
              'Orthopaedics': ['Basic BLS',
                               'Drawing venous blood',
                               'Starting an IV',
                               'Suturing',
                               'Other Procedure'
                               ]
              }

skills = {'Emergency Medicine': ['Observed surgery',  # 0
                                 'Assisted surgery',
                                 'Performed history',  # 2
                                 'Performed Clinical Exam',
                                 'Developed differential diagnosis',  # 4
                                 'Wrote patient note',
                                 'Performed oral patient presentation',  # 6
                                 'Incorporated literature into clinical decision-making',
                                 'Wrote orders',  # 8
                                 'Provided education to patient and/or family',
                                 'Interacted on patient care with at least one member of the inter-professional team (RN, case manager, physical therapist, pharmacist, social worker, nutritionist)',
                                 'Participated in a family meeting',  # 11
                                 'Performed a patient hand-off',
                                 'Obtained informed consent',  # 13
                                 'None'  # 14
                                 ],
          'GS - Periop. care': ['Observed surgery',  # 0
                                'Assisted surgery',
                                'Performed history',  # 2
                                'Performed Clinical Exam',
                                'Developed differential diagnosis',  # 4
                                'Wrote patient note',
                                'Performed oral patient presentation',  # 6
                                'Incorporated literature into clinical decision-making',
                                'Wrote orders',  # 8
                                'Provided education to patient and/or family',
                                'Interacted on patient care with at least one member of the inter-professional team (RN, case manager, physical therapist, pharmacist, social worker, nutritionist)',
                                'Participated in a family meeting',  # 11
                                'Performed a patient hand-off',
                                'Obtained informed consent',  # 13
                                'None'  # 14
                                ],
          'GS - Clinical prob.': ['Observed surgery',  # 0
                                  'Assisted surgery',
                                  'Performed history',  # 2
                                  'Performed Clinical Exam',
                                  'Developed differential diagnosis',  # 4
                                  'Wrote patient note',
                                  'Performed oral patient presentation',  # 6
                                  'Incorporated literature into clinical decision-making',
                                  'Wrote orders',  # 8
                                  'Provided education to patient and/or family',
                                  'Interacted on patient care with at least one member of the inter-professional team (RN, case manager, physical therapist, pharmacist, social worker, nutritionist)',
                                  'Participated in a family meeting',  # 11
                                  'Performed a patient hand-off',
                                  'Obtained informed consent',  # 13
                                  'None'  # 14
                                  ],
          'Orthopaedics': ['Observed surgery',  # 0
                           'Assisted surgery',
                           'Performed history',  # 2
                           'Performed Clinical Exam',
                           'Developed differential diagnosis',  # 4
                           'Wrote patient note',
                           'Performed oral patient presentation',  # 6
                           'Incorporated literature into clinical decision-making',
                           'Wrote orders',  # 8
                           'Provided education to patient and/or family',
                           'Interacted on patient care with at least one member of the inter-professional team (RN, case manager, physical therapist, pharmacist, social worker, nutritionist)',
                           'Participated in a family meeting',  # 11
                           'Performed a patient hand-off',
                           'Obtained informed consent',  # 13
                           'None'  # 14
                           ]
          }
