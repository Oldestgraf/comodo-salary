import matplotlib.pyplot as plt
import pandas as pd

salary_values = [100, 54, 46, 80, 0, 80, 80, 80, 80, 80, 85, 95, 73, 77, 100, 100, 0]

quantity_of_months = len(salary_values)

def comodo_debt():
    sum_of_expected_percent = quantity_of_months * 100
    sum_of_actual_percent = 0
    for i in salary_values:
        sum_of_actual_percent += i
    debt = sum_of_expected_percent - sum_of_actual_percent
    return debt

date = pd.date_range(start="2022-12-01", freq="ME", periods=quantity_of_months)
plt.plot(
  date,
  salary_values,
  label=f"Actual salary (Current debt: {comodo_debt()}%)",
  linestyle="--",
  color="#FF5733",
  linewidth=2,
  marker="D",
)

plt.ylim(0, 150)
plt.xlabel("Month", fontsize="small", color="midnightblue")
plt.ylabel("Percent", fontsize="small", color="midnightblue")
plt.title("Comodo salary", fontsize=15)
plt.legend()
plt.grid()
plt.show()
