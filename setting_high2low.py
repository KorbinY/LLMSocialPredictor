#  gpt version of v4 to v4-1106-preview
#  gpt versionn of v3.5-turbo to v3.5-turbo-1106
# for the setting 2 [low2high], mut -> immut
import os
import warnings, random
import pandas as pd
import numpy as np
from tqdm import tqdm
import re
from datetime import datetime

from template import question_codebook, fields_of_interest
from template2 import question_codebook2

from utils.converter import date_convert, timeout, person_convert, find_match_in_sentence, find_match_value, can_positive_int
from utils.editor import get_profile

import openai
with open('mykey', 'r') as k:
    os.environ["OPENAI_API_KEY"] = k.readline()
openai.api_key = os.getenv("OPENAI_API_KEY")

import argparse
parser = argparse.ArgumentParser(description="Gallup Simulation")
parser.add_argument('--person', type=int, default=1, choices=[1, 2], help='First=1 or Second=2 person; for prompt and dialogue settings.')
parser.add_argument('--year', action='store_false', help='Add YEAR into the prompts.')
parser.add_argument('--show_prompt', action='store_true', help='Show prompts in process.')
parser.add_argument('--temperature', type=float, default=0.7, help='temperature for GPT models.')
parser.add_argument('--api', type=str, default="3.5", choices=["3.5", "4"], help='API version of GPT. Options in (3.5) or (4). Default 3.5-turbo')
parser.add_argument('--truncate', type=int, default=-1,  help='if truncate the subset, -1 (default) = full subset, positive number = min(number, full)')
parser.add_argument('--output_dir', type=str, default="./Output", help='dir to save output files')

args = parser.parse_args()

api_name = {'3.5':"gpt-3.5-turbo-1106", '4':"gpt-4-1106-preview"}[args.api]

xcols = ['WP1219', 'age', 'WP1223', 'WP3117', 'EMP_2010', 'INCOME_1', 'WP14']
ycols = ['WP16056', 'WP27', 'WP10248', 'WP148', 'M30', 'WP108', 'WP109', 'WP110', 'WP150']
ycols2 = ['WP16056', 'WP10248', 'WP148', 'WP108', 'WP150']
mutable = [['WP16056'], ['WP27', 'WP10248'], ['WP148', 'M30'], ['WP108', 'WP109', 'WP110'], ['WP150']]

subset = pd.read_csv('./data/GallupWoldPoll_USA_year_clean.csv')

@timeout(15) ## temp=0.7
def get_response(profile, question, temperature = 0.7, max_tokens = 2):
    completion = openai.ChatCompletion.create(
        model=api_name,
        messages=[
            {"role": "system", "content": profile},
            {"role": "user", "content": question},
        ],
        temperature = temperature,
        max_tokens = max_tokens
    )
    predict = completion.choices[0].message['content']
    return predict


if not os.path.exists(args.output_dir):
    os.mkdir(args.output_dir)
#@@@@@@@@ PREDICTION STEP 
for output in xcols:
    filedir = '{}/Output-setting2-t{}-In-{}-Out-{}-p{}-v{}.csv'.format(args.output_dir, args.temperature, 'MUTABLE', output, args.person, args.api)
    print('Working on {}->{} ......'.format('MUTABLE', output))
    if not os.path.exists(filedir):
        subset_tmp = subset.copy()
        if args.truncate>0:
            subset_tmp = subset_tmp.sample(min(len(subset_tmp), int(args.truncate)))
        r_var = 'PREDICT_' + output

        if not r_var in subset_tmp.columns:
            subset_tmp.insert(subset_tmp.shape[1], r_var, 0)
    else:
        r_var = 'PREDICT_' + output
        subset_tmp = pd.read_csv(filedir)

    for i in tqdm(subset_tmp.index):
        if subset_tmp.loc[i, r_var] in [0, -1, '0', '-1']:
            item = subset_tmp.loc[i, ]
            profile = get_profile(item, fields_of_interest, ycols)
            # envs setting
            if args.person == 1:
                system_tmp = 'You are a bot completing self-description of human, making the self-description consistent.'
                if isinstance(question_codebook2[output]['vals'], dict):
                    system_tmp += ' Output format: one option label number in {}.'.format(str(question_codebook2[output]['vals']))
                elif output != 'INCOME_1':
                    system_tmp += ' Output format: a positive integer value.'
                else:
                    system_tmp += ' Output format: "$ + a positive integer value."'
                question_tmp = profile + question_codebook2[output]['question']
            elif args.person == 2:
                system_tmp = 'Assuming your identification is as below, please answer questions based on {} profile. '.format('this')

                question_tmp = question_codebook[output]['question']
                question_tmp = re.findall('\"(.*)\"', question_tmp)[0]
                question_tmp = person_convert(profile) + question_tmp

                if isinstance(question_codebook2[output]['vals'], dict):
                    question_tmp += ' Output format: one option label number in {}.'.format(str(question_codebook2[output]['vals']))
                elif output != 'INCOME_1':
                    question_tmp += ' Output format: a positive integer value. Directly give the number without other explanations.'
                else:
                    question_tmp += ' Output format: "$ + a positive integer value". Directly give the number without other explanations.'
            else:
                break

            if args.year:
                system_tmp = 'Assume today is {}. '.format(item['interview_date2']) + system_tmp
            if args.show_prompt:
                print('==ROLE== ', system_tmp)
                print('==QUES== ', question_tmp)

            predict = '-1'
            if isinstance(question_codebook2[output]['vals'], dict):
                count = 0 
                while count < 5:
                    count += 1
                    try:
                        if (int(predict) not in list(question_codebook2[output]['vals'].keys())): 
                            try:
                                predict = get_response(system_tmp, question_tmp, temperature = args.temperature, max_tokens = 5)
                                print(predict,'+')
                                predict = find_match_value(predict)
                            except:
                                predict = '-1'
                    except:
                        predict = '-1'
                    print(predict,'*')
                    if int(predict) in list(question_codebook2[output]['vals'].keys()):
                        break
            else:
                count = 0
                while count<5:
                    count += 1
                    if not can_positive_int(predict):
                        try:
                            predict = get_response(system_tmp, question_tmp, temperature = args.temperature, max_tokens = 50)
                            print(predict,'#')
                            predict = find_match_value(predict)
                            print(predict,'%')
                        except:
                            predict = '-1'
                    else:
                        break

            subset_tmp.loc[i, r_var] = predict

            subset_tmp.to_csv(filedir, header=True, index=True)