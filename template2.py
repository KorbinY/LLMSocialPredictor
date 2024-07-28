question_codebook2 = { 
    # Immutable Vars
    # gender
    'WP1219': { "question":'My gender is ', "vals":{ 1:"man", 2:"woman"}, },
    # age
    'age': { "question":'My age is ", my answer is ', "vals": lambda x: x, },
    # Marital status
    'WP1223': { "question":'My current marital status is ', "vals":{ 1:"Unmarried", 2:"Married", }, },     
    # education
    'WP3117': { "question":'My highest completed level of education status is ', "vals": { 1:"lower level", 2:"middle level", 3:"higher level",}, },
    # Employment 
    'EMP_2010': { "question":'My current employment status is ', "vals": { 1:"Employed", 2:"Unemployed", 3:"Out of the Workforce",}, },
    # Income
    'INCOME_1': { "question":'My Annual Household Income (in $ US dollar, not conditions rating) is ', "vals":lambda x: x, },
    # Urban/Rural
    'WP14': { "question":'Among urban (large city including the suburb) and rural (town, village, or farm), I am from ', "vals":{ 1:"urban", 2:"rural"}, }, 
    }