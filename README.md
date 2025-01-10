# Smart Order Tracking & Product FAQ Assistant AI Agent 🤖

[![LangFlow](https://img.shields.io/badge/LangFlow-Powered-blue)](https://langflow.org)
[![Streamlit](https://img.shields.io/badge/Streamlit-App-FF4B4B)](https://streamlit.io)
[![Vector DB](https://img.shields.io/badge/Astra-Vector%20DB-purple)](https://www.datastax.com/products/datastax-astra)

An intelligent order tracking and product FAQ system powered by LangFlow and Streamlit. This AI-powered application allows customers to easily look up their orders and get instant answers about products, shipping times, and more through natural language queries.
![](https://github.com/seotanvirbd/customer_care_order_agent/blob/main/st-gui.png)
## 🌟 Features

- **Smart Order Tracking**: Instantly lookup order status and details
- **Product FAQ**: AI-powered answers about product specifications and features
- **Multiple LLM Support**: Compatible with OpenAI, Groq, Ollama
- **Vector Database**: Efficient data storage and retrieval using Astra Vector Database
- **User-Friendly Interface**: Built with Streamlit for seamless interaction

## 🛠️ Technology Stack

- **Frontend**: Streamlit
- **AI Framework**: LangFlow
- **Database**: Astra Vector Database
- **Language Models**: OpenAI, Groq, Ollama (configurable)
- **Programming Language**: Python
![](https://github.com/seotanvirbd/customer_care_order_agent/blob/main/langflow_agent_pipeline.png)
## 📦 Installation & Setup

1. Clone the repository:
```bash
git clone [your-repo-url]
cd [your-repo-name]
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Set up environment variables:
```bash
cp .env.example .env
# Edit .env with your API keys and configurations
```

4. Run the application:
```bash
streamlit run streamlit_app.py
```

## 🎯 Usage Example

The application provides a simple chat interface where users can:

1. Enter their order number to track status
2. Ask questions about products in natural language
3. Inquire about shipping times and policies
4. Get detailed product specifications

## 🗂️ Project Structure

```
├── streamlit_app.py      # Main Streamlit application
├── sample_orders.csv     # Order database
├── sample_products.csv   # Product database
├── .env                  # Environment variables
└── requirements.txt      # Project dependencies
```

## 🔧 Configuration

The application uses the following environment variables:

```python
BASE_API_URL = "https://api.langflow.astra.datastax.com"
LANGFLOW_ID = "your-langflow-id"
FLOW_ID = "your-flow-id"
APPLICATION_TOKEN = "your-app-token"
```

## 👨‍💻 Developer Information

**Tanvir Bin Ali**  
AI Enthusiast & Data Analyst

📞 Contact Information:
- 📧 Email: [tanvirafra1@gmail.com](mailto:tanvirafra1@gmail.com)
- 💼 LinkedIn: [seotanvirbd](https://www.linkedin.com/in/seotanvirbd/)
- 🌐 Portfolio: [seotanvirbd.com](https://seotanvirbd.com/)
- 📱 WhatsApp: [+880 1687373830](https://api.whatsapp.com/send?phone=8801687373830)
- 📺 YouTube: [@tanvirbinali2200](https://www.youtube.com/@tanvirbinali2200)
- 👥 Facebook: [seotanvirbd](https://www.facebook.com/seotanvirbd)

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! Feel free to check the issues page.

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

---

Made with ❤️ by Tanvir Bin Ali
