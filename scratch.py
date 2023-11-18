# from scipy.stats import norm

# # find the area under std normal curve
# # to the **left** given a z score

# # with z = 1
# print(f"{norm.cdf(1):.3f}")
# # output: 0.841

# # with z = 0.25
# print(f"{norm.cdf(0.25):.3f}")
# # 0.599

# # with z = -0.45
# print(f"{norm.cdf(-0.45):.3f}")
# # 0.326


from sklearn import datasets

cancer_dataset = datasets.load_breast_cancer()
print(
    f"Data shape -> {cancer_dataset.data.shape} - "
    f"target shape -> {cancer_dataset.target.shape}"
)
