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

def plot(time1, x1, y1, time2, x2, y2):
    # first dataset
    plt.plot(time1, y1, color='green', linestyle='dashed', label= "Kinematics Calculated Result",
         marker='.', markerfacecolor='green')
    
    # second dataset
    plt.plot(time2, y2, label= "GPT Calculated Result", color= "blue", linestyle='dashed', 
                marker= ".")
    
    # x-axis label
    plt.xlabel('Time')
    # y-axis label
    plt.ylabel('Position')
    # plot title
    plt.title('Position over time')
    # showing legend
    plt.legend()
    
    # function to show the plot
    plt.show()

def print_extracted(data):
    for time, x, y in data:
        print(f"Time: {time}, X: {x}, Y: {y}")
    print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")

def extract_from_tuple(data):
    time_arr = []
    x_coords = []
    y_coords = []
    for time, x, y in data:
        time_arr.append(time)
        x_coords.append(x)
        y_coords.append(y)
    return time_arr, x_coords, y_coords

calculated_data = extract("calculated.txt")
gpt_data = extract("gpt_generated.txt")

print_extracted(calculated_data)
print_extracted(gpt_data)

calculated_time, calculated_x, calculated_y = extract_from_tuple(calculated_data)
gpt_time, gpt_x, gpt_y = extract_from_tuple(gpt_data)

plot(calculated_time, calculated_x, calculated_y, gpt_time, gpt_x, gpt_y)
