try:
    import matplotlib.pyplot as plt
except ModuleNotFoundError as errorModule:
    print("Problem with finding module:", errorModule)
    exit(1)


class Drawer:
    state_array = []
    total_production_array = []
    production_value_array = []
    mode = ""

    def __init__(self, mode, state_array, mode_array):
        if mode == "total production":
            self.mode = mode
            self.state_array = state_array
            self.total_production_array = mode_array
        elif mode == "production value":
            self.mode = mode
            self.state_array = state_array
            self.production_value_array = mode_array
        else:
            print("Wrong mode for Drawer.")
            exit(1)

    def draw_bar(self):
        if self.mode == "total production":
            plt.figure(figsize=(10, 4.8))
            plt.bar(self.state_array, self.total_production_array, align='edge')
            plt.ylabel('Total production [Pounds]')
            plt.title('Graph of total production in given year in different states.')
        else:
            plt.figure(figsize=(10, 4.8))
            plt.bar(self.state_array, self.production_value_array, align='edge')
            plt.ylabel('Production value [Dollars]')
            plt.title('Graph of production value in given year in different states.')

        plt.xlabel('State')
        plt.xticks(rotation=45)
        plt.show()
