#Input:
values = [10, 20, 30, 40, 50, 60, 70]
k = 3

#Expected Output:
#[20.0, 30.0, 40.0, 50.0, 60.0]

def moving_average(values, k):
    result_list=[]
    for i in range(len(values)-k+1):
        avg = round((values[i]+values[i+1]+values[i+2])/3,1)
        result_list.append(avg)

    return result_list


print(moving_average(values,k))