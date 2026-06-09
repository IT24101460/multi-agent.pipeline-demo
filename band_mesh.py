import json
import asyncio
from protocol import EnterprisePayload

class BandOrchestrationServer:
    def __init__(self):
        self.rooms = {}

    async def initialize_room(self, session_id: str, client_name: str, value: float):
        payload = EnterprisePayload(
            session_id=session_id,
            client_name=client_name,
            contract_value=value
        )
        self.rooms[session_id] = payload
        print(f"🟩 [BAND ROOM CREATED] Session: {session_id} initialized.")
        return payload

    async def update_room_state(self, session_id: str, updater_agent: str, mutations: dict):
        if session_id not in self.rooms:
            raise ValueError("Room not found")
        
        current_state = self.rooms[session_id]
        current_data = current_state.dict()
        current_data.update(mutations)
        updated_state = EnterprisePayload(**current_data)
        self.rooms[session_id] = updated_state
        
        print(f"🔄 [BAND STATE MUTATION] {updater_agent} updated room {session_id}.")
        print(f"   | Current Stage -> {updated_state.current_stage}")
        return updated_state

band_cloud_mesh = BandOrchestrationServer()