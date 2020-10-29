from __future__ import annotations

import abc


class Employee(abc.ABC):

    def __init__(self, uniqueId):
        self.uniqueId = uniqueId
        self.available = [True for i in range(5)]
        self.schedule = [None for i in range(5)]

    @abc.abstractmethod
    def setTask(self, workingDay: int, building) -> None:
        if self.available[workingDay]:
            self.available[workingDay] = False
            self.schedule[workingDay] = building
        else:
            print(f"{self.uniqueId} already scheduled on {workingDay}")

    @abc.abstractmethod
    def setVacation(self, workingDay: int) -> None:
        self.available[workingDay] = False
        self.schedule[workingDay] = None

    @abc.abstractmethod
    def isAvailable(self, workingDay: int) -> bool:
        return self.available[workingDay]

    def __repr__(self):
        return f"{self.uniqueId}"


class CertifiedInstaller(Employee):

    def __init__(self, uniqueId):
        super().__init__(uniqueId)

    def setTask(self, workingDay: int, building) -> None:
        super(CertifiedInstaller, self).setTask(workingDay, building)

    def setVacation(self, workingDay: int) -> None:
        super(CertifiedInstaller, self).setVacation(workingDay)

    def isAvailable(self, workingDay: int) -> bool:
        return super(CertifiedInstaller, self).isAvailable(workingDay)


class CertifiedPendingInstaller(Employee):

    def __init__(self, uniqueId):
        super().__init__(uniqueId)

    def isAvailable(self, workingDay: int) -> bool:
        return super(CertifiedPendingInstaller, self).isAvailable(workingDay)

    def setTask(self, workingDay: int, building) -> None:
        super(CertifiedPendingInstaller, self).setTask(workingDay, building)

    def setVacation(self, workingDay: int) -> None:
        pass


class Handyman(Employee):

    def __init__(self, uniqueId):
        super().__init__(uniqueId)

    def isAvailable(self, workingDay: int) -> bool:
        return super(Handyman, self).isAvailable(workingDay)

    def setTask(self, workingDay: int, building) -> None:
        super(Handyman, self).setTask(workingDay, building)

    def setVacation(self, workingDay: int) -> None:
        super(Handyman, self).setVacation(workingDay)


if __name__ == '__main__':
    employee = Handyman("something")
    employee.setVacation(0)
    employee.setTask(0, None)
    print(employee.isAvailable(0))
