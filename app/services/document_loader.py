from pathlib import Path
from typing import List


class DocumentLoader:
    """Loads documents from a local folder.

    In production, this can be extended to read from S3, SharePoint,
    Google Drive, Azure Blob Storage, or an enterprise document system.
    """

    def load_text_files(self, folder_path: str) -> List[dict]:
        folder = Path(folder_path)
        documents = []

        for file_path in folder.glob("*.txt"):
            documents.append(
                {
                    "source": str(file_path),
                    "content": file_path.read_text(encoding="utf-8"),
                }
            )

        return documents
