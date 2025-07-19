import random
import matplotlib.pyplot as plot
import csv

class results:
    def __init__(self):
        self.rounds = []
        self.coops = []
        self.betrays = []
        self.coopd = []
        self.betrayd = []
        self.round = 0
        self._coops = 0
        self._betrays = 0
        self._coopd = 0
        self._betrayd = 0
    def log(self, decision, ai_decision):
        self.round += 1
        if decision == 1:
            self._coops += 1
        elif decision == 2:
            self._betrays += 1

        if ai_decision == 1:
            self._coopd += 1
        elif ai_decision == 2:
            self._betrayd += 1

        self.rounds.append(self.round)
        self.coops.append(self._coops)
        self.betrays.append(self._betrays)
        self.coopd.append(self._coopd)
        self.betrayd.append(self._betrayd)
    def graph(self, filename="dilemma_plot.png"):
        plot.plot(self.rounds, self.coops, label="You Cooperated")
        plot.plot(self.rounds, self.betrays, label="You Betrayed")
        plot.plot(self.rounds, self.coopd, label="AI Cooperated")
        plot.plot(self.rounds, self.betrayd, label="AI Betrayed")
        plot.title("Results of the Prisoner's Dillema")
        plot.legend()
        plot.xlabel("Round")
        plot.savefig(filename)
        plot.show()
    @classmethod
    def load_data(cls, filename="dilemma_data.csv"):
        instance = cls()
        with open(filename, mode='r') as file:
            reader = csv.reader(file)
            next(reader)
            for row in reader:
                round_num = int(row[0])
                c = int(row[1])
                b = int(row[2])
                cd = int(row[3])
                bd = int(row[4])
                instance.rounds.append(round_num)
                instance.coops.append(c)
                instance.betrays.append(b)
                instance.coopd.append(cd)
                instance.betrayd.append(bd)
            if instance.rounds:
                instance.round = instance.rounds[-1]
                instance._coops = instance.coops[-1]
                instance._betrays = instance.betrays[-1]
                instance._coopd = instance.coopd[-1]
                instance._betrayd = instance.betrayd[-1]
        return instance

    def save_data(self, filename="dilemma_data.csv"):
        with open(filename, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Round", "You Cooperated", "You Betrayed", "AI Cooperated", "AI Betrayed"])
            for i in range(len(self.rounds)):
                writer.writerow([
                    self.rounds[i],
                    self.coops[i],
                    self.betrays[i],
                    self.coopd[i],
                    self.betrayd[i]
                ])


def dilemma(stats: results):
    print("What do you do? ")
    cont = 0
    while cont == 0:
        ai_dec = random.randint(1, 2)
        decision = int(input("Type 1 to cooperate with the prisoner, type 2 to betray the prisoner: "))
        if decision == 1 and ai_dec == 1:
            print("You and the prisoner both cooperated! You will both spend the next two years in prison ")
        elif decision == 2 and ai_dec == 1:
            print("You betrayed the prisoner and the other prisoner  cooperated! You will go free while the other prisoner will stay for ten years  ")
        elif decision == 2 and ai_dec == 2:
            print("You and the prisoner have betrayed each other! You both go to prison for ten years")
        elif decision == 1 and ai_dec == 2:
            print("You cooperated but have been betrayed! You will go to prison for ten years while the other prisoner goes free ")
        else:
            print("Invalid input")

        stats.log(decision, ai_dec)
        cont = int(input("Type 0 to play again, press any other input to stop"))

imp = ""
while imp != "y" and imp != "n":
    imp = input("Are you importing existing results? y/n").lower()
    if imp == "y":
        stats = results.load_data("dilemma_data.csv")
    elif imp == "n":
        stats = results()
    else:
        print("Invalid input! Please try again!")
print("You are a prisoner being interrogated in a room adjacent to another prisoners")
print("You are offered a deal by the officer interrogating you")
print("You can betray the other inmate, in exchange, if they do not betray you in like you will be allowed to go free from prison. While they will be imprisoned for 5 years")
print("However, if they also betray you, both you and the other prisoner will be imprisoned for ten years")
print("If you both cooperate, you will both stay in prison for two years.")
dilemma(stats)
stats.graph()
stats.save_data()
print("Thank you for playing! Find your exported data and graph")