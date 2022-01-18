from .models import Account
import pandas as pd

def income():
    df = pd.DataFrame(Account.objects.all().values())
    return df[df['credit'] == False]['amount'].sum()

def expense():
    df = pd.DataFrame(Account.objects.all().values())
    return df[df['credit'] == True]['amount'].sum()


