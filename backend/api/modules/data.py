from pydantic import BaseModel


class input_details(BaseModel):
    """
    This is the matching schema with the MongoDB Table - InputDetails
    """
    textId: str
    text :  str