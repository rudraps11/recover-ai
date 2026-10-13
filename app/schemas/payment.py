from pydantic import BaseModel

class PaymentEvent(BaseModel):
    payment_id: str
    order_id: str | None = None
    customer_id: str
    amount: float
    currency: str
    status: str
    payment_method: str
    failure_reason: str | None = None