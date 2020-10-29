from buildings import SingleStoryBuilding
from employees import CertifiedInstaller, CertifiedPendingInstaller, Handyman


class Scheduler:
    def __init__(self):
        pass

    def schedule(self, buildings: list, employees: list) -> dict:
        schedule = dict()
        for weekday in range(5):
            availableEmployees = [employee for employee in employees if employee.isAvailable(weekday)]
            for building in buildings:
                # Check for Certified Employee Requirement
                if not building.isAssigned():
                    availableEmployees = building.assignEmployees(weekday, availableEmployees)

        for building in buildings:
            print(building.uniqueId)
            for employee in building.assignedEmployees:
                print(employee.uniqueId)
                print(employee.schedule)
        return buildings


if __name__ == '__main__':
    testBuildings = list()
    testBuildings.append(SingleStoryBuilding('21 Jump Street'))
    testBuildings.append(SingleStoryBuilding('22 Jump Street'))

    testEmployees = [CertifiedInstaller('John'),
                     CertifiedPendingInstaller('Peter'),
                     CertifiedPendingInstaller('David'),
                     Handyman('Roger'),
                     Handyman('Mateo')]

    scheduler = Scheduler()
    scheduler.schedule(testBuildings, testEmployees)
