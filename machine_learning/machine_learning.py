import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn import preprocessing

from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier
from sklearn.naive_bayes import GaussianNB
from xgboost import XGBClassifier

from sklearn.metrics import f1_score

def ML_prediction(queryset):
    df = pd.DataFrame.from_records(queryset.values())
    #one hot encoding
    area_code_dummies = pd.get_dummies(df["area_code"])
    area_code_dummies = area_code_dummies.add_prefix('area_code_')

    df["voice_mail_plan"].loc[df["voice_mail_plan"] == "no"] = 0
    df["voice_mail_plan"].loc[df["voice_mail_plan"] == "yes"] = 1
    df["voice_mail_plan"] = df["voice_mail_plan"].astype("int64")

    df["international_plan"].loc[df["international_plan"] == "no"] = 0
    df["international_plan"].loc[df["international_plan"] == "yes"] = 1
    df["international_plan"] = df["international_plan"].astype("int64")

    df_final=df.drop(columns=["phone_number", "state", "area_code"])
    df_final = pd.concat([df_final,area_code_dummies], axis=1)

    # apply label encoder for churn since its values are also categories
    le = preprocessing.LabelEncoder()
    y = le.fit_transform(df_final["churn"])
    X = df_final.drop(columns=["churn"])
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    names = [
        "RandomForest",
        "AdaBoost",
        "Naive Bayes",
        "XGBoost"
    ]

    classifiers = [
        RandomForestClassifier(max_depth=5, random_state=42),
        AdaBoostClassifier(random_state=42),
        GaussianNB(),
        XGBClassifier(use_label_encoder=False, eval_metric='mlogloss', seed=0)
    ]

    results_accuracy = dict()
    results_f1 = dict()

    for name, clf in zip(names, classifiers):
        clf.fit(X_train, y_train)
        acc_score = clf.score(X_test, y_test)
        y_pred = clf.predict(X_test)
        f_score = f1_score(y_test, y_pred, average='macro')
        results_accuracy[name] = acc_score
        results_f1[name] = f_score

    return results_accuracy, results_f1