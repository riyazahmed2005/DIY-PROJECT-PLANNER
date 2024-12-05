from django.shortcuts import render
import google.generativeai as genai

def chat_view(request):
    response_text = ""
    
    if request.method == "POST":
        prompt = request.POST.get('prompt', '')
        if prompt:
            genai.configure(api_key="AIzaSyDyHSktxPtcOk8w2h16phzpKwkjvgDBncU")
            model = genai.GenerativeModel("gemini-1.5-flash")
            response = model.generate_content(f"give me the Title , description , material required ,steps to implement and butget(INR) for my project {prompt}")
            response_text = response.text

    return render(request, 'bot.html', {'response': response_text})
