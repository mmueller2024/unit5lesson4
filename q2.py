import pandas as pd
import matplotlib.pyplot as plt

url = "https://en.wikipedia.org/wiki/Wisconsin"
dfs = pd.read_html(
    url,
    match = "Historical population"
)
df = dfs[0]
df = df.iloc[0:-1]
df = df[["Census", "Pop."]].astype("int")
print(df.info())
df.plot(x = "Census", y = "Pop.")
plt.show()