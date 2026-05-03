### Summary
This project analyzes the Open Food Facts dataset to identify gaps in the healthy snack market. 

Initial exploration revealed a strong imbalance toward high-sugar, low-protein products, indicating market saturation in unhealthy snack segments. After refining category groupings and applying stricter nutritional thresholds, a significantly underrepresented segment was identified.

The analysis shows that products with more than 15g of protein and less than 3g of sugar are rare, particularly within the Snacks category, representing a clear opportunity for new product development.

### Technical Explanation
The definition of the “market gap” was iteratively refined from initial loose thresholds to stricter criteria (protein >15g, sugar <3g) to better reflect meaningful nutritional differentiation and uncover a truly under-served segment.

### Project Links
Notebook: https://colab.research.google.com/drive/1X8rEmItBggjWjLH6IdrARTdWagGjdFUH?usp=sharing

Dashboard: https://market-gap-analysis-dnl8yxrgjmshky5rk5xyam.streamlit.app/

Presentation: https://docs.google.com/presentation/d/1n8MExtP-ZbDDE9dpF3m-TdVCJfq4nR_NIYz0QaMstI0/edit?usp=sharing

### Data Cleaning
Missing values in key fields such as sugars_100g and proteins_100g were removed to ensure accuracy. Outliers outside biologically plausible ranges (0–100g per 100g) were filtered out.

### Candidate’s Choice
A custom "health score" metric (protein - sugar) was introduced to rank products by nutritional value. This helps highlight products that balance high protein and low sugar effectively.
