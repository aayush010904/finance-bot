# Fin-Bot: Your Finance Assistant

Fin-Bot is a Streamlit-based chatbot designed to assist users with finance-related queries, leveraging state-of-the-art AI models. It provides insights such as stock prices, analyst recommendations, and company fundamentals, making it a helpful tool for finance enthusiasts, investors, and professionals.

---

## Features

- **Stock Market Insights**: Get real-time stock prices and updates.
- **Analyst Recommendations**: Access expert opinions on various stocks.
- **Company Fundamentals**: Retrieve key financial metrics and insights.
- **Interactive Chat Interface**: A user-friendly chat interface to interact with the bot.
- **Custom AI Agent**: Powered by `llama-3.1-70b-versatile` and equipped with `YFinanceTools`.

---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/<your-username>/fin-bot.git
   cd fin-bot
   ```

2. Install the required Python packages:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up the environment variables by creating a `.env` file:
   ```env
   # Example .env file
   PHI_API_KEY=<your_phi_api_key>
   ```

4. Run the application:
   ```bash
   streamlit run app.py
   ```

---

## Usage

1. Open the application in your web browser (usually at `http://localhost:8501`).
2. Interact with the chatbot by typing finance-related queries in the input box.
3. Use the "Show T&Cs" button to view the terms and conditions.

---

## Tech Stack

- **Frontend**: [Streamlit](https://streamlit.io/)
- **Backend**: [Phi Labs API](https://phi-labs.ai/)
- **Model**: LLaMA 3.1 (70B Versatile)
- **Tools**: YFinanceTools for stock market data

---

## Project Structure

```
fin-bot/
├── app.py                # Main application script
├── requirements.txt      # Python dependencies
├── .env                  # Environment variables
├── README.md             # Project documentation
└── other_files/          # Additional scripts or resources
```

---

## Key Dependencies

- `streamlit`
- `phi-agent`
- `dotenv`
- `yfinance`

Install all dependencies using:
```bash
pip install -r requirements.txt
```

---

## How It Works

1. **Model Integration**: The bot uses `LLaMA 3.1` model for natural language understanding.
2. **Finance Tools**: YFinanceTools fetches live stock data and insights.
3. **Chat History**: Maintains a session-based chat history for seamless interaction.

---

## Terms and Conditions

- The bot's responses are subject to the accuracy of the AI model and available data.
- Rate limits may apply for API calls.

---

## Contributing

We welcome contributions! Please follow these steps:

1. Fork the repository.
2. Create a feature branch:
   ```bash
   git checkout -b feature/new-feature
   ```
3. Commit your changes:
   ```bash
   git commit -m "Add new feature"
   ```
4. Push to the branch:
   ```bash
   git push origin feature/new-feature
   ```
5. Open a pull request.

---


## Acknowledgments

- **Phi Labs**: For their robust API and tools.
- **Streamlit**: For an easy-to-use interface for building web apps.
- **YFinance**: For providing financial data seamlessly.

---

## Future Enhancements

- Add support for additional financial tools and APIs.
- Enhance the chatbot's ability to handle complex finance queries.
- Implement user authentication for personalized insights.

---

## Contact

For any questions or feedback, feel free to reach out:

- **Email**: [aayushchauhan019@gmail.com](mailto:aayushchauhan019@gmail.com)
- **GitHub Issues**: Open an issue [here](https://github.com/aayush010904/fin-bot/issues)
```
