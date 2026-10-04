import streamlit as st
import pandas as pd
import os
from openai import OpenAI
from io import BytesIO
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4

# =========================================================
# PAGE CONFIGURATION
# =========================================================

st.set_page_config(
    page_title="Lean Business Model Canvas Automation Tool",
    page_icon="🚀",
    layout="wide"
)

# =========================================================
# TITLE
# =========================================================

st.title("🚀 Lean Business Model Canvas Automation Tool")

st.write(
    "AI-assisted startup analysis, Lean Canvas generation, "
    "confidence assessment and business model recommendations."
)

st.divider()

# =========================================================
# STARTUP INPUT
# =========================================================

st.header("1. Startup Information")

startup_name = st.text_input(
    "Startup Name",
    value="CampusBite"
)

industry = st.text_input(
    "Industry",
    value="FoodTech / Student Services"
)

# =========================================================
# INDUSTRY-SPECIFIC TEMPLATE
# =========================================================

industry_template = st.selectbox(
    "Industry-Specific Template",
    [
        "General",
        "EdTech",
        "FinTech",
        "Retail",
        "EV",
        "FoodTech"
    ],
    index=5
)

industry_templates = {
    "General": {
        "Problem Focus": "Identify the most important customer problem and its frequency/severity.",
        "Customer Focus": "Define the primary customer, buyer, user and early adopter.",
        "UVP Focus": "State a clear benefit and explain how the offering is different.",
        "Revenue Focus": "Identify the primary revenue stream and validate willingness to pay.",
        "Key Metrics": "Customers, conversion, retention, revenue and acquisition cost."
    },
    "EdTech": {
        "Problem Focus": "Learning gaps, lack of personalized support, engagement or access to quality learning.",
        "Customer Focus": "Students/learners; distinguish user, payer and institutional buyer where applicable.",
        "UVP Focus": "Learning outcome, personalization, affordability, convenience or measurable improvement.",
        "Revenue Focus": "Subscription, course fee, freemium, institutional licensing or other validated model.",
        "Key Metrics": "Active learners, completion rate, engagement, conversion, retention and learning outcomes."
    },
    "FinTech": {
        "Problem Focus": "Payments, access to financial services, affordability, financial management or transaction friction.",
        "Customer Focus": "Define the user, payer and regulated/institutional stakeholders clearly.",
        "UVP Focus": "Convenience, accessibility, cost reduction, speed, transparency or trust.",
        "Revenue Focus": "Subscription, transaction fee, commission, interest-related model or partnership revenue, subject to validation.",
        "Key Metrics": "Active users, transactions, conversion, retention, transaction value and acquisition cost."
    },
    "Retail": {
        "Problem Focus": "Product discovery, price, convenience, availability, delivery or shopping experience.",
        "Customer Focus": "Define shopper, buyer and repeat customer segments.",
        "UVP Focus": "Selection, price, convenience, personalization, trust or differentiated shopping experience.",
        "Revenue Focus": "Product margin, commission, subscription, delivery fee or advertising, subject to validation.",
        "Key Metrics": "Orders, average order value, conversion, repeat purchase, retention and customer acquisition cost."
    },
    "EV": {
        "Problem Focus": "EV affordability, charging access, range concerns, maintenance or adoption barriers.",
        "Customer Focus": "Define vehicle owner, fleet operator, buyer or charging user.",
        "UVP Focus": "Lower operating friction, charging convenience, affordability, reliability or accessibility.",
        "Revenue Focus": "Vehicle/service sales, charging fees, subscription, maintenance or platform commission, subject to validation.",
        "Key Metrics": "Users, charging sessions, utilization, conversion, repeat usage, revenue and acquisition cost."
    },
    "FoodTech": {
        "Problem Focus": "Food affordability, reliability, convenience, quality or access.",
        "Customer Focus": "Define the student/user, payer and food-provider relationship.",
        "UVP Focus": "Affordability, convenience, reliability, meal flexibility and verified providers.",
        "Revenue Focus": "Subscriptions, provider commissions, delivery charges or premium plans, subject to validation.",
        "Key Metrics": "Subscriptions, orders, repeat orders, retention, churn, revenue and acquisition cost."
    }
}

selected_template = industry_templates[industry_template]

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
    ],
    index=0
)

# =========================================================
# CUSTOMER
# =========================================================

st.header("2. Customer Segments")

customer_segment = st.text_area(
    "Target Customers",
    value=(
        "College students living in hostels, PGs "
        "and rented accommodation."
    )
)

early_adopter = st.text_area(
    "Early Adopter",
    value=(
        "College students who regularly struggle to find "
        "affordable and reliable everyday meals."
    )
)

# =========================================================
# PROBLEM
# =========================================================

st.header("3. Problem")

problem = st.text_area(
    "Core Problem",
    value=(
        "College students living away from home may find it "
        "difficult to access affordable, reliable and convenient "
        "everyday meals."
    )
)

current_alternatives = st.text_area(
    "Current Alternatives",
    value=(
        "Restaurants, food delivery apps, college mess facilities, "
        "local food providers and cooking independently."
    )
)

# =========================================================
# VALUE PROPOSITION
# =========================================================

st.header("4. Unique Value Proposition")

value_proposition = st.text_area(
    "Unique Value Proposition",
    value=(
        "Affordable and flexible meal subscriptions designed "
        "specifically for college students."
    )
)

# =========================================================
# SOLUTION
# =========================================================

st.header("5. Solution")

solution = st.text_area(
    "Proposed Solution",
    value=(
        "A platform connecting college students with verified "
        "local food providers offering affordable weekly and "
        "monthly meal subscriptions."
    )
)

# =========================================================
# CHANNELS
# =========================================================

st.header("6. Channels")

channels = st.multiselect(
    "Customer Acquisition Channels",
    [
        "Instagram",
        "Social Media",
        "College Communities",
        "Student Ambassadors",
        "Referral Programs",
        "Google Search",
        "Paid Advertising",
        "College Partnerships",
        "WhatsApp"
    ],
    default=[
        "Instagram",
        "Social Media",
        "College Communities",
        "Student Ambassadors",
        "Referral Programs",
        "WhatsApp"
    ]
)

# =========================================================
# REVENUE
# =========================================================

st.header("7. Revenue Streams")

revenue_streams = st.multiselect(
    "Revenue Streams",
    [
        "Meal Subscriptions",
        "Commission from Food Providers",
        "Delivery Charges",
        "Premium Plans",
        "Advertising",
        "Partnership Revenue"
    ],
    default=[
        "Meal Subscriptions",
        "Commission from Food Providers",
        "Delivery Charges",
        "Premium Plans"
    ]
)

pricing = st.text_input(
    "Pricing Assumption",
    value="₹2,500 per month — initial hypothesis"
)

# =========================================================
# COST
# =========================================================

st.header("8. Cost Structure")

cost_structure = st.multiselect(
    "Major Costs",
    [
        "Technology",
        "Food Provider Payments",
        "Delivery",
        "Marketing",
        "Customer Support",
        "Employee Salaries",
        "Payment Gateway Fees",
        "Administration"
    ],
    default=[
        "Technology",
        "Food Provider Payments",
        "Delivery",
        "Marketing",
        "Customer Support",
        "Employee Salaries",
        "Payment Gateway Fees"
    ]
)

# =========================================================
# KEY METRICS
# =========================================================

st.header("9. Key Metrics")

key_metrics = st.multiselect(
    "Key Metrics",
    [
        "Number of Customers",
        "Monthly Revenue",
        "Customer Acquisition Cost",
        "Customer Retention",
        "Churn Rate",
        "Average Revenue per Customer",
        "Number of Subscriptions",
        "Conversion Rate",
        "Repeat Orders"
    ],
    default=[
        "Number of Customers",
        "Monthly Revenue",
        "Customer Acquisition Cost",
        "Customer Retention",
        "Churn Rate",
        "Number of Subscriptions",
        "Conversion Rate"
    ]
)

# =========================================================
# COMPETITION
# =========================================================

st.header("10. Competitors & Alternatives")

competitors = st.text_area(
    "Competitors / Alternatives",
    value=(
        "Food delivery apps, local restaurants, college mess "
        "facilities, local tiffin providers and self-cooking."
    )
)

# =========================================================
# EVIDENCE
# =========================================================

st.header("11. Available Evidence")

evidence = st.text_area(
    "Evidence Available",
    value=(
        "No primary customer evidence collected yet. "
        "These are initial founder hypotheses requiring validation."
    )
)

# =========================================================
# ASSUMPTIONS
# =========================================================

st.header("12. Business Assumptions")

assumptions = st.text_area(
    "Important Assumptions",
    value=(
        "Students need affordable everyday meals.\n"
        "Students are willing to use meal subscriptions.\n"
        "Students are willing to pay for the service.\n"
        "Students value convenient meal plans.\n"
        "Local food providers are willing to partner with CampusBite."
    )
)

# =========================================================
# STEP 7 – AI COMPETITOR ANALYSIS
# =========================================================

# -----------------------------------------------------
# AI COMPETITOR ANALYSIS
# -----------------------------------------------------

st.subheader("🔎 AI Competitor Analysis")

st.caption(
    "Enter competitor names and verified research evidence. "
    "The AI summarizes the supplied evidence; it does not invent competitor facts."
)

competitor_names = st.text_area(
    "Competitor Names / Alternatives",
    value=competitors,
    key="step7_competitor_names"
)

competitor_evidence = st.text_area(
    "Competitor Research Evidence",
    placeholder=(
        "Paste verified information collected from sources such as "
        "Crunchbase, company websites, annual reports or other research sources. "
        "Example: company name, product, target customer, funding information, "
        "pricing information and source URL."
    ),
    key="step7_competitor_evidence"
)

if st.button("🔍 Analyze Competitors with AI"):
    api_key = os.getenv("OPENAI_API_KEY")

    if not api_key:
        st.warning(
            "OPENAI_API_KEY is not configured. Add the API key in your "
            "Streamlit secrets/environment before using AI competitor analysis."
        )
    elif not competitor_names.strip():
        st.warning("Please enter at least one competitor or alternative.")
    elif not competitor_evidence.strip():
        st.warning(
            "Please provide research evidence first. "
            "The tool will not invent competitor facts."
        )
    else:
        competitor_prompt = f"""
You are analyzing competitors for the startup {startup_name}.

Industry: {industry}
Geography: {geography}
Target Customer: {customer_segment}

Competitors / Alternatives:
{competitor_names}

VERIFIED RESEARCH EVIDENCE SUPPLIED BY THE USER:
{competitor_evidence}

Create a concise competitor analysis with:
1. Competitor
2. Target customer
3. Main offering
4. Evidence-based strengths
5. Evidence-based weaknesses or gaps
6. Potential differentiation opportunity for the startup
7. Evidence still required

STRICT RULES:
- Use only facts contained in the supplied research evidence.
- Do not invent funding, customers, pricing, market share, partnerships, traction or other facts.
- Clearly label interpretation as analysis/opportunity rather than verified fact.
- If evidence is missing, write "Evidence required".
"""

        try:
            client = OpenAI(api_key=api_key)
            response = client.responses.create(
                model=os.getenv("OPENAI_MODEL", "gpt-6-luna"),
                instructions=(
                    "Analyze competitor research conservatively. "
                    "Never fabricate competitor facts. Separate verified evidence "
                    "from interpretation and identify missing evidence."
                ),
                input=competitor_prompt
            )

            competitor_output = response.output_text

            st.markdown("### 📊 AI Competitor Analysis")
            st.markdown(competitor_output)

            st.download_button(
                label="📥 Download Competitor Analysis",
                data=competitor_output,
                file_name=f"{startup_name.lower().replace(' ', '_')}_competitor_analysis.txt",
                mime="text/plain"
            )

        except Exception as e:
            st.error(f"Competitor analysis could not be completed: {e}")

# =========================================================
# STEP 7 – COLLABORATION WORKSPACE
# =========================================================

st.divider()
st.subheader("👥 Collaboration Workspace")
st.caption(
    "Add team-member reviews, comments and action items while refining the startup canvas. "
    "This MVP demonstrates collaborative review; persistent multi-user cloud editing can be added later."
)

if "collaboration_records" not in st.session_state:
    st.session_state.collaboration_records = []

collab_col1, collab_col2 = st.columns(2)
with collab_col1:
    reviewer_name = st.text_input(
        "Team Member / Reviewer Name",
        placeholder="e.g., Swetaa"
    )
with collab_col2:
    reviewer_role = st.selectbox(
        "Role",
        ["Founder", "Team Member", "Mentor", "Reviewer", "Other"]
    )

collab_col3, collab_col4 = st.columns(2)
with collab_col3:
    review_block = st.selectbox(
        "Canvas Area Reviewed",
        [
            "Problem", "Customer Segments", "Unique Value Proposition",
            "Solution", "Channels", "Revenue Streams", "Cost Structure",
            "Key Metrics", "Unfair Advantage", "Overall Business Model"
        ]
    )
with collab_col4:
    review_status = st.selectbox(
        "Review Status",
        ["Comment", "Needs Validation", "Suggested Change", "Approved"]
    )

review_comment = st.text_area(
    "Comment / Suggested Action",
    placeholder="Enter the team's feedback, correction or next action..."
)

if st.button("➕ Add Team Review"):
    if not reviewer_name.strip():
        st.warning("Please enter the team member/reviewer name.")
    elif not review_comment.strip():
        st.warning("Please enter a comment or suggested action.")
    else:
        st.session_state.collaboration_records.append({
            "Team Member": reviewer_name.strip(),
            "Role": reviewer_role,
            "Canvas Area": review_block,
            "Status": review_status,
            "Comment / Action": review_comment.strip()
        })
        st.success("Team review added successfully.")

if st.session_state.collaboration_records:
    collaboration_df = pd.DataFrame(st.session_state.collaboration_records)
    st.markdown("### 📝 Team Review Log")
    st.dataframe(
        collaboration_df,
        use_container_width=True,
        hide_index=True
    )

    collaboration_csv = collaboration_df.to_csv(index=False)
    st.download_button(
        label="📥 Download Collaboration Review Log",
        data=collaboration_csv,
        file_name=f"{startup_name.lower().replace(' ', '_')}_collaboration_review.csv",
        mime="text/csv"
    )
else:
    st.info("No team reviews added yet. Add the first review above.")

# =========================================================
# BUILD LEAN CANVAS
# =========================================================

if st.button(
    "🚀 Generate Lean Canvas & Dashboard",
    use_container_width=True
):

    # -----------------------------------------------------
    # LEAN CANVAS
    # -----------------------------------------------------

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

    # -----------------------------------------------------
    # INDUSTRY TEMPLATE
    # -----------------------------------------------------

    st.subheader(f"🏭 {industry_template} Industry Template")

    template_df = pd.DataFrame(
        [
            ["Problem Focus", selected_template["Problem Focus"]],
            ["Customer Focus", selected_template["Customer Focus"]],
            ["UVP Focus", selected_template["UVP Focus"]],
            ["Revenue Focus", selected_template["Revenue Focus"]],
            ["Key Metrics", selected_template["Key Metrics"]]
        ],
        columns=["Template Area", "Recommended Focus"]
    )

    st.dataframe(
        template_df,
        use_container_width=True,
        hide_index=True
    )

    st.caption(
        "Template guidance is a starting hypothesis. It does not replace "
        "industry research or customer validation."
    )

    # -----------------------------------------------------
    # DASHBOARD HEADER
    # -----------------------------------------------------

    st.divider()

    st.header("📊 Lean Business Model Dashboard")

    col1, col2, col3, col4 = st.columns(4)

    col1.metric(
        "Startup",
        startup_name
    )

    col2.metric(
        "Industry",
        industry
    )

    col3.metric(
        "Canvas Blocks",
        "9"
    )

    col4.metric(
        "Initial Confidence",
        "Low"
    )

    # -----------------------------------------------------
    # LEAN CANVAS
    # -----------------------------------------------------

    st.subheader("🧩 Lean Canvas")

    canvas_df = pd.DataFrame(
        list(lean_canvas.items()),
        columns=[
            "Lean Canvas Block",
            "Current Hypothesis"
        ]
    )

    st.dataframe(
        canvas_df,
        use_container_width=True,
        hide_index=True
    )

    # -----------------------------------------------------
    # CONFIDENCE
    # -----------------------------------------------------

    confidence_data = []

    for block in lean_canvas:

        confidence = 20

        if block == "Unfair Advantage":
            confidence = 10

        confidence_data.append({
            "Block": block,
            "Confidence Score": confidence,
            "Evidence Status": "Mostly Assumption",
            "Validation Required": "Yes"
        })

    confidence_df = pd.DataFrame(confidence_data)

    st.subheader("📈 Confidence Analysis")

    st.dataframe(
        confidence_df,
        use_container_width=True,
        hide_index=True
    )

    # -----------------------------------------------------
    # RISK AREAS
    # -----------------------------------------------------

    st.subheader("⚠️ Initial Risk Areas")

    risk_data = [
        {
            "Risk Area": "Customer Need",
            "Risk Level": "High",
            "Reason": "No primary customer research yet."
        },
        {
            "Risk Area": "Willingness to Pay",
            "Risk Level": "High",
            "Reason": "Pricing has not been validated."
        },
        {
            "Risk Area": "Provider Partnership",
            "Risk Level": "High",
            "Reason": "Provider willingness to participate is untested."
        },
        {
            "Risk Area": "Delivery Economics",
            "Risk Level": "High",
            "Reason": "Actual delivery costs are not established."
        },
        {
            "Risk Area": "Acquisition Channels",
            "Risk Level": "Medium",
            "Reason": "Channels have not been tested."
        }
    ]

    risk_df = pd.DataFrame(risk_data)

    st.dataframe(
        risk_df,
        use_container_width=True,
        hide_index=True
    )

    # =====================================================
    # AI RECOMMENDATION ENGINE
    # =====================================================

    st.divider()

    st.header("🤖 AI Business Model Recommendations")

    st.caption(
        "AI recommendations are hypotheses and suggestions. "
        "They do not replace real customer or market evidence."
    )

    if st.button(
        "🤖 Generate AI Recommendations",
        use_container_width=True
    ):

        # -------------------------------------------------
        # GET API KEY
        # -------------------------------------------------

        api_key = os.getenv("OPENAI_API_KEY")

        if not api_key:

            st.error(
                "OPENAI_API_KEY was not found. "
                "Add your API key as an environment variable "
                "before using AI recommendations."
            )

        else:

            client = OpenAI(
                api_key=api_key
            )

            # -------------------------------------------------
            # PREPARE AI INPUT
            # -------------------------------------------------

            startup_context = f"""
Startup Name:
{startup_name}

Industry:
{industry}

Geography:
{geography}

Business Type:
{business_type}

Customer Segments:
{customer_segment}

Early Adopter:
{early_adopter}

Problem:
{problem}

Current Alternatives:
{current_alternatives}

Unique Value Proposition:
{value_proposition}

Solution:
{solution}

Channels:
{", ".join(channels)}

Revenue Streams:
{", ".join(revenue_streams)}

Pricing:
{pricing}

Cost Structure:
{", ".join(cost_structure)}

Key Metrics:
{", ".join(key_metrics)}

Competitors / Alternatives:
{competitors}

Available Evidence:
{evidence}

Assumptions:
{assumptions}
"""

            # -------------------------------------------------
            # AI INSTRUCTIONS
            # -------------------------------------------------

            instructions = """
You are a startup strategy consultant helping evaluate
an early-stage Lean Business Model Canvas.

Analyze the startup information provided.

Return a structured business-model analysis containing:

1. Lean Canvas improvements
2. Customer recommendations
3. Problem validation recommendations
4. Revenue stream improvements
5. Pricing validation recommendations
6. Channel recommendations
7. Cost structure considerations
8. Top 5 risky assumptions
9. Recommended validation experiments
10. Immediate next actions

IMPORTANT RULES:

- Clearly distinguish assumptions from evidence.
- Do not fabricate customers.
- Do not fabricate interviews.
- Do not fabricate survey results.
- Do not fabricate revenue.
- Do not fabricate market statistics.
- Do not claim competitors have specific information unless it
  was provided as evidence.
- Do not treat AI-generated suggestions as real-world evidence.
- Identify missing evidence.
- Recommend experiments for high-risk assumptions.
- Keep recommendations practical for an MBA/BBA entrepreneurship
  project.
"""

            # -------------------------------------------------
            # CALL OPENAI RESPONSES API
            # -------------------------------------------------

            try:

                response = client.responses.create(
                    model=os.getenv(
                        "OPENAI_MODEL",
                        "gpt-6-luna"
                    ),
                    instructions=instructions,
                    input=startup_context
                )

                ai_output = response.output_text

                # -------------------------------------------------
                # DISPLAY AI RESULT
                # -------------------------------------------------

                st.subheader(
                    "💡 AI Analysis"
                )

                st.markdown(
                    ai_output
                )

                # -------------------------------------------------
                # SAVE AI RESULT
                # -------------------------------------------------

                st.download_button(
                    label="📥 Download AI Recommendations",
                    data=ai_output,
                    file_name="campusbite_ai_recommendations.txt",
                    mime="text/plain"
                )

            except Exception as e:

                st.error(
                    f"AI analysis could not be completed: {e}"
                )

    # -----------------------------------------------------
    # DOWNLOAD LEAN CANVAS
    # -----------------------------------------------------

    st.divider()

    # DOWNLOAD CSV
    canvas_csv = canvas_df.to_csv(index=False)

    st.download_button(
        label="📥 Download Lean Canvas CSV",
        data=canvas_csv,
        file_name="campusbite_lean_canvas.csv",
        mime="text/csv"
    )

    # DOWNLOAD EXCEL
    excel_buffer = BytesIO()

    with pd.ExcelWriter(
        excel_buffer,
        engine="openpyxl"
    ) as writer:

        canvas_df.to_excel(
            writer,
            index=False,
            sheet_name="Lean Canvas"
        )

    excel_buffer.seek(0)

    st.download_button(
        label="📊 Download Lean Canvas Excel",
        data=excel_buffer,
        file_name="campusbite_lean_canvas.xlsx",
        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )

    # DOWNLOAD PDF
    pdf_buffer = BytesIO()

    pdf = SimpleDocTemplate(
        pdf_buffer,
        pagesize=A4,
        rightMargin=30,
        leftMargin=30,
        topMargin=30,
        bottomMargin=30
    )

    pdf_data = [
        ["Lean Canvas Block", "Current Hypothesis"]
    ]

    for _, row in canvas_df.iterrows():

        pdf_data.append([
            str(row["Lean Canvas Block"]),
            str(row["Current Hypothesis"])
        ])

    pdf_table = Table(
        pdf_data,
        colWidths=[130, 380]
    )

    pdf_table.setStyle(
        TableStyle([
            ("BACKGROUND", (0, 0), (-1, 0), colors.lightgrey),
            ("TEXTCOLOR", (0, 0), (-1, 0), colors.black),
            ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
            ("FONTNAME", (0, 1), (-1, -1), "Helvetica"),
            ("FONTSIZE", (0, 0), (-1, -1), 8),
            ("GRID", (0, 0), (-1, -1), 0.5, colors.grey),
            ("VALIGN", (0, 0), (-1, -1), "TOP"),
            ("LEFTPADDING", (0, 0), (-1, -1), 5),
            ("RIGHTPADDING", (0, 0), (-1, -1), 5),
            ("TOPPADDING", (0, 0), (-1, -1), 5),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
        ])
    )

    pdf.build([pdf_table])

    pdf_buffer.seek(0)

    st.download_button(
        label="📄 Download Lean Canvas PDF",
        data=pdf_buffer,
        file_name="campusbite_lean_canvas.pdf",
        mime="application/pdf"
    )