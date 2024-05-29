import matplotlib.pyplot as plt
import pandas as pd

date = pd.date_range(start="2023-01-01", freq="M", periods=16)
plt.plot(
  date,
  [100, 54, 46, 80, 0, 80, 80, 80, 80, 80, 85, 95, 72, 27, 149, 50],
  label="Actual salary",
  linestyle="--",
  color="#FF5733",
  linewidth=2,
  marker="D",
)

plt.ylim(0, 200)
plt.xlabel("Date", fontsize="small", color="midnightblue")
plt.ylabel("Percent", fontsize="small", color="midnightblue")
plt.title("Comodo salary", fontsize=15)
plt.legend()
plt.grid()
plt.show()