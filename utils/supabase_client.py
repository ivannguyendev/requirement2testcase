from typing import Optional
import os
from dotenv import load_dotenv
from supabase import create_client, Client

load_dotenv()

class SupabaseManager:
    def __init__(self) -> None:
        self.supabase_url: str = os.getenv("SUPABASE_URL", "")
        self.supabase_key: str = os.getenv("SUPABASE_KEY", "")
        self.client: Client = create_client(self.supabase_url, self.supabase_key)

    def get_prompt(self, action_key: str) -> Optional[str]:
        """
        Fetch a prompt from the prompts table based on the action key.
        
        Args:
            action_key (str): The key to look up in the prompts table
            
        Returns:
            Optional[str]: The prompt text if found, None otherwise
        """
        try:
            response = (self.client.table("prompts")
                       .select("prompt")
                       .eq("key", action_key)
                       .execute())
            
            if response.data and len(response.data) > 0:
                return response.data[0]["prompt"]
            return None
        except Exception as e:
            print(f"Error fetching prompt: {e}")
            return None

    def initialize_prompts_table(self) -> None:
        """
        Initialize the prompts table with sample data.
        This should be run once when setting up the project.
        """
        sample_prompts = [
            {
                "key": "generate_text",
                "prompt": "Write a creative and engaging short story about {input}."
            },
            {
                "key": "summarize",
                "prompt": "Please provide a concise summary of the following text: {input}"
            },
            {
                "key": "analyze",
                "prompt": "Perform a detailed analysis of the following content, focusing on key themes and insights: {input}"
            }
        ]
        
        try:
            for prompt in sample_prompts:
                self.client.table("prompts").upsert(prompt).execute()
            print("Sample prompts initialized successfully")
        except Exception as e:
            print(f"Error initializing prompts: {e}")

# Create a singleton instance
supabase = SupabaseManager() 