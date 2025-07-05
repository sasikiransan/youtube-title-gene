# 🎬 YouTube Title & Description Generator

**Generate catchy, SEO-optimized YouTube titles and descriptions from video scripts using LLaMA 3 by Groq.**  
Perfect for content creators looking to boost engagement with AI-generated metadata! 😄❤️


##   APP
 
[Live App on Streamlit](https://sasi-kiran-youtube-title-generator.streamlit.app/)
 
---

## 🚨 IMPORTANT BEFORE YOU START

⚠️ Whether you're running **locally** or **on Streamlit Cloud**, read these first:

- ✅ You **MUST** get a **Groq API Key**:  
  → https://console.groq.com/keys

- ❌ **Do NOT** push `.env` (your API key) to GitHub!  
  Use `.gitignore` to exclude it.

- ✅ If deploying to **Streamlit Cloud**, you **MUST** set your API key under **Secrets**:
  ```toml
  GROQ_API_KEY = "your_api_key_here"
  ```

💣 Forgetting the secret is the most common reason the app fails to load or generate results!

---

## 🚀 Features

🔥 Uses Groq's ultra-fast LLaMA 3 model  
🧠 Analyzes video scripts to generate optimized metadata  
💻 Simple, elegant Streamlit UI  
🏷️ Generates SEO-rich descriptions with CTAs & hashtags  
☁️ Fully deployable on Streamlit Cloud  

---

## 📦 Project Structure

```
yt-title-generator/
├── app.py            # Streamlit UI logic
├── groq_api.py       # API call to Groq + prompt formatting
├── requirements.txt  # All Python dependencies
├── .gitignore        # Tells Git to ignore .env
└── .env              # (NOT tracked) Your private API key
```

---

## 🧰 Tech Stack

| Tool       | Purpose                        |
|------------|--------------------------------|
| Streamlit  | Frontend UI                    |
| Groq API   | LLaMA 3 backend text generation|
| Python     | Core logic                     |
| dotenv     | Secret key management          |

---

## 🧪 Demo

**1. **
![Picture 1](assets/image1.png)

**2.**
![Pic 2](assets/image2.png)

**3.**
![pic 3](assets/image3.png)

🔗 [Live App on Streamlit](https://sasi-kiran-youtube-title-generator.streamlit.app/)

---

## 🛠️ Local Setup (Run on your PC)

```bash
# 1. Clone the repo
git clone https://github.com/your-username/yt-title-generator.git
cd yt-title-generator

# 2. Install dependencies
pip install -r requirements.txt

# 3. ⚠️ Add your Groq API key to a `.env` file
echo GROQ_API_KEY=your_api_key_here > .env

# 4. Run the app
streamlit run app.py
```

> ⚠️ DO NOT commit `.env` to GitHub. Your key will get blocked!

---

## ☁️ Streamlit Cloud Deployment

🔹 Steps to deploy this app live using Streamlit Cloud:

- Push only safe files to GitHub (`app.py`, `groq_api.py`, `requirements.txt`)
- Make sure `.env` is ignored via `.gitignore`:
  ```
  .env
  ```
- Go to Streamlit Cloud → Create a new app
- Select your GitHub repo & `app.py` file
- ✅ Go to **Settings > Secrets** and add:
  ```toml
  GROQ_API_KEY = "your_actual_groq_api_key"
  ```
- 🔄 Wait for it to redeploy

🎉 Your app will now be LIVE!

> ⚠️ Missing the secret will crash your deployed app! Always check the Secrets tab if things don't work.

---

## 📋 Example Output

##   Input:


![pic2](assets/image2.png)
```
For a sample i have mentioned a input in the assets in sampleinput1 file .

### Summary  
The video discusses the ongoing deliberations within the Bharatiya Janata Party (BJP) about appointing a woman as the All India President of the party. This strategic move coincides with the upcoming 2026 census and subsequent delimitation process before the 2029 Lok Sabha elections, which will implement the Women’s Reservation Bill mandating one-third representation of women in Parliament and state assemblies. BJP sees this as an opportunity to lead the political transformation by promoting a woman leader, a decision reportedly supported by the Rashtriya Swayamsevak Sangh (RSS).  

The speculation highlights three prominent South Indian women leaders as potential candidates: Nirmala Sitharaman, Daggupati Purandeswari, and Vanathi Srinivasan. South India’s political significance is underscored given BJP’s attempts to strengthen its foothold in the region, where it has historically struggled compared to its dominance in North and Western India. The video elaborates on BJP’s electoral performance trends across India, emphasizing the relative challenges and breakthroughs in South India, including recent gains in Telangana, Tamil Nadu, and Kerala.  

Nirmala Sitharaman emerges as the frontrunner due to her strong national profile, holding key portfolios like Finance and Defence Minister, and her ability to connect two South Indian states (Tamil Nadu and Andhra Pradesh). Purandeswari, with her clean political image and multilingual capabilities, is considered the second probable candidate, while Vanathi Srinivasan is the third, recognized for her long-standing party work and leadership roles in Tamil Nadu.  

The analysis also touches upon BJP’s internal social engineering, balancing caste and regional representation, with the party’s top leadership (Modi and Amit Shah) focusing on collective leadership rather than individual prominence for the party president role. The appointment of a woman leader is seen as a strategic response to criticisms regarding women’s role in the party and the RSS, as well as a broader political maneuver to adapt to changing electoral dynamics.

### Highlights  
- 👩‍💼 BJP considers appointing a woman as All India President to align with upcoming Women’s Reservation legislation.  
- 🇮🇳 South Indian women leaders like Nirmala Sitharaman, Daggupati Purandeswari, and Vanathi Srinivasan are frontrunners for the role.  
- 📊 BJP has historically struggled in South India but is making notable recent electoral gains, especially in Telangana and Tamil Nadu.  
- 🔑 Nirmala Sitharaman’s strong national profile and key ministerial roles position her as the most probable candidate.  
- 🗳 The delimitation process after the 2026 census will reshape constituencies and increase women’s political representation.  
- 🤝 BJP’s leadership emphasizes collective leadership with Modi and Amit Shah at the helm, making the president’s role more organizational.  
- ♀ The move to appoint a woman leader also aims to counter criticisms about women’s roles within BJP and RSS structures.  

### Key Insights  
- 👩‍⚖ *Strategic Timing with Delimitation and Women’s Reservation:* The BJP’s consideration of a woman president is intricately linked to the political calendar, notably the 2026 census and subsequent delimitation before the 2029 Lok Sabha elections. The implementation of the Women’s Reservation Bill that guarantees one-third representation of women in legislative bodies makes it politically expedient for BJP to showcase women leadership at the highest organizational level, signaling inclusivity and foresight. This move reflects BJP's attempt to stay ahead of the curve in electoral politics by aligning its leadership structure with future legislative realities.  

- 🌏 *South India’s Growing Political Importance:* BJP’s focus on South Indian women leaders as presidential candidates underscores the party’s strategic priority to penetrate and consolidate its presence in South India, a region where it has traditionally been weaker. Despite BJP’s dominance in North and Western India, the South remains a challenging yet critical battleground. The choice of candidates from South India is thus both symbolic and tactical, aimed at bridging regional divides and appealing to a diverse electorate.  

- 📈 *Electoral Trends and Regional Dynamics:* The video details BJP’s fluctuating electoral performance across regions—strong consolidation in the North and West, expansion into Eastern India, and selective breakthroughs in South India, particularly Telangana. These insights reveal BJP’s adaptive electoral strategies, including alliances and grassroots penetration, as it aims to convert vote shares into legislative seats, especially in states where it has been historically marginal.  

- 🔥 *Nirmala Sitharaman’s Leadership Credentials:* Sitharaman’s tenure as Finance and Defence Minister has established her as a powerful and credible figure within BJP and national politics. Unlike typical gendered political appointments, her command over key ministries reflects Prime Minister Narendra Modi’s trust in her capabilities. Her bilingual and bi-regional appeal, spanning Tamil Nadu and Andhra Pradesh, enhances her suitability for the national leadership role, making her the most probable candidate for the party presidency.  

- 🎯 *Clean and Articulate Leadership in Purandeswari and Vanathi:* Both Daggupati Purandeswari and Vanathi Srinivasan bring valuable political experience and clean reputations, which are assets in BJP’s leadership image-building. Purandeswari’s legacy as NT Rama Rao’s daughter and her political moderation provide balance, while Vanathi’s long-term organizational work in Tamil Nadu shows BJP’s commitment to nurturing grassroots leadership. Their multilingual abilities also align with BJP’s pan-Indian outlook.  

- 🤝 *Collective Leadership Model in BJP:* The BJP’s party president role is viewed more as an organizational leadership position rather than a frontline political face leading electoral campaigns. With Modi as Prime Minister and Amit Shah as the number two leader, the party presidency functions within a collective leadership framework focused on party management and strategy rather than individual charisma. This reduces the political pressure on the president and allows the party to experiment with leadership diversity, including gender.  

- 🛡 *Response to Gender Criticism in BJP and RSS:* Historically, BJP and its ideological parent, the RSS, have faced criticism over the role and representation of women within their ranks. Appointing a woman as the party president addresses this criticism strategically, signaling inclusiveness and modernization. It also serves to counter opposition narratives, particularly from Congress leaders like Rahul Gandhi, who have highlighted gender issues within BJP and RSS. This move can be seen as both a political and ideological statement.  

- 🔄 *Social Engineering and Caste-Regional Balancing:* BJP’s leadership choices reflect a careful social engineering effort balancing caste, region, and gender identities. While the party has prioritized OBC and marginalized caste representation in government and ministerial appointments, the presidency role is less driven by caste considerations and more by organizational leadership capabilities. However, regional representation, especially from South India, is gaining ground, indicating BJP’s evolving approach to managing India’s complex social fabric.  

- 📊 *Women’s Reservation Bill Impact on Political Landscape:* The passing of the Women’s Reservation Bill, which reserves one-third of seats in Parliament and state assemblies for women, is a game-changer. It not only compels political parties to rethink candidate selection but also leadership roles. BJP’s contemplation of a woman president ahead of this change shows proactive adaptation to legislative reforms and an effort to capitalize on the political opportunities created by increased women’s representation.  

- 🏛 *Implications for 2029 Lok Sabha Elections:* The delimitation process and Women’s Reservation Bill will reshape electoral constituencies and voter profiles. BJP’s strategic leadership choices now are designed to prepare the party for these changes. By promoting a woman leader from South India, BJP aims to project inclusivity and regional balance, potentially appealing to broader voter segments, thereby strengthening its prospects for the 2029 general elections.  

In conclusion, the video provides a comprehensive analysis of BJP’s strategic considerations for appointing a woman as All India President, emphasizing the intersection of gender politics, regional dynamics, electoral strategy, and internal party organization. The focus on South Indian women leaders symbolizes BJP’s ambition to expand in the region while aligning with broader political reforms and social expectations. This leadership move fits within a collective party framework led by Modi and Shah, leveraging gender and regional representation to navigate India’s evolving political landscape ahead of critical electoral milestones.
```


##   Output:


![pic 3](assets/image3.png)
```
And the output is in the assets as well in sampleoutput1 file

Done! Here's your metadata:

🏷️ Title:
** "BJP's Game-Changing Move: A Woman As All India President? | Women's Reservation Bill & 2029 Lok Sabha Elections"

**

📋 Description:
**

"The Bharatiya Janata Party (BJP) is considering a historic move - appointing a woman as its All India President! This strategic decision coincides with the upcoming 2026 census, delimitation process, and the implementation of the Women's Reservation Bill. Join us as we analyze the top contenders from South India - Nirmala Sitharaman, Daggupati Purandeswari, and Vanathi Srinivasan.

Understand the significance of this move in the context of BJP's electoral performance trends across India, particularly in South India where the party has historically struggled. We'll also delve into the party's internal social engineering, balancing caste and regional representation, and its collective leadership model.

Watch till the end to grasp the implications of this decision on the 2029 Lok Sabha elections and how it might reshape the political landscape of India.

Like, Share, and Subscribe for more in-depth political analysis and insights!

Hashtags: #BJP #WomenInPolitics #WomensReservationBill #2029LokSabhaElections #NarendraModi #AmitShah #NirmalaSitharaman #DaggupatiPurandeswari #VanathiSrinivasan #SouthIndia #IndianPolitics #ElectionAnalysis"
```
---

## 🧠 How It Works

- User pastes a YouTube script or idea
- Prompt is sent to Groq's LLaMA 3 model
- The model responds with:
  - 🎯 Catchy Title
  - 📄 SEO-optimized Description (with hashtags + CTAs)

---

## ✅ To-Do / Improvements

- Auto-publish to YouTube via YouTube Data API  
- Export results to `.txt` or `.csv`  
- Add Google Sheets or MongoDB logging  
- Multi-language support (English, Hindi, Tamil, etc.)

---

## 🤝 Credits

👨‍💻 Built by [@iamsasikiran](https://github.com/iamsasikiran)  
🧠 Powered by Groq  
🎨 UI crafted with Streamlit

---

## 📜 License

MIT License  
Feel free to fork, remix, and share (with love and proper credit)! 😊❤️
