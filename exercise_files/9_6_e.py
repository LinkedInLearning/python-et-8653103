import csv
import json
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
client = OpenAI()

TAGS = [
    "shipping / delivery",
    "arrived broken",
    "missing product",
    "wrong product",
    "poor quality / durability",
    "cost too high",
    "size too big/small",
]

SYSTEM_PROMPT = """Given a product review, determine which complaint tags apply. Only include tags explicitly supported by the review text. If no issues are present, return an empty list."""

def extract_tags(review_text):
    response = client.responses.create(
        model="gpt-5.4-mini",
        instructions=SYSTEM_PROMPT,
        input=review_text,
        text={
            "format": {
                "type": "json_schema",
                "name": "tags_result",
                "schema": {
                    "type": "object",
                    "properties": {
                        "tags": {
                            "type": "array",
                            "items": {"type": "string", "enum": TAGS},
                        }
                    },
                    "required": ["tags"],
                    "additionalProperties": False,
                },
                "strict": True,
            }
        },
    )

    result = json.loads(response.output_text)
    return result.get("tags", [])


def print_result(row, tags):
	print("\n" + "-"*50)
	print(f"Product: {row['product_name']}")
	print(f"Reviewer: {row['reviewer_name']}")
	print("★" * int(row["star_rating"]))
	print(row["review_text"])
	print("\n")
	for tag in tags:
		print(f"  - {tag}")


def process_reviews(filename):
	with open(filename, "r") as f:
		reader = csv.DictReader(f)
		for row in list(reader)[0:10]:
			tags = extract_tags(row["review_text"])
			print_result(row, tags)


process_reviews("data_9_6_reviews.csv")
