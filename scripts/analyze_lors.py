import pandas as pd

lors = pd.read_csv(
    "../assets/lors_aggregated.csv", index_col="PLR_id", encoding="utf-8"
)

lors["pl_area_per_child"] = lors["playground_area"] / lors["total_children"]

corr_pov_pl_area = lors['poverty'].corr(lors['pl_area_per_child'])
print("Correlation Poverty/Playgroundarea: ", corr_pov_pl_area)

print("First quartile is: ", lors["pl_area_per_child"].quantile(0.25))
print("Third quartile is: ", lors["pl_area_per_child"].quantile(0.75))