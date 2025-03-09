from typing import Generator, Any
import os
from dotenv import load_dotenv
import anthropic
from anthropic import Anthropic

load_dotenv()

class ClaudeClient:
    def __init__(self) -> None:
        self.api_key: str = os.getenv("ANTHROPIC_API_KEY", "")
        self.client = Anthropic(api_key=self.api_key)

    def stream_response(self, prompt: str) -> Generator[str, Any, None]:
        """
        Stream a response from Claude 3.7 using the Anthropic API.
        
        Args:
            prompt (str): The prompt to send to Claude
            
        Yields:
            str: Chunks of the response text
        """
        try:
            with self.client.messages.stream(
                model="claude-3-haiku-20240307",
                max_tokens=1000,
                temperature=0.7,
                messages=[
                    {"role": "user", "content": prompt}
                ]
            ) as stream:
                for text in stream.text_stream:
                    yield text
        except Exception as e:
            yield f"Error generating response: {e}"

# Create a singleton instance
claude = ClaudeClient() 