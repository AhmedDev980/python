# Update a max connections to <some value> in server config file
# 1. Read the file
# 2. Store the data in the file in one variable
# 3. Write the file
# 4. If we came accross max connections update the value as required.

# open is the inbuilt function in python. No need to  install any module.
def update_server_config(file_path, key, value):
  #Read the file
  with open(file_path, "r") as file:
    # Store the data in the file in one variable
    lines = file.readlines()
    
# Write the file
  with open(file_path, "w") as file:
# Go through each line in file If we came accross max connections update the value as required.
    for line in lines:
      if key in line:
        file.write(key + "=" value + "/n")
      else:
        file.write(line)
        
# By giving the values as required it will change the value in file directly
update_server_config("server_config", "max_connections", "500")

