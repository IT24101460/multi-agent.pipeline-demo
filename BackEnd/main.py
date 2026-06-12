import asyncio
from BackEnd.band_mesh import band_cloud_mesh
from BackEnd.agents import ClaudeAnalystAgent, GPTComplianceAgent, ExecutiveGuardAgent

async def run_enterprise_pipeline():
    print("🚀 Starting Multi-Agent System on top of the Band Orchestration Layer...\n")
    
    analyst = ClaudeAnalystAgent()
    auditor = GPTComplianceAgent()
    gatekeeper = ExecutiveGuardAgent()
    
    session_id = "TXN_SECURE_9901A"
    await band_cloud_mesh.initialize_room(
        session_id=session_id, 
        client_name="Acme Global Logistics Inc", 
        value=1450000.00
    )
    
    await analyst.check_inbox_and_process(session_id)
    await auditor.watch_and_verify(session_id)
    await gatekeeper.final_gate(session_id)
    
    final_snapshot = band_cloud_mesh.rooms[session_id]
    
    print("\n🏁 [PIPELINE RUN COMPLETE]")
    print(f"Final Approval Status: {final_snapshot.audit_approved}")
    print(f"Compliance Ledger Log: {final_snapshot.compliance_verdict}")

if __name__ == "__main__":
    asyncio.run(run_enterprise_pipeline())