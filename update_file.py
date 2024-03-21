from rich import *

def update():
    import AutoUpdate
    import os
    import git
    import shutil
    import time

    
    cwd = os.getcwd()
    print(cwd)
    AutoUpdate.set_url("https://raw.githubusercontent.com/Pytholearn/test/main/version")
    download_link = "https://github.com/Pytholearn/test.git"
    AutoUpdate.set_current_version("1.1.2")

    if not AutoUpdate.is_up_to_date():
        print("""
                                [blue]   _  __          [/blue] [cyan]  __  _____     __     __      __ [/cyan]
                                [blue]  / |/ /__ _    __[/blue] [cyan] / / / / _ \___/ /__ _/ /____ / / [/cyan]
                                [blue] /    / -_) |/|/ /[/blue] [cyan]/ /_/ / ___/ _  / _ `/ __/ -_)_/  [/cyan]
                                [blue]/_/|_/\__/|__,__/ [/blue] [cyan]\____/_/   \_,_/\_,_/\__/\__(_)   [/cyan]
                                                    
""")
        print("Would you like to update your tool?")
        choice = input("If you like(Y) or you dont want to update (N)[>>>] ")
        if choice == "Y" or choice == "y":
        
            import git

            local_repo_path = os.path.join(cwd, "temp_repo")
            if not os.path.exists(local_repo_path):
                os.makedirs(local_repo_path)
            git.Repo.clone_from(download_link, local_repo_path)

            
            
            for root, dirs, files in os.walk(local_repo_path):
                relative_path = os.path.relpath(root, local_repo_path)
                for file in files:
                    source_file_path = os.path.join(root, file)
                    dest_file_path = os.path.join(cwd, relative_path, file)
                    if os.path.exists(dest_file_path):
                        os.remove(dest_file_path)  
                    shutil.move(source_file_path, dest_file_path)  
                for dir in dirs:
                    source_dir_path = os.path.join(root, dir)
                    dest_dir_path = os.path.join(cwd, relative_path, dir)
                    if not os.path.exists(dest_dir_path):
                        shutil.move(source_dir_path, dest_dir_path) 
            
            
            shutil.rmtree(local_repo_path)
            print("[green]Update Complete![/green]")
            time.sleep(2)
        elif choice == "n" or choice == "N":
            pass
    else:
        print("[red]Update Not Found![/red]")
        time.sleep(2)
