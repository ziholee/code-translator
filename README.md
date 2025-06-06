
# 📄 Code Translator

**Code Translator**는 C, Python, Java, C++ 등의 다양한 프로그래밍 언어 간의 코드 변환을 도와주는 AI 기반 도구입니다. OpenAI의 GPT 모델을 활용하여, 작성된 코드를 원하는 언어로 자연스럽고 정확하게 변환해줍니다.

## 🚀 주요 기능

- ✅ C, C++, Python, Java 등 다양한 언어 간 변환 지원  
- ✅ OpenAI API 기반의 정확한 코드 이해 및 재작성  
- ✅ CLI(Command Line Interface)로 간편한 사용  
- ✅ 향후 Google Gemini 등 대체 AI 모델로 확장 가능

## 💻 사용 방법

기본적으로 OpenAI API를 사용합니다. Google Gemini API를 사용하려면 `--api gemini` 옵션을 추가하세요.

```bash
python translator.py --file <변환할_파일명> --to <타겟_언어> [--api <openai|gemini>]
```

예시:
- OpenAI 사용 (기본값):
```bash
python translator.py --file sample.c --to python
```
- Google Gemini 사용:
```bash
python translator.py --file sample.c --to python --api gemini
```

## 📦 설치 방법

1. 의존성 설치:
```bash
pip install -r requirements.txt
```

2. `.env` 파일에 API 키 추가:
   - OpenAI API를 사용하려면:
     ```
     OPENAI_API_KEY=your_openai_api_key_here
     ```
   - Google Gemini API를 사용하려면:
     ```
     GOOGLE_API_KEY=your_google_api_key_here
     ```
   두 API 중 하나 또는 둘 다 설정할 수 있습니다. 사용할 API는 실행 시 `--api` 옵션으로 선택합니다.

3. 변환기 실행!

## 🧠 변환 언어 지원

| From | To |
|------|----|
| C    | Python, Java, C++ |
| Python | Java, C++ |
| ...  | ... (계속 확장 가능) |

## 🔧 향후 계획

- [x] Google Gemini API 지원 추가  
- [ ] GUI 기반 웹 인터페이스  
- [ ] 다양한 언어 스타일 옵션 추가 (함수형, 객체지향 등)
