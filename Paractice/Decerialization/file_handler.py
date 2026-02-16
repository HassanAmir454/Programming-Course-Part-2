
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
        return rows
    def write(self, items):
        try:
            with open(self.filepath, "w") as file:
                for item in items:
                    file.write(
                        f"{item.name},{item.value},{item.category},{item.weight}\n"
                    )
        except Exception:
            print(f"Failed to write file '{self.filepath}'")
