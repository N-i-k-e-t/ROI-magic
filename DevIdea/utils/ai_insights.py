import openai
import os
from typing import Dict, List

class AIPropertyAnalyst:
    def __init__(self):
        """Initialize the OpenAI client"""
        self.client = openai.OpenAI()

    def get_location_insights(self, city: str, area: str) -> Dict[str, str]:
        """Get AI-powered insights about a specific location"""
        prompt = f"""Analyze the real estate market for {area}, {city}, India. Focus on:
        1. Key advantages of this location
        2. Major development projects nearby
        3. Return potential
        4. Investment risks
        
        Provide a JSON response with these keys:
        - advantages
        - developments
        - potential
        - risks
        Make each response concise, about 20-30 words.
        """
        
        try:
            response = self.client.chat.completions.create(
                model="gpt-4o",  # the newest OpenAI model is "gpt-4o" which was released May 13, 2024
                messages=[{
                    "role": "user",
                    "content": prompt
                }],
                response_format={"type": "json_object"}
            )
            return eval(response.choices[0].message.content)
        except Exception as e:
            return {
                "advantages": "Analysis temporarily unavailable",
                "developments": "Information unavailable",
                "potential": "Calculation unavailable",
                "risks": "Risk assessment unavailable"
            }

    def get_investment_recommendations(self, property_data: Dict) -> Dict[str, str]:
        """Generate investment recommendations based on property data"""
        prompt = f"""Analyze this property investment opportunity:
        Location: {property_data['area']}, {property_data['city']}
        Price: ₹{property_data['price']:,}
        Size: {property_data['size']} sq ft
        Expected Rental: ₹{property_data['rental']:,}/month
        
        Provide investment recommendations in JSON format with these keys:
        - summary
        - pros
        - cons
        - action
        Keep each point concise, about 20-30 words.
        """
        
        try:
            response = self.client.chat.completions.create(
                model="gpt-4o",  # the newest OpenAI model is "gpt-4o" which was released May 13, 2024
                messages=[{
                    "role": "user",
                    "content": prompt
                }],
                response_format={"type": "json_object"}
            )
            return eval(response.choices[0].message.content)
        except Exception as e:
            return {
                "summary": "Analysis temporarily unavailable",
                "pros": "Information unavailable",
                "cons": "Information unavailable",
                "action": "Please try again later"
            }
