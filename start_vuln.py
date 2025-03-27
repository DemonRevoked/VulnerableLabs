#!/usr/bin/env python3
import subprocess
import os

def main():
    # Mapping user input to hidden folder names.
    targets = {
        "1": ".apache",
        "2": ".samba",
        "3": ".tomcat",
        "4": ".joomla",
        "5": ".gitlab",
        "6": ".couchdb"
    }
    
    print("Select the vulnerable target to start:")
    print("1: apache")
    print("2: samba")
    print("3: tomcat")
    print("4: joomla")
    print("5: gitlab")
    print("6: couchdb")
    
    choice = input("Enter choice (1-6): ").strip()
    
    if choice not in targets:
        print("Invalid choice. Please choose a number between 1 and 6.")
        return
    
    target_folder = targets[choice]
    
    # Check if the target folder exists
    if not os.path.isdir(target_folder):
        print(f"Error: Folder '{target_folder}' does not exist. Make sure it is present in the current directory.")
        return
    
    try:
        # Change to the target folder
        os.chdir(target_folder)
        print(f"Changed directory to {target_folder}.")
        
        # Clean up running Docker containers
        print("Cleaning Docker containers ...")
        ps_result = subprocess.run(
            ["sudo", "docker", "ps", "-q"],
            capture_output=True, text=True
        )
        container_ids = ps_result.stdout.strip().splitlines()
        if container_ids:
            print("Removing containers:", container_ids)
            rm_result = subprocess.run(
                ["sudo", "docker", "rm", "-f"] + container_ids,
                capture_output=True, text=True
            )
            print("Cleanup output:")
            print(rm_result.stdout)
            if rm_result.stderr:
                print("Cleanup errors:")
                print(rm_result.stderr)
        else:
            print("No running containers to remove.")
        
        # Start the selected vulnerable target using docker-compose
        print(f"Starting vulnerable target '{target_folder}' ...")
        dc_result = subprocess.run(
            ["sudo", "docker-compose", "up", "-d"],
            capture_output=True, text=True
        )
        if dc_result.returncode == 0:
            print("Docker container started successfully:")
            print(dc_result.stdout)
        else:
            print("Error starting docker container:")
            print(dc_result.stderr)
            
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == '__main__':
    main()
