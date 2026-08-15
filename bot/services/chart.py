import io
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt


def create_chart(times: list, temps: list, city_name: str):

    plt.figure(figsize=(10, 5))
    plt.plot(times, temps, marker = "o", color = "#DF0F0F" , linewidth = 2)
    plt.title(city_name)
    plt.xlabel("Время")
    plt.ylabel("Температура (°C)")
    plt.grid(True, linestyle = "--", alpha = 0.5)
    plt.xticks(rotation = 45)

    buf = io.BytesIO()
    plt.savefig(buf, format = "png", bbox_inches = "tight")
    buf.seek(0)
    plt.close()

    return buf 