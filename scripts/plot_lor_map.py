import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1 import make_axes_locatable

lors = pd.read_csv(
    "../assets/lors_aggregated.csv", index_col="PLR_id", encoding="utf-8"
)
lors_geo = gpd.read_file("../assets/lor_2021_rewound.geojson", encoding="utf-8")

# Set PLR_id as index for lors_geo
lors_geo = lors_geo[["geometry", "PLR_ID"]]
lors_geo["PLR_ID"] = lors_geo["PLR_ID"].astype(int)
lors_geo = lors_geo.set_index("PLR_ID")
lors_geo.index.name = "PLR_id"

# Enrich Lors_geo with aggregated LOR data
lors_geo = lors_geo.join(lors)
lors = None


fig, ax = plt.subplots(1, 1)

# Map playground area per child
# lors_geo["pl_area_per_child"] = lors_geo["playground_area"] / lors_geo["total_children"]
#
# ax = lors_geo.plot(
#     column="pl_area_per_child",
#     cmap="YlOrRd_r",
#     legend=True,
#     edgecolor='black', linewidth=1,
#     scheme='Quantiles', k=5,
#     missing_kwds={'color': 'grey', 'label': 'No Data'},
#     ax=ax,
# )

# leg = ax.get_legend()
# leg.set_title("Playarea per child [m²]")
# ax.title.set_text("Planungsräume Berlin: Playarea per child")
# plt.axis('off')

# fig.set_size_inches(12, 9)
# fig.tight_layout()
# plt.savefig("../figures/map_pl_area_per_child.svg", bbox_inches='tight')


# Map Playground area relative to total area
lors_geo["playground_percentage"] = lors_geo["playground_area"] * 10 / lors_geo["area_sqm"]

ax = lors_geo.plot(
    column="playground_percentage",
    cmap="Greens",
    legend=True,
    edgecolor='black', linewidth=1,
    scheme='Quantiles', k=5,
    missing_kwds={'color': 'grey', 'label': 'No Data'},
    ax=ax,
)

leg = ax.get_legend()
leg.set_title("Playgroundarea [‰]")
ax.title.set_text("Planungsräume Berlin: playground area relative to total area")
plt.axis('off')


fig.set_size_inches(12, 9)
fig.tight_layout()
plt.savefig("../figures/map_pl_area_permille.svg", bbox_inches='tight')

