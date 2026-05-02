import fitz
from PIL import Image
import io

def extract_pdf_content(pdf_bytes):
    doc = fitz.open(stream=pdf_bytes, filetype="pdf")
    text = ""
    images = []
    
    for i in range(len(doc)):
        page = doc[i]
        text += f"\n=== Page {i+1} ===\n{page.get_text()}\n"
        
        for img_idx, img in enumerate(page.get_images(full=True)):
            xref = img[0]
            base = doc.extract_image(xref)
            images.append({
                "page": i+1,
                "bytes": base["image"],
                "ext": base["ext"],
                "index": img_idx
            })
    return text, images