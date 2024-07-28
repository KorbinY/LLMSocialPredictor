import pandas as pd

def get_profile(item, fields_of_interest, cols, context = None):
    profile = ''
    for var in cols:
        template_val, template = item[var], fields_of_interest[var]["template"]
        if (not pd.isna(template_val)) and (len(str(template_val).strip())>0):
            if isinstance(fields_of_interest[var]['vals'], dict) and (template_val.lower() in fields_of_interest[var]['vals'].keys()):
                template_val = fields_of_interest[var]['vals'][template_val.lower()]
            temp = template.replace( "XXX", str(template_val )) + ' '
            profile += temp
    # if context:
    #     for var in context:
    #         template_val, template = context_codebook[var]["vals"][item[var]], context_codebook[var]["template"]
    #         temp = template.replace( "XXX", str(template_val ))
    #         profile += temp+' '
    if not "USA" in profile:
        profile = 'I am a person in the USA. ' + profile
    return profile