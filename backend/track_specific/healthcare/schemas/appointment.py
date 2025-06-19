from pydantic import BaseModel
from typing import Optional
from datetime import datetime

# Shared properties
class AppointmentBase(BaseModel):
    patient_id: Optional[int] = None
    doctor_id: Optional[int] = None
    appointment_time: Optional[datetime] = None
    status: Optional[str] = None

# Properties to receive on item creation
class AppointmentCreate(AppointmentBase):
    patient_id: int
    doctor_id: int
    appointment_time: datetime

# Properties to receive on item update
class AppointmentUpdate(AppointmentBase):
    pass

# Properties shared by models stored in DB
class AppointmentInDBBase(AppointmentBase):
    id: int
    patient_id: int
    doctor_id: int
    appointment_time: datetime
    status: str

    class Config:
        orm_mode = True

# Properties to return to client
class Appointment(AppointmentInDBBase):
    pass

# Properties stored in DB
class AppointmentInDB(AppointmentInDBBase):
    pass