import pandas as pd
from sklearn.preprocessing import MinMaxScaler
import matplotlib.pyplot as plt
import seaborn as sns

def load_data(file_path):
    """ טוען קובץ CSV ומחזיר DataFrame """
    return pd.read_csv(file_path)

def clean_data(df):
    """ מנקה את הנתונים על ידי הסרת ערכים חסרים וכפילויות """
    df.dropna(how='any', inplace=True)
    df.drop_duplicates(inplace=True)
    return df

def fill_missing_values(df):
    """ ממלא ערכים חסרים בעמודות המספריות והלא מספריות """
    for column in df.columns:
        if df[column].dtype in ['float64', 'int64']:
            df[column].fillna(df[column].mean(), inplace=True)
        else:
            df[column].fillna('Unknown', inplace=True)
    return df

def convert_date_column(df):
    """ ממיר את עמודת התאריך לפורמט נכון """
    df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
    return df

def normalize_data(df):
    """ נורמל את כל העמודות המספריות """
    scaler = MinMaxScaler(feature_range=(0, 1))  # כאן תיקנו את הטווח
    numeric_cols = df.select_dtypes(include=['float64', 'int64']).columns
    df[numeric_cols] = scaler.fit_transform(df[numeric_cols])
    return df

def calculate_metrics(df):
    """ מחשב מטריקות עבור כל עמודה ב-DataFrame """
    metrics = {}
    for column in df.columns:
        if df[column].dtype in ['float64', 'int64']:
            metrics[column] = {
                'ממוצע': df[column].mean(),
                'חציון': df[column].median(),
                'סטיית תקן': df[column].std(),
                'טווח': df[column].max() - df[column].min(),
                'ערכים חסרים': df[column].isnull().sum(),
            }
        else:
            metrics[column] = {
                'ערכים חסרים': df[column].isnull().sum(),
                'ספירת ערכים ייחודיים': df[column].nunique(),
                'ערך נפוץ': df[column].mode()[0] if not df[column].mode().empty else None,
            }
    return metrics

def plot_joint(df, x_column, y_column):
    """ מציג Joint Plot בין שתי עמודות """
    sns.jointplot(x=df[x_column], y=df[y_column], kind='scatter', color='blue')
    plt.title(f'Joint Plot של {x_column} ו-{y_column}')
    plt.show()

def plot_bar(df, x_column, y_column):
    """ מציג Bar Plot עבור עמודה נתונה """
    plt.figure(figsize=(10, 6))
    sns.barplot(x=x_column, y=y_column, data=df, palette='viridis')
    plt.title(f'Bar Plot של {y_column} לפי {x_column}')
    plt.xlabel(x_column)
    plt.ylabel(y_column)
    plt.xticks(rotation=90)  # סיבוב השמות של העמודות אם יש צורך
    plt.show()

def plot_kde(df, column):
    """ מציג KDE Plot עבור עמודה נתונה """
    plt.figure(figsize=(10, 6))
    sns.kdeplot(df[column], fill=True, color='blue')
    plt.title(f'KDE Plot של {column}')
    plt.xlabel(column)
    plt.ylabel('צפיפות')
    plt.show()

def plot_bubble(df, x_column, y_column, size_column):
    """ מציג Bubble Plot """
    plt.figure(figsize=(10, 6))
    plt.scatter(df[x_column], df[y_column], s=df[size_column]*100, alpha=0.5, edgecolors='w', linewidth=0.5)
    plt.title(f'Bubble Plot של {y_column} לפי {x_column}')
    plt.xlabel(x_column)
    plt.ylabel(y_column)
    plt.show()

def plot_pair(df):
    """ מציג Pair Plot עבור כל העמודות המספריות """
    sns.pairplot(df)
    plt.title('Pair Plot של כל העמודות המספריות')
    plt.show()

def main(file_path):
    """ פונקציית עזר מרכזית """
    df2 = load_data(file_path)
    
    print("סוג הנתונים של df2:", type(df2))
    print("שמות השדות:", df2.columns)
    print("סוגי הנתונים של כל שדה:", df2.dtypes)
    print("מספר השורות בקובץ:", len(df2))
    
    df2 = clean_data(df2)
    df2 = fill_missing_values(df2)
    df2 = convert_date_column(df2)
    df2 = normalize_data(df2)
    
    print("חקר נתונים:")
    print(df2.head())
    
    metrics = calculate_metrics(df2)
    print("מטריקות:")
    for column, metric in metrics.items():
        print(f"{column}: {metric}")

    # הוספת הגרפים
    print(" Joint Plot:")
    plot_joint(df2, 'Fatalities', 'Aboard')  # Joint Plot בין Fatalities ל-Aboard

    print(" Bar Plot:")
    plot_bar(df2, 'Operator', 'Fatalities')  # Bar Plot

    print(" KDE Plot:")
    plot_kde(df2, 'Fatalities')  # KDE Plot

    print(" Bubble Plot:")
    plot_bubble(df2, 'Aboard', 'Fatalities', 'Aboard')  # Bubble Plot

    print(" Pair Plot:")
    plot_pair(df2)  # Pair Plot

# הפעל את הפונקציה הראשית
file_path = r"C:\Users\user\Downloads\Airplane_Crashes_and_Fatalities_Since_1908_20190820105639.csv"
main(file_path)

