import fitz  # PyMuPDF

def extract_text_and_images(uploaded_file):
    """Works with Streamlit uploaded files"""
    if uploaded_file is None:
        return {"raw_text": "", "images": []}
    
    # Read the uploaded file as bytes
    pdf_bytes = uploaded_file.read()
    
    doc = fitz.open(stream=pdf_bytes, filetype="pdf")
    
    full_text = ""
    images = []
    
    for page_num in range(len(doc)):
        page = doc[page_num]
        full_text += f"\n=== Page {page_num+1} ===\n{page.get_text()}\n"
        
        # Extract images
        for img_index, img in enumerate(page.get_images(full=True)):
            xref = img[0]
            base_image = doc.extract_image(xref)
            images.append({
                "page": page_num + 1,
                "image_bytes": base_image["image"],
                "index": img_index
            })
    
    return {
        "raw_text": full_text,
        "images": images
    }