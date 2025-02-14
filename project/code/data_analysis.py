import pandas as pd
from matplotlib import pyplot as plt

def read_file(file_name: str):
    df = pd.read_csv(file_name)
    new_df = df.dropna().drop_duplicates()
    return new_df

def sort_li(li: list[int]) -> list[int]:
    for i in range(len(li)):
        for j in range(len(li) - i - 1):
            if li[j] > li[j + 1]:
                temp = li[j + 1]
                li[j + 1] = li[j]
                li[j] = temp
    return li

def director_percentage_pie(file_name: str) -> None:
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize = (12, 8))

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

    count = []
    for person in director_dict:
        count.append(director_dict[person])

    sorted_count = sort_li(count)
    count = sorted_count[-10:]
    
    top_ten = []
    for person in director_dict:
        if director_dict[person] in count:
            if len(top_ten) == 10:
                break
            top_ten.append(person)

    last_names = []
    for i in top_ten:
        last_names.append(i.split(" ")[1])

    # bar
    ax1.bar(top_ten, count)
    ax1.set_title("directors count")
    ax1.set_xticks(top_ten, labels = last_names, rotation = 45)
    ax1.set_yticks(range(min(count), max(count) + 1, 2))
    
    # pie
    ax2.pie(count, labels=last_names)
    ax2.set_title("Director Percentage Pie")

    plt.show()
    
director_percentage_pie("data_analysis_project/project/src/large_data.csv")