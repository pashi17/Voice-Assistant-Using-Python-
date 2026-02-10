# Requirements - Enhanced Citizen Services Chatbot

## Project Overview
Enhanced AI Citizen Services Chatbot for India's Digital India Initiative - A multilingual voice-enabled chatbot for assisting citizens with government service forms and offline information.

---

## System Requirements

### Operating System
- **Windows 10+** (with SAPI5 text-to-speech support)
- **macOS 10.12+** (with native TTS)
- **Linux** (Ubuntu 18.04+, Fedora 30+)

### Hardware Requirements
- **Processor**: Intel/AMD Dual Core or equivalent
- **RAM**: Minimum 2GB (4GB recommended)
- **Storage**: 500MB free space for application and cache
- **Microphone**: Required for voice input/speech recognition
- **Internet**: Optional (Offline mode supported)

### Python Version
- **Python 3.7** or higher
- **Python 3.9+** recommended for better compatibility

---

## Python Dependencies

### Core Libraries
```
pyttsx3==2.90              # Text-to-speech engine
SpeechRecognition==3.10.0  # Voice input/speech recognition
requests==2.28.0           # HTTP library for internet connectivity check
```

### Required for Speech Recognition
- **Google Speech Recognition API** (free tier, requires internet for full functionality)
- **Microphone access** (via pyaudio indirectly)

### Data & File Handling
```
pathlib                    # Path handling (built-in)
json                       # JSON serialization (built-in)
```

### Standard Library Modules (Built-in)
- `datetime` - Date/time handling
- `webbrowser` - Web browser integration
- `os` - Operating system operations
- `platform` - Platform detection
- `random` - Random selection
- `pathlib` - Cross-platform path handling

---

## Installation Instructions

### Step 1: Clone/Download Repository
```bash
git clone <repository-url>
cd citizen-services-chatbot
```

### Step 2: Create Virtual Environment (Recommended)
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

**Or install individually:**
```bash
pip install pyttsx3==2.90
pip install SpeechRecognition==3.10.0
pip install requests==2.28.0
```

### Step 4: Platform-Specific Setup

#### Windows
- SAPI5 is built-in (no additional installation needed)
- Ensure microphone is enabled in Sound Settings

#### macOS
```bash
brew install python-tkinter
```

#### Linux (Ubuntu/Debian)
```bash
sudo apt-get install python3-pyaudio
sudo apt-get install espeak
pip install pyttsx3
```

#### Linux (Fedora/RHEL)
```bash
sudo dnf install python3-pyaudio
sudo dnf install espeak
pip install pyttsx3
```

---

## API Requirements

### Google Speech Recognition API
- **Status**: Free (with rate limits)
- **Authentication**: None required for basic usage
- **Internet**: Required
- **Rate Limit**: ~50 requests per minute per IP

### Optional: Twilio API (for SMS/WhatsApp)
- **API Key**: Required for production SMS/WhatsApp features
- **Setup**: Add credentials in `send_sms()` and `send_whatsapp()` methods
- **Reference**: https://www.twilio.com/

---

## File Structure Requirements

```
citizen-services-chatbot/
├── main.py                          # Main application file
├── requirements.txt                 # Python dependencies
├── design.md                        # Architecture documentation
├── requirements.md                  # This file
├── README.md                        # Project overview
├── offline_cache.json              # Auto-generated offline data
└── forms/                          # Auto-created directory
    ├── aadhaar_data.json
    ├── passport_data.json
    └── voter_data.json
```

---

## Supported Languages

1. **English** (en)
   - Default language
   - Complete feature support

2. **Hindi** (hi)
   - Full Hindi translations
   - Devanagari script support
   - Text-to-speech in Hindi

3. **Tamil** (ta)
   - Basic Tamil translations
   - Tamil script support

4. **Telugu** (te)
   - Basic Telugu translations
   - Telugu script support

---

## Supported States & Services

### States Covered
1. Maharashtra
2. Delhi
3. Uttar Pradesh
4. Karnataka (placeholder)
5. Tamil Nadu (placeholder)

### Services Available
- **Aadhaar** - Aadhaar centers and enrollment
- **Passport** - Passport application assistance
- **Voter ID** - Voter registration forms
- **Driving License** - License information
- **PAN Card** - Income tax documentation
- **Education** - Scholarships and schemes
- **Health** - Health services information
- **Police** - Police service information
- **Tax Services** - Income tax assistance
- **Bills & Payments** - Utility bill payment
- **Grievance** - Complaint registration
- **Railway** - Railway services

---

## Feature Requirements

### Core Features
- ✅ Voice input via microphone
- ✅ Text-to-speech output
- ✅ Multilingual support (4 languages)
- ✅ Offline mode with cached data
- ✅ Form filling assistance
- ✅ State-specific services
- ✅ SMS/WhatsApp notifications (placeholder)

### Optional Features
- 📱 SMS integration (requires Twilio)
- 📱 WhatsApp integration (requires Twilio)
- 🌐 Online service linking
- 📊 User data persistence
- 📈 Usage analytics

---

## Performance Requirements

### Minimum Performance
- Speech recognition latency: < 5 seconds
- Text-to-speech response: < 2 seconds
- Form data save: < 1 second
- State lookup: < 500ms

### Network Requirements
- **Internet Check**: 2-second timeout
- **Google API**: Rate-limited to 50 req/min
- **Offline Fallback**: All features available without internet

---

## Security Requirements

### Data Protection
- ✅ Local JSON storage (encrypted file path recommended for production)
- ✅ No external API keys embedded (use environment variables for production)
- ✅ Input validation for phone numbers and emails
- ✅ Form data saved locally only

### Recommendations for Production
- Use `python-dotenv` for API key management
- Implement HTTPS for any online service integration
- Add user authentication
- Encrypt sensitive data in offline_cache.json
- Implement audit logging

### Production Security Setup
```bash
pip install python-dotenv
# Create .env file with:
# TWILIO_AUTH_TOKEN=your_token
# GOOGLE_API_KEY=your_key
```

---

## Testing Requirements

### Unit Testing
```bash
pip install pytest==7.0.0
pip install pytest-cov==3.0.0
```

### Voice Testing
- Microphone input validation
- Speech recognition accuracy testing
- Text-to-speech output verification
- Language translation accuracy

---

## Deployment Requirements

### Docker
```dockerfile
FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["python", "main.py"]
```

### Cloud Platforms
- **AWS**: EC2 with audio support
- **Google Cloud**: Compute Engine with API credentials
- **Azure**: Virtual Machine with speech services

---

## Browser/UI Requirements (if web version added)

- Modern browser supporting Web Audio API
- WebRTC for microphone access
- JavaScript ES6+ support
- Responsive design for mobile (320px+)

---

## Database Requirements (if scaled)

### Optional: For Production Scaling
- **PostgreSQL 12+** (for user data)
- **Redis 6.0+** (for caching)
- **MongoDB 4.4+** (for form data)

---

## Dependencies Summary Table

| Dependency | Version | Purpose | Platform |
|-----------|---------|---------|----------|
| pyttsx3 | 2.90 | Text-to-speech | All |
| SpeechRecognition | 3.10.0 | Voice input | All |
| requests | 2.28.0 | Network check | All |
| Google TTS API | Free | Speech recognition | All (needs internet) |
| SAPI5 | Built-in | TTS engine | Windows |
| espeak | OS package | TTS engine | Linux |
| AVFoundation | Built-in | TTS engine | macOS |

---

## Known Limitations

1. **Speech Recognition**: Requires internet for Google API (unless offline alternatives implemented)
2. **Language Support**: Limited to 4 languages (expandable)
3. **State Coverage**: Only 3 states fully populated with data
4. **SMS/WhatsApp**: Requires Twilio API credentials (currently placeholder)
5. **Audio Output**: SAPI5 on Windows may have voice quality limitations
6. **Background Noise**: Sensitive to ambient noise (configurable via `adjust_for_ambient_noise()`)

---

## Troubleshooting

### Common Issues

**Issue: "ModuleNotFoundError: No module named 'pyttsx3'"**
- Solution: `pip install pyttsx3`

**Issue: "No module named 'speech_recognition'"**
- Solution: `pip install SpeechRecognition`

**Issue: "Microphone not found"**
- Solution: Check system microphone permissions and audio input device

**Issue: "Internet connectivity check fails"**
- Solution: Check internet connection; app will enter offline mode

**Issue: "Voice not working on Linux"**
- Solution: Install espeak: `sudo apt-get install espeak`

---

## Contributing Requirements

- Python code must follow PEP 8
- Add docstrings to all functions
- Include unit tests for new features
- Support multilingual strings
- Test on Windows, macOS, and Linux

---

## Maintenance & Support

### Version History
- **v1.0** - Initial release with core features
- **v1.1** - Added offline mode
- **v1.2** - Added multilingual support
- **v2.0** - Enhanced form assistance

### Support Contact
For issues, feature requests, or contributions, please contact the development team.

---

**Last Updated**: February 2025
**Maintainer**: Digital India Initiative Team
