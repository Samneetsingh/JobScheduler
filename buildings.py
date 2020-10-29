import abc

from employees import CertifiedInstaller


class Building(abc.ABC):

    def __init__(self, uniqueId):
        self.uniqueId = uniqueId
        self.assignedEmployees = []
        self.assigned = False

    @abc.abstractmethod
    def assignEmployees(self, day: int, availableEmployees: list) -> list:
        pass

    @abc.abstractmethod
    def isAssigned(self):
        return self.assigned


class SingleStoryBuilding(Building):

    def __init__(self, uniqueId):
        super(SingleStoryBuilding, self).__init__(uniqueId)
        self.requiredCertifiedInstalled = 1

    def assignEmployees(self, day: int, availableEmployees: list) -> list:
        availableCertifiedInstaller = [employee for employee in availableEmployees if
                                       isinstance(employee, CertifiedInstaller)]
        if len(availableCertifiedInstaller) >= self.requiredCertifiedInstalled:
            certifiedInstaller = availableCertifiedInstaller[0]
            certifiedInstaller.setTask(day, self)
            self.assignedEmployees.append(certifiedInstaller)
            availableEmployees.remove(certifiedInstaller)
            self.assigned = True

        return availableEmployees

    def isAssigned(self):
        return super(SingleStoryBuilding, self).isAssigned()


class DoubleStoryBuilding(Building):

    def __init__(self, uniqueId):
        super(DoubleStoryBuilding, self).__init__(uniqueId)

    def assignEmployees(self, day: int, availableEmployees: list) -> list:
        pass

    def isAssigned(self):
        return super(DoubleStoryBuilding, self).isAssigned()


class CommercialBuilding(Building):

    def __init__(self, uniqueId):
        super(CommercialBuilding, self).__init__(uniqueId)

    def assignEmployees(self, day: int, availableEmployees: list) -> list:
        pass

    def isAssigned(self):
        return super(CommercialBuilding, self).isAssigned()
