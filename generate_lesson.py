import openai

def generate_lesson(python):
    openai.api_key = 'your-openai-api-key'

    try:
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=f"Create a detailed daily lesson plan for learning about {python}. Include objectives, materials needed, and activities.",
            temperature=0.5,
            max_tokens=500
        )
        return response.choices[0].text.strip()
    except Exception as e:
        return f"An error occurred: {e}"

# Example usage
topic = "Python programming"
lesson = generate_lesson(topic)
print(lesson)
