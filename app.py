from flask import Flask, request , jsonify ,render_template
import requests
import csv
    # Define the path to your CSV file
skincare_products=  'C:\\Users\\kunal\\skincare_products.csv'

# Function to read data from CSV
def read_data():
    data = []
    with open(skincare_products, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            data.append(row)
    return data


app = Flask("skin care tool")

# Define routes for your application
@app.route('/recommend')
def recommend_skincare():
    data=request.form
    print(data)

    return render_template('index.html',matching_products=[{'Age Range':'0-12'},{'Age Range':'13-17'}])
@app.route('/submit',methods=['POST'])
def submit():
    data=request.form
    age_range=data['age_range']
    skin_type=data['skin_type']

    
    return render_template('recommend.html',product=get_recommendations(age_range,skin_type))
def get_recommendations(age_range,skin_type):
    if age_range=='0-12':
        if skin_type=='3':
            data={'age_range':age_range,'skin_type':skin_type,"Skincare Product Specifications":[
        "- Exfoliating scrub for combination skin",
        "- Diluted apple cider vinegar toner",
        "- Lightweight moisturizer",
        "- Niacinamide serum for balance"
    ],"Avoid Harmful Chemicals": "Phthalates, artificial fragrances, propylene glycol",
    "Approximate Price (USD)":
        ["Face Scrub: $8-12",
        "Toner: $8-12",
        "Moisturizer: $10-15",
        "Serum: $15-25",
        "Sunscreen: $10-15"],        
    "Natural Treatment Products": [
        "- Oatmeal scrub for face wash",
        "- Apple cider vinegar as a toner",
        "- Argan oil as a moisturizer",
        "- Niacinamide serum"
    ],
    "Preparation Process": ['1. Grind oatmeal into a powder.',' 2. Mix with water to form a paste.',' 3. Gently exfoliate and rinse.', '4. Apply apple cider vinegar toner.']
            }
    return data


        
#     "Age Range": "Child (0-12 years)",
#     "Skin Types": "Child - Dry",
#     "Skincare Product Specifications": [
#         "- Creamy cleanser to prevent further dryness",
#         "- Soothing chamomile toner",
#         "- Rich, hydrating moisturizer",
#         "- Hyaluronic acid serum for added moisture"
#     ],
#     "Avoid Harmful Chemicals": "Alcohol denat, artificial colors, formaldehyde-releasing preservatives",
#     "Approximate Price (USD)": {
#         "Face Wash": "$5-10",
#         "Moisturizer": "$10-15",
#         "Toner": "$8-12",
#         "Serum": "$15-25",
#         "Sunscreen": "$10-15"
#     },
#     "Natural Treatment Products": [
#         "- Olive oil or coconut oil for a gentle face wash",
#         "- Chamomile tea as a toner",
#         "- Shea butter as a moisturizer",
#         "- Hyaluronic acid serum"
#     ],
#     "Preparation Process": "Olive Oil Face Wash: 1. Massage olive oil onto dry skin. 2. Gently wipe off with a warm, damp cloth. 3. Follow with chamomile tea toner."
# },
# {
#     "Age Range": "Child (0-12 years)",
#     "Skin Types": "Child - Combination",
#     "Skincare Product Specifications": [
#         "- Exfoliating scrub for combination skin",
#         "- Diluted apple cider vinegar toner",
#         "- Lightweight moisturizer",
#         "- Niacinamide serum for balance"
#     ],
#     "Avoid Harmful Chemicals": "Phthalates, artificial fragrances, propylene glycol",
#     "Approximate Price (USD)": {
#         "Face Scrub": "$8-12",
#         "Toner": "$8-12",
#         "Moisturizer": "$10-15",
#         "Serum": "$15-25",
#         "Sunscreen": "$10-15"
#     },
#     "Natural Treatment Products": [
#         "- Oatmeal scrub for face wash",
#         "- Apple cider vinegar as a toner",
#         "- Argan oil as a moisturizer",
#         "- Niacinamide serum"
#     ],
#     "Preparation Process": "Oatmeal Scrub: 1. Grind oatmeal into a powder. 2. Mix with water to form a paste. 3. Gently exfoliate and rinse. 4. Apply apple cider vinegar toner."
# },
# {
#     "Age Range": "Teen (13-17 years)",
#     "Skin Types": "Teen - Normal",
#     "Skincare Product Specifications": [
#         "- Gentle cleanser suitable for young skin",
#         "- Alcohol-free toner to avoid irritation",
#         "- Non-comedogenic moisturizer",
#         "- Vitamin C serum for brightening"
#     ],
#     "Avoid Harmful Chemicals": "Parabens, sulfates, synthetic fragrances",
#     "Approximate Price (USD)": {
#         "Face Wash": "$5-10",
#         "Moisturizer": "$10-15",
#         "Toner": "$8-12",
#         "Serum": "$15-25",
#         "Sunscreen": "$10-15"
#     },
#     "Natural Treatment Products": [
#         "- Honey or yogurt for a gentle face wash",
#         "- Rosewater or aloe vera as a toner",
#         "- Jojoba oil as a moisturizer",
#         "- Green tea extract or vitamin C serum"
#     ],
#     "Preparation Process": "Honey Face Wash: 1. Mix honey with a small amount of water to create a paste. 2. Gently massage onto damp face and rinse thoroughly."
# },
# {
#     "Age Range": "Teen (13-17 years)",
#     "Skin Types": "Teen - Oily",
#     "Skincare Product Specifications": [
#         "- Cleanser with salicylic acid for acne-prone skin",
#         "- Witch hazel toner to control oil",
#         "- Oil-free moisturizer",
#         "- Tea tree oil serum for acne control"
#     ],
#     "Avoid Harmful Chemicals": "Sodium lauryl sulfate, synthetic dyes, mineral oil",
#     "Approximate Price (USD)": {
#         "Face Wash": "$5-10",
#         "Moisturizer": "$10-15",
#         "Toner": "$8-12",
#         "Serum": "$15-25",
#         "Sunscreen": "$10-15"
#     },
#     "Natural Treatment Products": [
#         "- Lemon juice diluted in water for face wash",
#         "- Witch hazel as a toner",
#         "- Aloe vera gel as a moisturizer",
#         "- Tea tree oil serum"
#     ],
#     "Preparation Process": "Lemon Face Wash: 1. Mix lemon juice with water. 2. Apply to face, avoiding the eyes. Rinse thoroughly. 3. Follow with witch hazel toner."
# },
# {
#     "Age Range": "Teen (13-17 years)",
#     "Skin Types": "Teen - Dry",
#     "Skincare Product Specifications": [
#         "- Creamy cleanser for dry patches",
#         "- Soothing chamomile toner",
#         "- Rich, hydrating moisturizer",
#         "- Hyaluronic acid serum for added moisture"
#     ],
#     "Avoid Harmful Chemicals": "Alcohol denat, artificial colors, formaldehyde-releasing preservatives",
#     "Approximate Price (USD)": {
#         "Face Wash": "$5-10",
#         "Moisturizer": "$10-15",
#         "Toner": "$8-12",
#         "Serum": "$15-25",
#         "Sunscreen": "$10-15"
#     },
#     "Natural Treatment Products": [
#         "- Olive oil or coconut oil for a gentle face wash",
#         "- Chamomile tea as a toner",
#         "- Shea butter as a moisturizer",
#         "- Hyaluronic acid serum"
#     ],
#     "Preparation Process": "Olive Oil Face Wash: 1. Massage olive oil onto dry skin. 2. Gently wipe off with a warm, damp cloth. 3. Follow with chamomile tea toner."
# },
# {
#     "Age Range": "Teen (13-17 years)",
#     "Skin Types": "Teen - Combination",
#     "Skincare Product Specifications": [
#         "- Exfoliating scrub for combination skin",
#         "- Diluted apple cider vinegar toner",
#         "- Lightweight moisturizer",
#         "- Niacinamide serum for balance"
#     ],
#     "Avoid Harmful Chemicals": "Phthalates, artificial fragrances, propylene glycol",
#     "Approximate Price (USD)": {
#         "Face Scrub": "$8-12",
#         "Toner": "$8-12",
#         "Moisturizer": "$10-15",
#         "Serum": "$15-25",
#         "Sunscreen": "$10-15"
#     },
#     "Natural Treatment Products": [
#         "- Oatmeal scrub for face wash",
#         "- Apple cider vinegar as a toner",
#         "- Argan oil as a moisturizer",
#         "- Niacinamide serum"
#     ],
#     "Preparation Process": "Oatmeal Scrub: 1. Grind oatmeal into a powder. 2. Mix with water to form a paste. 3. Gently exfoliate and rinse. 4. Apply apple cider vinegar toner."
# },
# {
#     "Age Range": "Adult (18+ years)",
#     "Skin Types": "Adult - Normal",
#     "Skincare Product Specifications": [
#         "- Cleanser suitable for adult skin",
#         "- Alcohol-free toner to avoid irritation",
#         "- Non-comedogenic moisturizer",
#         "- Vitamin C serum for anti-aging"
#     ],
#     "Avoid Harmful Chemicals": "Parabens, sulfates, synthetic fragrances",
#     "Approximate Price (USD)": {
#         "Face Wash": "$5-10",
#         "Moisturizer": "$10-15",
#         "Toner": "$8-12",
#         "Serum": "$15-25",
#         "Sunscreen": "$10-15"
#     },
#     "Natural Treatment Products": [
#         "- Honey or yogurt for a gentle face wash",
#         "- Rosewater or aloe vera as a toner",
#         "- Jojoba oil as a moisturizer",
#         "- Green tea extract or vitamin C serum"
#     ],
#     "Preparation Process": "Honey Face Wash: 1. Mix honey with a small amount of water to create a paste. 2. Gently massage onto damp face and rinse thoroughly."
# },
# {
#     "Age Range": "Adult (18+ years)",
#     "Skin Types": "Adult - Oily",
#     "Skincare Product Specifications": [
#         "- Cleanser with salicylic acid for oily skin",
#         "- Witch hazel toner to control oil",
#         "- Oil-free moisturizer",
#         "- Tea tree oil serum for acne control"
#     ],
#     "Avoid Harmful Chemicals": "Sodium lauryl sulfate, synthetic dyes, mineral oil",
#     "Approximate Price (USD)": {
#         "Face Wash": "$5-10",
#         "Moisturizer": "$10-15",
#         "Toner": "$8-12",
#         "Serum": "$15-25",
#         "Sunscreen": "$10-15"
#     },
#     "Natural Treatment Products": [
#         "- Lemon juice diluted in water for face wash",
#         "- Witch hazel as a toner",
#         "- Aloe vera gel as a moisturizer",
#         "- Tea tree oil serum"
#     ],
#     "Preparation Process": "Lemon Face Wash: 1. Mix lemon juice with water. 2. Apply to face, avoiding the eyes. Rinse thoroughly. 3. Follow with witch hazel toner."
# },
# {
#     "Age Range": "Adult (18+ years)",
#     "Skin Types": "Adult - Dry",
#     "Skincare Product Specifications": [
#         "- Creamy cleanser for dry skin",
#         "- Soothing chamomile toner",
#         "- Rich, anti-aging moisturizer",
#         "- Hyaluronic acid serum for added moisture"
#     ],
#     "Avoid Harmful Chemicals": "Alcohol denat, artificial colors, formaldehyde-releasing preservatives",
#     "Approximate Price (USD)": {
#         "Face Wash": "$5-10",
#         "Moisturizer": "$10-15",
#         "Toner": "$8-12",
#         "Serum": "$15-25",
#         "Sunscreen": "$10-15"
#     },
#     "Natural Treatment Products": [
#         "- Olive oil or coconut oil for a gentle face wash",
#         "- Chamomile tea or chamomile-infused oil as a toner",
#         "- Shea butter as a moisturizer",
#         "- Hyaluronic acid serum"
#     ],
#     "Preparation Process": "Olive Oil Face Wash: 1. Massage olive oil onto dry skin. 2. Gently wipe off with a warm, damp cloth. 3. Follow with chamomile-infused oil toner."
# },
# {
#     "Age Range": "Adult (18+ years)",
#     "Skin Types": "Adult - Combination",
#     "Skincare Product Specifications": [
#         "- Exfoliating scrub for combination skin",
#         "- Diluted apple cider vinegar toner",
#         "- Lightweight anti-aging moisturizer",
#         "- Niacinamide serum for balance"
#     ],
#     "Avoid Harmful Chemicals": "Phthalates, artificial fragrances, propylene glycol",
#     "Approximate Price (USD)": {
#         "Face Scrub": "$8-12",
#         "Toner": "$8-12",
#         "Moisturizer": "$10-15",
#         "Serum": "$15-25",
#         "Sunscreen": "$10-15"
#     },
#     "Natural Treatment Products": [
#         "- Oatmeal scrub for face wash",
#         "- Apple cider vinegar as a toner",
#         "- Argan oil as a moisturizer",
#         "- Niacinamide serum"
#     ],
#     "Preparation Process": "Oatmeal Scrub: 1. Grind oatmeal into a powder. 2. Mix with water to form a paste. 3. Gently exfoliate and rinse. 4. Apply apple cider vinegar toner."
# },
# {
#     "Age Range": "Old Age (65+ years)",
#     "Skin Types": "Old Age - Normal",
#     "Skincare Product Specifications": [
#         "- Gentle cleanser for mature skin",
#         "- Alcohol-free toner to avoid irritation",
#         "- Anti-aging moisturizer",
#         "- Vitamin C serum for wrinkle reduction"
#     ],
#     "Avoid Harmful Chemicals": "Parabens, sulfates, synthetic fragrances",
#     "Approximate Price (USD)": {
#         "Face Wash": "$5-10",
#         "Moisturizer": "$10-15",
#         "Toner": "$8-12",
#         "Serum": "$15-25",
#         "Sunscreen": "$10-15"
#     },
#     "Natural Treatment Products": [
#         "- Honey or yogurt for a gentle face wash",
#         "- Rosewater or aloe vera as a toner",
#         "- Jojoba oil as a moisturizer",
#         "- Green tea extract or vitamin C serum"
#     ],
#     "Preparation Process": "Honey Face Wash: 1. Mix honey with a small amount of water to create a paste. 2. Gently massage onto damp face and rinse thoroughly."
# },
# {
#     "Age Range": "Old Age (65+ years)",
#     "Skin Types": "Old Age - Oily",
#     "Skincare Product Specifications": [
#         "- Cleanser with salicylic acid for aging skin",
#         "- Witch hazel toner to control oil",
#         "- Oil-free anti-aging moisturizer",
#         "- Tea tree oil serum for acne control"
#     ],
#     "Avoid Harmful Chemicals": "Sodium lauryl sulfate, synthetic dyes, mineral oil",
#     "Approximate Price (USD)": {
#         "Face Wash": "$5-10",
#         "Moisturizer": "$10-15",
#         "Toner": "$8-12",
#         "Serum": "$15-25",
#         "Sunscreen": "$10-15"
#     },
#     "Natural Treatment Products": [
#         "- Lemon juice diluted in water for face wash",
#         "- Witch hazel as a toner",
#         "- Aloe vera gel as a moisturizer",
#         "- Tea tree oil serum"
#     ],
#     "Preparation Process": "Lemon Face Wash: 1. Mix lemon juice with water. 2. Apply to face, avoiding the eyes. Rinse thoroughly. 3. Follow with witch hazel toner."
# },
# {
#     "Age Range": "Old Age (65+ years)",
#     "Skin Types": "Old Age - Dry",
#     "Skincare Product Specifications": [
#         "- Creamy cleanser for mature, dry skin",
#         "- Soothing chamomile toner",
#         "- Rich, anti-aging moisturizer",
#         "- Hyaluronic acid serum for added moisture"
#     ],
#     "Avoid Harmful Chemicals": "Alcohol denat, artificial colors, formaldehyde-releasing preservatives",
#     "Approximate Price (USD)": {
#         "Face Wash": "$5-10",
#         "Moisturizer": "$10-15",
#         "Toner": "$8-12",
#         "Serum": "$15-25",
#         "Sunscreen": "$10-15"
#     },
#     "Natural Treatment Products": [
#         "- Olive oil or coconut oil for a gentle face wash",
#         "- Chamomile tea or chamomile-infused oil as a toner",
#         "- Shea butter as a moisturizer",
#         "- Hyaluronic acid serum"
#     ],
#     "Preparation Process": "Olive Oil Face Wash: 1. Massage olive oil onto dry skin. 2. Gently wipe off with a warm, damp cloth. 3. Follow with chamomile-infused oil toner."
# },
# {
#     "Age Range": "Old Age (65+ years)",
#     "Skin Types": "Old Age - Combination",
#     "Skincare Product Specifications": [
#         "- Exfoliating scrub for mature, combination skin",
#         "- Diluted apple cider vinegar toner",
#         "- Lightweight anti-aging moisturizer",
#         "- Niacinamide serum for balance"
#     ],
#     "Avoid Harmful Chemicals": "Phthalates, artificial fragrances, propylene glycol",
#     "Approximate Price (USD)": {
#         "Face Scrub": "$8-12",
#         "Toner": "$8-12",
#         "Moisturizer": "$10-15",
#         "Serum": "$15-25",
#         "Sunscreen": "$10-15"
#     },
#     "Natural Treatment Products": [
#         "- Oatmeal scrub for face wash",
#         "- Apple cider vinegar as a toner",
#         "- Argan oil as a moisturizer",
#         "- Niacinamide serum"
#     ],
#     "Preparation Process": "Oatmeal Scrub: 1. Grind oatmeal into a powder. 2. Mix with water to form a paste. 3. Gently exfoliate and rinse. 4. Apply apple cider vinegar toner."
# }

#    #return recommendations

#     # Implement your recommendation logic here
#     # Use user_data and API data to generate skincare recommendations

#     # Example:
#     # recommendations = {
#     #     "home_remedies": ["Honey face mask", "Aloe vera gel"],
#     #     "product_specifications": ["Moisturizer with hyaluronic acid"],
#     #     "avoid_harmful_chemicals": ["Parabens", "Sulfates"]
#     # }

if __name__ == '__main__':
    app.run(debug=True)
