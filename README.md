# Claude 3.7 Text Generation with Supabase

This project demonstrates integration between Supabase for prompt management and Claude 3.7 using the official Anthropic API, with streaming responses.

## Setup

1. Clone the repository
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Create a `.env` file with your credentials:
   ```
   SUPABASE_URL=your_supabase_url
   SUPABASE_KEY=your_supabase_key
   ANTHROPIC_API_KEY=your_anthropic_api_key
   ```

4. Set up the Supabase database:
   - Create a new project in Supabase
   - Create a table named `prompts` with the following schema:
     ```sql
     create table prompts (
       key text primary key,
       prompt text not null
     );
     ```
   - Initialize the table with sample prompts:
     ```bash
     python main.py --init-db
     ```

## Usage

The CLI supports different text generation actions using stored prompts:

1. Generate a creative text:
   ```bash
   python main.py --action generate_text --input "a magical forest"
   ```

2. Summarize text:
   ```bash
   python main.py --action summarize --input "Your text to summarize here"
   ```

3. Analyze content:
   ```bash
   python main.py --action analyze --input "Your content to analyze here"
   ```

## Project Structure

- `main.py`: CLI interface and main logic
- `utils/`:
  - `supabase_client.py`: Supabase connection and prompt management
  - `claude_client.py`: Claude 3.7 integration with streaming support via Anthropic API
- `requirements.txt`: Project dependencies
- `.env`: Environment variables (not tracked in git)

## Features

- Prompt template management in Supabase
- Streaming responses from Claude 3.7 via official Anthropic API
- Type hints and PEP 8 compliant
- Error handling and graceful fallbacks
- Easy CLI interface

## Requirements

- Python 3.8+
- Supabase account
- Anthropic API key 