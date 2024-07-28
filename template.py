fields_of_interest = { 
    # Immutable Vars
    # gender
    'WP1219': { "template":"I am a XXX in the USA.",  "vals": lambda x: str(x).lower(), 'desc':'Gender'},
    # age
    'age': { "template":"I am XXX years old.", "vals": lambda x: str(x).lower(), 'desc':'Age'},
    # Marital status
    # 'WP1223': { "template":"My current marital status is XXX.", "vals":{ 1:"Single/Never been married", 2:"Married", 3:"Separated", 4:"Divorced", 5:"Widowed", 8:"Domestic partner"}, 'desc':'Marital Status'},     
     'WP1223': { "template":"My current marital status is XXX.", "vals": lambda x: str(x).lower(), 'desc':'Marital Status'},     
    # education
    'WP3117': { "template":"My highest completed level of education is XXX.", "vals": lambda x: str(x).lower(), 'desc':'Education Level'},
    # Employment 
    'EMP_2010': { "template":"My current employment status is XXX.", "vals":lambda x: str(x).lower(), 'desc':'Employment Status'},
    # Income
    'INCOME_1': { "template":"My Annual Household Income is $ XXX.", "vals":lambda x: str(x).lower(), 'desc':'Annual Household Income'},
    # Urban/Rural
    'WP14': { "template":"I am from XXX.", "vals":lambda x: str(x).lower(), 'desc':'Urbanity'}, 

    # Mutable Vars
    'WP109': { 'desc':'Civic Engagement 2', 'vals': {'yes':"have", 'no':"have not"}, 'template': 'I XXX volunteered my time to an organization in the  past month.', },
    'WP110': { 'desc':'Civic Engagement 3', 'vals': {'yes':"have", 'no':"have not"}, 'template': 'I XXX helped a stranger or someone I did not know who needed help in the past month.', },
    'WP16056': { 'desc':'Internet Use', 'vals': {'yes':"have", 'no':"have no"}, 'template': 'I XXX access to the internet on a mobile phone, a computer, or some other device.', },
    ## nre context vars
    # Social Life Index
    'WP27': { 'desc':'Social Support', 'vals': {"yes":"have", "no":"do not have"}, 'template': 'If I was in trouble, I XXX relatives or friends I can count on to help me whenever I need them.', },
    # Economic Confidence Index
    'WP148': { 'desc':'Economic Confidence', 'vals': {"better":"better", "worse":"worse"}, 'template': 'Right now, I think that economic conditions in this country are getting XXX.', },
    # Civic Engagement Index
    'WP108': { 'desc':'Civic Engagement', 'vals': {"yes":"have", "no":"have not"}, 'template': 'I XXX donated money to a charity in the past month.', },
    # Approval of leadership // with and without date/ 
    'WP150': { 'desc':'Leadership', 'vals': {"approve":"approve", "disapprove":"disapprove"}, 'template': 'I XXX of the job performance of the leadership of this country.', },
    # Social Life Index 2
    'WP10248': {'vals': {"satisfied":"satisfied", "dissatisfied":"dissatisfied"}, 'template': 'In the city or area where I live, I am XXX with the opportunities to meet people and make friends.', },
    # Economic Confidence  2
    ### M30
    'M30': {'vals': {"excellent": "excellent", "good": "good", "fair": "fair", "poor": "poor"}, 'template': 'I rate my economic conditions in this country today  as XXX.', },
}


question_codebook = {    #question book with person 1 / 2; 
    # Communication Use Index
    'WP16056': { 'desc':'Internet Use', 'vals': {1:"yes", 2:"no"}, 'question': 'When I\'m asked "Do you have access to the internet in any way, whether on a mobile phone, a computer, or some other device?", my answer is ', },
    # Social Life Index
    'WP27': { 'desc':'Social Support', 'vals': {1:"yes", 2:"no"}, 'question': 'When I\'m asked  "If you were in trouble, do you have relatives or friends you can count on to help you whenever you need them, or not?", my answer is ', },
    # Economic Confidence Index
    'WP148': { 'desc':'Economic Confidence', 'vals': {1:"better", 2:"worse"}, 'question': 'When I\'m asked  "Right now, do you think that economic conditions in this country, as a whole, are getting better or getting worse?", my answer is ', },
    # Civic Engagement Index
    'WP108': { 'desc':'Civic Engagement', 'vals': {1:"yes", 2:"no"}, 'question': 'When I\'m asked  "Have you donated money to a charity in the past month?", my answer is ', },
    # Approval of leadership // with and without date/ 
    'WP150': { 'desc':'Leadership', 'vals': {1:"approve", 2:"disapprove"}, 'question': 'When I\'m asked  "Do you approve or disapprove of the job performance of the leadership of this country?", my answer is ', },
    #==========
        # Social Life Index 2
    'WP10248': {'vals': {1:"satisfied", 2:"dissatisfied"}, 'desc':'Social Support 2', 'question': 'When I\'m asked  "In the city or area where you live, are you satisfied or dissatisfied with the opportunities to meet people and make friends?", my answer is ', },
        # Economic Confidence  2
        ### M30
    'M30': {'vals': {1:"excellent", 2:"good", 3:"fair", 4:"poor"}, 'desc':'Economic Confidence 2 (4-classes)', 'question': 'When I\'m asked  "How would you rate your economic conditions in this country today – as excellent, good, fair, or poor?", my answer is ', },
        # Civic Engagement Index 2
    'WP109': {'vals': {1:"yes", 2:"no"}, 'desc':'Civic Engagement 2', 'question': 'When I\'m asked  "Have you volunteered your time to an organization in the past month?", my answer is ', },
        # Civic Engagement Index 3
    'WP110': {'vals': {1:"yes", 2:"no"}, 'desc':'Civic Engagement 3', 'question': 'When I\'m asked  "Have you helped a stranger or someone you did not know who needed help?", my answer is ', },
    ## ===
    # Immutable Vars
    # gender
    'WP1219': { "question":'When I\'m asked "What is your gender?", my answer is ', "vals":{ 1:"man", 2:"woman"}, },
    # age
    'age': { "question":'When I\'m asked "What is your age?", my answer is ', "vals": lambda x: x, },
    # Marital status
    'WP1223': { "question":'When I\'m asked "What is your current marital status?", my answer is ', "vals":{ 1:"Unmarried", 2:"Married", }, },     
    # education
    'WP3117': { "question":'When I\'m asked "What is your highest completed level of education status?", my answer is ', "vals": { 1:"lower level", 2:"middle level", 3:"higher level",}, },
    # Employment 
    'EMP_2010': { "question":'When I\'m asked "What is your current employment status?", my answer is ', "vals": { 1:"Employed", 2:"Unemployed", 3:"Out of the Workforce",}, },
    # Income
    'INCOME_1': { "question":'When I\'m asked "What is your Annual Household Income (in $ US dollar, not conditions rating)?", my answer is ', "vals":lambda x: x, },
    # Urban/Rural
    'WP14': { "question":'When I\'m asked "Where are you from, urban (large city including the suburb) or rural (town, village, or farm)?", my answer is ', "vals":{ 1:"urban", 2:"rural"}, }, }