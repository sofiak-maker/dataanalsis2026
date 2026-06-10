def process_data(data: str) -> str:
   
    return data.upper()

def get_data_length(data: str) -> int:
   
    return len(data)

def is_valid(data: str) -> bool:
    
    return bool(data and data.strip()) 
