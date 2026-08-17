import streamlit as st
import pandas as pd
import numpy as np
import joblib

# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="Bahrain Rent Predictor",
    page_icon="🏠",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =========================================================
# CUSTOM CSS
# =========================================================

st.markdown(
    """
    <style>
    .main {
        background-color: #f8fafc;
    }

    .block-container {
        padding-top: 2rem;
        padding-bottom: 3rem;
        max-width: 1200px;
    }

    .hero {
        padding: 2.2rem;
        border-radius: 24px;
        background: linear-gradient(
            135deg,
            #0f172a 0%,
            #1e293b 50%,
            #334155 100%
        );
        color: white;
        margin-bottom: 2rem;
    }

    .hero h1 {
        font-size: 3rem;
        margin-bottom: 0.3rem;
    }

    .hero p {
        font-size: 1.15rem;
        color: #cbd5e1;
    }

    .metric-card {
        background: white;
        padding: 1.2rem;
        border-radius: 18px;
        border: 1px solid #e2e8f0;
        text-align: center;
        box-shadow: 0 4px 14px rgba(0,0,0,0.04);
    }

    .prediction-value {
        font-size: 3.5rem;
        font-weight: 800;
        color: #111827;
        line-height: 1.1;
    }

    .small-text {
        color: #94a3b8;
        font-size: 0.9rem;
    }

    div[data-testid="stSidebar"] {
        background-color: #f1f5f9;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# =========================================================
# LOAD MODEL
# =========================================================

@st.cache_resource
def load_model():
    return joblib.load("bahrain_rent_model.pkl")


try:
    model = load_model()
except Exception:
    st.error(
        "⚠️ Model file not found. Please make sure "
        "`bahrain_rent_model.pkl` is in the same folder as the app."
    )
    st.stop()

# =========================================================
# OPTIONS
# =========================================================

areas = [
    "Al Juffair",
    "Seef",
    "Saar",
    "Janabiya",
    "Hidd",
    "Amwaj Islands",
    "Busaiteen",
    "Mahooz",
    "Adliya",
    "Reef Island",
    "Um Al Hasam",
    "Zinj",
    "Sanabis",
    "Diyar Al Muharraq",
    "Tubli",
    "Hamala",
    "Bahrain Bay",
    "Al Burhama",
    "Bahrain Financial Harbour",
    "Segaya",
    "Budaiya",
    "Al Jasra",
    "Barbar",
    "Galali",
    "Arad",
    "Dilmunia Island",
    "Abraj Al Lulu",
    "Salmaniya",
    "Jid Ali",
    "Manama",
    "Muharraq",
    "Riffa",
    "Unknown"
]

governorates = [
    "Capital Governorate",
    "Muharraq Governorate",
    "Northern Governorate",
    "Southern Governorate"
]

property_types = [
    "Apartment",
    "Villa",
    "Penthouse",
    "Townhouse",
    "Duplex",
    "Compound",
    "Other"
]

agencies = [
    "Other",
    "Al Bariq Real Estate",
    "Casa Lusso Real Estate",
    "Kensington Real Estate",
    "Best Buy Real Estate",
    "Paradise House Real Estate",
    "Arizona Homes Real Estate",
    "AlWard Real Estate",
    "San Siro Real Estate"
]

# =========================================================
# HERO
# =========================================================

st.markdown(
    """
    <div class="hero">
        <h1>🏠 Bahrain Rent Predictor</h1>
        <p>
            Estimate the monthly rental price of a property in Bahrain
            using a machine learning model trained on property listings.
        </p>
    </div>
    """,
    unsafe_allow_html=True
)

# =========================================================
# MODEL PERFORMANCE
# =========================================================

c1, c2, c3, c4 = st.columns(4)

with c1:
    st.markdown(
        """
        <div class="metric-card">
            <h4>🤖 Model</h4>
            <h3>XGBoost</h3>
            <p class="small-text">Tuned Model</p>
        </div>
        """,
        unsafe_allow_html=True
    )

with c2:
    st.markdown(
        """
        <div class="metric-card">
            <h4>📈 Test R²</h4>
            <h3>77.9%</h3>
            <p class="small-text">Model performance</p>
        </div>
        """,
        unsafe_allow_html=True
    )

with c3:
    st.markdown(
        """
        <div class="metric-card">
            <h4>💰 Test MAE</h4>
            <h3>≈ BHD 99</h3>
            <p class="small-text">Average absolute error</p>
        </div>
        """,
        unsafe_allow_html=True
    )

with c4:
    st.markdown(
        """
        <div class="metric-card">
            <h4>🏘️ Project</h4>
            <h3>Real Estate</h3>
            <p class="small-text">Bahrain Market</p>
        </div>
        """,
        unsafe_allow_html=True
    )

st.markdown("---")

# =========================================================
# SIDEBAR
# =========================================================

st.sidebar.title("🏠 Property Details")
st.sidebar.caption("Enter the property information below.")

st.sidebar.markdown("### 📍 Location")

area = st.sidebar.selectbox(
    "Area",
    areas
)

governorate = st.sidebar.selectbox(
    "Governorate",
    governorates
)

agency = st.sidebar.selectbox(
    "Agency",
    agencies
)

st.sidebar.markdown("### 🏡 Property")

property_type = st.sidebar.selectbox(
    "Property Type",
    property_types
)

beds = st.sidebar.number_input(
    "Bedrooms",
    min_value=0,
    max_value=10,
    value=2,
    step=1
)

baths = st.sidebar.number_input(
    "Bathrooms",
    min_value=1,
    max_value=10,
    value=2,
    step=1
)

size_sqm = st.sidebar.number_input(
    "Size (sqm)",
    min_value=20,
    max_value=1500,
    value=100,
    step=5
)

amenities = st.sidebar.number_input(
    "Number of Amenities",
    min_value=0,
    max_value=30,
    value=3,
    step=1
)

include_we = st.sidebar.selectbox(
    "Utilities",
    [
        "Inclusive",
        "Exclusive",
        "Unknown"
    ]
)

season = st.sidebar.selectbox(
    "Availability Season",
    [
        "Winter",
        "Spring",
        "Summer",
        "Autumn",
        "Unknown"
    ]
)

st.sidebar.markdown("### ✨ Features")

col_a, col_b = st.sidebar.columns(2)

with col_a:
    sea_view = st.checkbox("🌊 Sea View")
    pool = st.checkbox("🏊 Pool")
    garden = st.checkbox("🌳 Garden")
    parking = st.checkbox("🚗 Parking")
    gym = st.checkbox("🏋️ Gym")
    balcony = st.checkbox("🌇 Balcony")

with col_b:
    luxury = st.checkbox("💎 Luxury")
    private = st.checkbox("🔐 Private")
    duplex = st.checkbox("🏠 Duplex")
    beach = st.checkbox("🏖️ Beach")
    modern = st.checkbox("✨ Modern")
    renovated = st.checkbox("🛠️ Renovated")

st.sidebar.markdown("### 🛋️ Furnishing")

furnished = st.sidebar.checkbox("Furnished")
semi_furnished = st.sidebar.checkbox("Semi-furnished")
unfurnished = st.sidebar.checkbox("Unfurnished")

# =========================================================
# PROPERTY SUMMARY
# =========================================================

st.subheader("🏡 Your Property")

summary1, summary2, summary3 = st.columns(3)

with summary1:
    st.info(
        f"**{property_type}**\n\n"
        f"{beds} Bedrooms • {baths} Bathrooms"
    )

with summary2:
    st.info(
        f"**{size_sqm:,} sqm**\n\n"
        f"{area}"
    )

with summary3:

    features_count = sum([
        sea_view,
        pool,
        garden,
        parking,
        gym,
        balcony,
        luxury,
        private,
        duplex,
        beach,
        modern,
        renovated
    ])

    furnishing_status = (
        "Furnished"
        if furnished
        else "Semi-furnished"
        if semi_furnished
        else "Unfurnished"
    )

    st.info(
        f"**{features_count} Special Features**\n\n"
        f"{furnishing_status}"
    )

# =========================================================
# FEATURE ENGINEERING
# =========================================================

def create_features():

    maid_room = 0

    is_studio = 1 if beds == 0 else 0

    total_rooms = beds + baths + maid_room

    size_per_room = (
        size_sqm / total_rooms
        if total_rooms > 0
        else size_sqm
    )

    baths_per_bed = (
        int(baths / beds)
        if beds > 0
        else 0
    )

    baths_7plus = 1 if baths >= 7 else 0

    available_now = 0

    agent_listing_count = 0

    return pd.DataFrame([{
        "Beds": beds,
        "Baths": baths,
        "Amenities": amenities,
        "Agent_listing_count": agent_listing_count,
        "Baths_7plus": baths_7plus,
        "Maid_room": maid_room,
        "Is_studio": is_studio,
        "Size_sqm": size_sqm,
        "Total_rooms": total_rooms,
        "Size_per_room": size_per_room,

        "Sea_View": int(sea_view),
        "Luxury": int(luxury),
        "Private": int(private),
        "Garden": int(garden),
        "Duplex": int(duplex),
        "Pool": int(pool),

        "Unfurnished": int(unfurnished),
        "Semi_furnished": int(semi_furnished),
        "Furnished": int(furnished),

        "Brand_new": 0,
        "Balcony": int(balcony),
        "Spacious": 0,
        "Modern": int(modern),
        "Prime_location": 0,
        "Gym": int(gym),
        "Beach": int(beach),
        "Compound": 0,
        "Navy_approved": 0,
        "Approved": 0,
        "EWA": 0,
        "Family": 0,
        "Renovated": int(renovated),
        "Parking": int(parking),

        "Available_now": available_now,
        "Baths_per_bed": baths_per_bed,

        "Property_type": property_type,
        "Include_w_e": include_we,
        "Governorate": governorate,
        "Agency": agency,
        "Area_grouped": area,
        "Season": season
    }])


# =========================================================
# PREDICTION
# =========================================================

st.markdown("### ✨ Ready to estimate?")

if st.button(
    "🔮 Predict Monthly Rent",
    use_container_width=True,
    type="primary"
):

    input_data = create_features()

    try:

        prediction = model.predict(input_data)[0]

        prediction = max(0, prediction)

        # -------------------------------------------------
        # CLEAN PREDICTION DISPLAY
        # -------------------------------------------------

        st.markdown(
            f'<div style="text-align:center; padding:1.5rem 0;">'
            f'<div style="font-size:1.1rem; color:#64748b;">'
            f'🏠 Estimated Monthly Rent'
            f'</div>'
            f'<div style="font-size:3.5rem; font-weight:800; color:#111827;">'
            f'BHD {prediction:,.0f}'
            f'</div>'
            f'<div style="font-size:0.9rem; color:#94a3b8;">'
            f'Estimated using the trained XGBoost model'
            f'</div>'
            f'</div>',
            unsafe_allow_html=True
        )

        # -------------------------------------------------
        # PREDICTION SUMMARY
        # -------------------------------------------------

        st.markdown("### 📋 Prediction Summary")

        result_col1, result_col2 = st.columns(2)

        with result_col1:

            st.write(
                "**Property:**",
                property_type
            )

            st.write(
                "**Location:**",
                area
            )

            st.write(
                "**Governorate:**",
                governorate
            )

        with result_col2:

            st.write(
                "**Size:**",
                f"{size_sqm:,} sqm"
            )

            st.write(
                "**Bedrooms:**",
                beds
            )

            st.write(
                "**Bathrooms:**",
                baths
            )

        st.success(
            "💡 This prediction is an estimate. "
            "Actual rental prices may vary depending on "
            "market conditions and property details."
        )

    except Exception as e:

        st.error("Prediction failed.")
        st.exception(e)

# =========================================================
# ABOUT MODEL
# =========================================================

st.markdown("---")

with st.expander("🤖 About the Model"):

    st.write(
        """
        This application uses a tuned XGBoost regression model
        developed for Bahrain property rental price prediction.

        Several regression algorithms were compared before selecting
        XGBoost as the final model.
        """
    )

    st.markdown(
        """
        **Final Test Performance**

        - MAE: **99.06 BHD**
        - RMSE: **183.99 BHD**
        - R²: **0.779**
        """
    )

# =========================================================
# TOP FEATURES
# =========================================================

with st.expander("📊 What Influences Rent?"):

    feature_data = pd.DataFrame({
        "Feature": [
            "Bathrooms",
            "Location",
            "Studio / Property Layout",
            "Total Rooms",
            "Property Type",
            "Property Size",
            "Sea View",
            "Furnishing"
        ],
        "Role": [
            "Strong influence",
            "Strong influence",
            "Important",
            "Important",
            "Important",
            "Important",
            "Can affect price",
            "Can affect price"
        ]
    })

    st.dataframe(
        feature_data,
        use_container_width=True,
        hide_index=True
    )

# =========================================================
# FOOTER
# =========================================================

st.markdown(
    """
    <div style="
        text-align:center;
        padding:2rem 0 1rem 0;
        color:#64748b;
    ">

        🏠 <b>Bahrain Rent Predictor</b>

        <br><br>

        Built with Python • XGBoost • Streamlit

        <br><br>

        <small>
        Data Science Project
        </small>

    </div>
    """,
    unsafe_allow_html=True
)
