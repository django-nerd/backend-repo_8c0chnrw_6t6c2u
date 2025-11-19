"""
Database Schemas

Define your MongoDB collection schemas here using Pydantic models.
These schemas are used for data validation in your application.

Each Pydantic model represents a collection in your database.
Model name is converted to lowercase for the collection name:
- User -> "user" collection
- Product -> "product" collection
- BlogPost -> "blogs" collection
"""

from pydantic import BaseModel, Field, EmailStr
from typing import Optional, Literal

# --------------------------------------------------
# Donor U Application Schema
# --------------------------------------------------

class Application(BaseModel):
    """
    Applications submitted from the Donor U landing page
    Collection name: "application" (lowercase of class name)
    """
    name: str = Field(..., description="Full name of the applicant")
    email: EmailStr = Field(..., description="Contact email")
    org_name: str = Field(..., description="Organization name")
    org_size: Optional[Literal[
        "solo", "1-5", "6-20", "21-50", "51-200", "200+"
    ]] = Field(None, description="Organization team size range")
    budget_range: Optional[Literal[
        "<250k", "250k-500k", "500k-1m", "1m-5m", "5m+"
    ]] = Field(None, description="Annual org budget range")
    top_goal: Optional[str] = Field(None, max_length=500, description="Top donor goal for this quarter")
    tier: Literal["core", "premium"] = Field(..., description="Selected plan tier")
    billing: Literal["monthly", "annual"] = Field(..., description="Billing preference")
    scholarship: bool = Field(False, description="Applying for scholarship consideration")
    notes: Optional[str] = Field(None, max_length=1000, description="Anything else we should know")
    source: Optional[str] = Field(None, description="How did you hear about Donor U?")


# Example schemas retained for reference (not used by app directly)
class User(BaseModel):
    name: str = Field(..., description="Full name")
    email: str = Field(..., description="Email address")
    address: str = Field(..., description="Address")
    age: Optional[int] = Field(None, ge=0, le=120, description="Age in years")
    is_active: bool = Field(True, description="Whether user is active")

class Product(BaseModel):
    title: str = Field(..., description="Product title")
    description: Optional[str] = Field(None, description="Product description")
    price: float = Field(..., ge=0, description="Price in dollars")
    category: str = Field(..., description="Product category")
    in_stock: bool = Field(True, description="Whether product is in stock")
