print("===== FINGERPRINT VOTING SYSTEM =====")

registered_voters = ["FP001", "FP002", "FP003", "FP067", "FP099"]
voted_voters = []

while True:
    fingerprint_id = input("\nEnter your Fingerprint ID: ").upper()

    if fingerprint_id not in registered_voters:
        print("Fingerprint not Verified!")
        
        fingerprint_id = input("\nEnter your Fingerprint ID again: ").upper()
        
        if fingerprint_id not in registered_voters:
            print("You are not registered to Vote!")
            break
        
    if fingerprint_id in voted_voters:
        print("You have already Voted!")
        break
        
    print("Fingerprint Verified!")
    print("You can Vote!")
        
    print("\n1. Candidate A")
    print("2. Candidate B")
    print("3. Candidate C")
        
    choice = input("\nEnter your choice: ")
        
    if choice == "1":
        voted_voters.append(fingerprint_id)
        print("You voted for Candidate A.")
            
    elif choice == "2":
        voted_voters.append(fingerprint_id)
        print("You voted for Candidate B.")
            
    elif choice == "3":
        voted_voters.append(fingerprint_id)
        print("You voted for Candidate C.")
            
    else:
        print("Invalid Choice!")
        continue
    
    print("\nVote recorded successfully!")