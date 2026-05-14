import pandas as pd

df = pd.read_excel('events_data.xlsx')

P_A = df[df['Event'] == 'Alarm sounded (A)']['Probability'].values[0]
P_B = df[df['Event'] == 'Burglary occurred (B)']['Probability'].values[0]
P_E = df[df['Event'] == 'Earthquake occurred (E)']['Probability'].values[0]
P_D_given_A = df[df['Event'] == 'David calls Harry (D|A)']['Probability'].values[0]
P_S_given_A = df[df['Event'] == 'Sophia calls Harry (S|A)']['Probability'].values[0]
P_not_B = df[df['Event'] == 'No Burglary (¬B)']['Probability'].values[0]
P_not_E = df[df['Event'] == 'No Earthquake (¬E)']['Probability'].values[0]

P_A_and_not_B_and_not_E = P_A * P_not_B * P_not_E

P_D_and_S_given_A = P_D_given_A * P_S_given_A

final_probability = P_A_and_not_B_and_not_E * P_D_and_S_given_A

print(
    f"The probability is: {final_probability:.4f}"
)
