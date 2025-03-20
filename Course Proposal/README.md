# Course Proposal Tool

## Introduction

The **Course Proposal Tool** is a Flask-based web application designed to help users generate professional course proposals dynamically. It uses a language model (LLM) to create structured and detailed course proposals based on user-provided inputs. The tool is ideal for educators, trainers, and organizations looking to streamline the process of creating course outlines and proposals.

---

## Installation

### Prerequisites

Before you begin, ensure you have the following installed:

- Python 3.8 or higher
- pip (Python package manager)
- Docker (for containerized deployment)

---

#### Step 1: Clone the Repository

Clone the repository to your local machine:

```bash
git clone https://git.homains.org/lrnova/ai-tools.git
cd 'ai-tools'
```

#### Step 2: Set Up Environment Variables

1. Copy the `.env.example` file to `.env`:

   ```bash
   cp .env.example .env
   ```

2. Open the `.env` file and fill in the required environment variables. For example:

   ```plaintext
   GOOGLE_API_KEY=your_google_api_key_here
   ```

   Replace `your_google_api_key_here` with your actual Google API key. You can obtain the API key from [Google AI Studio](https://aistudio.google.com/apikey).


#### Step 3: Build and Run the Docker Container

1. Build the Docker image:

   ```bash
   docker-compose build
   ```

2. Start the Docker container:

   ```bash
   docker-compose up
   ```

The application will start running at `http://0.0.0.0:5000/`. Open this URL in your browser to access the tool.


---

## Usage

### Generating a Course Proposal

**Send a POST Request**: Use tools like Postman to send a POST request to the `/text-generator/proposal` endpoint with the required JSON payload.

#### Example JSON Payload:

Here’s an example of the JSON payload you can send:

```json
{
  "subject": "أساسيات الذكاء الاصطناعي",
  "training_method": "عبر الإنترنت",
  "target_audience": "المبتدئين",
  "key_points": "التعرف على الذكاء الاصطناعي وتطبيقاته",
  "duration": "20 ساعة",
  "other_information": "تشمل الدورة أنشطة عملية ومناقشات جماعية."
}
```

---

## Suggestions and Feedback

If you have any suggestions or feedback, feel free to contact me directly. Your input is highly valued and will help improve the tool!

---

Enjoy using the **Course Proposal Tool**! 🚀
