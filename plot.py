import matplotlib.pyplot as plt

def extract(filename):
    data = []

    with open(filename, "r") as f:
        lines = f.readlines()

    for line in lines:
        # remove parentheses and split string into three parts
        parts = line.strip("()\n").split(", ")
        
        # convert parts to floats
        parts = tuple(map(float, parts))
        
        # add tuple to data list
        data.append(parts)
    
    return data

def plot():
    # x-axis values
    x = [1,2,3,4,5,6,7,8,9,10]
    # y-axis values
    y = [2,4,5,7,6,8,9,11,12,12]
    
    # plotting points as a scatter plot
    plt.scatter(x, y, label= "stars", color= "green", 
                marker= "*", s=30)
    
    # x-axis label
    plt.xlabel('x - axis')
    # frequency label
    plt.ylabel('y - axis')
    # plot title
    plt.title('My scatter plot!')
    # showing legend
    plt.legend()
    
    # function to show the plot
    plt.show()

calculated_data = extract("calculated.txt")
gpt_data = extract("gpt_generated.txt")

for time, x, y in calculated_data:
    print(f"Time: {time}, X: {x}, Y: {y}")

print("======================")
for time, x, y in gpt_data:
    print(f"Time: {time}, X: {x}, Y: {y}")