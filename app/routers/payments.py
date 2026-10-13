from fastapi import APIRouter
from app.schemas.payment import PaymentEvent


router = APIRouter(
    prefix="/payments",
    tags=["Payments"]
)


@router.post("/events")
def receive_payment_event(event: PaymentEvent):
    return {
        "message": "Payment event received",
        "payment_id": event.payment_id,
        "status": event.status
    }

