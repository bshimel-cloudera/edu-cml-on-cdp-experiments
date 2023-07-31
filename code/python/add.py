import sys
import mlflow

mlflow.set_experiment("Add It Up")
mlflow.start_run()

params = [int(number) for number in sys.argv[1:]]
count = len(params)  
total = sum(params)
    
with open("result.txt", "w") as output_file:
    output_file.write(f"Input: {params},")
    output_file.write(f"Count: {count},")
    output_file.write(f"Sum: {total}\n")
    output_file.close()

mlflow.log_param("Input", params)
mlflow.log_metric("Count", count)
mlflow.log_metric("Sum", total)

mlflow.log_artifact("result.txt")

print ("Sum of the numbers is: %i." % total)

mlflow.end_run()
