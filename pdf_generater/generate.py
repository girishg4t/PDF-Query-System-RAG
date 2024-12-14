from fpdf import FPDF

pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", size=12)

content = [
    "Frequently Asked Questions - AI and Machine Learning",
    "",
    "1. What is Artificial Intelligence (AI)?",
    "Artificial Intelligence (AI) refers to the simulation of human intelligence in machines that are programmed to think, learn, and adapt like humans.",
    "",
    "2. What is Machine Learning (ML)?",
    "Machine Learning is a subset of AI that focuses on building systems that can learn from and make decisions based on data without explicit programming.",
    "",
    "3. What are neural networks?",
    "Neural networks are a series of algorithms designed to recognize patterns and interpret data through a process that mimics the human brain.",
    "",
    "4. What are embeddings in AI?",
    "Embeddings are numerical representations of data (like text or images) in a continuous vector space, allowing for easier computations and comparisons.",
    "",
    "5. What is the difference between AI and ML?",
    "AI is the broader concept of machines being able to carry out tasks in a way we consider smart, while ML is a specific application of AI that allows machines to learn from data.",
    "",
    "6. How is AI used in real life?",
    "AI is used in various applications, including virtual assistants, recommendation systems, fraud detection, medical diagnosis, and autonomous vehicles.",
    "",
    "7. What is natural language processing (NLP)?",
    "NLP is a branch of AI that focuses on enabling machines to understand, interpret, and respond to human language in a meaningful way.",
    "",
    "8. What is the role of data in AI?",
    "Data is the foundation of AI. It provides the training examples needed for AI systems to learn and improve their performance.",
    "",
    "9. Can AI replace human jobs?",
    "While AI can automate repetitive tasks, it is more likely to complement human jobs by handling mundane tasks and enabling humans to focus on creative and strategic work.",
    "",
    "10. What are some ethical concerns related to AI?",
    "Key ethical concerns include bias in AI algorithms, data privacy issues, and the potential misuse of AI technologies."
]

for line in content:
    pdf.cell(200, 10, txt=line, ln=True)

pdf.output("../data/sample_faq.pdf")
