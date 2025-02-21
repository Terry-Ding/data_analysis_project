import pandas as pd
from matplotlib import pyplot as plt
FILE_NAME = "data_analysis_project/project/csv_file/project/amazon.csv"

def read_file(filename: str):
    """
    This function reads a csv file and 
    returns a clean, non-null value DataFrame.
    """

    original_df = pd.read_csv(filename)
    new_df = original_df.copy()
    # print(new_df[:].isnull().sum()) 
    # rating count is null, fillna 0
    new_df["rating_count"] = new_df["rating_count"].fillna("0")
    # print("*" * 50)
    # print("total null values: ", end = "")
    # print((new_df[:].isnull().sum()).sum())
    new_df = new_df.drop_duplicates()
    # print("total duplicated values: ", end = "")
    # print(new_df.duplicated().sum())
    new_df["discounted_price"] = new_df["discounted_price"].str.strip("₹").str.replace(",", "").astype(float)
    new_df["actual_price"] = new_df["actual_price"].str.strip("₹").str.replace(",", "").astype(float)
    new_df["discount_percentage"] = new_df["discount_percentage"].str.strip("%").astype(float)
    new_df["rating_count"] = new_df["rating_count"].str.replace(",", "").astype(int)
    # print(new_df["discounted_price"])
    # print(new_df["actual_price"])
    # print(new_df["discount_percentage"])
    # print(new_df["rating_count"])

    return new_df

def descending_sort(li: list[int]) -> list[int]:
    """
    This function uses bubble sort to sort a list in
    descending order.
    """

    for i in range(len(li)):
        for j in range(len(li) - i - 1):
            if li[j] < li[j + 1]:
                temp = li[j + 1]
                li[j + 1] = li[j]
                li[j] = temp
    return li

def category_sale_analysis(filename: str) -> None:
    """
    This function analysis sales of different categories.
    """

    df = read_file(filename)
    category_li1 = df["category"].str.split("|").tolist()
    category_li2 = []
    for i in category_li1:
        for j in i:
            category_li2.append(j.lower().strip())
    
    category_dict = {}
    for items in category_li2:
        if items not in category_dict:
            category_dict[items] = 1
        else:
            category_dict[items] += 1

    count = []
    for key in category_dict:
        count.append(category_dict[key])
    count = descending_sort(count)
    top_ten_count = count[:10]
    top_ten_dict = {}
    for key in category_dict:
        if category_dict[key] in top_ten_count:
            top_ten_dict[key] = category_dict[key]
    
    labels = []
    sizes = []
    mycolor = ["#1f77b4", "#ff7f0e", "#2ca02c", 
               "#d62728", "#9467bd", "#8c564b", "#e377c2", "#7f7f7f", "#bcbd22", "#17becf"]
    for (category, count) in top_ten_dict.items():
        labels.append(category)
        sizes.append(count)
    myexplode = []
    for i in labels:
        if i != "electronics":
            myexplode.append(0)
        else :
            myexplode.append(0.2)
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize = (18, 10), dpi = 80)
    ax1.pie(sizes, colors = mycolor, autopct='%1.0f%%', shadow = True, 
            explode = myexplode, startangle = 220)
    ax1.legend(labels, ncol = 2, loc = (-0.3, 1))
    ax2.barh(labels, sizes, color = mycolor)
    fig.suptitle('Sales analysis of the top ten categories', fontsize = 25)
    plt.grid(alpha = 0.3)
    plt.show()

def main():
    # test_read = read_file(FILE_NAME)
    # print(test_read)
    category_sale_analysis(FILE_NAME)

if __name__ == "__main__":
    main()