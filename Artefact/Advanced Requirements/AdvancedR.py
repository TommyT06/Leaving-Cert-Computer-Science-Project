from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error 
import pandas as pd 


# Training the model
data = pd.read_csv('Personal_Dataset.csv')        # Retrieving data from CSV file

#Establishes inputs and outputs
inputs = data[['Workload', 'Exercise_Hours', 'Sleep_Quality']]
output = data['Stress']

# Splits the data into a training and testing dataset
X_train, X_test, Y_train, Y_test = train_test_split(inputs, output, test_size=0.15, random_state=0)

LinearR = LinearRegression()           # Creating Linear Regression model


LinearR.fit(X_train, Y_train)
Y_pred = LinearR.predict(X_test)     
# Fitting the model with the training data 

print("Model Complete!")

mse = mean_squared_error(Y_test, Y_pred)
print(f"Mean Squared Error: {mse}")


def interpret_mse(mse):
    if mse < 5:
        return "Excellent model accuracy"
    elif mse < 10:
        return "Good model accuracy"
    elif mse < 15:
        return "Ok model accuracy"
    else:
        return "Poor model accuracy"


mse_val = interpret_mse(mse)
print("How good is this model? ", mse_val)

# Function to make a prediction with model

def predictStress(Workload,Exercise_Hours,Sleep_Quality):
    data = pd.DataFrame([[Workload,Exercise_Hours,Sleep_Quality]],
                      columns=['Workload','Exercise_Hours','Sleep_Quality'])
    return LinearR.predict(data)[0]

#What If Question 1
print("------------------------------------------------------")
print("What if question 1")
print("Let's test what the stress will be if workload 3, 2 hour of exercise and a 4 sleep quality")

# 3 parameters
workload_1 = 3
exercise_1 = 2
sleep_1 = 4

stress_whatif_1 = predictStress(workload_1, exercise_1, sleep_1)  
print("\n What if Q1 stress level is", stress_whatif_1)



# What If Question 2
print("------------------------------------------------------")
print("What if question 2")
print("Let's test what the stress will be if workload 10, 1 hours of exercsie, 1 sleep quality")

# 3 parameters
workload_2 = 10
exercise_2 = 1
sleep_2 = 1

stress_whatif_2 = predictStress(workload_2, exercise_2, sleep_2)  
print("\n What if Q2 stress level is", stress_whatif_2)

#Graphical Format

variables = ['Stress what if 1', 'Stress what if 2']
values = [stress_whatif_1, stress_whatif_2]

# Creating the bar chart
plt.bar(variables, values)

# Adding labels and title
plt.xlabel('Q1-2')
plt.ylabel('Stress')
plt.title('Bar Chart of WHAT-IF Q1, Q2 Outcomes')

# Show the plot
plt.show()