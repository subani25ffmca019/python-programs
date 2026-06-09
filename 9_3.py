file_path="example.text"
with open(file_path,"r") as file:
    file.write("this is a addtional lines")
    print("content append to",file_path)
