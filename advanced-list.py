submitted = ["Alice", "Bob", "Charlie", "David"]
attended = ["Charlie", "Eve", "Alice", "Frank"]

both_submitted_and_attended = set(submitted) & set(attended) #Seeing who submitted and attended class

print("Students who both submitted assignments and attended the class:")
print(both_submitted_and_attended)
  
if submitted == attended:  #Checking to see if the list is identical or not
    print("The are identical")
    
else:
    print("the are not identical")
    
    attended.remove("Frank") #Removing students from attended list who did not submitt 
    print("Did not submitt work", attended)
    
    attended.remove("Eve")
    print("Did not submitt work", attended)