import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns
import plotly


# ヒートマップ
df = pd.DataFrame()
plt.figure(figsize=(12, 10))
ax = sns.heatmap(
    df,
    cmap=sns.color_palette('coolwarm', 10),
    annot=True,
    fmt='.2f',
    vmin=-1,
    vmax=1,
    annot_kws={"size": 15})
plt.tick_params(labelsize=15)
cbar = ax.collections[0].colorbar
cbar.ax.tick_params(labelsize=15)
plt.tight_layout()

# パレート図
fig, ax1 = plt.subplots(figsize=(14, 6))
data_num = len(df)

ax1.bar(range(data_num), df["counts"], color="#1E90FF")
ax1.set_xticks(range(data_num))
ax1.set_xticklabels(df["label"].tolist(), rotation=70)
ax1.set_xlabel("category ids", fontsize=15)
ax1.set_ylabel("counts", fontsize=15)

ax2 = ax1.twinx()
ax2.plot(range(data_num), df["accum_percent"], c="r", marker="o")
ax2.set_ylim([0, 100])
ax2.set_ylabel("cumulative ratio", fontsize=15)
ax1.tick_params(labelsize=15)
ax2.tick_params(labelsize=15)
# ax1.set_title("PARETO_CHART", fontsize=15)
plt.tight_layout()
plt.grid(axis='y')
