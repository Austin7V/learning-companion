import os
import logging
from openai import OpenAI, APIError, APIConnectionError, RateLimitError

logger = logging.getLogger(__name__)


def get_summary(notes: str) -> str:
    """
    Generate a summary of learning session notes using OpenAI API.

    Args:
        notes: The learning session notes to summarize

    Returns:
        A string containing 3-5 bullet point summary

    Raises:
        ValueError: If OPENAI_API_KEY is not configured
        APIError: If OpenAI API call fails
    """
    api_key = os.getenv("OPENAI_API_KEY")

    if not api_key:
        logger.error("OPENAI_API_KEY environment variable not set")
        raise ValueError(
            "OpenAI API key not configured. Please set OPENAI_API_KEY in .env file."
        )

    client = OpenAI(api_key=api_key)
    logger.info(f"Generating summary for notes ({len(notes)} characters)")

    prompt = f"""Summarize these learning session notes in 3-5 concise bullet points.
Each bullet should be a key takeaway or learning point.

Notes:
{notes}

Format: Return only the bullet points, one per line, starting with '-'."""

    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {
                    "role": "system",
                    "content": "You are a helpful learning assistant. Create concise summaries of learning sessions.",
                },
                {"role": "user", "content": prompt},
            ],
            temperature=0.7,
            max_tokens=500,
        )

        summary = response.choices[0].message.content.strip()
        logger.info("Summary generated successfully")
        return summary

    except RateLimitError as e:
        error_msg = "OpenAI API rate limit exceeded. Please try again later."
        logger.warning(f"Rate limit error: {e}")
        return error_msg

    except APIConnectionError as e:
        error_msg = "Failed to connect to OpenAI API. Please check your internet connection."
        logger.error(f"Connection error: {e}")
        return error_msg

    except APIError as e:
        error_msg = f"OpenAI API error: {str(e)}"
        logger.error(f"API error: {e}")
        return error_msg

    except Exception as e:
        error_msg = f"Unexpected error generating summary: {str(e)}"
        logger.error(f"Unexpected error: {e}")
        return error_msg
