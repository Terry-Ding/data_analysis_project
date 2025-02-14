import pandas as pd
from matplotlib import pyplot as plt
# fig = plt.figure(figsize=(12, 6), dpi = 80)

def read_file(file_name: str):
    df = pd.read_csv(file_name)
    new_df = df.dropna().drop_duplicates()
    return new_df

def director_percentage_pie(file_name: str) -> None:
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize = (12, 6))

    df = read_file(file_name)
    director_name = []
    directors = df["director"].tolist()
    for p in directors:
        director_name.extend(p.split(":"))

    director_dict = {}
    for key in director_name:
        if key not in director_dict:
            director_dict[key] = 1
        else:
            director_dict[key] += 1

    name = []
    count = []
    for key in director_dict:
        name.append(key)
        count.append(director_dict[key])

    ax1.plot(name, count)
    ax1.set_xticklabels(name, rotation=45)
    ax1.set_title("Director Count Plot")

    ax2.pie(count, labels=name)
    ax2.set_title("Director Percentage Pie")

    plt.show()

director_percentage_pie("data_analysis_project/project/src/large_data.csv")