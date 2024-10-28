import pandas as pd
import seaborn as sns
import numpy as np
import warnings
import matplotlib.pyplot as plt
from scipy import stats

warnings.filterwarnings("ignore")

#Let's take a look at the crimes dataset
##print(df.info()) We only know what weapon was used in around 75% of cases
##print(df.describe()) The investigation time is relatively equally distributed
#df['Evidence Found'] = df['Evidence Found'].str.title()

def plot_weapon_perpetrator(df):
    df = pd.read_csv('Crimes_Dataset.csv')
    df.duplicated().sum()
    df = df.drop_duplicates()
    df = df.dropna()
    df['Monster involved'] = df['Monster involved'].str.title()
    plt.figure(figsize=(12, 6))
    sns.countplot(x='Monster involved', data=df, hue=(df['Crime Weapon'] == 'knife'))
    plt.title('Knife used as a weapon by different monsters')
    plt.xlabel('Perpetrator')
    plt.ylabel('Number of Cases')
    plt.xticks(rotation=45)  # Rotate x-axis labels for readability if needed
    plt.legend(title='Crime Weapon', labels=['Other', 'knife'])
    plt.show()
#The ghost seems to use the knife a bit more than the others, but the distribution is fairly uniform and doesn't provide us with any hints.
#25% of cases have an unidentified weapon though, maybe we should investigate which monster commits most of the crimes where the weapon is unidentified?

df = pd.read_csv('Crimes_Dataset.csv')
plot_weapon_perpetrator(df)

#insert code that does this


def plot_evidence_monster(df):
    df = pd.read_csv('Crimes_Dataset.csv')
    df.duplicated().sum()
    df = df.drop_duplicates()
    df = df.dropna()
    plt.figure(figsize=(12, 6))
    sns.countplot(x='Monster involved', data=df, hue=(df['Evidence Found'] == 'bones'))
    plt.title('Bones found at the crimescene by perpetrator')
    plt.xlabel('Perpetrator')
    plt.ylabel('Number of Cases')
    plt.xticks(rotation=45)  # Rotate x-axis labels for readability if needed
    plt.legend(title='Evidence Found', labels=['Other', 'bones'])
    plt.show()
#There were bones found on site, which potentially excludes the Vampire and Ghost as no bones were ever found on murder cases perpetrated by them.
#Furthermore, the skeleton seems like a likely suspect


#let's turn to the suspects' dataset
#We know the crime was committed in broad daylight, so we could quickly exclude any suspects with sunlight allergies

def plot_suspects_sun_allergy(df):
    plt.figure(figsize=(12, 6))
    sns.countplot(x='Monster', data=df, hue=(df['Allergy'] == 'sunlight'))
    plt.title('Sunlight allergy')
    plt.xlabel('Monster')
    plt.ylabel('Sunlight allergy')
    plt.xticks(rotation=45)  # Rotate x-axis labels for readability if needed
    plt.legend(title='Allergy', labels=['Other', 'sunlight'])
    plt.show()
df = pd.read_csv('Suspects_Dataset.csv')
plot_suspects_sun_allergy(df)
"""
#...yeah, that didn't help at all
#Okay, let's see who likes killing in the village
"""""
def plot_suspects_height(df):
    df = pd.read_csv('Suspects_Dataset.csv')
    df.duplicated().sum()
    df = df.drop_duplicates()
    df = df.dropna()
    sns.swarmplot(x='Monster', y='Height in cm', data=df)
    plt.title('Height of Monsters')
    plt.show()



#df['Crime Weapon'] = df['Crime Weapon'].replace('N/A', 'Unknown weapon')
#print(df.head(15))
