from random_survival_forest import RandomSurvivalForest


def rsf(features, labels, timeline=range(0, 10, 1), n_estimators=100, n_jobs=-1,  min_leaf=3, unique_deaths=3,
        random_state=None):
    model = RandomSurvivalForest(n_estimators=n_estimators, timeline=timeline, n_jobs=n_jobs, min_leaf=min_leaf,
                                 unique_deaths=unique_deaths, random_state=random_state)
    model.fit(features, labels)
    oob_c = round(model.oob_score, 3)
    return oob_c
