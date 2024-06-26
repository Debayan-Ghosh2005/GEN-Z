import google.generativeai as genai
import eel

api_key1 = "AIzaSyCjFhvLS3FG2JfFOyl1WqIBmH8qstbM_zA"
genai.configure(api_key = api_key1)

@eel.expose
def AI(query):
        try:
                generation_config = {
                "temperature": 0.9,
                "top_p": 1,
                "top_k": 1,
                "max_output_tokens": 400,
                }
                model = genai.GenerativeModel(model_name="gemini-pro",
                                        generation_config=generation_config)
                
                convo = model.start_chat()
                formatted_query = f'''
                                You are WellnessBot, a virtual mental health counselor dedicated to supporting individuals through their mental health journeys. Your role is to provide empathetic listening, evidence-based advice, and practical strategies for managing mental health issues. Your responses should be compassionate, non-judgmental, and tailored to the individual's needs.

                                Here is the user query:
                                {query}.

                                Your response:

                                '''
                convo.send_message(formatted_query)
                resp = (convo.last.text).replace('*', ' ')
                eel.handleChat(resp);
                print(resp)
                return resp;
        except:
               return "Try Again"



if __name__ == '__main__':
        while(True):
            message = input("Enter the message ");
            AI(message)
            if message == "exit":
                   exit(0);
