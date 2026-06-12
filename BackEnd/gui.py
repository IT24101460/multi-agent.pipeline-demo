import streamlit as st
import asyncio
from BackEnd.band_mesh import band_cloud_mesh
from BackEnd.main import run_enterprise_pipeline

st.title("🛡️ Enterprise Multi-Agent Audit Desk")

# User Inputs Data in Frontend
client = st.text_input("Client Name", "Acme Global Logistics Inc")
value = st.number_input("Contract Value ($)", value=1450000.0)

if st.button("Trigger Multi-Agent Compliance Audit"):
    with st.spinner("Agents are collaborating via Band..."):
        # Run your background async pipeline
        asyncio.run(run_enterprise_pipeline())
        
        # Pull the final results from the Band Room to show visually
        final_state = band_cloud_mesh.rooms["TXN_SECURE_9901A"]
        
    # Display clear UI Alert Cards based on Agent Outputs
    if final_state.audit_approved:
        st.success("✅ Audit Status: APPROVED BY EXECUTIVE GUARD")
    else:
        st.error("❌ Audit Status: REJECTED")
        
    # Show step-by-step breakdown of what each agent said
    st.subheader("🤖 Claude Analyst Notes")
    st.write(final_state.financial_analysis)
    
    st.subheader("🤖 GPT Compliance Verdict")
    st.write(final_state.compliance_verdict)