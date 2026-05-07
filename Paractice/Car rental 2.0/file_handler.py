class FileHandler():
    def __init__(self, filepath:str):
        self.filepath = filepath

    def read(self):
            rows = []
            with open(self.filepath, "r") as file:
                for line in file:
                    rows.append(line.strip())
            return rows
        
    def write(self, vehicles):
            with open(self.filepath, "w") as file:
                for v in vehicles:
                    v_type = v.__class__.__name__
                    file.write(f"{v_type},{v._name},{v._price_per_day},{v._wheels}\n")
                

                

