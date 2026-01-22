class FileHandler:
    filepath: str
    def __init__(self, filepath):
        self.filepath = filepath
    def read(self)->list[str]:
        rows: list[str] = []
        try:
            with open(self.filepath, "r") as file:
                row = file.readline()
                while row != "":
                    rows.append(row.rstrip('\n'))
                    row = file.readline()
        except Exception:
            print(f"Failed to read file '{self.filepath}'")
