from sqlalchemy.orm import Session
from .base import CRUDBase
from backend.track_specific.healthcare.models.appointment import Appointment
from backend.track_specific.healthcare.schemas.appointment import AppointmentCreate, AppointmentUpdate

class CRUDAppointment(CRUDBase[Appointment, AppointmentCreate, AppointmentUpdate]):
    def get_by_patient(self, db: Session, *, patient_id: int) -> list[Appointment]:
        return db.query(Appointment).filter(Appointment.patient_id == patient_id).all()

    def get_by_doctor(self, db: Session, *, doctor_id: int) -> list[Appointment]:
        return db.query(Appointment).filter(Appointment.doctor_id == doctor_id).all()

appointment = CRUDAppointment(Appointment)