import json
from pydantic import BaseModel
from typing import List, Optional

class EnterprisePayload(BaseModel):
    session_id: str
    current_stage: str = "INTAKE"
    client_name: str
    contract_value: float
    risk_signals: List[str] = []
    financial_analysis: Optional[str] = None
    compliance_verdict: Optional[str] = None
    audit_approved: bool = False

    def to_band_message(self) -> str:
        return self.json()

    @classmethod
    def from_band_message(cls, json_str: str):
        return cls(**json.loads(json_str))