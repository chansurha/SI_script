""" NOTE: "jmp_score.py" file must be in the same directory to perform the predictions"""

""" import generated python codes for prediction from JMP """
import neural_var

""" import library for data analysis """
import pandas as pd

""" read test dataset """
df = pd.read_excel('prediction_set.xlsx')

""" apply the prediction code to the test dataset and append the results"""
df['pred_neural_var'] = df[neural_var.getInputMetadata()].apply(lambda s: neural_var.score(s, {}), axis=1)

""" print the predicitons with the originals"""
prd = df[['Variety','pred_neural_var']]
prd