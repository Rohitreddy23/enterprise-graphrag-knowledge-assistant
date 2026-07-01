from typing import List


class TextChunker:
    """Simple text chunker for demonstration.

    Production systems should tune chunk size and overlap based on
    document type, retrieval quality, latency, and model context window.
    """

    def __init__(self, chunk_size: int = 800, overlap: int = 100):
        self.chunk_size = chunk_size
        self.overlap = overlap

    def chunk(self, text: str) -> List[str]:
        if not text:
            return []

        chunks = []
        start = 0

        while start < len(text):
            end = start + self.chunk_size
            chunks.append(text[start:end])
            start += self.chunk_size - self.overlap

        return chunks
