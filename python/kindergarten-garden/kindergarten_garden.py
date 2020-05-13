defaultStudents = ["Alice","Bob","Charlie","David",
    "Eve","Fred","Ginny","Harriet",
    "Ileana","Joseph","Kincaid","Larry"]

plantNames = {"V" : "Violets",
    "R" : "Radishes",
    "C" : "Clover",
    "G" : "Grass"}

class Garden:
    def __init__(self, diagram, students = defaultStudents):
        self.diagram = [row for row in diagram.split('\n')]
        self.students = {}
        i = 1

        for x in sorted(students):
            self.students[x] = [i,i+1]
            i += 2

    def plants(self, student):
        selectedPlants = []

        selectedPlants.append(self.diagram[0][(self.students[student][0]-1)])
        selectedPlants.append(self.diagram[0][(self.students[student][1]-1)])
        selectedPlants.append(self.diagram[1][(self.students[student][0]-1)])
        selectedPlants.append(self.diagram[1][(self.students[student][1]-1)])

        return [plantNames[x] for x in selectedPlants]

Garden("VCRRGVRG\nRVGCCGCV", students=["Samantha", "Patricia", "Xander", "Roger"])
Garden("VCRRGVRG\nRVGCCGCV")