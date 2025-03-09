import argparse
import sys
from typing import Optional
from utils.supabase_client import supabase
from utils.claude_client import claude

def get_prompt_from_supabase(action_key: str) -> Optional[str]:
    """
    Fetch a prompt template from Supabase based on the action key.
    
    Args:
        action_key (str): The key to look up in the prompts table
        
    Returns:
        Optional[str]: The prompt template if found, None otherwise
    """
    return supabase.get_prompt(action_key)

def stream_claude_response(prompt: str) -> None:
    """
    Stream a response from Claude and print it to stdout.
    
    Args:
        prompt (str): The prompt to send to Claude
    """
    try:
        for chunk in claude.stream_response(prompt):
            print(chunk, end="", flush=True)
        print()  # Add a newline at the end
    except Exception as e:
        print(f"Error streaming response: {e}", file=sys.stderr)

def main() -> None:
    parser = argparse.ArgumentParser(description="CLI tool for generating text using Claude 3.7")
    parser.add_argument("--action", type=str, required=True,
                       help="Action key to fetch the prompt template (e.g., generate_text, summarize)")
    parser.add_argument("--input", type=str, required=True,
                       help="Input text to be used in the prompt template")
    parser.add_argument("--init-db", action="store_true",
                       help="Initialize the Supabase prompts table with sample data")

    args = parser.parse_args()

    if args.init_db:
        supabase.initialize_prompts_table()
        return

    prompt_template = get_prompt_from_supabase(args.action)
    if not prompt_template:
        print(f"Error: No prompt template found for action '{args.action}'", file=sys.stderr)
        sys.exit(1)

    # Format the prompt template with the input
    formatted_prompt = prompt_template.format(input=args.input)
    stream_claude_response(formatted_prompt)

if __name__ == "__main__":
    main() 