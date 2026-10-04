import streamlit as st
import pandas as pd

# ---------------------------------------------------
# PAGE CONFIGURATION
# ---------------------------------------------------

st.set_page_config(
    page_title="Lean Business Model Canvas Tool",
    page_icon="🚀",
    layout="wide"
)

# ---------------------------------------------------
# TITLE
# ---------------------------------------------------

st.title("🚀 Lean Business Model Canvas Automation Tool")

st.write(
    "Enter your startup information below to create a structured "
    "Lean Business Model Canvas input."
)

st.divider()

# ---------------------------------------------------
# STARTUP INFORMATION
# ---------------------------------------------------

st.header("1. Startup Information")

startup_name = st.text_input(
    "Startup Name",
    value="CampusBite"
)

industry = st.text_input(
    "Industry",
    value="FoodTech / Student Services"
)

geography = st.text_input(
    "Target Geography",
    value="Chennai, Tamil Nadu, India"
)

business_type = st.selectbox(
    "Business Type",
    [
        "B2C",
        "B2B",
        "B2B2C",
        "Marketplace",
        "Subscription",
        "Other"
    ]
)

# ---------------------------------------------------
# CUSTOMER SEGMENTS
# ---------------------------------------------------

st.header("2. Customer Segments")

customer_segment = st.text_area(
    "Who are your target customers?",
    value="College students living in hostels, PGs and rented accommodation."
)

early_adopter = st.text_area(
    "Who is your ideal early adopter?",
    placeholder="Example: College students who regularly struggle to find affordable everyday meals."
)

# ---------------------------------------------------
# PROBLEM
# ---------------------------------------------------

st.header("3. Problem")

problem = st.text_area(
    "What problem are you solving?",
    value=(
        "College students living away from home may find it difficult "
        "to access affordable, reliable and convenient everyday meals."
    )
)

current_alternatives = st.text_area(
    "How do customers currently solve this problem?",
    placeholder="Example: Restaurants, food delivery apps, mess facilities, local food providers, cooking themselves."
)

# ---------------------------------------------------
# VALUE PROPOSITION
# ---------------------------------------------------

st.header("4. Unique Value Proposition")

value_proposition = st.text_area(
    "What value do you provide?",
    value=(
        "Affordable and flexible meal subscriptions designed specifically "
        "for college students."
    )
)

# ---------------------------------------------------
# SOLUTION
# ---------------------------------------------------

st.header("5. Solution")

solution = st.text_area(
    "What is your proposed solution?",
    value=(
        "A platform connecting college students with verified local food "
        "providers offering affordable weekly and monthly meal subscriptions."
    )
)

# ---------------------------------------------------
# CHANNELS
# ---------------------------------------------------

st.header("6. Channels")

channels = st.multiselect(
    "How will customers find your startup?",
    [
        "Instagram",
        "Social Media",
        "College Communities",
        "Student Ambassadors",
        "Referral Programs",
        "Google Search",
        "Paid Advertising",
        "Partnerships with Colleges",
        "WhatsApp",
        "Food Delivery Platforms"
    ]
)

# ---------------------------------------------------
# REVENUE STREAMS
# ---------------------------------------------------

st.header("7. Revenue Streams")

revenue_streams = st.multiselect(
    "How will the startup make money?",
    [
        "Meal Subscription",
        "Commission from Food Providers",
        "Delivery Charges",
        "Premium Plans",
        "Advertising",
        "Partnership Revenue"
    ]
)

pricing = st.text_input(
    "What is your expected pricing?",
    placeholder="Example: ₹2,500 per month"
)

# ---------------------------------------------------
# COST STRUCTURE
# ---------------------------------------------------

st.header("8. Cost Structure")

cost_structure = st.multiselect(
    "What are your major costs?",
    [
        "Technology",
        "Food Provider Payments",
        "Delivery",
        "Marketing",
        "Customer Support",
        "Employee Salaries",
        "Payment Gateway Fees",
        "Administration"
    ]
)

# ---------------------------------------------------
# KEY METRICS
# ---------------------------------------------------

st.header("9. Key Metrics")

key_metrics = st.multiselect(
    "Which metrics will you track?",
    [
        "Number of Customers",
        "Monthly Revenue",
        "Customer Acquisition Cost (CAC)",
        "Customer Retention",
        "Churn Rate",
        "Average Revenue per Customer",
        "Number of Subscriptions",
        "Conversion Rate",
        "Repeat Orders"
    ]
)

# ---------------------------------------------------
# COMPETITORS
# ---------------------------------------------------

st.header("10. Competitors & Alternatives")

competitors = st.text_area(
    "Who are your competitors or alternatives?",
    placeholder="Enter competitor names or existing alternatives."
)

# ---------------------------------------------------
# EVIDENCE
# ---------------------------------------------------

st.header("11. Available Evidence")

evidence = st.text_area(
    "What evidence do you currently have?",
    placeholder=(
        "Example: Market research, customer interviews, surveys, "
        "competitor research, observations, etc."
    )
)

# ---------------------------------------------------
# ASSUMPTIONS
# ---------------------------------------------------

st.header("12. Important Assumptions")

assumptions = st.text_area(
    "What assumptions are you making about this business?",
    placeholder=(
        "Example: Students are willing to pay for monthly meal subscriptions."
    )
)

# ---------------------------------------------------
# GENERATE CANVAS
# ---------------------------------------------------

st.divider()

if st.button("🚀 Generate Lean Canvas", use_container_width=True):

    data = {
        "Startup Name": [startup_name],
        "Industry": [industry],
        "Geography": [geography],
        "Business Type": [business_type],
        "Customer Segments": [customer_segment],
        "Early Adopter": [early_adopter],
        "Problem": [problem],
        "Current Alternatives": [current_alternatives],
        "Unique Value Proposition": [value_proposition],
        "Solution": [solution],
        "Channels": [", ".join(channels)],
        "Revenue Streams": [", ".join(revenue_streams)],
        "Pricing Assumption": [pricing],
        "Cost Structure": [", ".join(cost_structure)],
        "Key Metrics": [", ".join(key_metrics)],
        "Competitors": [competitors],
        "Evidence": [evidence],
        "Assumptions": [assumptions]
    }

    df = pd.DataFrame(data)

    st.success("✅ Startup information collected successfully!")

    st.subheader("📋 Collected Startup Data")

    st.dataframe(
        df,
        use_container_width=True
    )

    # ------------------------------------------------
    # SAVE DATA
    # ------------------------------------------------

    csv = df.to_csv(index=False)

    st.download_button(
        label="📥 Download Startup Data",
        data=csv,
        file_name="campusbite_startup_input.csv",
        mime="text/csv"
    )

    st.info(
        "The collected information can now be used for "
        "Lean Canvas generation, assumption analysis and validation."
    )# ---------------------------------------------------
# LEAN BUSINESS MODEL CANVAS
# ---------------------------------------------------

st.divider()

st.header("🧩 Generate Lean Business Model Canvas")

if st.button("🧩 Build Lean Canvas", use_container_width=True):

    st.success("Lean Canvas generated successfully!")

    # ------------------------------------------------
    # LEAN CANVAS DATA
    # ------------------------------------------------

    lean_canvas = {
        "Problem": problem,

        "Customer Segments": customer_segment,

        "Unique Value Proposition": value_proposition,

        "Solution": solution,

        "Channels": ", ".join(channels),

        "Revenue Streams": ", ".join(revenue_streams),

        "Cost Structure": ", ".join(cost_structure),

        "Key Metrics": ", ".join(key_metrics),

        "Unfair Advantage":
            "Defensible advantage has not yet been established."
    }

    # ------------------------------------------------
    # DISPLAY LEAN CANVAS
    # ------------------------------------------------

    st.subheader("📋 CampusBite Lean Canvas")

    for block, content in lean_canvas.items():

        st.markdown(f"### {block}")

        st.info(content)

    # ------------------------------------------------
    # ASSUMPTION NOTICE
    # ------------------------------------------------

    st.warning(
        "⚠️ These Lean Canvas elements are initial business "
        "hypotheses and require real-world validation."
    )

    # ------------------------------------------------
    # CREATE LEAN CANVAS DATAFRAME
    # ------------------------------------------------

    canvas_df = pd.DataFrame(
        list(lean_canvas.items()),
        columns=["Lean Canvas Block", "Current Hypothesis"]
    )

    st.subheader("📊 Lean Canvas Data Table")

    st.dataframe(
        canvas_df,
        use_container_width=True
    )

    # ------------------------------------------------
    # DOWNLOAD LEAN CANVAS
    # ------------------------------------------------

    canvas_csv = canvas_df.to_csv(index=False)

    st.download_button(
        label="📥 Download Lean Canvas",
        data=canvas_csv,
        file_name="campusbite_lean_canvas.csv",
        mime="text/csv"
    )# ---------------------------------------------------
# EVIDENCE, CONFIDENCE & VALIDATION
# ---------------------------------------------------

st.divider()

st.header("🔎 Evidence & Validation Analysis")

if st.button("🔎 Analyze Evidence & Validation", use_container_width=True):

    evidence_analysis = {

        "Problem": {
            "Hypothesis": problem,
            "Evidence": "No primary customer research collected yet.",
            "Confidence": 20,
            "Validation Required": "Conduct customer interviews and surveys."
        },

        "Customer Segments": {
            "Hypothesis": customer_segment,
            "Evidence": "Initial founder assumption.",
            "Confidence": 20,
            "Validation Required": "Conduct customer research to identify the most affected student segment."
        },

        "Unique Value Proposition": {
            "Hypothesis": value_proposition,
            "Evidence": "Proposed value proposition; no customer validation yet.",
            "Confidence": 20,
            "Validation Required": "Test the value proposition through interviews and landing-page experiments."
        },

        "Solution": {
            "Hypothesis": solution,
            "Evidence": "Proposed solution based on the identified problem.",
            "Confidence": 20,
            "Validation Required": "Test the solution using a prototype or MVP."
        },

        "Channels": {
            "Hypothesis": ", ".join(channels),
            "Evidence": "Potential acquisition channels identified during initial planning.",
            "Confidence": 20,
            "Validation Required": "Test different channels and measure customer acquisition."
        },

        "Revenue Streams": {
            "Hypothesis": ", ".join(revenue_streams),
            "Evidence": "Initial revenue-model hypothesis.",
            "Confidence": 20,
            "Validation Required": "Conduct pricing tests and test willingness to pay."
        },

        "Cost Structure": {
            "Hypothesis": ", ".join(cost_structure),
            "Evidence": "Initial identification of potential business costs.",
            "Confidence": 20,
            "Validation Required": "Obtain actual supplier, technology, delivery and operating cost estimates."
        },

        "Key Metrics": {
            "Hypothesis": ", ".join(key_metrics),
            "Evidence": "Metrics selected based on the proposed business model.",
            "Confidence": 20,
            "Validation Required": "Track these metrics during pilot testing."
        },

        "Unfair Advantage": {
            "Hypothesis": "Defensible advantage has not yet been established.",
            "Evidence": "No defensible advantage has been validated yet.",
            "Confidence": 10,
            "Validation Required": "Research potential defensibility through technology, partnerships, data, brand or network effects."
        }
    }

    # ------------------------------------------------
    # CREATE DATAFRAME
    # ------------------------------------------------

    evidence_df = pd.DataFrame.from_dict(
        evidence_analysis,
        orient="index"
    ).reset_index()

    evidence_df.rename(
        columns={
            "index": "Lean Canvas Block"
        },
        inplace=True
    )

    # ------------------------------------------------
    # DISPLAY TABLE
    # ------------------------------------------------

    st.subheader("📊 Evidence & Confidence Assessment")

    st.dataframe(
        evidence_df,
        use_container_width=True
    )

    # ------------------------------------------------
    # CONFIDENCE INTERPRETATION
    # ------------------------------------------------

    st.subheader("📈 Confidence Interpretation")

    st.info(
        "0–25 = Mostly Assumption | "
        "26–50 = Some Research | "
        "51–75 = Moderate Evidence | "
        "76–100 = Stronger Evidence"
    )

    # ------------------------------------------------
    # DOWNLOAD
    # ------------------------------------------------

    evidence_csv = evidence_df.to_csv(index=False)

    st.download_button(
        label="📥 Download Evidence Analysis",
        data=evidence_csv,
        file_name="campusbite_evidence_confidence.csv",
        mime="text/csv"
    )

    st.warning(
        "⚠️ Confidence scores are based on the current evidence available. "
        "They do not replace real-world customer or market validation."
    )