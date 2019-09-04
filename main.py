from download_helper import login, download_file_by_project
from feature_creator import extract_gene_affected_counts
from label_creator import extract_survival_labels
from surv_analysis import rsf

print("Download SSM file...")
token = ...
df = download_file_by_project(token=token, filetype="simple_somatic_mutation",
                              release=28, project_code="ALL-US", keep_file=False)
print("Extract gene affected features...")
ssm_gene_affected_counts = extract_gene_affected_counts(df)
print("Extract survival labels...")
labels, features = extract_survival_labels(token, ssm_gene_affected_counts)
print("Train Random Survival Forest...")
oob_score = rsf(features, labels, n_estimators=500, random_state=42)
print(oob_score)

