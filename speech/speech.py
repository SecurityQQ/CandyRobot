from google.cloud import texttospeech
import os
from google.oauth2 import service_account
from random import randint

credentials = service_account.Credentials.from_service_account_file("C:/Users/dyako/Downloads/moscowhack-c25932a920be.json")

scoped_credentials = credentials.with_scopes(
    ['https://www.googleapis.com/auth/cloud-platform'])

# Instantiates a client
client = texttospeech.TextToSpeechClient(credentials=credentials)

def playsound(text, name):
	# Set the text input to be synthesized
	synthesis_input = texttospeech.types.SynthesisInput(text=text)

	# Build the voice request, select the language code ("en-US") and the ssml
	# voice gender ("neutral")
	voice = texttospeech.types.VoiceSelectionParams(
	    language_code='en-US',
	    name=name)

	# Select the type of audio file you want returned
	audio_config = texttospeech.types.AudioConfig(
	    audio_encoding=texttospeech.enums.AudioEncoding.MP3)

	# Perform the text-to-speech request on the text input with the selected
	# voice parameters and audio file type
	response = client.synthesize_speech(synthesis_input, voice, audio_config)

	# The response's audio_content is binary.
	with open('output.mp3', 'wb') as out:
	    # Write the response to the output file.
	    out.write(response.audio_content)
	    print('Audio content written to file "output.mp3"')



	from pydub import AudioSegment

	sound = AudioSegment.from_mp3("output.mp3")
	sound.export("output.wav", format="wav")


	import winsound
	winsound.PlaySound('output.wav', winsound.SND_ALIAS)


phrases_men = ['Hi guy, if you brave enough try your lack to win some candies',
	'Hi guuuuuuuuy, areeee you ready to try some sweets',
	'Heeeeeey, whats up men, we have some candies here', 
	"Hey! I wanna play a game with you! Yes, you. Come here! Right now!",
	"Good morning my sweety! Would like to play a game and win some candies?"]

def greeting(age, gender):

	if (age<14 and gender=='male'):
		playsound('Hello Little Boy, do you want some candies?', 'en-US-Wavenet-F')
	elif (age<14 and gender=='female'):
		playsound('Hello Little Girl, do you want some candies?', 'en-US-Wavenet-F')
	elif (age<30 and gender=='male'):
		playsound(phrases_men[randint(0, 4)], 'en-US-Wavenet-E')
	elif (age<30 and gender=='female'):
		playsound('Hi girl, you is as sweet as my candies, I have a personal present for you', "en-US-Wavenet-B")
	elif (age>30 and gender=='male'):
		playsound('Welcome men, we have a special offer for you', 'en-US-Wavenet-A')
	else:
		playsound('Welcome lady, do you want to get a special offer?', 'en-US-Wavenet-A')


def greeting_with_object(age, gender, object_name):

	if (age<14 and gender=='male'):
		playsound('Cool' + object_name + ', do you want some candies?', 'en-US-Wavenet-F')
	elif (age<14 and gender=='female'):
		playsound('Hello Little Girl with ' + object_name + ', do you want some candies?', 'en-US-Wavenet-F')
	elif (age<30 and gender=='male'):
		playsound('Hi guy with ' + object_name + ', if you brave enough try your lack to win some candies', 'en-US-Wavenet-E')
	elif (age<30 and gender=='female'):
		playsound('Hi girl with ' + object_name + ', you is as sweet as my candies, I have a personal present for you', "en-US-Wavenet-B")
	elif (age>30 and gender=='male'):
		playsound('Welcome men with ' + object_name + ', we have a special offer for you', 'en-US-Wavenet-A')
	else:
		playsound('Welcome lady with ' + object_name + ', do you want to get a special offer?', 'en-US-Wavenet-A')

# if __main__ == "__main__":
# 	greeting(5, 'female')



def greeting_with_only_object(object_name):
	phrases = ["Hey! Cool {}, Let's play with Robot Arm and Candies!".format(object_name),
				"Dude! Look at this {}. So Nice! Wanna play and win candies?".format(object_name)]
	from random import choice

	playsound(choice(phrases), 'en-US-Wavenet-F')