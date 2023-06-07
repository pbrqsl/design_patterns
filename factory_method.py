# Informal interface (ducktyping)

class InformalParserInterface:
    def load_data_source(self, path: str, file_name: str) -> str:
        """Load in the file for extracting text"""
        pass

    def extract_text(self, full_file_name: str) -> str:
        """Extract text from the currently loaded file"""
        pass


dictionary1 = {"car": "samochod", "bike": "motocykl"}

print(dictionary1.get("moon"))


