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
    new_df["about_product"] = new_df["about_product"].str.split("|")
    new_df["actual_price"] = new_df["actual_price"].str.strip("₹").str.replace(",", "").astype(float)
    new_df["category"] = new_df["category"].str.split("|")
    new_df["discounted_price"] = new_df["discounted_price"].str.strip("₹").str.replace(",", "").astype(float)
    new_df["discount_percentage"] = new_df["discount_percentage"].str.strip("%").astype(float)
    new_df["rating_count"] = new_df["rating_count"].str.replace(",", "").astype(int)
    new_df["review_id"] = new_df["review_id"].str.split(",")
    new_df["user_id"] = new_df["user_id"].str.split(",")
    new_df["user_name"] = new_df["user_name"].str.split(",")
    
    # print(new_df["discounted_price"])
    # print(new_df["actual_price"])
    # print(new_df["discount_percentage"])
    # print(new_df["rating_count"])
    # print(new_df["category"])
    # print(new_df["about_product"])
    # print(new_df["user_id"])
    # print(new_df["user_name"])
    # print(new_df["review_id"])

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
    category_li1 = df["category"]
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
    fig.suptitle('Sales analysis of the top ten categories - pie + bar', fontsize = 25)
    ax2.grid(alpha = 0.3)

def calculate_bin_width(num: int) -> None:
    """
    This is a helper function, it calculates
    every possible bin width.
    """

    ans = []
    for divisor in range(100, num):
        if num % divisor == 0:
            ans.append(divisor)
    print(ans)

def same_length_li(li1: list[float], li2: list[float]) -> list[list[float], list[float]]:
    """
    This is a helper function.
    It put two lists togegher, where they have the same length.
    """
    ans = [[], []]
    length = min(len(li1), len(li2))
    for i in range(length):
        ans[0].append(li1[i])
        ans[1].append(li2[i])
    return ans

def price_analysis(filename: str) -> None:
    """
    This function analysis price
    """
    fig, axes = plt.subplots(2, 2, figsize = (18, 10), dpi = 80)
    (ax1, ax2, ax3, ax4) = (axes[0, 0], axes[0, 1], axes[1, 0], axes[1, 1])

    df = read_file(filename)
    actual_price = df["actual_price"].tolist()
    discounted_price = df["discounted_price"].tolist()

    ax1.set_title("Boxplot of Actual Price")
    ax1.boxplot(actual_price)

    """
    as is shown in the boxplot, the reasonable price range
    is around (0, 5000).
    """
    
    """
    scatter: 
    if the dots are below the red line, which means discounted_price < actual price
    if the dots are above the red line, which means discounted_price > actual price
    it shows that some dishonest online retailers even use tricks to avoid offering 
    real discounts in a bid to deceive buyers into thinking they are getting a bargain
    """
    reasonable_price = []
    reasonable_discounted_price = []
    for price in actual_price:
        if price <= 5000:
            reasonable_price.append(price)

    for price in discounted_price:
        if price <= 5000:
            reasonable_discounted_price.append(price)

    price_li = same_length_li(reasonable_price, reasonable_discounted_price)
    reasonable_price = price_li[0]
    reasonable_discounted_price = price_li[1]

    ax2.scatter(reasonable_price, reasonable_discounted_price, label='Discounted Price')
    ax2.plot(reasonable_price, reasonable_price, color='red', label = "Actual Price")

    ax2.set_xlabel('Actual Price (₹)', fontsize = 15)
    ax2.set_ylabel('Discounted Price (₹)', fontsize = 15)
    ax2.set_title('Scatter Plot of Actual vs Discounted Prices')

    ax2.legend(loc = "upper right")

    # d_range = calculate_bin_width(int(max(reasonable_discounted_price) - min(reasonable_discounted_price)))
    # print(d_range)
    d = 451
    d_discounted = 496
    # print(int(max(reasonable_price) - min(reasonable_price)))
    num_bins = int(max(reasonable_price) - min(reasonable_price)) // d
    ax3.set_xticks(range(int(min(reasonable_price)), int(max(reasonable_price)) + d, d))

    num_bins_discounted = int(max(reasonable_discounted_price) - min(reasonable_discounted_price)) // d_discounted
    ax4.set_xticks(range(int(min(reasonable_discounted_price)), int(max(reasonable_discounted_price) + d_discounted), d_discounted))

    ax3.tick_params(labelrotation = 45)
    ax4.tick_params(labelrotation = 45)
    ax3.grid(alpha = 0.3)
    ax4.grid(alpha = 0.3)
    ax3.set_xlabel("Actual Price (₹)", fontsize = 15)
    ax4.set_xlabel("Discounted Price (₹)", fontsize = 15)
    ax3.set_ylabel("Frequency", fontsize =15)
    ax4.set_ylabel("Frequency", fontsize = 15)
    ax3.set_title("Histogram of Actual Price")
    ax4.set_title("Histogram of Discounted Price")
    fig.suptitle('actual & discounted price analysis - box + hist + scatter', fontsize = 25)
    ax3.hist(reasonable_price, int(num_bins), color = "orange")
    ax4.hist(reasonable_discounted_price, int(num_bins_discounted))

def main():
    # test_read = read_file(FILE_NAME)
    # print(test_read)
    # test read_file ends here

    # category distribution
    # pie + bar 
    category_sale_analysis(FILE_NAME)
    plt.savefig("data_analysis_project/project/analysis_results/category_sale_analysis")

    # price analysis
    # hist + box 
    price_analysis(FILE_NAME)
    plt.savefig("data_analysis_project/project/analysis_results/price_analysis")

    plt.show()

if __name__ == "__main__":
    main()