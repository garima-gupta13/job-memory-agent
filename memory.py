import asyncio
import cognee

async def save_job(company, role, notes):
    text = f"Company: {company}. Role: {role}. Notes: {notes}"
    await cognee.remember(text, dataset_name="job_applications")
    print(f"✅ Saved: {company} - {role}")

async def ask_memory(question):
    results = await cognee.recall(question, datasets=["job_applications"])
    for r in results:
        print(f"💡 {r.text}")
    return results

async def main():
    # Save 3 real job applications
    await save_job("Razorpay", "AI Engineer", "Applied June 29. No reply yet.")
    await save_job("PhonePe", "Backend Engineer", "Applied June 28. Interview scheduled July 5.")
    await save_job("CRED", "Python Developer", "Applied June 30. Asked for RAG experience.")
    
    print("\n--- Asking memory ---\n")
    
    await ask_memory("Which companies did I apply to?")
    await ask_memory("Which company has interview scheduled?")
    await ask_memory("Which company asked for RAG experience?")

asyncio.run(main())