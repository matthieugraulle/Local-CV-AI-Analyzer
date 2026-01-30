import ollama
from pypdf import PdfReader
import os

# 1. Chemin du fichier
pdf_path = "CV_Matthieu_GRAULLE_2026.pdf"

if not os.path.exists(pdf_path):
    print(f"❌ Fichier introuvable : {pdf_path}")
else:
    print("📖 Extraction du texte (méthode directe)...")
    reader = PdfReader(pdf_path)
    text_segments = []
    
    for page in reader.pages:
        content = page.extract_text()
        if content:
            text_segments.append(content)
    
    full_text = "\n".join(text_segments)
    
    if not full_text.strip():
        print("⚠️ Le texte extrait est vide. Vérifie si le PDF n'est pas une image.")
    else:
        print(f"🚀 Analyse par Llama 3 ({len(full_text)} caractères extraits)...")
        
        prompt = f"""
        Tu es un expert en recrutement IA. Analyse ce CV :
        
        {full_text[:4000]} 
        
        Réponds en français :
        1. Résumé du profil.
        2. Top 3 compétences techniques.::
        3. Une suggestion d'amélioration pour le référencement (ATS).
        4. À partir de mon CV, pose-moi 5 questions techniques difficiles qu'un recruteur pourrait me poser pour un poste de Lead DevOps / Expert IA.
        5. Rédige un mail de motivation court (150 mots max) pour postuler à une mission de freelance en architecture Cloud souveraine.

        
        """
        
        response = ollama.generate(model='llama3', prompt=prompt)
        print("\n✅ RÉPONSE :\n", response['response'])
