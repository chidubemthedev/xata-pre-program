from fastapi import APIRouter, File, UploadFile
from pathlib import Path

pdf_router = APIRouter()

@pdf_router.post("/upload-pdf/")
async def upload_pdf(pdf: UploadFile = File(...)):
    if pdf.content_type != "application/pdf":
        return {"error": "Only PDF files allowed"}
    content = await pdf.read()
    save_path = Path("files") / pdf.filename
    save_path.parent.mkdir(parents=True, exist_ok=True)
    with open(save_path, "wb") as save_file:
        save_file.write(content)
    return {"message": "File uploaded successfully"}