import datetime
from project import Project

MENU = "\
- (L)oad projects\n\
- (S)ave projects\n\
- (D)isplay projects\n\
- (F)ilter projects by date\n\
- (A)dd new project\n\
- (U)pdate project\n\
- (Q)uit"
VALID_CHOICES = "LSDFAUQ"
NAME_INDEX = 0
START_DATE_INDEX = 1
PRIORITY_INDEX = 2
COST_ESTIMATE_INDEX = 3
COMPLETION_PERCENTAGE_INDEX = 4


def main():
    print("Welcome to the Project Management Program")
    print(MENU)

    choice = get_valid_choice()
    while choice != "Q":
        if choice == "L":
            projects = load_projects()
        elif choice == "S":
            save_projects(projects)
        elif choice == "D":
            display_projects(projects)
        elif choice == "F":
            filter_projects_by_date(projects)
        elif choice == "A":
            projects = add_new_project(projects)
        elif choice == "U":
            update_project(projects)
            print(MENU)
            choice = get_valid_choice()
    print("Thank you for using custom-built project management software.")

def run_test():
    # projects = load_projects()
    # print(projects)
    # projects = []
    # projects = add_new_project(projects)
    # print(projects)

    # e.g., "30/9/2022"
    date_string = input("Show projects that start after date (dd/mm/yy):")
    date = datetime.datetime.strptime(date_string, "%d/%m/%Y").date()
    print(date)


def get_valid_choice():
    # ask user for choice
    choice = input(">>> ").upper()
    while choice not in VALID_CHOICES:
        print("Invalid choice")
        choice = input(">>> ").upper()

    return choice


def get_valid_project_index(projects):
    # ask user for project index
    project_index = int(input("Project choice: "))
    while project_index < 0 or project_index >= len(projects):
        print("Invalid project number")
        project_index = int(input("Project choice: "))
    return project_index


def get_valid_completion_percentage(minimum, maximum):
    # ask user for completion percentage
    new_completion_percentage = int(input("New Percentage: "))
    while new_completion_percentage < minimum or new_completion_percentage > maximum:
        print("Invalid completion percentage")
        new_completion_percentage = int(input("Completion percentage: "))
    return new_completion_percentage


def load_projects():
    # ask user for filename
    projects = None
    while projects is None:
        filename = input("Filename: ")
        # filename = "projects.txt"
    try:
        infile = open(filename, "r")
        infile.readline()
        projects = []
        for line in infile:
            parts = line.strip().split("\t")
            projects.append(Project(parts[NAME_INDEX], datetime.datetime.strptime(parts[START_DATE_INDEX], "%d/%m/%Y").date(),
                                    int(parts[PRIORITY_INDEX]), float(parts[COST_ESTIMATE_INDEX]), int(parts[COMPLETION_PERCENTAGE_INDEX])))
    except FileNotFoundError:
        print("File not found")
    return projects

def save_projects(projects):
    # ask user for filename
    filename = input("Filename: ")
    # filename = "temp.txt"
    outfile = open(filename, "w")
    outfile.write("name\tstart_date\tpriority\tcost\tcompletion_percentage\n")
    for project in projects:
        outfile.write(
            f"{project.name}\t{project.start_date.strftime('%d/%m/%Y')}\t{project.priority}\t{project.cost}\t{project.completion_percentage}\n")
    outfile.close()


def display_projects(projects):
    incomplete_projects = []
    completed_projects = []
    for project in projects:
        if project.completion_percentage < 100:
            incomplete_projects.append(project)
        else:
            completed_projects.append(project)
    # sort projects by priority
    incomplete_projects.sort()
    print("Incomplete projects:")
    for project in incomplete_projects:
        print("\t", project)
    print("Completed projects:")
    for project in completed_projects:
        print("\t", project)


def get_date_elem(elem):
    return elem.start_date


def add_new_project(projects):
    print("Let's add a new project")
    # get project name
    name = input("Name: ")
    # get start date
    start_date = input("Start date (dd/mm/yyyy): ")
    # get priority
    priority = int(input("Priority: "))
    # get cost estimate
    cost_estimate = float(input("Cost estimate: "))
    # get completion percentage
    completion_percentage = get_valid_completion_percentage(0, 100)
    # add project to list
    projects.append(Project(name, datetime.datetime.strptime(
        start_date, "%d/%m/%Y").date(), priority, cost_estimate, completion_percentage))
    return projects


def update_project(projects):
    for index, project in enumerate(projects):
        print(f"{index} {project}")
    project_index = get_valid_project_index(projects)
    print(projects[project_index])

    # update completion percentage
    new_completion_percentage = get_valid_completion_percentage(0, 100)
    projects[project_index].completion_percentage = new_completion_percentage
    # update priority
    try:
        new_priority = int(input("New Priority: "))
    except ValueError:
        return projects
        projects[project_index].priority = new_priority

        return projects


main()
# run_test()