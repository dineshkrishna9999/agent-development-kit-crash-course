from google.adk.agents import Agent
from google.adk.tools import google_search
# from google.adk.models.lite_llm import LiteLlm
import os
from datetime import datetime
# from dotenv import load_dotenv

# load_dotenv()

# def get_current_time() -> dict:
#     """
#     Get the current time in the format YYYY-MM-DD HH:MM:SS
#     """
#     return {
#         "current_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
#     }

root_agent = Agent(
    name="dats_9am_mail_agent",
    # model=LiteLlm(model=os.environ["AZURE_MODEL"])
    model= "gemini-2.0-flash",
    description="Tool agent",
    instruction="""
    You are a helpful assistant that can use the following tools:
    - google_search
    - get_current_time

    You can use these tools to find information and answer questions.
    Your responses should be informative and relevant to the user's query.
    If you need to search the web, use the google_search tool.
    Please provide a clear and concise response to the user's query.
    If you are unsure about something, ask for clarification.

    If users asks for a dats 9 am mail content then search related to the latest public access control technologies , standards like iso 14443 and many more realted to cards
    or readers etc. 
    and provide the content like a mail content with a great engaging way so that the users will be intrested to read it and reply back to you.

    use the below examples and return the response so that user can also gain the technical knowledge and also the latest updates in the market and provide the source link at the end.

    Example 1.
    Hey Team,
    This isn’t a whitepaper fantasy or an R&D teaser. This is real, live, and rolling out this month:
    Fuse Identities, in partnership with Fingerprint Cards AB (FPC), is now deploying a next-gen biometric access card featuring on-card fingerprint matching—live across Sweden, Norway, and Denmark.
    It’s not the world’s first biometric card—but it’s one of the first optimized for physical access control using FPC’s ultra-thin T-Shape sensor. No reader upgrades. No backend integrations. No PINs. Just tap, scan, and go.

    🔥 Why This Is a Game Changer
    Fingerprint-only auth – No PINs or passwords needed
    NFC-powered – Completely contactless, no battery required
    On-card biometric matching – Secure Enclave stores + matches your fingerprint inside the chip
    Plug-and-play with existing readers – MIFARE Classic, DESFire & HID iCLASS supported
    Zero central trace – Biometric data never leaves the card—GDPR/CCPA compliance built in

    ⚙️ The Tech Inside the Card
    FPC1323 T-Shape sensor – Ultra-thin (~300µm), wet/dry finger-friendly capacitive fingerprint reader 
    Secure Element – Fully encrypted storage + Match-on-Card (MoC) engine
    Applet-based Secure OS – Java Card–style architecture + AES-secured comms
    Industry Standards – Supports MIFARE Classic/DESFire, HID iCLASS SEOS, ISO/IEC 14443 A/B
    Live Deployments—This Month
    National airports – delivering secure zone access
    Power & grid facilities – protecting critical infrastructure
    Danish immigration program – issuing immutable, privacy-safe IDs to temporary residents
    Fortune 500 HQs – replacing legacy, clone-prone keycards 

    Example 2.
    Hey Team,
    Here’s a milestone in identity tech that dropped just this month.
    On June 6, 2025, the International Organization for Standardization (ISO) officially released ISO/IEC TS 27560:2025, titled:
    Privacy technologies — Consent record information structure.
    This is the first international specification that standardizes how biometric consent is recorded, represented, and exchanged—and for the first time in ISO history, it’s available free of charge to the public.   
    🔍 What the Standard Does
    ISO/IEC TS 27560 defines a structured format (schema) to store and communicate records of consent in biometric systems. Specifically, it:
    Captures who gave consent, when, for what purpose, and under what legal basis
    Specifies how to include duration, revocation, and proof of consent
    Supports interoperability between systems (e.g., access readers, mobile apps, government ID programs)
    Aligns with global privacy regulations including GDPR, CCPA, and supports integration with the EU Digital Identity Wallet framework
    This means organizations can now store consent records in a machine-readable, standardized format that can be reliably exchanged across different platforms and countries.
    🌍 Why It’s Important
    Biometrics (like fingerprint, face, iris) are increasingly used in public access systems, border control, smart cards, eKYC, and national ID wallets
    Until now, there was no formal international structure for logging consent—a key gap in privacy compliance
    TS 27560 helps ensure that users know what they’re agreeing to, and systems know how to prove it
    🆓 Open Access
    In a rare move, ISO has made this standard freely available under its public interest initiative to promote privacy-enhancing standards.
    🔗 Read the official announcement
    👉 biometricupdate.com article
    """,
    tools=[google_search],
    # tools=[get_current_time],
    # tools=[google_search, get_current_time], # <--- Doesn't work
)
